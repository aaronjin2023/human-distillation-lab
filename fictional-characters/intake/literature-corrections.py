#!/usr/bin/env python3
"""Recover explicitly located novel pages while keeping wrong-source drafts quarantined."""
import json
from pathlib import Path
import urllib.parse
from literature_collect import verify_wikipedia

ROOT=Path(__file__).parent
checks={r['id']:r for r in [json.loads(x) for x in (ROOT.parent/'verification/literature-source-checks.jsonl').read_text().splitlines()] if r.get('audit_version')==4}
out=ROOT/'literature-corrections-candidates.jsonl'
known={json.loads(x)['id'] for x in out.read_text().splitlines()} if out.exists() else set()
for name in ('literature-candidates.jsonl','global-literature-candidates.jsonl'):
    for line in (ROOT/name).read_text().splitlines():
        old=json.loads(line);check=checks.get(old['id'],{})
        identifier=old['id']+'-novel-source-corrected'
        if check.get('ok',True) or not check.get('actual_url') or identifier in known:continue
        title=urllib.parse.unquote(urllib.parse.urlparse(check['actual_url']).path.removeprefix('/wiki/')).replace('_',' ')
        url,count,text,revision,page_title,_,truncated=verify_wikipedia(title,old['authors'][0])
        assert url==check['actual_url'] and url!=old['source_url']
        revision_url='https://en.wikipedia.org/w/index.php?'+urllib.parse.urlencode({'title':page_title.replace(' ','_'),'oldid':revision})
        row={**old,'id':identifier,'source_url':url,'canonical_url':url,'source_page_title':page_title,'source_revision':revision,'source_revision_url':revision_url,'source_text':text,'source_attribution':f'Wikipedia contributors, {page_title}, {revision_url}; accessed 2026-10-28. Plot/character sections selected and joined; CC BY-SA 4.0.','source_form_author_verified':True,'source_identity_check_version':4,'replaces_bad_source_record':old['id'],'source_excerpt_note':'Corrected novel source; prior adaptation/series-source record excluded. Selected synopsis only.'+(' Truncated at cap.' if truncated else '')}
        with out.open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
        known.add(identifier);print('RECOVERED',row['title'],url,flush=True)
