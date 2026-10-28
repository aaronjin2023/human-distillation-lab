#!/usr/bin/env python3
"""Build and validate the frozen DATUMOJ comment-persona collection."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from distill_characters import normalized, read_lines, require, write_json, write_lines

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'commentary-personas'
LABELS = dict(zip(('personality', 'motivation', 'attention', 'reasoning', 'voice', 'interaction'),
                  ('情境性格', '人设动机', '注意焦点', '思考方式', '表达风格', '互动动作')))
EVIDENCE_FIELDS = {'desc', 'lines.0', 'lines.1', 'lines.2'}


def validate_data(sources, records, manifest):
    source_ids = [s['id'] for s in sources]
    expected = set(manifest['public_character_ids'])
    hidden = set(manifest['hidden_ids'])
    require(len(source_ids) == len(set(source_ids)) and set(source_ids) == expected, 'Source IDs do not match snapshot')
    require(not expected & hidden and expected | hidden == set(range(1, manifest['declared_slots'] + 1)), 'Missing or overlapping slots')
    require(len({normalized(s['name']) for s in sources}) == len(sources), 'Duplicate source name needs review')
    require(all(s['desc'] and len(s['lines']) == 3 and all(s['lines']) for s in sources), 'Missing source evidence')
    ids = [r['source_id'] for r in records]
    require(len(ids) == len(set(ids)) and set(ids) == expected, 'Public/hidden character coverage mismatch')
    for row in records:
        obs = row['observations']
        require(len(obs) == len(LABELS) and {o['dimension'] for o in obs} == set(LABELS), 'Duplicate or missing dimensions')
        for o in obs:
            require(isinstance(o['claim'], str) and o['claim'].strip(), 'Empty claim')
            refs = o['evidence_fields']
            require(refs and set(refs) <= EVIDENCE_FIELDS, 'Unsupported evidence field')
        a = row['application']
        require(len(a['steps']) == 3 and all(isinstance(s, str) and s.strip() for s in a['steps']), 'Invalid application steps')
        require(a['example']['context'] and a['example']['comment'] and a['boundary'], 'Missing application context or boundary')
    return True


def build():
    sources = read_lines(BASE / 'source-records.jsonl')
    manifest = json.loads((BASE / 'source-manifest.json').read_text())
    inputs = sorted((BASE / 'intake').glob('batch-*.output.json'))
    records = [r for file in inputs for r in json.loads(file.read_text())]
    validate_data(sources, records, manifest)
    require(hashlib.sha256((BASE / 'source-records.jsonl').read_bytes()).hexdigest() == manifest['source_records_sha256'], 'Changed source snapshot')
    by_id = {r['source_id']: r for r in records}
    groups = json.loads((BASE / 'related-roles.json').read_text())['groups']
    profiles, catalog = [], []
    for s in sources:
        n = s['id']
        slug = f'datumoj-commentator-{n:03d}'
        row = by_id[n]
        profile = {**row, 'id': f'datumoj-72:{n:02d}', 'name': s['name'], 'source_title': s['title'],
                   'faction': s['faction'], 'kind': 'synthetic-comment-persona', 'status': 'available',
                   'source_url': s['source_url'], 'source_record_sha256': s['source_sha256'],
                   'evidence_level': 'artifact', 'claim_scope': 'Distillation of authored persona descriptions, not a real-person psychological assessment.',
                   'application_scope': 'Original illustrative application; examples and steps are not source quotations.',
                   'source_stats': {'values': s['stats'], 'meaning': 'Illustrative game feel only; not personality test scores.'},
                   'unknown': ['真实人格测量', '真人身份与生活史', '跨情境稳定性', '行为预测效度']}
        profiles.append(profile)
        path = f'personas/{slug}/SKILL.md'
        catalog.append({'source_id': n, 'id': profile['id'], 'name': s['name'], 'title': s['title'], 'faction': s['faction'], 'status': 'available', 'path': path})
        description = f"使用{s['name']}（{s['title']}）的虚构评论风格开展角色创作或内容压力测试；按需加载，不用于真人心理判断。"
        md = ['---', f'name: {slug}', 'description: ' + json.dumps(description, ensure_ascii=False), '---', '',
              f"# {n:02d} · {s['name']} — {s['title']}", '', f"阵营：{s['faction']} · 类型：原站合成角色 · ID：`{profile['id']}`", '',
              f"[原站角色卡]({s['source_url']}) · [结构化记录](manifest.json) · [全库用法](../../SKILL.md)", '',
              '根据用户给出的内容、语境和事实生成此角色的评论。保留其辨识度；缺少历史作品、数据或个人经历时不要假装拥有这些材料。', '',
              '## 来源内的角色设定', '',
              '以下是对作者人设的概括，证据级别为 artifact；其中动机不代表对真实评论者的判断。', '']
        for o in row['observations']:
            md.append(f"- **{LABELS[o['dimension']]}**：{o['claim']}〔{', '.join(o['evidence_fields'])}〕")
        md += ['', '## 应用步骤', '', '以下步骤及示例由本库编写，不是原站原话。', '']
        md += [f'{i}. {step}' for i, step in enumerate(row['application']['steps'], 1)]
        example = row['application']['example']
        md += ['', '**虚构场景**：' + example['context'], '', '**原创示例**：' + example['comment'], '',
               '**使用边界**：' + row['application']['boundary'], '', '## 近似角色与区别', '']
        related = [g for g in groups if n in g['ids']]
        for g in related:
            links = '、'.join(f'[{i:02d}](../datumoj-commentator-{i:03d}/SKILL.md)' for i in g['ids'] if i != n)
            md.append(f'- {links}：{g["distinction"]}')
        if not related:
            md.append('本次未标注需要特别区分的近似角色；不据此断言与其他角色完全不相似。')
        md += ['', '## 原站证据', '', '`desc`：' + s['desc'], '']
        md += [f'- `lines.{i}`：{line}' for i, line in enumerate(s['lines'])]
        md += ['', '原站手感参数只作为素材元数据保留，不是心理测评分数。原站个别类型名称为修辞标签，不能当作疾病诊断。', '',
               '尚无依据：' + '、'.join(profile['unknown']) + '。', '',
               '来源：DATUMOJ 评论区人物资产库；来源内容未重新授予许可证。', '']
        target = BASE / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text('\n'.join(md))
        write_json(target.parent / 'manifest.json', profile)
    for n in manifest['hidden_ids']:
        catalog.append({'source_id': n, 'id': f'datumoj-72:{n:02d}', 'name': None, 'title': '隐藏角色（原站尚未揭晓）', 'faction': None, 'status': 'unrevealed', 'path': None})
    catalog.sort(key=lambda r: r['source_id'])
    write_lines(BASE / 'personas.jsonl', profiles)
    write_json(BASE / 'catalog.json', catalog)
    counts = dict(Counter(p['faction'] for p in profiles))
    md = ['# DATUMOJ 72 · 评论区角色目录', '', f"72 个位置：{len(profiles)} 份公开角色已整理，3 个隐藏位未补造。", '',
          '[使用说明](README.md) · [加载入口](SKILL.md) · [结构化目录](catalog.json)', '',
          '| 编号 | 人物 | 原站类型 | 阵营 | 状态 |', '|---|---|---|---|---|']
    for r in catalog:
        name = f"[{r['name']}]({r['path']})" if r['path'] else '未揭晓'
        md.append(f"| {r['source_id']:02d} | {name} | {r['title']} | {r['faction'] or '—'} | {'已整理' if r['status']=='available' else '隐藏位'} |")
    (BASE / 'CATALOG.md').write_text('\n'.join(md) + '\n')
    files = [BASE/'personas.jsonl', BASE/'catalog.json', BASE/'CATALOG.md', BASE/'source-records.jsonl', BASE/'related-roles.json', BASE/'source-manifest.json'] + sorted((BASE/'personas').glob('*/*'))
    receipt = {'status': 'public-source-complete', 'slots': 72, 'available': len(profiles), 'unrevealed': len(manifest['hidden_ids']),
               'observations': sum(len(r['observations']) for r in profiles), 'factions': counts,
               'artifact_sha256': {str(f.relative_to(BASE)): hashlib.sha256(f.read_bytes()).hexdigest() for f in files if f.is_file()}}
    write_json(BASE/'verification/build.json', receipt)
    validate()
    print(json.dumps({k:v for k,v in receipt.items() if k!='artifact_sha256'}, ensure_ascii=False))


def validate():
    sources = read_lines(BASE/'source-records.jsonl')
    profiles = read_lines(BASE/'personas.jsonl')
    manifest = json.loads((BASE/'source-manifest.json').read_text())
    validate_data(sources, profiles, manifest)
    source_by_id = {s['id']:s for s in sources}
    for p in profiles:
        s = source_by_id[p['source_id']]
        require(p['name']==s['name'] and p['source_title']==s['title'] and p['faction']==s['faction'], 'Source identity mismatch')
        require(p['source_url']==s['source_url'] and p['source_record_sha256']==s['source_sha256'], 'Source binding mismatch')
        require(p['source_stats']['values']==s['stats'] and p['kind']=='synthetic-comment-persona', 'Changed source metadata')
    catalog = json.loads((BASE/'catalog.json').read_text())
    require([r['source_id'] for r in catalog] == list(range(1,73)), 'Catalog does not cover 72 slots')
    by_id = {p['source_id']:p for p in profiles}
    for r in catalog:
        if r['source_id'] in manifest['hidden_ids']:
            require(r['status']=='unrevealed' and r['path'] is None and r['name'] is None, 'Invented hidden character')
            continue
        require(r['status']=='available' and r['path'], 'Missing public skill')
        file = BASE/r['path']
        require(file.exists() and json.loads(file.with_name('manifest.json').read_text())==by_id[r['source_id']], 'Skill data mismatch')
        for link in re.findall(r'\]\(([^)]+)\)',file.read_text()):
            if '://' not in link:
                require((file.parent/link).exists(), 'Broken skill link: '+link)
    require(len(list((BASE/'personas').glob('*/SKILL.md')))==len(profiles), 'Stale or missing persona cards')
    for file, expected in json.loads((BASE/'verification/build.json').read_text())['artifact_sha256'].items():
        require(hashlib.sha256((BASE/file).read_bytes()).hexdigest()==expected, 'Modified or mixed output: '+file)
    return True


def self_test():
    import copy
    sources=[{'id':1,'name':'角色甲','desc':'设定','lines':['甲','乙','丙']}]
    manifest={'public_character_ids':[1],'hidden_ids':[2],'declared_slots':2}
    good=[{'source_id':1,'observations':[{'dimension':d,'claim':'有来源的概括','evidence_fields':['desc']} for d in LABELS],
           'application':{'steps':['一步','二步','三步'],'example':{'context':'虚构场景','comment':'示例'},'boundary':'不可推断真人'}}]
    assert validate_data(sources,good,manifest)
    bad_ref=copy.deepcopy(good);bad_ref[0]['observations'][0]['evidence_fields']=['stats.reason']
    missing_dim=copy.deepcopy(good);missing_dim[0]['observations'][0]['dimension']='voice'
    fake_hidden=copy.deepcopy(good);fake_hidden.append({**good[0],'source_id':2})
    for invalid in [bad_ref,missing_dim,fake_hidden,good+good]:
        try:validate_data(sources,invalid,manifest)
        except ValueError:pass
        else:raise AssertionError('Invalid evidence, duplicate or hidden profile accepted')
    print('Self-test passed: evidence binding, unique dimensions/IDs, hidden slots excluded')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['build','validate','self-test'])
    args=parser.parse_args()
    if args.action=='build':build()
    elif args.action=='validate':validate();print('Commentary persona validation passed')
    else:self_test()
