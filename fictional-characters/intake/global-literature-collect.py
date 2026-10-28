#!/usr/bin/env python3
"""Supplement NYT candidates with individually listed global best-selling novels."""
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
import urllib.parse
import urllib.error
from literature_collect import get, verify_wikipedia, NoQualifyingPage

ROOT=Path(__file__).parent
URL='https://en.wikipedia.org/wiki/List_of_best-selling_books'
OUT=ROOT/'global-literature-candidates.jsonl'


class Tables(HTMLParser):
    def __init__(self):
        super().__init__();self.rows=[];self.row=None;self.cell=None;self.depth=0
    def handle_starttag(self,tag,attrs):
        if tag=='table':self.depth+=1
        if self.depth!=1:return
        if tag=='tr':self.row=[]
        elif tag in ('td','th') and self.row is not None:self.cell={'text':[],'links':[]}
        elif tag=='a' and self.cell is not None:
            href=dict(attrs).get('href','')
            if href:self.cell['links'].append(href)
    def handle_data(self,data):
        if self.depth==1 and self.cell is not None:self.cell['text'].append(data)
    def handle_endtag(self,tag):
        if tag=='table':self.depth-=1
        if tag in ('td','th') and self.cell is not None:
            self.cell['text']=' '.join(''.join(self.cell['text']).split())
            self.row.append(self.cell);self.cell=None
        elif tag=='tr' and self.row is not None:
            if self.row:self.rows.append(self.row)
            self.row=None


def main():
    raw=get(URL).decode('utf-8')
    (ROOT/'global-literature-list.html').write_text(raw)
    parser=Tables();parser.feed(raw)
    existing=[json.loads(line) for line in OUT.read_text().splitlines()] if OUT.exists() else []
    known={x['source_url'] for x in existing}
    prior={x['title'].casefold() for x in existing}
    for r in parser.rows:
        # Series tables have another column count; only individually listed books qualify.
        if len(r)!=6 or not re.search(r'\d',r[3]['text']) or r[2]['text']=='Chinese':continue
        genre=r[5]['text'].casefold()
        if not any(x in genre for x in ('novel','fiction','fantasy','romance','thriller','mystery')):continue
        links=[urllib.parse.urlparse(x).path if x.startswith('https://en.wikipedia.org/') else x for x in r[0]['links']]
        href=next((x for x in links if x.startswith(('/wiki/','./')) and ':' not in x),'')
        if not href:continue
        slug=urllib.parse.unquote(href.split('/wiki/')[-1].removeprefix('./'))
        title=slug.replace('_',' ')
        if title.casefold() in prior:continue
        try:
            canonical,count,text,revision,page_title,_,truncated=verify_wikipedia(title,re.sub(r'\[.*?\]','',r[1]['text']).strip())
        except (NoQualifyingPage,urllib.error.HTTPError,TimeoutError) as exc:
            print('SKIP',title,type(exc).__name__,flush=True);continue
        if canonical in known:continue
        author=re.sub(r'\[.*?\]','',r[1]['text']).strip()
        revision_url='https://en.wikipedia.org/w/index.php?'+urllib.parse.urlencode({'title':page_title.replace(' ','_'),'oldid':revision})
        refs=[urllib.parse.urljoin(URL,x) for x in r[4]['links'] if '#cite_note' in x]
        row={'id':'global-'+re.sub(r'[^a-z0-9]+','-',title.casefold()).strip('-'),'title':title,'authors':[author],'medium':'literature','original_language_label':r[2]['text'],'year':int(re.search(r'\d{4}',r[3]['text']).group()) if re.search(r'\d{4}',r[3]['text']) else None,
             'popularity':{'basis':'Individual book listed in Wikipedia sourced historical sales-estimate table; '+r[4]['text'],'url':URL,'note':'Secondary compilation, not audited sales or a current ranking; original references are linked at '+', '.join(refs)},
             'source_url':canonical,'canonical_url':canonical,'source_page_title':page_title,'source_revision':revision,'source_revision_url':revision_url,'source_license':'CC BY-SA 4.0','source_attribution':f'Wikipedia contributors, {page_title}, {revision_url}; accessed 2026-10-28. Selected plot/character sections, joined and possibly truncated; CC BY-SA 4.0.','source_text':text,'source_excerpt_note':'Plot/character sections only; not the whole original book.'+(' Truncated at 10,000 characters.' if truncated else ''),'status':'candidate-verified','source_form_author_verified':True}
        with OUT.open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
        known.add(canonical);prior.add(title.casefold())
        print('SAVED',title,count,flush=True)
        time.sleep(1)


if __name__=='__main__':
    test=Tables();test.feed('<table><tr><td><a href="/wiki/A">A</a></td><td>B</td></tr></table>')
    assert test.rows[0][0]=={'text':'A','links':['/wiki/A']} and test.rows[0][1]['text']=='B'
    main()
