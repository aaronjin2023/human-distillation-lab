#!/usr/bin/env python3
"""Build the reviewed character library and validate its evidence/identity links."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import re
from pathlib import Path
import tempfile
import shutil
import fcntl
from urllib.parse import unquote, urlsplit
import unicodedata

from distill_characters import BASE, DIMS, LABELS, task_constraints, normalized, read_lines, require, validate_result, write_json, write_lines


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()[:16]


def source_key(source):
    url=urlsplit(source.get('canonical_url') or source['source_url'])
    return (url.netloc.casefold(),unicodedata.normalize('NFC',unquote(url.path)).replace(' ','_'),url.query)


def reviewed_links(rows):
    links={}
    for row in rows:
        require(row['key'].startswith('reviewed:') and len(set(row['member_keys']))>=2,'Invalid identity decision')
        require(row['rationale'] and row['evidence'],'Identity decision lacks evidence')
        for member in row['member_keys']:
            require(member not in links,'Conflicting identity decisions')
            links[member]=row
    return links


def series_confirmed(source,checks):
    series=source.get('series_verified')
    return not series or bool(series.get('article_series_field') or checks.get(source['id'],{}).get('ok'))


def identity_key(character, source):
    # Only exact, unambiguous source entity matches merge identities across works.
    names={normalized(x) for x in [character['name']]+character['aliases']}
    matches={x['character_id'] for x in source.get('character_candidates',[]) if normalized(x['name']) in names and x.get('character_id')}
    if len(matches)==1:
        return 'freebase:'+next(iter(matches)), 'source-character-id'
    name_parts=[x for x in re.findall(r'[^\W\d_]+',character['name']) if x.casefold() not in {'the','lord','lady','captain','dr','doctor','mr','mrs','ms','sir','professor'}]
    if source.get('series_verified') and len(name_parts)>=2:
        return 'series:'+normalized(source['series_verified']['name'])+':'+normalized(character['name']), 'source-series-and-exact-name'
    return source['id']+':'+normalized(character['name']), 'work-local-unresolved'


def resolved_identity(character, source, overrides):
    key,method=identity_key(character,source)
    decision=overrides.get((source['id'],normalized(character['name'])))
    if decision:
        require(decision['source_key']==key and decision['key'].startswith('work-separated:'),'Identity exception does not match source')
        require(decision['reason'] and decision['evidence'],'Identity exception lacks evidence')
        return decision['key'],'reviewed-source-identity-exception'
    return key,method


def source_info(row):
    p=row.get('provenance',{})
    return {'url':row.get('source_revision_url') or row['source_url'],
            'canonical_url':row.get('canonical_url') or row['source_url'],
            'revision':row.get('source_revision') or 'Wikipedia 2012-11-02 / Freebase 2012-11-04 snapshot',
            'license':row.get('source_license') or p.get('license',''),
            'license_url':p.get('license_url') or 'https://creativecommons.org/licenses/by-sa/4.0/',
            'attribution':row.get('source_attribution') or ('Wikipedia contributors; '+p.get('citation','')+'; '+p.get('dataset_url','')),
            'source_sha256':row['source_sha256']}


def render_card(w, profiles, e):
    info=w['source']
    md=[f"# {w['title']}", '', f"作品类型：{w['medium']} · 年份：{w.get('year','未单独核验')}", '',f"传播依据：{w['popularity']['basis']}",f"[依据来源]({w['popularity']['url']}) · {w['popularity'].get('note','')}", '',f"剧情来源：[原页面/修订]({info['url']})", '', '## 角色资料', '', '加载契约：每个独立版本必须一起加载 task_constraints、unknown_constraint_categories、traits、unknown_dimensions 与引用证据；未知条件不能默认满足。任务约束中的应用规则为编者转译，不是原文引语。', '']
    for c in profiles:
        md.extend([f"### {c['name']}", '',f"角色职责：{c['role']} · 身份：`{c['identity_id']}` · 独立版本：`{c['id']}`", ''])
        md.extend(['**任务约束（绑定本版本）**', ''])
        for t in c['task_constraints']:
            md.append(f"- **{t['category']}**：{t['fact']}；任务应用：{t['task_rule']}（{ '、'.join(t['evidence_ids']) }）")
        md.extend(['约束未知／未专项核读：'+('、'.join(c['unknown_constraint_categories']) or '无类别缺项；各类仍限所引摘要，不代表穷尽'), ''])
        for t in c['traits']:
            refs='、'.join('S'+r.rsplit(':s',1)[1] for r in t['evidence_ids'])
            md.append(f"- **{LABELS[t['dimension']]}**：{t['claim']}（{'行为推断' if t['basis']=='interpretation' else '摘要直接叙述'}；{refs}）")
        md.extend(['', '暂无支持：'+'、'.join(LABELS[d] for d in c['unknown_dimensions']), ''])
        if c['tensions']:
            md.extend(['矛盾与变化：'+'；'.join(c['tensions']), '', '以上为依据完整摘要审校的综合笔记，未逐项标注句号；可结合下列完整选摘核对。', ''])
    md.extend(['## 材料限制', '',*['- '+x for x in w['limitations']], '', '## 引用证据', '', '以下保留提炼与审校所用的完整摘要选摘，包括未被维度判断直接引用的句子，以保全综合笔记的上下文。', ''])
    md.extend(f"- **S{x['source_sentence']}**：{x['text']}" for x in e['sentences'])
    md.extend(['', '## 来源与许可', '',info['attribution'], '',f"[{info['license']}]({info['license_url']})；本页相应改写按同一许可提供。", '', '本页为有改写的角色研究与证据选摘；不是原著/剧本全文，也不代表测量结果。', ''])
    return '\n'.join(md)


def validate_cards(base, works, profiles, evidence):
    expected={f"{w['id']}.md" for w in works}
    require({p.relative_to(base/'works').as_posix() for p in (base/'works').rglob('*') if p.is_file()}==expected, 'Missing or extra readable card')
    by_profile={c['id']:c for c in profiles}
    by_evidence={e['work_id']:e for e in evidence}
    for w in works:
        require((base/'works'/f"{w['id']}.md").read_bytes()==render_card(w,[by_profile[pid] for pid in w['profile_ids']],by_evidence[w['id']]).encode(), 'Readable card differs from reviewed data: '+w['id'])


def build():
    previous=read_lines(BASE/'works.jsonl')
    source_checks={r['id']:r for r in read_lines(BASE/'verification'/'literature-source-checks.jsonl') if r.get('audit_version')==4}
    series_checks={r['id']:r for r in read_lines(BASE/'verification'/'series-membership-checks.jsonl') if r.get('audit_version')==1}
    groups=json.loads((BASE/'selection.json').read_text())['groups']
    accepted, rejected, duplicates=[],[],[]
    seen_ids, seen_urls=set(),set()
    receipts=[]
    links=reviewed_links(read_lines(BASE/'identity-merges.jsonl'))
    override_rows=read_lines(BASE/'identity-overrides.jsonl')
    overrides={(x['work_id'],normalized(x['character_name'])):x for x in override_rows}
    require(len(overrides)==len(override_rows),'Duplicate identity exception')
    popularity_corrections={x['work_id']:x for x in read_lines(BASE/'verification'/'popularity-corrections.jsonl')}
    series_by_url={}
    for group in groups:
        for file in sorted((BASE/'batches'/group).glob('*.input.json')):
            output=file.with_name(file.name.replace('.input.json','.output.json'))
            receipt=file.with_name(file.name.replace('.input.json','.receipt.json'))
            if not output.exists() or not receipt.exists():
                continue
            r=json.loads(receipt.read_text())
            if not r.get('review'):
                continue
            inputs=json.loads(file.read_text())
            for s in inputs:
                if s.get('source_identity_check_version')==4 and s.get('series_verified') and series_confirmed(s,series_checks):
                    series_by_url[source_key(s)]=s['series_verified']
            sources={x['id']:x for x in inputs}
            result=validate_result(json.loads(output.read_text()),inputs)
            receipts.append({'group':group,**r})
            for row in result['results']:
                s=sources[row['work_id']]
                if not series_confirmed(s,series_checks):
                    rejected.append({'id':s['id'],'title':s['title'],'medium':s['medium'],'limitations':['Series membership verification pending or did not pass.'],'batch':str(file.relative_to(BASE)),'rejection_stage':'series-membership'})
                    continue
                confirmed=s.get('source_identity_check_version')==4 or bool(s.get('source_identity_evidence') and s.get('source_form_author_verified')) or source_checks.get(s['id'],{}).get('ok',False)
                if s['medium']=='literature' and not confirmed:
                    rejected.append({'id':s['id'],'title':s['title'],'medium':s['medium'],'limitations':['Current source identity verification is pending or did not pass.'],'batch':str(file.relative_to(BASE)),'rejection_stage':'source-identity'})
                    continue
                if s['medium']=='literature' and s['id'] in source_checks and not source_checks[s['id']]['ok']:
                    rejected.append({'id':s['id'],'title':s['title'],'medium':s['medium'],'limitations':['Source identity verification did not pass: '+source_checks[s['id']]['reason']],'batch':str(file.relative_to(BASE)),'rejection_stage':'source-identity'})
                    continue
                if not row['source_sufficient']:
                    rejected.append({'id':s['id'],'title':s['title'],'medium':s['medium'],'limitations':row['limitations'],'batch':str(file.relative_to(BASE))})
                    continue
                key=source_key(s)
                if s['id'] in seen_ids or key in seen_urls:
                    duplicates.append({'id':s['id'],'source_url':s.get('canonical_url') or s['source_url'],'reason':'Repeated work/source record'})
                    continue
                seen_ids.add(s['id']);seen_urls.add(key)
                accepted.append((s,row,group,file.name,r))
    # Explicit quotas keep failed or unsupported candidates from becoming count padding.
    selected=[]
    for medium in ('literature','film'):
        selected.extend(x for x in accepted if x[0]['medium']==medium)
    selected=[x for medium in ('literature','film') for x in [v for v in selected if v[0]['medium']==medium][:500]]
    works,profiles,evidence=[],[],[]
    identities={}
    staging=Path(tempfile.mkdtemp(prefix='.build-',dir=BASE))
    cards=staging/'works'
    cards.mkdir(exist_ok=True)
    for s,row,group,batch,r in selected:
        if s['id'] in popularity_corrections:
            correction=popularity_corrections[s['id']]
            require(correction['reason'] and correction['popularity']['url'],'Unsupported popularity correction')
            s={**s,'popularity':correction['popularity']}
        if source_key(s) in series_by_url:
            s={**s,'series_verified':series_by_url[source_key(s)]}
        work_id=s['id']
        require('/' not in work_id and '..' not in work_id,'Unsafe work ID')
        info=source_info(s)
        info['form_author_verified']=s['medium']=='film' or s.get('source_identity_check_version')==4 or bool(s.get('source_identity_evidence') and s.get('source_form_author_verified')) or source_checks.get(s['id'],{}).get('ok',False)
        require(info['license'] and info['attribution'],'Missing source rights/provenance')
        # Tension notes are reviewed against the whole excerpt, so retain that context too.
        ev=[{'id':f"{work_id}:s{x['index']}",'text':x['text'],'source_sentence':x['index']} for x in s['source_units']]
        evidence.append({'work_id':work_id,'source':info,'scope':'complete-model-input-synopsis','source_unit_count':len(s['source_units']),'source_units_sha256':hashlib.sha256(json.dumps(s['source_units'],ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'sentences':ev})
        profile_ids=[]
        for c in row['characters']:
            profile_id='profile-'+digest(work_id+'|'+normalized(c['name']))
            key,method=resolved_identity(c,s,overrides)
            original_key=key
            if key in links:
                key,method=links[key]['key'],'reviewed-work-family-and-synopsis'
            entity_id='identity-'+digest(key)
            traits=[{**t,'evidence_ids':[f'{work_id}:s{i}' for i in t['evidence_sentences']]} for t in c['traits']]
            for t in traits:
                del t['evidence_sentences']
            profile={**c,'id':profile_id,'work_id':work_id,'identity_id':entity_id,'identity_link_method':method,'traits':traits,'interpretation_scope':'This narrative version and cited synopsis only; not an actor or real-person assessment.'}
            if c['tensions']:
                profile['tensions_evidence_scope']='Whole retained synopsis; separately reviewed notes without individual sentence indices.'
            profiles.append(profile);profile_ids.append(profile_id)
            identity=identities.setdefault(entity_id,{'id':entity_id,'source_key':key,'link_method':method,'canonical_name':links[original_key]['canonical_name'] if original_key in links else c['name'],'names':[],'profile_ids':[],'source_keys':[],'scope':'Character concept; separate work profiles preserve continuities and adaptations.'})
            identity['source_keys']=sorted(set(identity['source_keys']+[original_key]))
            identity['names']=sorted(set(identity['names']+[c['name']]+c['aliases']))
            identity['profile_ids'].append(profile_id)
        works.append({'id':work_id,'title':s['title'],'medium':s['medium'],'year':s.get('year'),'authors':s.get('authors',[]),'original_language_label':s.get('original_language_label'),'reported_language_labels':s.get('reported_languages',[]),'production_region_labels':s.get('production_countries',[]),'popularity':s['popularity'],'source':info,'profile_ids':profile_ids,'limitations':row['limitations'],'review':{'group':group,'batch':batch,'extraction_model':r['extraction'].get('model'),'review_model':r['review']['model']}})
    constraint_rows=read_lines(BASE/'task-constraints.jsonl')
    require((BASE/'task-constraints.jsonl').exists(), 'Missing constraint supplement')
    merged=task_constraints(constraint_rows,profiles,evidence)
    for c in profiles:
        c.update(merged[c['id']])
    by_profile={c['id']:c for c in profiles}
    by_evidence={e['work_id']:e for e in evidence}
    for w in works:
        (cards/f"{w['id']}.md").write_text(render_card(w,[by_profile[pid] for pid in w['profile_ids']],by_evidence[w['id']]))
    write_lines(staging/'task-constraints.jsonl',constraint_rows)
    shutil.copyfile(BASE/'task-constraints.schema.json',staging/'task-constraints.schema.json')
    for filename,rows in [('works.jsonl',works),('characters.jsonl',profiles),('identities.jsonl',list(identities.values())),('evidence.jsonl',evidence),('rejected.jsonl',rejected)]:
        write_lines(staging/filename,rows)
    # Same-name unresolved records are review candidates, never automatic identity merges.
    names=defaultdict(set)
    for c in profiles:
        for name in [c['name']]+c['aliases']:
            if normalized(name):
                names[normalized(name)].add(c['identity_id'])
    separations={x['normalized_name']:x for x in read_lines(BASE/'identity-separations.jsonl')}
    unresolved=[]
    for name,ids in sorted(names.items()):
        if len(ids)<2:continue
        decision=separations.get(name,{})
        known=bool(decision.get('reason')) and {identities[i]['source_key'] for i in ids}<=set(decision.get('member_keys',[]))
        unresolved.append({'normalized_name':name,'identity_ids':sorted(ids),'status':'reviewed-distinct-characters' if known else 'requires-source-confirmation'})
    write_lines(staging/'identity-review.jsonl',unresolved)
    stats={'works':len(works),'medium_counts':dict(Counter(w['medium'] for w in works)),'character_versions':len(profiles),'identities':len(identities),'identity_links_saved':len(profiles)-len(identities),'trait_claims':sum(len(c['traits']) for c in profiles),'dimension_coverage':dict(Counter(t['dimension'] for c in profiles for t in c['traits'])),'film_production_regions':dict(Counter(region for w in works if w['medium']=='film' for region in w['production_region_labels'])),'rejected_source_records':len(rejected),'deduplicated_work_records':duplicates,'unresolved_same_name_groups':sum(x['status']=='requires-source-confirmation' for x in unresolved),'reviewed_distinct_name_groups':sum(x['status']=='reviewed-distinct-characters' for x in unresolved),'target_works':1000,'complete':len(works)==1000,'scope':'500 narrative literary works and 500 films; global sources with Chinese works; two to five central characters per work.'}
    write_json(staging/'verification'/'model-batches.json',receipts)
    catalog=['# 文学与影视角色目录','',f"已保存 {len(works)} 部作品、{len(profiles)} 个角色版本、{len(identities)} 个身份节点。",'', '每个版本独立保留判断与证据；身份关联不会覆盖原著、改编或续作差异。', '', '| 作品 | 类型 | 角色数 |', '|---|---|---|']
    catalog.extend(f"| [{w['title'].replace('|','/')}](works/{w['id']}.md) | {w['medium']} | {len(w['profile_ids'])} |" for w in works)
    (staging/'CATALOG.md').write_text('\n'.join(catalog)+'\n')
    stats['artifact_sha256']={p.relative_to(staging).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in staging.rglob('*') if p.is_file()}
    stats['readable_cards_integrity']='all cards byte-equivalent to render of reviewed exports; exact file set'
    stats['task_constraint_claims']=sum(len(c['task_constraints']) for c in profiles)
    stats['profiles_with_task_constraints']=sum(bool(c['task_constraints']) for c in profiles)
    stats['constraint_scope']='Todd supplement locally checked against retained synopsis; all other categories unknown/unreviewed'
    write_json(staging/'verification'/'build.json',stats)
    validate(False,staging)
    # Validate the whole generated set first; publish its integrity receipt last.
    files=sorted((p for p in staging.rglob('*') if p.is_file()),key=lambda p:(p.relative_to(staging).as_posix()=='verification/build.json',p.as_posix()))
    for p in files:
        target=BASE/p.relative_to(staging)
        target.parent.mkdir(parents=True,exist_ok=True)
        p.replace(target)
    kept={w['id'] for w in works}
    for w in previous:
        if w['id'] not in kept:
            (BASE/'works'/f"{w['id']}.md").unlink(missing_ok=True)
    shutil.rmtree(staging)
    print(json.dumps(stats,ensure_ascii=False,indent=2))


def validate(complete,base=BASE):
    works=read_lines(base/'works.jsonl');profiles=read_lines(base/'characters.jsonl');identities=read_lines(base/'identities.jsonl');evidence=read_lines(base/'evidence.jsonl')
    def unique(rows):
        ids=[r['id'] for r in rows]
        require(len(ids)==len(set(ids)),'Duplicate ID')
        return set(ids)
    wids,pids,iids=unique(works),unique(profiles),unique(identities)
    lookup={e['work_id']:{s['id'] for s in e['sentences']} for e in evidence}
    require(set(lookup)==wids,'Missing evidence work')
    for e in evidence:
        units=[{'index':s['source_sentence'],'text':s['text']} for s in e['sentences']]
        require(e.get('scope')=='complete-model-input-synopsis' and len(units)==e.get('source_unit_count'),'Incomplete synopsis evidence')
        require([u['index'] for u in units]==list(range(1,len(units)+1)),'Missing or reordered source unit')
        require(hashlib.sha256(json.dumps(units,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==e.get('source_units_sha256'),'Changed synopsis evidence')
    for w in works:
        require(2<=len(w['profile_ids'])<=5 and set(w['profile_ids'])<=pids,'Invalid work profiles')
        require(set(w['profile_ids'])=={c['id'] for c in profiles if c['work_id']==w['id']},'Work/profile membership mismatch')
    for c in profiles:
        require(c['work_id'] in wids and c['identity_id'] in iids,'Broken profile link')
        dims={t['dimension'] for t in c['traits']}
        require(len(dims)==len(c['traits'])>=4 and set(c['unknown_dimensions'])==set(DIMS)-dims,'Invalid dimensions')
        require(all(t['evidence_ids'] and set(t['evidence_ids'])<=lookup[c['work_id']] for t in c['traits']),'Broken evidence link')
        require(not c.get('tensions') or c.get('tensions_evidence_scope'),'Unlabelled tension evidence scope')
    merged=task_constraints(read_lines(base/'task-constraints.jsonl'),profiles,evidence)
    for c in profiles:
        require(all(c.get(k)==v for k,v in merged[c['id']].items()), 'Missing or modified loaded task constraints')
    validate_cards(base,works,profiles,evidence)
    for i in identities:
        require(set(i['profile_ids'])<=pids,'Broken identity links')
        require(set(i['profile_ids'])=={c['id'] for c in profiles if c['identity_id']==i['id']},'Identity/profile membership mismatch')
    require(sum(len(i['profile_ids']) for i in identities)==len(profiles),'Profile identity membership mismatch')
    receipt=json.loads((base/'verification'/'build.json').read_text())
    hashes=receipt.get('artifact_sha256',{})
    required={'works.jsonl','characters.jsonl','identities.jsonl','evidence.jsonl','task-constraints.jsonl','task-constraints.schema.json','CATALOG.md'}|{f"works/{w['id']}.md" for w in works}
    require(required<=set(hashes), 'Integrity receipt does not cover every loaded artifact')
    for name,expected in hashes.items():
        require(not Path(name).is_absolute() and '..' not in Path(name).parts, 'Unsafe artifact path')
        require(hashlib.sha256((base/name).read_bytes()).hexdigest()==expected,'Mixed or modified export: '+name)
    if complete:
        require(Counter(w['medium'] for w in works)=={'literature':500,'film':500},'Target not complete')
        require(all(w['source'].get('form_author_verified') for w in works),'Work identity verification incomplete')
    return True


def self_test():
    c={'name':'Harry Potter','aliases':['Harry']}
    s={'id':'book-a','character_candidates':[{'name':'Harry Potter','character_id':'/m/h'}]}
    assert identity_key(c,s)==('freebase:/m/h','source-character-id')
    override={'source_key':'freebase:/m/h','key':'work-separated:book-a:harry','reason':'A source entity conflates different individuals','evidence':[{'id':'book-a:s1'}]}
    assert resolved_identity(c,s,{('book-a','harrypotter'):override})[0]=='work-separated:book-a:harry'
    assert resolved_identity(c,{**s,'id':'book-b'},{('book-a','harrypotter'):override})[0]=='freebase:/m/h'
    try:resolved_identity(c,s,{('book-a','harrypotter'):{**override,'source_key':'wrong'}})
    except ValueError:pass
    else:raise AssertionError('Unbound identity exception accepted')
    assert identity_key(c,{'id':'book-b'})[0]!=identity_key(c,{'id':'book-c'})[0]
    s['character_candidates'].append({'name':'Harry','character_id':'/m/other'})
    assert identity_key(c,s)[1]=='work-local-unresolved'
    assert identity_key(c,{'id':'a','series_verified':{'name':'Harry Potter'}})[0]==identity_key(c,{'id':'b','series_verified':{'name':'Harry Potter'}})[0]
    assert identity_key(c,{'id':'a','series_verified':{'name':'Harry Potter'}})[0]!=identity_key(c,{'id':'b','series_verified':{'name':'Other'}})[0]
    assert identity_key({'name':'Thomas','aliases':[]},{'id':'a','series_verified':{'name':'Example'}})[1]=='work-local-unresolved'
    assert digest('a|bc')!=digest('ab|c')
    assert source_key({'source_url':'https://en.wikipedia.org/wiki/Harry%27s_Book'})==source_key({'source_url':"https://en.wikipedia.org/wiki/Harry's Book"})
    assert source_key({'source_url':'https://en.wikipedia.org/?curid=1'})!=source_key({'source_url':'https://en.wikipedia.org/?curid=2'})
    decision={'key':'reviewed:example','member_keys':['a','b'],'rationale':'Same named character in linked works','evidence':[{'url':'https://example.org'}]}
    assert reviewed_links([decision])['a']['key']=='reviewed:example'
    try:reviewed_links([decision,decision])
    except ValueError:pass
    else:raise AssertionError('Conflicting identity decisions accepted')
    legacy={'id':'legacy','series_verified':{'name':'Twilight'}}
    assert not series_confirmed(legacy,{})
    assert not series_confirmed(legacy,{'legacy':{'ok':False}})
    assert series_confirmed(legacy,{'legacy':{'ok':True}})
    assert series_confirmed({'id':'new','series_verified':{'article_series_field':'Twilight'}},{})
    # Exercise the public validator on an isolated real-source fixture, including forged hashes.
    w=read_lines(BASE/'works.jsonl')[0]
    profiles=[c for c in read_lines(BASE/'characters.jsonl') if c['id'] in w['profile_ids']]
    evidence=[e for e in read_lines(BASE/'evidence.jsonl') if e['work_id']==w['id']]
    identities=[i for i in read_lines(BASE/'identities.jsonl') if i['id'] in {c['identity_id'] for c in profiles}]
    for i in identities:
        i['profile_ids']=[c['id'] for c in profiles if c['identity_id']==i['id']]
    merged=task_constraints([],profiles,evidence)
    for c in profiles:c.update(merged[c['id']])
    with tempfile.TemporaryDirectory() as folder:
        base=Path(folder);(base/'works').mkdir()
        for name,rows in [('works', [w]),('characters',profiles),('identities',identities),('evidence',evidence),('task-constraints',[])]:
            write_lines(base/(name+'.jsonl'),rows)
        shutil.copyfile(BASE/'task-constraints.schema.json',base/'task-constraints.schema.json')
        (base/'CATALOG.md').write_text('Fixture catalog')
        card=base/'works'/f"{w['id']}.md"
        text=render_card(w,profiles,evidence[0]);card.write_text(text)
        hashes={p.relative_to(base).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in base.rglob('*') if p.is_file()}
        write_json(base/'verification'/'build.json',{'artifact_sha256':hashes})
        assert validate(False,base)
        def must_fail(label):
            try:validate(False,base)
            except ValueError:return
            raise AssertionError('Invalid readable export accepted: '+label)
        card.write_text('# damaged card\n');must_fail('body deleted but file exists')
        hashes['works/'+card.name]=hashlib.sha256(card.read_bytes()).hexdigest()
        write_json(base/'verification'/'build.json',{'artifact_sha256':hashes})
        must_fail('damaged card rehashed into receipt')
        card.write_text(text.replace(profiles[0]['traits'][0]['claim'],'受保护正文已被替换',1));must_fail('protected trait text modified')
        card.unlink();must_fail('missing card')
        card.write_text(text)
        extra=base/'works'/'unexpected.md';extra.write_text('extra');must_fail('extra card');extra.unlink()
        hashes['works/'+card.name]=hashlib.sha256(card.read_bytes()).hexdigest()
        del hashes['works/'+card.name]
        write_json(base/'verification'/'build.json',{'artifact_sha256':hashes})
        must_fail('card omitted from receipt')
    print('Readable-card negative tests passed: deleted body, modified trait, missing/extra card, forged/omitted receipt hash')
    print('Self-test passed: exact identity evidence, ambiguity, different-work separation, stable IDs')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['build','validate','self-test'])
    parser.add_argument('--complete',action='store_true')
    args=parser.parse_args()
    if args.action=='build':
        with (BASE/'.build.lock').open('w') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
            build()
    elif args.action=='validate':validate(args.complete);print('Character library validation passed')
    else:self_test()
