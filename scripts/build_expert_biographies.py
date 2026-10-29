#!/usr/bin/env python3
"""Build source-labelled biographical facets without guessing missing identities."""
import argparse
import copy
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-10-29'
FIELDS = ('birth_places', 'work_locations', 'citizenships', 'ethnicity')

def read(path):
    return json.loads(path.read_text())

def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def names(data):
    keys = [k[:-3] for k in data if k.endswith('_zh') and k != 'test_question_zh' and k[:-3] in data]
    if len(keys) != 1:
        raise ValueError('Ambiguous expert name keys: ' + str(keys))
    return data[keys[0]], data[keys[0] + '_zh']

def entries(root):
    for path in sorted(root.glob('*/*/manifest.json')):
        data = read(path)
        if 'list_position' in data or data.get('kind') == 'expert-method':
            yield path, data

def normalized(value):
    return ''.join(c for c in unicodedata.normalize('NFKD', value).casefold() if c.isalnum())

def parse_lifespan(text):
    # Only unambiguous life ranges become filterable years; activity centuries remain text.
    cleaned = re.sub(r'（在世）|\(living\)', '', text or '').strip()
    match = re.fullmatch(r'(c\.?\s*)?(\d{1,4})\s*(BCE|BC)?\s*[–—−-]\s*(c\.?\s*)?(\d{1,4})?\s*(BCE|BC|CE|AD)?', cleaned)
    if not match:
        return {'birth_year': None, 'death_year': None, 'approximate': False}
    a, b = int(match[2]), int(match[5]) if match[5] else None
    if match[3] in ('BCE', 'BC') or match[6] in ('BCE', 'BC'):
        a = -a
    if b is not None and match[6] in ('BCE', 'BC'):
        b = -b
    if a == 0 or b == 0 or (b is not None and a > b):
        return {'birth_year': None, 'death_year': None, 'approximate': False}
    return {'birth_year': a, 'death_year': b, 'approximate': bool(match[1] or match[4])}

def identify(row, resolved, records):
    candidates = {}
    legacy = parse_lifespan(row.get('dates'))
    for title in row['titles']:
        qid = resolved.get(title, {}).get('qid')
        record = records.get(qid, {})
        if not record.get('human'):
            continue
        aliases = {normalized(x) for x in record.get('names', [])}
        if normalized(row['name']) not in aliases:
            continue
        compared, conflicts = 0, []
        for field in ('birth_year', 'death_year'):
            old = legacy[field]
            values = [v['value'] for v in record.get(field, [])]
            if len(set(values)) > 1:
                conflicts.append(field + '_multiple_claims')
            if old is not None and values:
                compared += 1
                if not any(abs(old - v) <= (30 if legacy['approximate'] else 1) for v in values):
                    conflicts.append(field)
        # A full-name match without a date check is retained only as a review candidate.
        status = 'matched' if compared and not conflicts else 'needs_identity_review'
        candidates[qid] = {'qid': qid, 'status': status, 'conflicts': conflicts,
                           'match_basis': {'name': row['name'], 'compared_date_fields': compared}}
    matches = [x for x in candidates.values() if x['status'] == 'matched']
    if len(matches) == 1:
        return matches[0]
    return {'qid': None, 'status': 'ambiguous' if len(matches) > 1 else 'unresolved', 'candidates': list(candidates.values())}

def one_year(values, fallback):
    if any((v.get('precision') or 9) < 9 or v.get('before', 0) or v.get('after', 0) or v.get('qualifiers', {}).get('P1480') for v in values):
        return {'value': None, 'status': 'unknown', 'claims': values}
    years = sorted({v['value'] for v in values})
    if len(years) > 1:
        return {'value': None, 'status': 'conflict', 'claims': values}
    if years:
        return {'value': years[0], 'status': 'source_recorded', 'claims': values}
    return {'value': fallback, 'status': 'legacy_unverified' if fallback is not None else 'unknown', 'claims': []}

def make_biography(data, relative, source, overrides):
    original = data.get('dates', '')
    legacy = parse_lifespan(original)
    mapping = source['mappings'].get(relative, {'qid': None, 'status': 'unresolved'})
    record = source['records'].get(mapping.get('qid'), {}) if mapping.get('status') == 'matched' else {}
    if mapping.get('status') == 'matched':
        assert record and record.get('human'), 'Matched identity must reference a human source record: ' + relative
        record = copy.deepcopy(record)
        # Full reference chains live once in biography-sources.json; statement IDs retain the link.
        for field in ('birth_year', 'death_year', 'birth_places', 'work_locations', 'citizenships', 'ethnicity'):
            for claim in record.get(field, []):
                claim.pop('references', None)
    english, chinese = names(data)
    collective = any(x in english.lower() for x in ('tradition', 'anonymous', 'lennon–mccartney', 'lennon-mccartney', 'jagger–richards', 'jagger-richards')) or any(x in chinese for x in ('集合体', '集体', '传统', '佚名', '组合', '学派'))
    override = overrides.get(relative, {})
    collective = (collective or data.get('collective') is True or
                  relative in {'cartoonists/clamp','singers/abba','directors/coen-brothers',
                               'architects/herzog-de-meuron','fashion-designers/dolce-gabbana',
                               'astronomers/babylonian-astronomers','dancers/mevlevi-sema','lyricists/jagger-richards'} or
                  override.get('entity_kind') == 'collective_or_tradition')
    if collective:
        record = {}
        mapping = {'qid': None, 'status': 'not_applicable'}
    bio = {
        'schema_version': 1, 'updated_at': DATE,
        'entity_kind': 'person' if record else ('collective_or_tradition' if collective else 'unresolved'),
        'identity': copy.deepcopy(mapping),
        'life': {'original_text': original or None, 'birth_year': one_year(record.get('birth_year', []), legacy['birth_year']),
                 'death_year': one_year(record.get('death_year', []), legacy['death_year']),
                 'legacy_approximate': legacy['approximate'], 'activity_period': None,
                 'living_person_legacy': data.get('living_person')},
        'birth_places': copy.deepcopy(record.get('birth_places', [])),
        'work_locations': copy.deepcopy(record.get('work_locations', [])),
        'citizenships': copy.deepcopy(record.get('citizenships', [])),
        'ethnicity': {'status': 'unknown', 'documented': [], 'unreviewed_source_claims': copy.deepcopy(record.get('ethnicity', []))},
        'legacy_context': {k: data[k] for k in ('field', 'school', 'genre') if data.get(k)},
        'sources': [record['source']] if record else [],
    }
    if not legacy['birth_year'] and original and ('活动' in original or '世纪' in original or collective):
        bio['life']['activity_period'] = {'text': original, 'status': 'legacy_unverified'}
    if collective:
        bio['entity_kind'] = 'collective_or_tradition'
        bio['life']['birth_year'] = one_year([], None)
        bio['life']['death_year'] = one_year([], None)
    if override:
        if override.get('entity_kind'):
            bio['entity_kind'] = override['entity_kind']
        bio['sources'].extend(copy.deepcopy(override.get('sources', [])))
        for field in ('birth_year', 'death_year'):
            if field in override:
                previous_claims = bio['life'][field]['claims']
                date_ids = override.get('date_source_ids', [])
                if isinstance(date_ids, dict):
                    date_ids = date_ids.get(field, [])
                bio['life'][field] = ({'value': override[field], 'status': 'documented', 'claims': [{'value': override[field], 'source_ids': date_ids}]}
                                      if override[field] is not None else one_year([], None))
                if any(c['value'] != override[field] for c in previous_claims):
                    bio['life'][field]['other_source_claims'] = previous_claims
        for field in ('birth_places', 'work_locations', 'citizenships'):
            bio[field].extend(copy.deepcopy(override.get(field, [])))
        bio['ethnicity']['documented'] = copy.deepcopy(override.get('ethnicity', []))
        if override.get('lifespan_text'):
            bio['life']['documented_text'] = override['lifespan_text']
    if bio['ethnicity']['documented']:
        bio['ethnicity']['status'] = 'documented'
    elif bio['ethnicity']['unreviewed_source_claims']:
        bio['ethnicity']['status'] = 'requires_source_review'
    if record and not collective:
        for field in ('birth_year', 'death_year'):
            current = bio['life'][field]
            if legacy[field] is not None and current['value'] is not None and legacy[field] != current['value']:
                current['legacy_disagrees'] = legacy[field]
    birth, death = (bio['life'][f] for f in ('birth_year', 'death_year'))
    if birth['value'] is not None and death['value'] is not None and birth['value'] > death['value']:
        for item in (birth, death):
            item.update(invalid_chronology_value=item['value'], value=None, status='conflict')
    return bio

def validate_biography(bio):
    assert bio['schema_version'] == 1
    assert bio['entity_kind'] in ('person', 'collective_or_tradition', 'unresolved')
    ids = [s['id'] for s in bio['sources']]
    assert len(ids) == len(set(ids)), 'Duplicate biography source'
    for source in bio['sources']:
        assert source['url'].startswith(('https://', 'http://')) and source.get('accessed_at')
    for field in ('birth_year', 'death_year'):
        item = bio['life'][field]
        assert item['value'] is None or (type(item['value']) is int and item['value'] != 0)
        assert item['status'] in ('source_recorded', 'documented', 'legacy_unverified', 'unknown', 'conflict')
        if item['status'] in ('source_recorded', 'documented'):
            assert item['claims'] and all(c.get('source_ids') and set(c['source_ids']) <= set(ids) for c in item['claims'])
        for claim in item['claims'] + item.get('other_source_claims', []):
            assert claim.get('source_ids') and set(claim['source_ids']) <= set(ids)
    for field in ('birth_places', 'work_locations', 'citizenships'):
        for item in bio[field]:
            assert item.get('label') and item.get('source_ids') and set(item['source_ids']) <= set(ids)
            assert item['status'] in ('documented', 'source_recorded')
    for item in bio['ethnicity']['documented']:
        assert item.get('evidence_basis') in ('self_identification', 'explicit_public_biography')
        assert item.get('label') and item.get('source_ids') and set(item['source_ids']) <= set(ids)
    for item in bio['ethnicity']['unreviewed_source_claims']:
        assert item.get('source_ids') and set(item['source_ids']) <= set(ids)
    if bio['entity_kind'] == 'collective_or_tradition':
        assert bio['life']['birth_year']['value'] is None and bio['life']['death_year']['value'] is None
        assert not bio['birth_places'] and not bio['citizenships'] and not bio['ethnicity']['unreviewed_source_claims']
    birth, death = (bio['life'][f]['value'] for f in ('birth_year', 'death_year'))
    assert birth is None or death is None or birth <= death

def render(data, bio):
    english, chinese = names(data)
    def year(key):
        value = bio['life'][key]
        n = value['value']
        label = '未知' if n is None else ('公元前 ' + str(-n) if n < 0 else str(n))
        return label + '（' + value['status'] + '）'
    def places(key):
        return '；'.join(x['label'] + ' [' + ', '.join(x['source_ids']) + ']' for x in bio[key]) or '未知：没有可采纳的记录'
    text = f'# {chinese}（{english}）基本资料\n\n'
    text += '[专家方法](SKILL.md) · [元数据](manifest.json) · [字段说明](../../people/README.md)\n\n'
    text += f"- 对象类型：{bio['entity_kind']}；身份关联：{bio['identity']['status']}。\n"
    text += f"- 原生卒／年代记录：{bio['life']['original_text'] or '原条目未提供'}。\n"
    text += f"- 出生年：{year('birth_year')}；逝世年：{year('death_year')}。\n"
    text += f"- 出生地：{places('birth_places')}。\n- 主要工作地记录：{places('work_locations')}。\n- 国籍／历史政治归属记录：{places('citizenships')}。\n"
    ethnic = bio['ethnicity']
    text += '- 民族／文化认同：' + ('；'.join(x['label'] + ' [' + ', '.join(x['source_ids']) + ']' for x in ethnic['documented']) if ethnic['documented'] else '未知：尚无本轮核读并采纳的明确公开依据') + '。\n'
    if bio['life']['activity_period']:
        text += '- 活动年代原文：' + bio['life']['activity_period']['text'] + '（待独立核实）。\n'
    if bio['life'].get('documented_text'):
        text += '- 本轮核读的年代说明：' + bio['life']['documented_text'].rstrip('。') + '。\n'
    if any(bio['life'][k].get('legacy_disagrees') for k in ('birth_year', 'death_year')):
        text += '- 日期存在与旧记录不一致之处，原文保留；请查看 manifest 中的 legacy_disagrees 后再采用。\n'
    if any(bio['life'][k].get('other_source_claims') for k in ('birth_year', 'death_year')):
        text += '- 日期存在其他来源说法；本条采用已明确引证的传记，其他声明保存在 manifest 的 other_source_claims 中。\n'
    if ethnic['unreviewed_source_claims']:
        text += '\n## 待核对的公开结构化声明\n\n以下仅表示 Wikidata 收录了该声明，尚未核读它的底层出处，不进入默认民族筛选：\n\n'
        for item in ethnic['unreviewed_source_claims']:
            text += f"- {item['label']}；声明 {item.get('statement_id', '')}；底层引用数 {item.get('reference_count', 0)}。\n"
    text += '\n## 来源与使用\n\n'
    for source in bio['sources']:
        text += f"- {source['id']}：[{source['title']}]({source['url']})；访问 {source['accessed_at']}；{source.get('access_note', '结构化记录，非独立史实核验').rstrip('。')}。\n"
    if not bio['sources']:
        text += '- 当前仅整理原 manifest 的记录，没有新增可采纳的外部身份来源。\n'
    text += '\n来源状态与身份核验是不同维度。地域、国籍与民族不能相互代填；这些字段用于历史语境与资料发现，不代表能力、人格或观点。\n'
    return text

def build(root, write=False):
    source = read(root / 'people/biography-sources.json')
    overrides = read(root / 'people/biography-overrides.json')['entries']
    index, counts = [], Counter()
    domain_map = {}
    for domain in read(root / 'domains/index.json')['domains']:
        for relative in domain['existing_paths'] + domain['new_paths']:
            domain_map.setdefault(relative, []).append(domain['id'])
    for path, data in entries(root):
        relative = path.parent.relative_to(root).as_posix()
        bio = make_biography(data, relative, source, overrides)
        validate_biography(bio)
        content = render(data, bio)
        skill_path = path.parent / 'SKILL.md'
        skill = skill_path.read_text()
        link = '\n## 基本资料与筛选\n\n生卒／活动年代、出生地、工作地、国籍与民族／文化认同见 [基本资料](biography.md)；未知与待核对字段明确保留。\n'
        if '[基本资料](biography.md)' not in skill:
            skill = skill.rstrip() + '\n' + link
        if write:
            data['biography'] = bio
            dump(path, data)
            (path.parent / 'biography.md').write_text(content)
            skill_path.write_text(skill)
        else:
            assert data.get('biography') == bio, f'Stale biography: {relative}'
            assert (path.parent / 'biography.md').read_text() == content, f'Stale biography text: {relative}'
            assert '[基本资料](biography.md)' in skill_path.read_text(), f'Missing biography entrypoint: {relative}'
        english, chinese = names(data)
        facets = {'entity_kind': bio['entity_kind'], 'identity': {k: bio['identity'].get(k) for k in ('qid','status')},
                  'life': {k: {f: bio['life'][k][f] for f in ('value','status')} for k in ('birth_year','death_year')},
                  'ethnicity': {'status': bio['ethnicity']['status'], 'documented': bio['ethnicity']['documented']}}
        for field in ('birth_places','work_locations','citizenships'):
            facets[field] = [{k: v[k] for k in ('label','label_en','qid','status','source_ids') if k in v} for v in bio[field]]
        index.append({'path': relative, 'name': english, 'name_zh': chinese, 'domains': domain_map.get(relative, []),
                      'category': path.parts[-3], 'details': relative + '/manifest.json', 'biography': facets})
        counts['entries'] += 1
        counts['identity_' + bio['identity']['status']] += 1
        counts['ethnicity_' + bio['ethnicity']['status']] += 1
        for field in ('birth_places', 'work_locations', 'citizenships'):
            counts[field + '_recorded'] += bool(bio[field])
        for field in ('birth_year', 'death_year'):
            counts[field + '_' + bio['life'][field]['status']] += 1
    payload = {'schema_version': 1, 'updated_at': DATE, 'coverage': 'expert-entry-biographical-facets-not-unique-people', 'entries': index}
    report = {'updated_at': DATE, 'status': 'structural_checks_passed', 'counts': dict(sorted(counts.items())), 'limitations': ['来源收录不等于独立核验；民族默认仅匹配documented。', '缺失值、身份歧义、集合体与日期冲突不自动补造。', '本次未对全部底层传记来源逐条进行人工核读。']}
    if write:
        dump(root / 'people/biographical-index.json', payload)
        dump(root / 'people/biographical-coverage.json', report)
    else:
        assert read(root / 'people/biographical-index.json') == payload
        assert read(root / 'people/biographical-coverage.json') == report
    return report

def selected(row, args):
    bio = row['biography']
    if args.domain and args.domain not in row['domains']:
        return False
    if args.region:
        values = bio[args.region_kind] if args.region_kind != 'any' else sum((bio[k] for k in ('birth_places', 'work_locations', 'citizenships')), [])
        if not any(args.region.casefold() in (v['label'] + ' ' + v.get('label_en', '')).casefold() for v in values):
            return False
    if args.ethnicity and not any(args.ethnicity.casefold() in x['label'].casefold() for x in bio['ethnicity']['documented']):
        return False
    birth = bio['life']['birth_year']
    if args.born_after is not None or args.born_before is not None:
        if birth['value'] is None or birth['status'] not in ('source_recorded', 'documented'):
            return False
        if args.born_after is not None and birth['value'] < args.born_after:
            return False
        if args.born_before is not None and birth['value'] > args.born_before:
            return False
    return True

def self_test():
    assert parse_lifespan('c.624–c.546 BCE')['birth_year'] == -624
    assert parse_lifespan('63 BCE–14 CE')['death_year'] == 14
    assert parse_lifespan('约前 8 世纪')['birth_year'] is None
    assert parse_lifespan('1942–')['death_year'] is None
    assert parse_lifespan('1943– / 1943–')['birth_year'] is None
    row = {'name': 'John Smith', 'name_zh': '约翰', 'dates': '1800–1870', 'titles': ['John Smith']}
    records = {'Q1': {'human': True, 'names': ['John Smith'], 'birth_year': [{'value': 1980}]}}
    assert identify(row, {'John Smith': {'qid': 'Q1'}}, records)['qid'] is None
    records['Q1']['birth_year'] = [{'value': 1800}]
    assert identify(row, {'John Smith': {'qid': 'Q1'}}, records)['status'] == 'matched'
    records['Q1']['names'] = ['约翰']
    assert identify(row, {'John Smith': {'qid': 'Q1'}}, records)['qid'] is None
    records['Q1']['names'] = ['John Smith']
    records['Q1']['birth_year'].append({'value': 1980})
    assert identify(row, {'John Smith': {'qid': 'Q1'}}, records)['qid'] is None
    assert one_year([{'value': 1800}, {'value': 1801}], None)['status'] == 'conflict'
    assert one_year([{'value': 1800, 'precision': 8}], None)['value'] is None
    assert one_year([{'value': -520, 'qualifiers': {'P1480': ['circa']}}], None)['value'] is None
    data = {'name': 'John Smith', 'name_zh': '约翰', 'dates': '1800–1870'}
    source = {'mappings': {'x': {'qid': 'Q1', 'status': 'matched'}}, 'records': {'Q1': {
        'human': True,
        'source': {'id':'B1','url':'https://example.org/bio','accessed_at':DATE},
        'birth_year':[{'value':1800,'source_ids':['B1']}],
        'birth_places':[{'label':'Germany','source_ids':['B1'],'status':'source_recorded'}]}}}
    assert make_biography(data, 'x', source, {'x': {'birth_year': None}})['life']['birth_year']['value'] is None
    collective = make_biography(data, 'x', source, {'x': {'entity_kind':'collective_or_tradition'}})
    validate_biography(collective)
    assert not collective['birth_places'] and collective['identity']['status'] == 'not_applicable'
    wrong = make_biography(data, 'x', source, {'x': {'birth_year':2000,'date_source_ids':['B1']}})
    assert wrong['life']['birth_year']['status'] == 'conflict'
    validate_biography(wrong)
    fake = {'domains': [], 'biography': {'ethnicity': {'documented': [], 'unreviewed_source_claims': [{'label':'汉族'}]}, 'life':{'birth_year':{'value':1800,'status':'legacy_unverified'}}}}
    args = argparse.Namespace(domain=None, region=None, ethnicity='汉族', born_after=None, born_before=None)
    assert not selected(fake, args)
    args.ethnicity = None; args.born_after = 1700
    assert not selected(fake, args)
    print('self-test passed: BCE, namesakes, chronology, uncertainty, null overrides, collectives and ethnicity filtering')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('build','validate','self-test','search'))
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--domain'); parser.add_argument('--region'); parser.add_argument('--ethnicity')
    parser.add_argument('--region-kind', choices=('any','birth_places','work_locations','citizenships'), default='any')
    parser.add_argument('--born-after', type=int); parser.add_argument('--born-before', type=int)
    args = parser.parse_args()
    if args.command == 'self-test':
        self_test()
    elif args.command == 'search':
        result = [r for r in read(args.root / 'people/biographical-index.json')['entries'] if selected(r,args)]
        print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        print(json.dumps(build(args.root,args.command=='build'),ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
