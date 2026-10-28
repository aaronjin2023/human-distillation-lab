#!/usr/bin/env python3
"""Render and validate source-grounded worldview cards from the two tracked inputs."""
import argparse
import copy
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

from distill_characters import normalized, read_lines, require, write_json

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'worldviews'
LABELS = dict(zip(('reality', 'knowledge', 'agency', 'values', 'order', 'change'),
                  ('世界由什么构成', '凭什么获得知识', '主体能做什么', '价值与取舍', '秩序如何维持', '变化如何发生')))
KINDS = {'real': '现实思想与信念', 'fictional': '虚构世界设定'}
TARGETS = {'real': 50, 'fictional': 50}
BASIS = {'source_summary': '来源概括', 'synthesis': '本库解读', 'unknown': '材料不足'}


def read_records():
    records = []
    for kind in KINDS:
        rows = json.loads((BASE / f'{kind}.json').read_text())
        require(isinstance(rows, list) and rows, f'Empty collection: {kind}')
        require(all(r['kind'] == kind for r in rows), f'Mixed collection: {kind}')
        records.extend(rows)
    return records


def check_records(records, work_ids):
    require(records and len({r['id'] for r in records}) == len(records), 'Duplicate or empty worldview IDs')
    worldview_ids = {r['id'] for r in records}
    require(len({(r['kind'], normalized(r['title'])) for r in records}) == len(records), 'Duplicate titles need review')
    for r in records:
        require(r['kind'] in KINDS and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', r['slug']), 'Invalid kind or slug')
        require(r['id'] == r['kind'] + ':' + r['slug'], 'ID does not bind kind and slug')
        require(all(isinstance(r.get(k), str) and r[k].strip() for k in ('title', 'family', 'scope', 'summary')), 'Missing scope or summary')
        require(isinstance(r['aliases'], list) and all(isinstance(a, str) and a.strip() for a in r['aliases']), 'Invalid aliases')
        require(r['sources'] and len({s['id'] for s in r['sources']}) == len(r['sources']), 'Missing or duplicate source IDs')
        sources = {s['id'] for s in r['sources']}
        for s in r['sources']:
            require(all(isinstance(s.get(k), str) and s[k].strip() for k in ('id', 'url', 'title', 'publisher', 'locator', 'accessed_at', 'access_method', 'support_note')), 'Incomplete source')
            u = urlsplit(s['url'])
            require(u.scheme in ('http', 'https') and u.hostname and not u.username and not u.password, 'Invalid source URL')
            require(s['evidence_kind'] in ('primary', 'authoritative_secondary'), 'Unclassified source')
        require(len(r['claims']) == len(LABELS) and {c['dimension'] for c in r['claims']} == set(LABELS), 'Missing or repeated dimension')
        for c in r['claims']:
            require(c['basis'] in BASIS and isinstance(c['text'], str) and c['text'].strip(), 'Invalid claim')
            require(isinstance(c['source_ids'], list) and set(c['source_ids']) <= sources, 'Unresolved claim source')
            require(c['basis'] == 'unknown' or c['source_ids'], 'Unsupported claim')
        for field in ('boundaries', 'tensions'):
            require(isinstance(r[field], list) and len(r[field]) >= 2 and all(isinstance(t, str) and t.strip() for t in r[field]), f'Missing {field}')
        a = r['application']
        require(a['scope'] == 'original_synthesis' and isinstance(a['steps'], list) and len(a['steps']) == 3 and all(isinstance(s, str) and s.strip() for s in a['steps']), 'Invalid application steps')
        require(all(isinstance(a[k], str) and a[k].strip() for k in ('scenario', 'example')), 'Incomplete application example')
        require(set(r.get('related_work_ids', [])) <= work_ids, 'Unknown character-library work ID')
        related = set(r.get('related_worldview_ids', []))
        require(related <= worldview_ids - {r['id']}, 'Unknown or self-referencing worldview relation')
    return True


def skill_text(r):
    description = f"以{r['title']}分析世界规则、价值冲突与行动条件；仅适用条目限定的思想或作品版本，区分来源、解读与原创设定。"
    lines = ['---', f"name: worldview-{r['kind']}-{r['slug']}", 'description: ' + json.dumps(description, ensure_ascii=False), '---', '',
             '# ' + r['title'], '', r['summary'], '', f"类别：{KINDS[r['kind']]} / {r['family']} · ID：`{r['id']}`", '',
             '**范围**：' + r['scope'], '', '[总目录](../../CATALOG.md) · [结构化记录](manifest.json) · [组合方法](../../README.md)', '',
             '## 使用方式', '', '先确认用户任务和版本。按下列来源理解框架；材料不足就保留未知，新增设定必须标为原创。现实信念不自动成为客观事实，虚构规则不直接用于现实预测。', '',
             '## 六个观察维度', '']
    for c in r['claims']:
        refs = '、'.join(c['source_ids']) or '无充分来源'
        lines += [f"- **{LABELS[c['dimension']]}**（{BASIS[c['basis']]}）：{c['text']}〔{refs}〕"]
    lines += ['', '## 张力与限制', ''] + ['- ' + t for t in r['tensions']]
    lines += [''] + ['- ' + b for b in r['boundaries']]
    if r.get('related_worldview_ids'):
        lines += ['', '相关条目（关系与区别以上述边界为准）：']
        for wid in r['related_worldview_ids']:
            kind, slug = wid.split(':', 1)
            lines += [f'- [{wid}](../../{kind}/{slug}/SKILL.md)']
    lines += ['', '## 原创应用', '', '以下是本库设计的应用，非原典观点或官方续写。', '']
    lines += [f'{i}. {step}' for i, step in enumerate(r['application']['steps'], 1)]
    lines += ['', '**场景**：' + r['application']['scenario'], '', '**示例**：' + r['application']['example'], '', '## 来源', '']
    for s in r['sources']:
        lines += [f"- **{s['id']}** [{s['title']}]({s['url']}) — {s['publisher']}；{s['locator']}。访问：{s['accessed_at']}（{s['access_method']} / {s['evidence_kind']}）。支持：{s['support_note']}"]
    if r.get('related_work_ids'):
        lines += ['', '## 已有人物材料', '', '只按下列作品 ID 查找叙事材料；关联不代表不同改编版本规则相同。', '']
        lines += [f'- [{wid}](../../../fictional-characters/works/{wid}.md)' for wid in r['related_work_ids']]
    return '\n'.join(lines) + '\n'


def generated(records):
    output = {}
    catalog = []
    lines = ['# 世界观目录', '', '[使用说明](README.md) · [加载入口](SKILL.md) · [机器目录](catalog.json)', '',
             '这是有范围限定的资料选集，不是所有思想或虚构宇宙的穷尽清单。', '']
    for kind, label in KINDS.items():
        rows = [r for r in records if r['kind'] == kind]
        lines += [f'## {label}（{len(rows)}）', '', '| 世界观 | 类型 | 限定范围 |', '|---|---|---|']
        for r in rows:
            folder = f"{kind}/{r['slug']}"
            path = folder + '/SKILL.md'
            output[path] = skill_text(r)
            output[folder + '/manifest.json'] = json.dumps(r, ensure_ascii=False, indent=2) + '\n'
            catalog.append({k: r[k] for k in ('id', 'title', 'kind', 'family', 'scope')} | {'path': path})
            lines += [f"| [{r['title']}]({path}) | {r['family']} | {r['scope'].replace('|', '／')} |"]
        lines += ['']
    output['CATALOG.md'] = '\n'.join(lines).rstrip() + '\n'
    output['catalog.json'] = json.dumps(catalog, ensure_ascii=False, indent=2) + '\n'
    return output


def run(build=False):
    records = read_records()
    works = {r['id'] for r in read_lines(ROOT / 'fictional-characters/works.jsonl')}
    check_records(records, works)
    require(dict(Counter(r['kind'] for r in records)) == TARGETS, 'Collection does not meet the requested 50 + 50 scope')
    output = generated(records)
    for relative, content in output.items():
        file = BASE / relative
        if build:
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text(content)
        require(file.exists() and file.read_text() == content, f'Missing or stale output: {relative}')
    cards = {str(f.relative_to(BASE)) for k in KINDS for f in (BASE / k).glob('*/SKILL.md')}
    require(cards == {p for p in output if p.endswith('/SKILL.md')}, 'Extra or missing worldview cards')
    for file in list(BASE.rglob('*.md')):
        for link in re.findall(r'\]\(([^)]+)\)', file.read_text()):
            if '://' not in link and not link.startswith('#'):
                target = (file.parent / link.split('#')[0]).resolve()
                # The build receipt is written only after every other check passes.
                pending_receipt = build and target == (BASE / 'verification/build.json').resolve()
                require(target.exists() or pending_receipt, f'Broken link: {file}: {link}')
    receipt = {'status': 'passed', 'worldviews': dict(Counter(r['kind'] for r in records)),
               'claims': dict(Counter(c['basis'] for r in records for c in r['claims'])),
               'source_records': sum(len(r['sources']) for r in records),
               'unique_source_urls': len({s['url'] for r in records for s in r['sources']}),
               'checks': ['unique scoped IDs', 'six dimensions', 'resolved source IDs', 'source metadata', 'version scope', 'original application label', 'character work references', 'generated content equality', 'local links'],
               'input_sha256': {k + '.json': hashlib.sha256((BASE / (k + '.json')).read_bytes()).hexdigest() for k in KINDS}}
    if build:
        write_json(BASE / 'verification/build.json', receipt)
    else:
        require(json.loads((BASE / 'verification/build.json').read_text()) == receipt, 'Stale verification receipt')
    print(json.dumps(receipt, ensure_ascii=False))


def self_test():
    rows = read_records()
    works = {r['id'] for r in read_lines(ROOT / 'fictional-characters/works.jsonl')}
    assert check_records(rows, works)
    missing_source = copy.deepcopy(rows); missing_source[0]['claims'][0]['source_ids'] = ['not-a-source']
    duplicate_dim = copy.deepcopy(rows); duplicate_dim[0]['claims'][0]['dimension'] = rows[0]['claims'][1]['dimension']
    unsafe_slug = copy.deepcopy(rows); unsafe_slug[0]['slug'] = '../escape'
    missing_scope = copy.deepcopy(rows); missing_scope[0]['scope'] = ''
    wrong_steps = copy.deepcopy(rows); wrong_steps[0]['application']['steps'] = 'abc'
    for bad in (rows + [rows[0]], missing_source, duplicate_dim, unsafe_slug, missing_scope, wrong_steps):
        try:
            check_records(bad, works)
        except ValueError:
            continue
        raise AssertionError('Invalid record accepted')
    print('Worldview self-test passed: duplicates, references, dimensions, paths and scope')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['build', 'validate', 'self-test'])
    args = parser.parse_args()
    if args.action == 'self-test':
        self_test()
    else:
        run(build=args.action == 'build')
