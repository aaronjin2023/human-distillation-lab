#!/usr/bin/env python3
"""Add named Chinese novels with explicit historical purchase/chart evidence."""
import html
import json
from pathlib import Path
import re
import time
from urllib.parse import quote, urlencode
from literature_collect import get, novel_lead_matches, SectionCollector, bounded_sections, word_count

BASE=Path(__file__).parent
JIN='https://ip.people.com.cn/n1/2019/0122/c179663-30583592.html'
MO='https://www.chinanews.com/cul/2013/01-11/4481265.shtml'
TAN='https://www.chinanews.com/cul/2012/11-09/4315909.shtml'
YU='https://www.sohu.com/a/771779927_121117491'
TITLES=[
('笑傲江湖','The Smiling, Proud Wanderer','Jin Yong',JIN),
('鹿鼎记','The Deer and the Cauldron','Jin Yong',JIN),
('倚天屠龙记','The Heaven Sword and Dragon Saber','Jin Yong',JIN),
('神雕侠侣','The Return of the Condor Heroes','Jin Yong',JIN),
('书剑恩仇录','The Book and the Sword','Jin Yong',JIN),
('雪山飞狐','Fox Volant of the Snowy Mountain','Jin Yong',JIN),
('碧血剑','Sword Stained with Royal Blood','Jin Yong',JIN),
('飞狐外传','The Young Flying Fox','Jin Yong',JIN),
('侠客行','Ode to Gallantry','Jin Yong',JIN),
('连城诀','A Deadly Secret','Jin Yong',JIN),
('蛙','Frog (novel)','Mo Yan',MO),
('丰乳肥臀','Big Breasts and Wide Hips','Mo Yan',MO),
('红高粱家族','Red Sorghum (novel)','Mo Yan',MO),
('生死疲劳','Life and Death Are Wearing Me Out','Mo Yan',MO),
('檀香刑','Sandalwood Death','Mo Yan',TAN),
('许三观卖血记','Chronicle of a Blood Merchant','Yu Hua',YU)]

def main():
    out=BASE/'chinese-supplement-candidates.jsonl'
    existing=[json.loads(l) for l in out.read_text().splitlines()] if out.exists() else []
    known={r['title'] for r in existing}
    for title,page,author,popularity_url in TITLES:
        if title in known:continue
        url='https://en.wikipedia.org/wiki/'+quote(page.replace(' ','_'),safe='(),')
        try:body=get(url).decode('utf-8')
        except (OSError,TimeoutError) as e:print('FETCH_FAILED',title,str(e),flush=True);continue
        if not novel_lead_matches(body,author):print('IDENTITY_FAILED',title,flush=True);continue
        sections=SectionCollector();sections.feed(body)
        text,truncated=bounded_sections(sections.sections)
        if word_count(text)<150:print('SHORT',title,word_count(text),flush=True);continue
        paragraphs=re.findall(r'<p\b[^>]*>(.*?)</p>',body,re.S)
        intro=' '.join(' '.join(html.unescape(re.sub(r'<[^>]+>',' ',x)).split()) for x in paragraphs[:12])[:1800]
        canonical_match=re.search(r'<link rel="canonical" href="([^"]+)"',body)
        canonical=html.unescape(canonical_match.group(1)) if canonical_match else url
        revision_match=re.search(r'oldid=(\d+)',html.unescape(body))
        if not revision_match:print('NO_REVISION',title,flush=True);continue
        revision=revision_match.group(1)
        revision_url='https://en.wikipedia.org/w/index.php?'+urlencode({'title':page.replace(' ','_'),'oldid':revision})
        basis='京东金庸单书购买排行，2018-10-30事件期报道' if author=='Jin Yong' else ('2012年开卷虚构畅销榜报道列名作品' if author=='Mo Yan' else '2024年3月开卷实体店虚构类新书销量第4名（2024版；转引）')
        row={'id':'chinese-'+re.sub(r'[^a-z0-9]+','-',page.casefold()).strip('-'),'title':title,'authors':[author],'medium':'literature','original_language_label':'Chinese',
             'popularity':{'basis':basis,'url':popularity_url,'note':'历史榜单或购买排行；不据此主张当前销量、全球名次或单册累计销量。'},
             'source_url':canonical,'canonical_url':canonical,'source_revision':revision,'source_revision_url':revision_url,'source_license':'CC BY-SA 4.0',
             'source_attribution':f'Wikipedia contributors, {page}, {revision_url}; accessed 2026-10-28. Selected lead and narrative sections; CC BY-SA 4.0.',
             'source_text':intro+'\n\n'+text,'source_identity_evidence':intro,'source_form_author_verified':True,'source_identity_check_version':4,
             'source_excerpt_note':'Public synopsis, not the original novel.'+(' Plot/character excerpt capped at 10,000 characters.' if truncated else '')}
        with out.open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
        known.add(title);print('SAVED',title,word_count(text),flush=True);time.sleep(0.5)

if __name__=='__main__':
    assert len({x[0] for x in TITLES})==len(TITLES)==16
    main()
