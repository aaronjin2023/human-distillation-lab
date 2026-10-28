#!/usr/bin/env python3
"""Check legacy literature intake against the actual novel lead and expected author."""
import json
from pathlib import Path
import time
import urllib.error
from literature_collect import verify_wikipedia, NoQualifyingPage

ROOT=Path(__file__).parent
OUT=ROOT.parent/'verification'/'literature-source-checks.jsonl'

def main():
    checked={r['id'] for r in [json.loads(x) for x in OUT.read_text().splitlines()] if r.get('audit_version')==4} if OUT.exists() else set()
    for name in ('literature-candidates.jsonl','global-literature-candidates.jsonl'):
        path=ROOT/name
        if not path.exists():continue
        for line in path.read_text().splitlines():
            row=json.loads(line)
            if row['id'] in checked:continue
            result={'id':row['id'],'title':row['title'],'expected_author':row['authors'],'expected_url':row['source_url'],'audit_version':4}
            try:
                actual=verify_wikipedia(row.get('source_page_title') or row['title'],row['authors'][0])[0]
                result.update(ok=actual==row['source_url'],actual_url=actual,reason='Novel/novella lead and author surname checked; canonical URL compared.')
            except NoQualifyingPage:
                result.update(ok=False,reason='No matching single-novel lead, author, and plot page; requires manual source review.')
            except (urllib.error.HTTPError,TimeoutError,OSError) as exc:
                print('TEMPORARY ERROR',row['id'],type(exc).__name__,flush=True);continue
            with OUT.open('a') as f:f.write(json.dumps(result,ensure_ascii=False)+'\n')
            checked.add(row['id']);print(row['id'],result['ok'],flush=True)
            time.sleep(0.5)

if __name__=='__main__':main()
