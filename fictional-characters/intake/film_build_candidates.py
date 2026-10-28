#!/usr/bin/env python3
"""Build a bounded, source-traceable film candidate file from the CMU snapshot.

Only reads the three named CMU corpus members; never extracts archive paths.
Character candidates are matched from plot-text name mentions and carry Freebase
character IDs (metadata column 12), never actor or actor-map attributes.
"""
from __future__ import annotations
import csv, gzip, hashlib, io, json, re, tarfile
from collections import defaultdict
from datetime import date
from pathlib import Path

INTAKE = Path(__file__).resolve().parent
CACHE = INTAKE / 'film-cache'
ARCHIVE = CACHE / 'MovieSummaries.tar.gz'
OUTPUT = INTAKE / 'film-candidates.jsonl'
EXCLUSIONS = INTAKE / 'film-exclusions.jsonl'
DATASET_URL = 'https://www.cs.cmu.edu/~ark/personas/'
README_URL = 'https://www.cs.cmu.edu/~ark/personas/data/README.txt'
PAPER_URL = 'https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman%2Boconnor%2Bsmith.acl13.pdf'
LICENSE_URL = 'https://creativecommons.org/licenses/by-sa/3.0/us/'
TARGET = 600
PRIMARY_TARGET = 500
MIN_WORDS = 150
# These are the only archive members accepted; extraction to disk is not used.
ALIASES = {
    'plot': ('plot_summaries.txt', 'plot_summaries.txt.gz'),
    'movies': ('movie.metadata.tsv', 'movie.metadata.tsv.gz'),
    'characters': ('character.metadata.tsv', 'character.metadata.tsv.gz'),
}

def read_member(tf: tarfile.TarFile, accepted: tuple[str, ...]) -> bytes:
    matches = [m for m in tf.getmembers() if Path(m.name).name in accepted and m.isfile()]
    if len(matches) != 1:
        raise RuntimeError(f'Expected exactly one archive member from {accepted}; found {[m.name for m in matches]}')
    member = matches[0]
    if Path(member.name).name not in accepted or member.size > 100_000_000:
        raise RuntimeError(f'Refusing unexpected member: {member.name} ({member.size} bytes)')
    raw = tf.extractfile(member).read()
    if member.name.endswith('.gz'):
        raw = gzip.decompress(raw)
    return raw

def year_of(value: str) -> int | None:
    try:
        return date.fromisoformat(value[:10]).year
    except (ValueError, TypeError):
        m = re.search(r'(?<!\d)(18|19|20)\d{2}(?!\d)', value or '')
        return int(m.group()) if m else None

def freebase_labels(value: str) -> list[str]:
    """Decode the source's Freebase-ID-to-label JSON cell without inventing labels."""
    try:
        obj = json.loads(value)
    except (ValueError, TypeError):
        return []
    return sorted({str(label).strip() for label in obj.values() if str(label).strip()}) if isinstance(obj, dict) else []

NON_TARGET_GENRES = ('documentary', 'concert film', 'concert movie', 'music video', 'short film', 'short subject')
ENDING_FRAGMENTS = {'and', 'or', 'but', 'because', 'with', 'the', 'to', 'of', 'as', 'when', 'after', 'for'}

def severe_damage_flags(summary: str) -> list[str]:
    flags = []
    if summary.count('\ufffd') >= 2:
        flags.append('multiple_unicode_replacement_characters')
    if len(re.findall(r'\{\{[^\n]{0,100}\}\}', summary)) >= 3:
        flags.append('repeated_unexpanded_template_markup')
    if len(re.findall(r'<(?:ref|div|span|br|nowiki)\b', summary, re.I)) >= 3:
        flags.append('repeated_raw_wiki_html')
    words = re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", summary)
    if words and words[-1].casefold() in ENDING_FRAGMENTS:
        flags.append('possibly_truncated_ending')
    return flags

def mention_count(name: str, summary: str) -> int:
    # Full name plus plausible first/last-name references. A short single name is
    # retained in the inventory but not treated as reliable evidence of salience.
    variants = {name.strip()}
    parts = [p for p in re.split(r'\s+', name.strip()) if p]
    if len(parts) > 1:
        variants.update(p.strip('.,:;()[]{}') for p in (parts[0], parts[-1]) if len(p.strip('.,:;()[]{}')) >= 3)
    total = 0
    for variant in variants:
        if len(variant) < 3:
            continue
        pattern = re.compile(r'(?<![A-Za-z0-9])' + re.escape(variant) + r'(?![A-Za-z0-9])', re.I)
        total += len(pattern.findall(summary))
    return total

def main() -> None:
    if not ARCHIVE.is_file():
        raise SystemExit(f'Missing downloaded archive: {ARCHIVE}')
    with tarfile.open(ARCHIVE, 'r:gz') as tf:
        plots_raw = read_member(tf, ALIASES['plot'])
        movies_raw = read_member(tf, ALIASES['movies'])
        chars_raw = read_member(tf, ALIASES['characters'])
    plots: dict[str, tuple[str, str]] = {}
    for line in plots_raw.decode('utf-8', 'replace').splitlines():
        movie_id, sep, summary = line.partition('\t')
        if sep and movie_id.isdigit():
            plots[movie_id] = (summary, hashlib.sha256(line.encode('utf-8')).hexdigest())
    movie_rows: dict[str, list[str]] = {}
    for row in csv.reader(io.StringIO(movies_raw.decode('utf-8', 'replace')), delimiter='\t'):
        if len(row) >= 9 and row[0].isdigit():
            movie_rows[row[0]] = row
    chars: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for row in csv.reader(io.StringIO(chars_raw.decode('utf-8', 'replace')), delimiter='\t'):
        # README column order: 1 Wikipedia movie ID, 4 character name,
        # 11 Freebase character/actor map ID, 12 Freebase character ID.
        if len(row) >= 12 and row[0].isdigit():
            name = row[3].strip()
            character_id = row[11].strip()
            if name and character_id:
                chars[row[0]].append((name, character_id))
    eligible = []
    excluded = []
    for movie_id, (summary, row_hash) in plots.items():
        words = re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", summary)
        meta = movie_rows.get(movie_id)
        title = meta[2].strip() if meta and len(meta) >= 9 else ''
        genre_labels = freebase_labels(meta[8]) if meta else []
        nonfilm = [g for g in genre_labels if any(term in g.casefold() for term in NON_TARGET_GENRES)]
        if nonfilm:
            excluded.append({'id':f'cmu-wp-{movie_id}','title':title,'reason':'non-target audiovisual form by corpus genre metadata','genre_flags':nonfilm,'source_url':f'https://en.wikipedia.org/?curid={movie_id}','plot_row_sha256':row_hash})
            continue
        damage = severe_damage_flags(summary)
        if len(words) < MIN_WORDS:
            if damage:
                excluded.append({'id':f'cmu-wp-{movie_id}','title':title,'reason':'short plot plus severe source-text damage','quality_flags':damage,'source_url':f'https://en.wikipedia.org/?curid={movie_id}','plot_row_sha256':row_hash})
            continue
        if not meta or not meta[2].strip():
            continue
        if 'multiple_unicode_replacement_characters' in damage or 'repeated_unexpanded_template_markup' in damage or 'repeated_raw_wiki_html' in damage:
            excluded.append({'id':f'cmu-wp-{movie_id}','title':title,'reason':'severe source-text damage flag','quality_flags':damage,'source_url':f'https://en.wikipedia.org/?curid={movie_id}','plot_row_sha256':row_hash})
            continue
        try:
            revenue = float(meta[4].replace(',', '').strip())
        except (ValueError, AttributeError):
            continue
        if revenue <= 0:
            continue
        year = year_of(meta[3])
        if year is None:
            continue
        # Retain the complete source character inventory by stable Freebase character ID.
        # Name mentions are only review hints; the plot can use aliases or first names.
        seen = set(); inventory = []
        for name, character_id in chars.get(movie_id, []):
            if character_id in seen:
                continue
            seen.add(character_id)
            inventory.append({'name':name,'character_id':character_id,'name_mention_hint':mention_count(name,summary)})
        named_evidence = sum(1 for c in inventory if c['name_mention_hint'] > 0)
        if len(inventory) < 2 or named_evidence < 2:
            continue
        candidates = sorted(inventory,key=lambda c:(-c['name_mention_hint'],c['name'].casefold(),c['character_id']))
        depicted_person_caution = any('biograph' in g.casefold() or 'biopic' in g.casefold() for g in genre_labels)
        eligible.append((revenue, movie_id, meta, year, summary, row_hash, candidates, len(words), damage, genre_labels, named_evidence, depicted_person_caution))
    eligible.sort(key=lambda x: (-x[0], int(x[1])))
    if len(eligible) < TARGET:
        raise SystemExit(f'Only {len(eligible)} movies meet criteria; refusing to claim a {TARGET}-item list.')
    primary = eligible[:PRIMARY_TARGET]
    primary_ids = {r[1] for r in primary}
    # Use the replacement tranche to widen geographic coverage where metadata
    # supports it: highest-revenue eligible records outside the US-production set.
    # Values remain raw snapshot fields and are not treated as currency-normalized.
    non_us = [r for r in eligible[PRIMARY_TARGET:] if 'United States of America' not in freebase_labels(r[2][7])]
    backup = non_us[:TARGET-PRIMARY_TARGET]
    if len(backup) < TARGET-PRIMARY_TARGET:
        used = primary_ids | {r[1] for r in backup}
        backup.extend(r for r in eligible[PRIMARY_TARGET:] if r[1] not in used and len(backup) < TARGET-PRIMARY_TARGET)
    selected = primary + backup
    with EXCLUSIONS.open('w', encoding='utf-8') as out:
        for rec in excluded:
            out.write(json.dumps(rec,ensure_ascii=False,separators=(',',':'))+'\n')
    with OUTPUT.open('w', encoding='utf-8') as out:
        for rank, (revenue, movie_id, meta, year, summary, row_hash, candidates, nwords, damage, genre_labels, named_evidence, depicted_person_caution) in enumerate(selected, 1):
            title = meta[2].strip()
            record = {
                'id': f'cmu-wp-{movie_id}', 'title': title, 'year': year, 'medium': 'film',
                'popularity': {
                    'basis': 'CMU/Freebase 2012 snapshot box-office field; descending raw numeric value among eligible snapshot entries; backups prioritize records without US production-country label',
                    'value': revenue,
                    'url': README_URL,
                    'note': f"{'Primary raw-revenue rank ' + str(rank) if rank <= PRIMARY_TARGET else 'Non-US-market backup rank ' + str(rank-PRIMARY_TARGET)} in this filtered historical snapshot; not a current worldwide ranking. README specifies the box-office field but not a consistent currency/unit; raw values may be incomparable across markets and are not inflation-adjusted."
                },
                'source_url': f'https://en.wikipedia.org/?curid={movie_id}',
                'source_text': summary,
                'character_candidates': candidates,
                'reported_languages': freebase_labels(meta[6]),
                'production_countries': freebase_labels(meta[7]),
                'status': 'primary-candidate' if rank <= PRIMARY_TARGET else 'backup-substitute',
                'selection_note': 'Positions 1-500 are the highest raw revenue values among eligible corpus records. Positions 501-600 are eligible high-revenue records with no United States production-country label, prioritized as region/language diversity and material-rejection backups. All source character entities with stable Freebase character IDs are preserved; mention hints are not main-character labels.',
                'narrative_name_link_count': named_evidence,
                'depicted_person_caution': depicted_person_caution,
                'data_quality_flags': damage,
                'genre_metadata': genre_labels,
                'provenance': {
                    'dataset': 'CMU Movie Summary Corpus / Freebase metadata',
                    'dataset_url': DATASET_URL, 'readme_url': README_URL,
                    'license': 'CC BY-SA 3.0 US', 'license_url': LICENSE_URL,
                    'citation': 'David Bamman, Brendan O’Connor, Noah A. Smith, Learning Latent Personas of Film Characters, ACL 2013',
                    'paper_url': PAPER_URL, 'wikipedia_movie_id': movie_id,
                    'movie_row_id': movie_id, 'plot_row_sha256': row_hash,
                    'summary_word_count': nwords,
                    'raw_eligible_revenue_rank': next(i for i,r in enumerate(eligible,1) if r[1] == movie_id),
                    'character_id_namespace': 'Freebase character ID (character.metadata.tsv column 12); excludes column 11 character/actor map ID and all actor attributes'
                }
            }
            out.write(json.dumps(record, ensure_ascii=False, separators=(',', ':')) + '\n')
    print(json.dumps({'archive': str(ARCHIVE), 'plots': len(plots), 'movie_metadata': len(movie_rows), 'character_movie_ids': len(chars), 'eligible': len(eligible), 'written': len(selected), 'output': str(OUTPUT)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
