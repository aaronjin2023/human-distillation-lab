#!/usr/bin/env python3
"""Recheck legacy series candidates against each novel's own Series field."""
import importlib.util
import json
from pathlib import Path
import time

BASE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('series_collect',BASE/'series-literature-collect.py')
collect=importlib.util.module_from_spec(spec);spec.loader.exec_module(collect)
OUT=BASE.parent/'verification'/'series-membership-checks.jsonl'

def main():
    rows=[json.loads(l) for l in (BASE/'series-literature-candidates.jsonl').read_text().splitlines()]
    previous=[json.loads(l) for l in OUT.read_text().splitlines()] if OUT.exists() else []
    done={x['id'] for x in previous if x.get('audit_version')==1}
    for row in rows:
        if row['id'] in done or row['series_verified'].get('article_series_field'):continue
        name=row['series_verified']['name']
        try:
            body=collect.get(row['source_url']).decode('utf-8')
            table=collect.global_books.Tables();table.feed(body)
            field=next((r[1]['text'] for r in table.rows if len(r)>=2 and r[0]['text']=='Series'),'')
            form=collect.novel_lead_matches(body,row['authors'][0])
            ok=form and any(alias.casefold() in field.casefold() for alias in collect.SERIES[name])
            result={'id':row['id'],'title':row['title'],'series':name,'article_series_field':field,'form_author_match':form,'ok':ok,'reason':'Novel author/form and explicit infobox series match' if ok else 'Missing or different series field, or novel author/form mismatch','source_url':row['source_url'],'audit_version':1}
        except (OSError,TimeoutError) as e:
            print('FETCH_FAILED',row['id'],str(e),flush=True);continue
        with OUT.open('a') as f:f.write(json.dumps(result,ensure_ascii=False)+'\n')
        print('CHECKED',row['title'],ok,field,flush=True);time.sleep(0.25)

if __name__=='__main__':main()
