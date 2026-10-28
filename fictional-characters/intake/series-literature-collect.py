#!/usr/bin/env python3
"""Collect individual novels from explicitly documented best-selling series."""
import html
import importlib.util
import json
from pathlib import Path
import re
import time
import urllib.parse
import urllib.error
from literature_collect import get, novel_lead_matches, SectionCollector, bounded_sections, word_count

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location('global_books',ROOT/'global-literature-collect.py')
global_books=importlib.util.module_from_spec(spec);spec.loader.exec_module(global_books)
URL=global_books.URL
OUT=ROOT/'series-literature-candidates.jsonl'
SERIES={'Harry Potter':['Harry Potter'],'Goosebumps':['Goosebumps'],'Percy Jackson & the Olympians':['Percy Jackson'],'Twilight':['Twilight'],'The Chronicles of Narnia':['Narnia'],'A Song of Ice and Fire':['A Song of Ice and Fire'],'The Wheel of Time':['Wheel of Time'],'Discworld':['Discworld'],'The Vampire Chronicles':['Vampire Chronicles'],'Left Behind':['Left Behind'],'The Dark Tower':['Dark Tower'],'Outlander':['Outlander']}
SERIES.update({'Dirk Pitt':['Dirk Pitt'],'James Bond':['James Bond'],'Millennium':['Millennium'],'A Series of Unfortunate Events':['Unfortunate Events'],'Little House on the Prairie':['Little House'],'Tarzan':['Tarzan'],'The Inheritance Cycle':['Inheritance Cycle'],'Redwall':['Redwall'],'Erast Fandorin series':['Erast Fandorin'],"The Hitchhiker's Guide to the Galaxy":['Hitchhiker'],'Wiedźmin (The Witcher)':['Witcher']})


def article_links(cells):
    links=[]
    for c in cells:
        for href in c['links']:
            url=urllib.parse.urljoin('https://en.wikipedia.org/',href)
            parsed=urllib.parse.urlparse(url)
            namespace=urllib.parse.unquote(parsed.path.removeprefix('/wiki/')).split(':',1)[0].casefold()
            if parsed.netloc=='en.wikipedia.org' and parsed.path.startswith('/wiki/') and namespace not in {'file','category','help','special','template','portal','wikipedia','talk'} and not parsed.fragment:
                links.append(url)
    return list(dict.fromkeys(links))


def main():
    listing=global_books.Tables();listing.feed((ROOT/'global-literature-list.html').read_text())
    existing=[json.loads(l) for l in OUT.read_text().splitlines()] if OUT.exists() else []
    known={x['source_url'] for x in existing}
    revisions={x['source_revision'] for x in existing if x.get('source_revision')}
    for row in listing.rows:
        if row[0]['text'] not in SERIES or len(row)!=6 or 'million' not in row[-1]['text']:continue
        name=row[0]['text'];series_url=article_links(row[:1])[0]
        raw=get(series_url).decode('utf-8')
        tables=global_books.Tables();tables.feed(raw)
        candidates=list(dict.fromkeys(link for r in tables.rows if any(re.search(r'\b(?:19|20)\d{2}\b',c['text']) for c in r) for link in article_links(r[:2])))
        # The Goosebumps article delegates its individual-title table to a linked list.
        if name=='Goosebumps':
            links=re.findall(r'href="([^"]+)"',raw)
            extra=next((urllib.parse.urljoin(series_url,html.unescape(x)) for x in links if 'List_of_Goosebumps_books' in x and '#' not in x),None)
            if extra:
                t=global_books.Tables();t.feed(get(extra).decode('utf-8'))
                candidates.extend(link for r in t.rows for link in article_links(r[:2]))
        for url in dict.fromkeys(candidates):
            if url in known:continue
            try:body=get(url).decode('utf-8')
            except (urllib.error.HTTPError,TimeoutError,OSError):continue
            if not novel_lead_matches(body):continue
            paragraphs=re.findall(r'<p\b[^>]*>(.*?)</p>',body,re.S)
            intro=' '.join(' '.join(html.unescape(re.sub(r'<[^>]+>',' ',x)).split()) for x in paragraphs[:12])[:6000]
            if not any(alias.casefold() in intro.casefold() for alias in SERIES[name]):continue
            info=global_books.Tables();info.feed(body)
            series_label=next((r[1]['text'] for r in info.rows if len(r)>=2 and r[0]['text']=='Series'),'')
            if not any(alias.casefold() in series_label.casefold() for alias in SERIES[name]):continue
            author=next((re.sub(r'\[.*?\]','',r[1]['text']).strip() for r in info.rows if len(r)>=2 and r[0]['text'] in ('Author','Authors')),'')
            if not author or not novel_lead_matches(body,author):continue
            sections=SectionCollector();sections.feed(body)
            text,truncated=bounded_sections(sections.sections)
            if word_count(text)<150:continue
            canon=re.search(r'<link rel="canonical" href="([^"]+)"',body)
            canonical=html.unescape(canon.group(1)) if canon else url
            if canonical in known:continue
            title=urllib.parse.unquote(urllib.parse.urlparse(canonical).path.removeprefix('/wiki/')).replace('_',' ')
            revision_match=re.search(r'oldid=(\d+)',html.unescape(body));revision=revision_match.group(1) if revision_match else ''
            if revision and revision in revisions:continue
            revision_url='https://en.wikipedia.org/w/index.php?'+urllib.parse.urlencode({'title':title.replace(' ','_'),'oldid':revision}) if revision else canonical
            item={'id':'series-'+re.sub(r'[^a-z0-9]+','-',title.casefold()).strip('-'),'title':title,'authors':[author],'medium':'literature',
                  'popularity':{'basis':f'Individual novel in the documented best-selling series {name}; reported series sales: {row[-1]["text"]}','url':URL,'note':'Series-level historical estimate from a secondary sourced compilation. Individual-volume sales are not asserted. Series membership source: '+series_url},
                  'source_url':canonical,'canonical_url':canonical,'source_page_title':title,'source_revision':revision,'source_revision_url':revision_url,'source_license':'CC BY-SA 4.0','source_attribution':f'Wikipedia contributors, {title}, {revision_url}; accessed 2026-10-28. Lead and plot/character sections selected and joined; CC BY-SA 4.0.',
                  'source_text':intro[:1800]+'\n\n'+text,'source_identity_evidence':intro[:1200],'source_form_author_verified':True,'source_identity_check_version':4,'series_verified':{'name':name,'url':series_url,'article_series_field':series_label},'source_excerpt_note':'Selected synopsis, not full original book.'+(' Synopsis truncated at 10,000 characters.' if truncated else '')}
            with OUT.open('a') as f:f.write(json.dumps(item,ensure_ascii=False)+'\n')
            known.add(canonical);revisions.add(revision);print('SAVED',name,title,word_count(text),flush=True)
            time.sleep(0.5)


if __name__=='__main__':
    assert article_links([{'links':['/wiki/A','/wiki/File:X','https://example.com/wiki/A','/wiki/A#x']}])==['https://en.wikipedia.org/wiki/A']
    assert article_links([{'links':['/wiki/Novel:_Subtitle']}])==['https://en.wikipedia.org/wiki/Novel:_Subtitle']
    main()
