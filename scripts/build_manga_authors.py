#!/usr/bin/env python3
"""Build and check 80 manga-artist and 20 illustrator studies and original drawing briefs."""
import argparse
import copy
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

from distill_characters import normalized, require, write_json
from validate_library import check_links, local_path

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-11-01'
DIMENSIONS = {'line':'线条', 'shapes':'形体与人物', 'composition':'构图', 'panel_rhythm':'分镜节奏',
              'tonal_design':'黑白与网点', 'environment':'环境', 'acting':'表情动作', 'color':'彩色方案'}
ACCESS = {'page_text','search_excerpt','visual_preview','interview_text'}
SUBJECT_ZH = '雨后的浮岛港口，一名成年修理工把迷路的机械鸟归还给一位成年旅人。人物与服饰均为本项目原创。'
SUBJECT_EN = 'At a floating-island harbor after rain, an adult repair technician returns a lost mechanical bird to an adult traveler. Use original characters and clothing designed for this project.'

def text_list(values, minimum):
    return isinstance(values,list) and len(values)>=minimum and all(isinstance(v,str) and v.strip() for v in values)

def check_prompt(prompt, records):
    require(isinstance(prompt,str) and prompt.strip(), 'Empty drawing brief')
    # Author names may identify a requested stage; attribution claims remain prohibited.
    require(not re.search(r'(?:本人亲绘|官方授权作品|officially endorsed|drawn by the artist)',prompt,re.I), 'Unsubstantiated authorship or endorsement')

def check_author(r, root):
    for key in ('id','name','name_zh','name_ja','family','scope','prompt_core_zh','prompt_core_en','sheet_traits_zh'):
        require(isinstance(r.get(key),str) and r[key].strip(), 'Missing author field: '+key)
    require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',r['id']), 'Unsafe author slug')
    require(r.get('kind')=='manga-author-study' and r.get('entity_kind')=='person', 'Only individual author studies count')
    require(r.get('generation_mode')=='original-general-techniques' and r.get('image_validation')=='not-run', 'Do not imply a model or render has been validated')
    require(r.get('status')=='source-grounded-draft' and r.get('task_modes')==['technique-study','work-stage-target'], 'Missing task modes or unsupported acceptance status')
    require(r.get('recipe_basis')=='original_synthesis', 'Creation recipes must retain their evidence boundary')
    require(isinstance(r.get('legacy_refs'),list), 'Legacy references must be explicit')
    for ref in r['legacy_refs']:
        p=local_path(root,ref)/'manifest.json'
        require(p.is_file(), 'Missing legacy author: '+ref)
        old=json.loads(p.read_text())
        require(normalized(old.get('cartoonist',''))==normalized(r['name']), 'Legacy reference is a different author')
    require(r.get('sources') and len({s['id'] for s in r['sources']})==len(r['sources']), 'Missing or duplicate source IDs')
    ids={s['id'] for s in r['sources']}
    require(r.get('creator_type') in ('manga-artist','illustrator'), 'Missing creator category')
    focus=r.get('recent_focus',{})
    require(focus.get('work') and focus.get('date_basis') and focus.get('source_ids') and set(focus['source_ids'])<=ids, 'Unsupported work-stage selection')
    require(focus.get('year') is None or type(focus['year']) is int and 1900<=focus['year']<=2026, 'Invalid focus year')
    require(isinstance(r.get('method_evidence_source_ids'),list) and r['method_evidence_source_ids']
            and set(r['method_evidence_source_ids'])<=ids, 'A drawing study needs method or inspected visual evidence')
    for s in r['sources']:
        for key in ('id','title','url','publisher','accessed_at','access_method','access_note'):
            require(isinstance(s.get(key),str) and s[key].strip(), 'Incomplete source: '+key)
        url=urlsplit(s['url'])
        require(url.scheme in ('https','http') and url.hostname and not url.username and not url.password, 'Unsafe source URL')
        require(s['access_method'] in ACCESS and text_list(s.get('supports'),1), 'Missing source access/support boundary')
    sources={s['id']:s for s in r['sources']}
    for source in sources.values():
        require(source.get('evidence_type') in ('bibliographic-context','inspected-visual','method-statement'), 'Missing source evidence type')
        require(isinstance(source.get('supported_claims'),list), 'Missing explicit source claims')
        if source['evidence_type']=='inspected-visual':
            require(source['access_method']=='visual_preview', 'Visual evidence requires inspected visual access')
        if source['evidence_type']=='method-statement':
            require(source['access_method'] in ('page_text','interview_text'), 'Method statement requires read text')
    for sid in r['method_evidence_source_ids']:
        source=sources[sid]
        require(source['evidence_type']!='bibliographic-context' and text_list(source['supported_claims'],1), 'Bibliography is not method evidence')
        expected='visual_observation' if source['evidence_type']=='inspected-visual' else 'source_summary'
        require(all(any(c.get('basis')==expected and sid in c.get('source_ids',[]) and c.get('text')==claim
                        for c in r['findings']) for claim in source['supported_claims']), 'Method support must resolve to the inspected finding, not only a source ID')
    features=r.get('recognition_features')
    require(isinstance(features,list), 'Missing sourced recognition features')
    require(features or r.get('recognition_unknown')=='No inspected visual finding; work-stage visual target requires references and review.', 'Missing visual features must be explicit unknown')
    for feature in features:
        require(feature.get('text') and feature.get('basis')=='visual_observation' and feature.get('source_ids')
                and set(feature['source_ids'])<=set(r['method_evidence_source_ids']), 'Unsourced recognition feature')
        for sid in feature['source_ids']:
            require(sources[sid]['evidence_type']=='inspected-visual' and feature.get('observation') in sources[sid]['supported_claims'], 'Recognition feature without inspected observation')
        require(feature['text'] in feature['observation'], 'Recognition feature must retain exact observed wording')
    require(r.get('feature_review') in ('single-cover-contract-example','observation-transfer-pending-review'), 'Unknown feature review status')
    require(r.get('reference_works') and r.get('findings'), 'Missing credited works or source findings')
    for work in r['reference_works']:
        require(work.get('title') and work.get('role') and work.get('source_ids') and set(work['source_ids'])<=ids, 'Unsupported work or drawing credit')
    for claim in r['findings']:
        require(claim.get('text') and claim.get('basis') in ('source_summary','visual_observation'), 'Invalid finding')
        require(claim.get('source_ids') and set(claim['source_ids'])<=ids, 'Unresolved finding source')
        if claim['basis']=='visual_observation':
            require(any(s['id'] in claim['source_ids'] and s['access_method']=='visual_preview' for s in r['sources']), 'Visual observation without inspected visual source')
    require(set(r.get('visual_recipe',{}))==set(DIMENSIONS), 'Eight drawing dimensions are required')
    require(all(isinstance(v,str) and v.strip() for v in r['visual_recipe'].values()), 'Empty drawing dimension')
    require(text_list(r.get('recognition_limits'),1), 'Missing recognition limits')
    for key,minimum in [('drawing_steps',4),('review_checks',3),('avoid',2),('best_for',2),('known_gaps',1)]:
        require(text_list(r.get(key),minimum), 'Missing actionable '+key)
    b=r.get('biography',{})
    for field in ('birth_year','death_year'):
        require(field in b and (b[field] is None or type(b[field]) is int), 'Date must be known or explicit null')
        if b[field] is not None:
            require(1700<=b[field]<=2026 and b.get('source_ids') and set(b['source_ids'])<=ids, 'Unsupported biographical year')
    require(b['birth_year'] is None or b['death_year'] is None or b['birth_year']<=b['death_year'], 'Invalid lifespan')
    require(b.get('region_context') and b.get('note') and isinstance(b.get('source_ids'),list) and set(b['source_ids'])<=ids, 'Missing biographical scope')
    require(b.get('ethnicity')=={'value':None,'status':'unknown'}, 'Ethnicity is not inferred by this visual study')

def task_contract(r):
    """Loadable research payload; mode/output selection is still required before execution."""
    return {
        'schema_version':1, 'kind':'manga-task-contract', 'author_id':r['id'],
        'legacy_generation_mode_note':'generation_mode preserves recipe provenance for old consumers; select execution intent through task_modes, not this legacy field.',
        'status':r['status'], 'image_validation':r['image_validation'],
        'modes':{
            'technique-study':'Select compatible techniques for a stated purpose; selection is not a complete author method.',
            'work-stage-target':'Use the exact researched work/stage and all applicable recognition features. Missing visual evidence, unresolved conflicts or discarded identifying features require narrowing the target or marking it unverified.'},
        'required_files':['SKILL.md','drawing.md','manifest.json','task-contract.json','../../WORKFLOW.md'],
        'required_task_inputs':['mode','output_form','target_work_stage','medium','user_character_and_world_constraints'],
        'scope':r['scope'], 'recent_focus':r['recent_focus'], 'sources':r['sources'], 'findings':r['findings'],
        'recognition_features':r['recognition_features'], 'recognition_limits':r['recognition_limits'],
        'recognition_unknown':r.get('recognition_unknown'), 'feature_review':r['feature_review'],
        'method_evidence_source_ids':r['method_evidence_source_ids'],
        'editorial_recipe':r['visual_recipe'], 'steps':r['drawing_steps'], 'checks':r['review_checks'],
        'sheet_traits_zh':r['sheet_traits_zh'], 'avoid':r['avoid'], 'unknowns':r['known_gaps'],
        'replaceable_content':['subject','characters','clothing','props','setting','action','emotion'],
        'adaptation_rules':{
            'all':'Replace example story content in steps/checks; preserve sourced method scope. Record applied, adapted, omitted features and why. Do not paste all eight dimensions into every task.',
            'character-sheet':'Orthographic front/right/back, neutral pose and user body/clothing win. Use only compatible line/shape/tone; omit scene composition, perspective, dramatic gestures and panel rhythm. Adapt shape ratios to the locked user body; log any lost recognition feature.',
            'illustration':'Resolve composition and environment against the user scene; apply color relations only if compatible with locked colors and the selected medium.',
            'six-panel-page':'Panel rhythm from a single cover is editorial synthesis, never observed author page grammar; keep user continuity and panel order.',
            'conflicts':'User identity/body/palette/world and output geometry take priority. Remove or rewrite conflicting instructions, not an appended keep-consistent sentence. If a required identifying feature is lost, disclose reduced target coverage; never claim a full match.'},
        'validation':'Document/source checks only; image resemblance and cross-subject transfer not run.'}


def contract_digest(r):
    return hashlib.sha256(json.dumps(task_contract(r),ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def prompts(r):
    core_zh=r['prompt_core_zh'];core_en=r['prompt_core_en']
    sheet_zh='角色设定页：同一名成年修理工的正面、右侧面、背面三个完整视图；短发、短外套、工具腰带、工作靴，三视图衣物结构及比例一致。中性站姿、平视、无透视夸张、纯净背景，三个完整身体不重叠。'
    sheet_en='Character design sheet: front, right-side and rear full-body views of the same adult repair technician, with short hair, a short work jacket, tool belt and work boots. Keep anatomy, garment construction and proportions consistent. Use neutral standing poses, eye-level orthographic views, a plain background and no overlapping figures.'
    sequence_zh='六格漫画页，按日式从右到左、从上到下阅读。格1港口建立空间；格2修理工发现机械鸟；格3检查鸟翅；格4旅人赶来；格5修理工交还鸟；格6鸟起飞，两人目送。每格明确一个动作，角色、工具及场景方向连续。预留空白对话框，文字后期排版；不要生成签名或水印。'
    sequence_en='A six-panel manga page, read from right to left and top to bottom. Panel 1 establishes the harbor; 2 the technician discovers the bird; 3 inspects its wing; 4 the traveler arrives; 5 the bird is returned; 6 it flies away as both adults watch. Show one clear action per panel; preserve character, prop and screen-direction continuity. Leave speech balloons empty for later lettering. No signatures or watermarks.'
    # Reviewed static traits avoid importing action poses or scene objects into a neutral character sheet.
    sheet_traits=r['sheet_traits_zh']
    return {
        'illustration': {'zh':SUBJECT_ZH+' 单幅叙事插画。'+core_zh+' 不画原作品角色、标志或签名；文字如需出现，保留位置后期排版。',
                         'en':SUBJECT_EN+' One narrative illustration. '+core_en+' No existing franchise designs, logos or signatures. Reserve any text for later lettering.'},
        'character-sheet': {'zh':sheet_zh+' 以下技法服从上述成年角色、服装和站姿约束；只转用造型与画面处理，忽略示例动作和场景：'+sheet_traits,
                            'en':sheet_en+' Apply the following bilingual line, shape and tone specification subject to the adult character, clothing and neutral pose above; omit any example actions and scene directions: '+sheet_traits},
        'six-panel-page': {'zh':SUBJECT_ZH+' '+sequence_zh+' 将以下技法用于各格，不改变上述事件、格数或顺序：'+core_zh,
                           'en':SUBJECT_EN+' '+sequence_en+' Apply the following techniques within each panel without changing the events, panel count or sequence: '+core_en}}

def bullets(items):
    return '\n'.join('- '+x for x in items)

def render(r):
    label=f"{r['name_zh']}（{r['name']}）"
    refs='\n'.join(f"- **{s['id']}** [{s['title']}]({s['url']}) — {s['publisher']}；{s['accessed_at']}；`{s['access_method']}`。{s['access_note']} 支持：{'；'.join(s['supports'])}。" for s in r['sources'])
    facts='\n'.join(f"- {c['text']}〔{c['basis']}；{', '.join(c['source_ids'])}〕" for c in r['findings'])
    credit='\n'.join(f"- {w['title']}：{w['role']}〔{', '.join(w['source_ids'])}〕" for w in r['reference_works'])
    bio=r['biography']
    def year(x):return str(x) if x is not None else '未知／本轮未核定'
    basic=f"出生年：{year(bio['birth_year'])}；逝世年：{year(bio['death_year'])}。\n\n活动／出版语境（非国籍）：{bio['region_context'].rstrip('。')}。民族：未知，不根据姓名或出版地区推断。{bio['note']}"
    if bio['source_ids']:basic+=' 〔'+', '.join(bio['source_ids'])+'〕'
    legacy='\n'.join(f"- [原专业条目](../../../{p}/SKILL.md) · [已有基本资料](../../../{p}/biography.md)" for p in r['legacy_refs']) or '本次新增研究对象；未复制成其他专家分类条目。'
    description=r['name_zh']+'公开漫画／插画研究与原创绘图参谋；适用于'+'、'.join(r['best_for'])+'；按具体视觉技法编写方案。'
    focus=r['recent_focus']; category={'manga-artist':'当代漫画家','illustrator':'日系插画／同人画师'}[r['creator_type']]
    period=f"选材类型：{category}。本轮重点：{focus['work']}；参考年份：{focus['year'] or '未核定'}。{focus['date_basis'].rstrip('。')}。〔{', '.join(focus['source_ids'])}〕"
    skill=f'''---
name: manga-{r['id']}
description: {json.dumps(description,ensure_ascii=False)}
---

# {label} · 漫画／插画创作研究卡

{r['scope']}

{period}

方向：{r['family']}。本卡研究公开作品与方法；绘图配方是本库原创转译，未训练模型、未做出图效果验证。

[100人目录](../../CATALOG.md) · [八维绘画方案](drawing.md) · [绘图提示词](prompts.md) · [结构化记录](manifest.json) · [任务契约](task-contract.json) · [完整创作流程](../../WORKFLOW.md)

## 适用任务

{bullets(r['best_for'])}

先读本页、drawing.md、manifest.json、[任务契约](task-contract.json)和完整流程。选择技法借鉴或指定作品阶段目标；前者可选兼容技法，后者必须逐项处理有来源的关键识别特征，不能以任意少数通用技法代替。作者姓名可用于识别目标与来源，不代表本人绘制或背书。prompts.md只是起稿模板，不是完整执行单元；加载任务契约中的范围、特征、步骤、检查点、冲突与未知，按输出媒介裁剪并记录取舍。

## 本轮公开依据

{facts}

绘画／叙事方法或限定画面观察的依据：{', '.join(r['method_evidence_source_ids'])}。下述原创配方不代表这些来源逐项规定了所有参数。

## 选材与分工

{credit}

## 基本资料

{basic}

{legacy}

## 缺口

{bullets(r['known_gaps'])}

## 来源

{refs}
'''
    drawing=f'# {label} · 八维绘画方案\n\n以下全部是**本库原创创作转译**，不是作者原话或其全部作品的统一规则。对应公开事实与访问范围见[研究卡](SKILL.md)。先确定所选作品阶段，彩色建议不自动视为作者固定色板。\n\n'
    for key,name in DIMENSIONS.items():drawing+=f'## {name}\n\n{r["visual_recipe"][key]}\n\n'
    drawing+='## 落地步骤\n\n'+'\n'.join(f'{i}. {s}' for i,s in enumerate(r['drawing_steps'],1))+'\n\n## 图像检查\n\n'+bullets(r['review_checks'])+'\n\n## 容易失败的做法\n\n'+bullets(r['avoid'])+'\n'
    prompt_text=f'# {label} · 原创绘图提示词\n\n这些是可编辑的起稿模板，**不是完整执行单元**，未实际出图。必须加载[任务契约](task-contract.json)及其中必读文件，选择任务模式后逐项处理关键特征、步骤、检查点、冲突和未知。契约版本SHA256：`{contract_digest(r)}`。比较时统一使用“雨后浮岛港口归还机械鸟”的原创题材。角色设定页只转用形体、线条和黑白处理，不沿用场景镜头；英文版的角色技法段保留中文规格以免未经审核的翻译改变约束。\n\n作者姓名可用于标识指定作品阶段目标，不作全局禁名；不得冒充本人创作或背书。需要其他题材时替换角色、场景、行动和情绪，保留所选择的通用技法；既定发色、发长、肤色、衣色与体型优先，冲突技法或色板必须删改；最后执行[连贯性与输出检查](../../WORKFLOW.md)。\n'
    labels={'illustration':'单幅叙事插画','character-sheet':'角色三视图','six-panel-page':'六格漫画页'}
    for name,pair in prompts(r).items():
        prompt_text+=f'\n## {labels[name]}\n\n### 中文\n\n```text\n{pair["zh"]}\n```\n\n### English / bilingual specification\n\n```text\n{pair["en"]}\n```\n'
    return {'SKILL.md':skill,'drawing.md':drawing,'prompts.md':prompt_text,'manifest.json':json.dumps(r,ensure_ascii=False,indent=2)+'\n','task-contract.json':json.dumps(task_contract(r),ensure_ascii=False,indent=2)+'\n'}

def generated(records):
    output={};catalog=[]
    lines=['# 100位当代漫画家与日系插画师目录','','[使用说明](README.md) · [加载入口](SKILL.md) · [画图流程](WORKFLOW.md) · [机器目录](catalog.json)','',
           '80位当代漫画家＋20位日系插画／同人画师，按个人去重；别名合并，团体不占个人名额。研究卡记录作者，绘图端明确选择技法借鉴或指定作品阶段目标，加载任务契约。并非排名，也不表示全部来源已读全文或画面效果已验证。','']
    for family in sorted({r['family'] for r in records}):
        rows=[r for r in records if r['family']==family]
        lines += ['## '+family,'','| 作者 | 类型与研究阶段 | 选材 / 绘画分工 | 适用任务 |','|---|---|---|---|']
        for r in rows:
            folder='authors/'+r['id']
            for f,body in render(r).items():output[folder+'/'+f]=body
            role='；'.join(w['title']+'（'+w['role']+'）' for w in r['reference_works'])
            lines.append(f"| [{r['name_zh']}]({folder}/SKILL.md) | {r['creator_type']} · {r['recent_focus']['work']}（{r['recent_focus']['year'] or '年份未核'}） | {role.replace('|','／')} | {'、'.join(r['best_for'])} |")
            catalog.append({k:r[k] for k in ('id','name','name_zh','name_ja','family','creator_type','recent_focus','best_for','legacy_refs','generation_mode','image_validation')} | {'path':folder+'/SKILL.md','prompts_path':folder+'/prompts.md','task_contract_path':folder+'/task-contract.json'})
        lines.append('')
    output['CATALOG.md']='\n'.join(lines)
    output['catalog.json']=json.dumps(catalog,ensure_ascii=False,indent=2)+'\n'
    return output

def run(root, build=False):
    base=root/'manga-authors';input_path=base/'authors.json'
    records=json.loads(input_path.read_text())
    require(len(records)==100 and len({r['id'] for r in records})==100, 'Exactly 100 unique author IDs required')
    require(Counter(r.get('creator_type') for r in records)=={'manga-artist':80,'illustrator':20}, 'Exactly 80 manga artists and 20 illustrators required')
    require(len({normalized(r['name']) for r in records})==100 and len({normalized(r['name_ja']) for r in records})==100, 'Aliases must not inflate author count')
    require(len({r['prompt_core_zh'] for r in records})==100, 'Generic renamed prompt templates found')
    for r in records:
        check_author(r,root)
        for variants in prompts(r).values():
            for prompt in variants.values():check_prompt(prompt,records)
    output=generated(records)
    for relative,content in output.items():
        path=base/relative
        if build:
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content)
        require(path.is_file() and path.read_text()==content,'Missing or stale output: '+relative)
    require({p.parent.name for p in (base/'authors').glob('*/manifest.json')}=={r['id'] for r in records}, 'Extra or missing generated authors')
    source_urls={s['url'] for r in records for s in r['sources']}
    receipt={'status':'structural-checks-passed-render-not-run','research_date':DATE,'authors':100,'creator_types':dict(sorted(Counter(r['creator_type'] for r in records).items())),
             'legacy_author_links':sum(bool(r['legacy_refs']) for r in records),
             'new_research_subjects':sum(not r['legacy_refs'] for r in records),
             'generated_author_files':500,'prompt_templates':300,'language_variants':600,
             'source_records':sum(len(r['sources']) for r in records),'unique_source_urls':len(source_urls),
             'access_methods':dict(sorted(Counter(s['access_method'] for r in records for s in r['sources']).items())),
             'finding_basis':dict(sorted(Counter(c['basis'] for r in records for c in r['findings']).items())),
             'recipes':'100 original syntheses and unvalidated task contracts; no image style acceptance',
             'input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),
             'checks':['100 distinct individual author IDs and names','80 manga artists and 20 illustrators','traceable work stages and date bases','source scope and credit references','8 drawing dimensions','different creative briefs','legacy identity links','artist names allowed; no false authorship', 'typed method evidence and exact supported findings', 'sourced recognition features and explicit unknowns', 'loadable task contracts with output conflict rules','generated file equality','local links']}
    receipt['focus_years']=dict(sorted(Counter(str(r['recent_focus']['year']) if r['recent_focus']['year'] is not None else 'unknown' for r in records).items()))
    receipt['focus_years_note']='Reference years include original volumes, project releases and method interviews; not all are artwork creation dates.'
    receipt['authors_with_method_or_visual_evidence']=sum(bool(r['method_evidence_source_ids']) for r in records)
    receipt['authors_with_visual_observations']=sum(any(c['basis']=='visual_observation' for c in r['findings']) for r in records)
    receipt_path=base/'verification/build.json'
    # The README links the receipt; create a pending receipt before checking links, never a premature pass.
    if build:write_json(receipt_path,{'status':'pending-link-check'})
    links=check_links(root,list(base.rglob('*.md')))
    if build:write_json(receipt_path,receipt)
    else:require(json.loads(receipt_path.read_text())==receipt,'Stale verification receipt')
    print(json.dumps(receipt|{'checked_local_links':links},ensure_ascii=False,indent=2))

def self_test(root):
    records=json.loads((root/'manga-authors/authors.json').read_text());r=records[0]
    check_author(r,root)
    for mutate in (lambda x:x['findings'][0].update(source_ids=['missing']),
                   lambda x:x['sources'][0].update(url='javascript:bad'),
                   lambda x:x.update(entity_kind='collective'),
                   lambda x:x['recent_focus'].update(source_ids=['missing']),
                   lambda x:x['recent_focus'].update(year=2029),
                   lambda x:x.update(creator_type='collective'),
                   lambda x:x['biography'].update(birth_year=2000,death_year=1900,source_ids=[x['sources'][0]['id']]),
                   lambda x:x.update(method_evidence_source_ids=[]),
                   lambda x:x['visual_recipe'].pop('acting'),
                   lambda x:x.update(image_validation='passed')):
        bad=copy.deepcopy(r);mutate(bad)
        try:check_author(bad,root)
        except ValueError:pass
        else:raise AssertionError('Invalid research record accepted')
    try:check_prompt('Officially endorsed artwork',records)
    except ValueError:pass
    else:raise AssertionError('False endorsement accepted')
    for prompt in [records[0]['name']+' inspired picture','ONE drawing style','abec drawing style',
                   'Hirohiko Araki, The JOJOLands volume 1 cover study; preserve the original character.']:
        check_prompt(prompt,records)
    for mutate in (
        lambda x:x.update(recognition_features=None),
        lambda x:x.pop('task_modes'),
        lambda x:x.update(drawing_steps=[]),
        lambda x:x.update(review_checks=[]),
        lambda x:next(s for s in x['sources'] if s['id']=='RECENT2').pop('evidence_type'),
        lambda x:x.update(recognition_limits=[]),
        lambda x:x.update(method_evidence_source_ids=[next(s['id'] for s in x['sources'] if s['evidence_type']=='bibliographic-context')]),
        lambda x:x['recognition_features'][0].update(source_ids=['RECENT1']),
        lambda x:next(s for s in x['sources'] if s['id']=='RECENT2').update(supported_claims=['Invented visual claim']),
        lambda x:x['recognition_features'][0].update(text='Generic attractive drawing')):
        bad=copy.deepcopy(next(x for x in records if x['id']=='araki-hirohiko'));mutate(bad)
        try:check_author(bad,root)
        except ValueError:pass
        else:raise AssertionError('Invalid method/feature contract accepted')
    araki=next(x for x in records if x['id']=='araki-hirohiko')
    for mutate in (lambda x:x['visual_recipe'].update(shapes='Changed shape method'),
                   lambda x:x['drawing_steps'].append('New necessary step'),
                   lambda x:x['review_checks'].append('New necessary check'),
                   lambda x:x['recognition_features'][0].update(text='短排线和棱角分面')):
        changed=copy.deepcopy(araki);mutate(changed)
        require(task_contract(changed)!=task_contract(araki), 'Core method did not reach task package')
        require(render(changed)['prompts.md']!=render(araki)['prompts.md'], 'Prompt starter version did not follow core contract')
    require('orthographic' in task_contract(araki)['adaptation_rules']['character-sheet'].lower(), 'Missing sheet conflict resolution')
    require(task_contract(araki)['image_validation']=='not-run', 'False image acceptance')
    print('Self-test passed: invalid evidence/features rejected; names allowed; key method changes reach task contracts and prompt starter versions; output conflicts explicit. Image validation not run.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    mode=parser.add_mutually_exclusive_group();mode.add_argument('--build',action='store_true');mode.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    if args.self_test:self_test(args.root)
    else:run(args.root,args.build)
