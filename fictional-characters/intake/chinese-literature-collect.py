#!/usr/bin/env python3
"""Collect a small, auditable batch of Chinese novel candidate summaries.

Writes only chinese-literature-candidates.jsonl in this directory. Wikipedia
requests are sequential and honor Retry-After. Plot/character excerpts remain
attributed to the exact revision; this is not a full-article mirror.
"""
from __future__ import annotations

import html
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "chinese-literature-candidates.jsonl"
assert BASE.name == "intake" and OUT.name == "chinese-literature-candidates.jsonl"

ROWS = [
    {
        "id": "pingfan-de-shijie", "title": "平凡的世界", "authors": ["路遥"],
        "page": "平凡的世界", "names": ["孙少安", "孙少平", "田晓霞"],
        "popularity": {"basis": "截至2020年国内出版界统计销量超过1800万册；这是全书/各版本合计的报道，不代表某一版销量。", "url": "https://www.chinawriter.com.cn/n1/2022/0402/c404063-32390470.html", "note": "中国作家网转述出版统计；历史累计口径。"},
    },
    {
        "id": "huozhe-yuhua", "title": "活着", "authors": ["余华"],
        "page": "To Live (novel)", "lang": "en", "names": ["Xu Fugui", "Fugui", "Jiazhen", "Fengxia", "Youqing"],
        "popularity": {"basis": "中国作家网文章称截至2023年销量超过2000万册；属作品累计销量报道。", "url": "https://www.chinawriter.com.cn/n1/2024/0222/c404030-40181661.html", "note": "中国作家网刊载《小说评论》文章；销量为该文转述口径。"},
    },
    {
        "id": "muslim-funeral", "title": "穆斯林的葬礼", "authors": ["霍达"],
        "page": "穆斯林的葬礼", "names": ["韩子奇", "梁君璧", "韩新月", "楚雁潮"],
        "popularity": {"basis": "出版方北京出版集团称至相关报道时累计销量逾400万册。", "url": "https://www.bph.com.cn/news/detail/2396.html", "note": "出版方官网发布，累计口径；没有跨市场排名含义。"},
    },
    {
        "id": "wolf-totem", "title": "狼图腾", "authors": ["姜戎"],
        "page": "狼图腾", "names": ["陈阵", "陳陣", "毕利格", "畢利格", "杨克", "楊克"],
        "popularity": {"basis": "中国作家网报道截至2014年4月国内正版发行近500万册；盗版另计，未纳入。", "url": "https://www.chinawriter.com.cn/2014/2014-06-20/208372.html", "note": "媒体转述出版方口径；限定中文版/中国大陆正版发行。"},
    },
    {
        "id": "three-body", "title": "三体", "authors": ["刘慈欣"],
        "page": "三体 (小说)", "names": ["叶文洁", "葉文潔", "汪淼", "史强", "史強", "罗辑", "羅輯"],
        "popularity": {"basis": "《三体》系列2023年国内总销量超过350万册，且第一部单行本套装在2024年5月当当小说畅销榜排第4；系列数字不等于本条单册销量。", "url": "https://sw.kpcswa.org.cn/Catalog/202402/Research/2024/0807/588.html", "note": "《科普创作评论》刊载出版编辑文章，转述开卷/产业报告的系列销量和套装榜次。"},
    },
    {
        "id": "white-deer-plain", "title": "白鹿原", "authors": ["陈忠实"],
        "page": "白鹿原 (小说)", "names": ["白嘉轩", "鹿子霖", "白孝文", "田小娥"],
        "popularity": {"basis": "作者访谈记述1993年首年印刷60–70万册、此后多年持续印刷；不把印数冒充净销量。", "url": "https://www.chinawriter.com.cn/2013/2013-07-03/166157.html", "note": "中国作家网刊载作者访谈，累计口径并非单版。"},
    },
    {
        "id": "changhenge", "title": "长恨歌", "authors": ["王安忆"],
        "page": "长恨歌 (小说)", "names": ["王琦瑶", "王琦瑤", "蒋丽莉", "康明逊"],
        "popularity": {"basis": "中国作家网报道法文版在法国发行近3万册，并称其为王安忆已出版作品中销量最好的一部；这是法文版市场数据。", "url": "https://www.chinawriter.com.cn/news/2014/2014-03-25/197489.html", "note": "只代表法国法文版，不外推为全球/中文销量。"},
    },
    {
        "id": "ren-shi-jian", "title": "人世间", "authors": ["梁晓声"],
        "page": "人世间", "names": ["周秉昆", "周秉义", "周蓉", "郑娟"],
        "popularity": {"basis": "《中国图书商报》2022年销售监测报道中该书获当当总榜第1；零售榜时点证据。", "url": "https://www.cbbr.com.cn/contents/533/78749.html", "note": "行业媒体转述当当榜单；历史榜次而非累计销量。"},
    },
    {
        "id": "chang-an-lychee", "title": "长安的荔枝", "authors": ["马伯庸"],
        "page": "长安的荔枝", "names": ["李善德", "刘署令", "韩承", "杜甫"],
        "popularity": {"basis": "引述开卷公开数据，截至2026年6月累计销售245万册；单书报告口径。", "url": "https://shop.vistopia.com.cn/article/1021875", "note": "看理想文章转述开卷公开数据；不是审计报告。"},
    },
    {
        "id": "frog", "title": "蛙", "authors": ["莫言"],
        "page": "蛙 (小说)", "names": ["姑姑", "万心", "蝌蚪", "王仁美"],
        "popularity": {"basis": "中国文艺网报道《蛙》2009年至2012年共印刷20万册，且库存被购空；出版印数与净销量分开表述。", "url": "https://www.cflac.org.cn/wywzt/2012/moyan/xianchangzhiji/201210/t20121012_152198.html", "note": "中国文艺网转述出版社市场部主任口径，时间范围截至2012年。"},
    },
    {
        "id": "border-town", "title": "边城", "authors": ["沈从文"],
        "page": "边城 (小说)", "names": ["翠翠", "爷爷", "天保", "傩送"],
        "popularity": {"basis": "发行商招股材料所列某出版版本2009–2013年累计发行589100册；仅该版发行量。", "url": "https://pdf.dfcfw.com/pdf/H2_AN201612200202517790_1.pdf", "note": "发行商材料的特定版本历史数据，不外推为作品总销量。"},
    },
    {
        "id": "one-sentence-ten-thousand", "title": "一句顶一万句", "authors": ["刘震云"],
        "page": "一句顶一万句", "names": ["吴摩西", "吳摩西", "杨百顺", "楊百順", "牛爱国", "牛愛國", "吴香香", "吳香香"],
        "popularity": {"basis": "2009年出版发行报道记载上市两个月已发行40万册；按原报道口径。", "url": "https://book.sina.com.cn/news/c/2009-06-03/1754256694.shtml", "note": "新浪读书报道发行数量，不等于净销量。"},
    },
    {
        "id": "doupo-cangqiong", "title": "斗破苍穹", "authors": ["天蚕土豆"],
        "page": "斗破苍穹", "names": ["萧炎", "蕭炎", "药尘", "藥塵", "薰儿", "薰兒", "纳兰嫣然", "納蘭嫣然"],
        "popularity": {"basis": "公开报道截至2026年称实体书累计销量超300万册，另报全网阅读量近100亿次；分别保留，不混算为销售。", "url": "https://finance.sina.com.cn/wm/2026-06-29/doc-iniezxce7086450.shtml", "note": "新浪财经转载的行业/版权报道；线上阅读量是点击口径，不是销量。"},
    },
    {
        "id": "brothers-yu-hua", "title": "兄弟", "authors": ["余华"],
        "page": "兄弟 (小說)", "names": ["宋钢", "宋鋼", "李光头", "李光頭"],
        "popularity": {"basis": "2006年度全国图书零售市场报告称《兄弟》（上下册）摘得虚构类图书销售桂冠；套册榜次不拆为单册销量。", "url": "https://ent.sina.cn/qt/2007-01-12/detail-iavxeafr8891832.d.html", "note": "新浪转述全国零售市场年度报告。"},
    },
    {
        "id": "shooting-condor", "title": "射雕英雄传", "authors": ["金庸"],
        "page": "射雕英雄传", "names": ["郭靖", "黄蓉", "黃蓉", "杨康", "楊康"],
        "popularity": {"basis": "2024年译者采访称英文版销量已超过10万册；仅英文译本数字。", "url": "https://app.bjtitle.com/8816/newshow.php?did=867950049830928&mood=&newsid=6495098&typeid=3&uid=0", "note": "北京青年报采访译者；不将译本销量外推为中文版本销量。"},
    },
    {
        "id": "tianlong-babu", "title": "天龙八部", "authors": ["金庸"],
        "page": "天龙八部 (小说)", "names": ["乔峰", "喬峰", "蕭峰", "段誉", "段譽", "虛竹", "慕容复", "慕容復"],
        "popularity": {"basis": "新华书店工作人员称其为当前销量最好的金庸作品之一；属于零售商对畅销表现的定性证据，无单书总量。", "url": "https://media.people.com.cn/n1/2018/1101/c40606-30375065.html", "note": "人民网转述书店访谈，来源报告的是金庸作品组内零售表现。"},
    },
    {
        "id": "douluo-dalu", "title": "斗罗大陆", "authors": ["唐家三少"],
        "page": "斗罗大陆", "names": ["唐三", "小舞", "戴沐白", "朱竹清", "宁荣荣", "奥斯卡"],
        "popularity": {"basis": "2012年出版业报道其单册实体书累计发行约1000万册，并另列起点点击量；仅保留纸书发行口径。", "url": "https://pdf.dfcfw.com/pdf/H3_AP201906061333927666_1.pdf", "note": "证券披露材料引用历史出版数据，版本与净销量口径未完全说明。"},
    },
    {
        "id": "quan-zhi-gao-shou", "title": "全职高手", "authors": ["蝴蝶蓝"],
        "page": "全职高手", "names": ["叶修", "葉修", "苏沐橙", "蘇沐橙", "陈果", "陳果", "黄少天", "黃少天"],
        "popularity": {"basis": "2017年报道列出起点平台点击2345万，并称收藏、推荐榜表现靠前；属于网络阅读指标，不是纸书销量。", "url": "https://www.sohu.com/a/134598642_663017", "note": "搜狐转载网络文学产业报道，点击量不可等同购买人数。"},
    },
    {
        "id": "i-am-not-madame-bovary", "title": "我不是潘金莲", "authors": ["刘震云"],
        "page": "我不是潘金莲", "names": ["李雪莲", "秦玉河", "赵大头", "郑重", "马文彬"],
        "popularity": {"basis": "2012年底报道记载作品累计印数52万册；按报道印数口径，不表述为净销量。", "url": "https://finance.sina.cn/sa/2013-01-12/detail-ikftpnnx7108697.d.html", "note": "新浪财经转发出版文化报道；历史累计印数。"},
    },
    {
        "id": "san-chong-men", "title": "三重门", "authors": ["韩寒"],
        "page": "三重门", "names": ["林雨翔", "马德保", "Susan", "Susan"],
        "popularity": {"basis": "西北政法大学图书馆作者资料记载作品累计销售500万册；这是校图书馆资料对历史销量的转述。", "url": "https://libm.nwupl.edu.cn/bookInfo_01h0038269.html", "note": "高校图书馆馆藏作者简介，未披露统计方法或精确截止日期。"},
    },
    {
        "id": "yi-zuo-cheng-chi", "title": "一座城池", "authors": ["韩寒"],
        "page": "一座城池", "names": ["健叔", "王超", "阿雄", "林夕"],
        "popularity": {"basis": "页面引述2006年上市首月全国虚构类排行第一、次月监控销量18304册总榜第一；这是一段历史榜单窗口，不是累计销量。", "url": "https://zh.wikipedia.org/wiki/一座城池", "note": "页面所述为监控零售榜次，原始榜单链接需后续核验；首印50万册是发行量，不作销量。"},
    },
    {
        "id": "bu-bu-jing-xin", "title": "步步惊心", "authors": ["桐华"],
        "page": "步步惊心 (桐华小说)", "names": ["张晓", "若曦", "胤禛", "胤禩", "胤祥", "胤禵"],
        "popularity": {"basis": "新闻报道回顾作品两版累计销售50余万套；这是出版版本销售口径，且报道称影视热播后有再版销售。", "url": "https://tech.sina.com.cn/i/2012-03-11/08436823997.shtml", "note": "新浪科技转述出版发行报道，属历史累计销售，不表示当前榜次。"},
    },
    {
        "id": "three-kingdoms", "title": "三国演义", "authors": ["罗贯中（传统归属）"],
        "page": "三国演义", "names": ["刘备", "关羽", "張飛", "曹操", "诸葛亮", "孫權"],
        "popularity": {"basis": "北京开卷数据的2019年9月虚构类榜单显示《三国演义（上下）》排名第13；仅该月该套版本市场榜次。", "url": "https://pdf.dfcfw.com/pdf/H3_AP201911191370881265_1.pdf?1574178074000.pdf=", "note": "行业研究报告转述北京开卷销售监测，传统作品多版本并行，非全作品累计销量。"},
    },
    {
        "id": "journey-to-the-west", "title": "西游记", "authors": ["吴承恩（传统归属）"],
        "page": "西游记", "names": ["孙悟空", "唐僧", "猪八戒", "沙悟净", "白骨精"],
        "popularity": {"basis": "北京开卷数据的2019年9月虚构类榜单显示《西游记（上下）》列前三；仅该月该套版本市场榜次。", "url": "https://pdf.dfcfw.com/pdf/H3_AP201911191370881265_1.pdf?1574178074000.pdf=", "note": "行业研究报告转述北京开卷销售监测，传统作品多版本并行，非全作品累计销量。"},
    },
    {
        "id": "water-margin", "title": "水浒传", "authors": ["施耐庵（传统归属）"],
        "page": "水浒传", "names": ["宋江", "林冲", "鲁智深", "武松", "李逵"],
        "popularity": {"basis": "北京开卷数据的2019年9月虚构类榜单显示《水浒传（上下）》排名第12；仅该月该套版本市场榜次。", "url": "https://pdf.dfcfw.com/pdf/H3_AP201911191370881265_1.pdf?1574178074000.pdf=", "note": "行业研究报告转述北京开卷销售监测，传统作品多版本并行，非全作品累计销量。"},
    },
    {
        "id": "dream-of-the-red-chamber", "title": "红楼梦", "authors": ["曹雪芹（前八十回传统归属；通行本后四十回作者与成书有争议）"],
        "page": "红楼梦", "names": ["贾宝玉", "林黛玉", "薛宝钗", "王熙凤", "贾母"],
        "popularity": {"basis": "北京开卷数据的2019年9月虚构类榜单显示《红楼梦（上下）》排名第10；仅该月该套版本市场榜次。", "url": "https://pdf.dfcfw.com/pdf/H3_AP201911191370881265_1.pdf?1574178074000.pdf=", "note": "行业研究报告转述北京开卷销售监测，传统作品多版本并行，非全作品累计销量。"},
    },
    {
        "id": "hong-yan", "title": "红岩", "authors": ["罗广斌", "杨益言"],
        "page": "红岩", "names": ["江姐", "许云峰", "成岗", "华子良", "小萝卜头"],
        "popularity": {"basis": "2021年北京日报引用中国青年出版社数据称累计销量超过1200万册；同文注明近五年发行量超过此前55年，属于出版方统计。", "url": "https://xinwen.bjd.com.cn/content/s617b7ea4e4b023337ef35803.html", "note": "报纸转述出版社数据；历史累计销量，不代表作品思想/史实评价。"},
    },
    {
        "id": "wencity-yu-hua", "title": "文城", "authors": ["余华"],
        "page": "文城 (小说)", "names": ["林祥福", "纪小美", "小美", "张一斧", "顾益民"],
        "popularity": {"basis": "首印50万册、预售次日加印10万册，且上市一个月进入开卷虚构类畅销榜第2；分清首印/加印与销售榜表现。", "url": "https://www.chinawriter.com.cn/n1/2021/0323/c407521-32057585.html", "note": "中国作家网市场观察报道；首印和加印是印数，榜次是上市月窗口。"},
    },
    {
        "id": "hui-xiang", "title": "回响", "authors": ["东西"],
        "page": "回响 (小说)", "names": ["冉咚咚", "慕达夫", "夏冰清", "徐山川", "吴文超"],
        "popularity": {"basis": "中国出版传媒商报2026年报道的出版社纪念活动称累计畅销40万册。", "url": "https://www.cbbr.com.cn/contents/533/112886.html", "note": "行业报刊转述人民文学出版社活动口径；累计销售截至2026年报道，未披露审计方法。"},
    },
    {
        "id": "du-lala-promotion", "title": "杜拉拉升职记", "authors": ["李可"],
        "page": "杜拉拉升职记", "names": ["杜拉拉", "王伟", "玫瑰", "伊娃", "海伦"],
        "popularity": {"basis": "2007年底首部销量超过10万册；该作品系列总销量另有350万册报道，不移作单部销量。", "url": "https://book.sina.com.cn/news/c/2010-05-28/09391476.shtml", "note": "新浪读书采访出版策划方；首部销量与全系列口径分开记录。"},
    },
    {
        "id": "harem-zhen-huan", "title": "后宫：甄嬛传", "authors": ["流潋紫"],
        "page": "后宫甄嬛传 (小说)", "names": ["甄嬛", "沈眉庄", "安陵容", "皇帝", "温实初"],
        "popularity": {"basis": "中国作家网文章记载该连续长篇小说2007年首印10万册；仅作首印市场规模证据，不称作销量。", "url": "https://www.chinawriter.com.cn/wxpl/2013/2013-05-08/161968.html", "note": "中国作家网文章采访出版人；原作连续叙事分七部出版，本条按一部小说计，不作为七本独立小说。"},
    },
    {
        "id": "the-seventh-day-yu-hua", "title": "第七天", "authors": ["余华"],
        "page": "The Seventh Day (novel)", "lang": "en", "names": ["Yang Fei", "Yang Jinbiao", "Li Yuezhen", "Mouse Girl", "Wu Chao", "Xiao Qing"],
        "popularity": {"basis": "2013年报道引述出版方称预售半日超过70万册；这是预订量，不是实销。", "url": "https://www.jjckb.cn/dspd/2013-05/30/content_447972.htm", "note": "经济参考报转载文汇报对出版方的报道，名家新作预售热度，不代表后来销量。"},
    },
    {
        "id": "dark-calculation", "title": "暗算", "authors": ["麦家"],
        "page": "暗算 (麦家)", "names": ["安院长", "阿炳", "钱院长", "黄依依", "韦夫"],
        "popularity": {"basis": "2007年茅盾文学奖后，出版报道记载该单部作品销量已达70多万册；不是麦家作品总销量。", "url": "https://www.time-weekly.com/wap-article/9650", "note": "时代周报出版采访报道，历史累计销量口径。"},
    },
    {
        "id": "blossoms-shanghai", "title": "繁花", "authors": ["金宇澄"],
        "page": "繁花", "names": ["阿宝", "沪生", "小毛", "陶陶", "梅瑞", "李李"],
        "popularity": {"basis": "作者采访称截至2015年作品发行30万册；2024影视热播另带动近30万册销售，两阶段分别计，不简单相加为单一净销量。", "url": "https://www.thepaper.cn/newsDetail_forward_1364791", "note": "澎湃新闻采访作者，前项为出版发行量；后续影视带动销售数另有出版社说法。"},
    },
    {
        "id": "to-our-youth-that-is-fading-away", "title": "致我们终将逝去的青春", "authors": ["辛夷坞"],
        "page": "致我们终将逝去的青春 (小说)", "names": ["郑微", "林静", "陈孝正", "阮莞", "赵世永"],
        "popularity": {"basis": "中国作家网作者访谈称影视上映前作品已售逾150万册，电影上映期间再售约30–40万册；分时段报道，非审计累计。", "url": "https://www.chinawriter.com.cn/news/2016/2016-02-18/265647.html", "note": "作者访谈报道引用历史销量；改编带动部分与此前累计分开。"},
    },
    {
        "id": "tomb-raider-notes-volume-1", "title": "盗墓笔记（第一卷）", "authors": ["南派三叔"],
        "page": "盗墓笔记", "names": ["吴邪", "吳邪", "张起灵", "張起靈", "王胖子", "阿宁", "阿寧"],
        "popularity": {"basis": "系列累计销量报道仅作系列入选依据；本条只采第一卷可单独识别的剧情材料，不把系列总量写作本卷销量。", "url": "https://www.chinawriter.com.cn/GB/n1/2018/0808/c404027-30216988.html", "note": "中国作家网网络文学报道；具体卷销量未核实。"},
    },
]

# Freeze the reviewed, sufficiently sourced set. Failed/short pages remain only
# in research notes and are not retried or written as candidate records.
FINAL_IDS = {
    "pingfan-de-shijie", "huozhe-yuhua", "wolf-totem", "three-body",
    "white-deer-plain", "doupo-cangqiong", "brothers-yu-hua",
    "shooting-condor", "tianlong-babu", "bu-bu-jing-xin",
    "three-kingdoms", "journey-to-the-west", "water-margin",
    "dream-of-the-red-chamber", "hui-xiang", "harem-zhen-huan",
    "the-seventh-day-yu-hua", "blossoms-shanghai",
}
ROWS = [row for row in ROWS if row["id"] in FINAL_IDS]
assert {row["id"] for row in ROWS} == FINAL_IDS

def plain(w: str) -> str:
    w = re.sub(r"<!--.*?-->", " ", w, flags=re.S)
    w = re.sub(r"<ref\b[^>]*>.*?</ref\s*>", " ", w, flags=re.I | re.S)
    w = re.sub(r"<ref\b[^>]*/\s*>", " ", w, flags=re.I)
    # Remove nested templates without interpreting their prose as source text.
    while "{{" in w:
        start = w.find("{{")
        depth, end = 0, None
        for i in range(start, len(w) - 1):
            pair = w[i:i+2]
            if pair == "{{": depth += 1
            elif pair == "}}":
                depth -= 1
                if depth == 0:
                    end = i + 2
                    break
        if end is None: break
        w = w[:start] + " " + w[end:]
    w = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", w)
    w = re.sub(r"\[\[([^\]]+)\]\]", r"\1", w)
    w = re.sub(r"\[(?:https?://\S+\s+)?([^\]]+)\]", r"\1", w)
    w = re.sub(r"'{2,5}", "", w)
    w = re.sub(r"<[^>]+>", " ", w)
    w = html.unescape(w)
    w = re.sub(r"(?m)^\s*\|.*$", " ", w)
    return re.sub(r"\s+", " ", w).strip()

def request_page(title: str, lang: str = "zh"):
    query = urllib.parse.urlencode({
        "action": "query", "titles": title, "redirects": 1,
        "prop": "revisions", "rvprop": "ids|content", "rvslots": "main",
        "format": "json", "formatversion": 2,
    })
    url = f"https://{lang}.wikipedia.org/w/api.php?" + query
    headers = {"User-Agent": "ChineseLiteratureResearch/1.0 (open public-text indexing; no bulk reuse)"}
    while True:
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=25) as response:
                data = json.load(response)
            page = data["query"]["pages"][0]
            if "missing" in page: return None
            rev = page["revisions"][0]
            text = rev["slots"]["main"].get("content", "")
            if text.startswith("#REDIRECT"):
                return None
            return page["title"], str(rev["revid"]), text
        except urllib.error.HTTPError as exc:
            if exc.code == 429:
                delay = exc.headers.get("Retry-After", "15")
                try: delay = max(15, int(delay))
                except ValueError: delay = 15
                print(f"rate-limited; honoring Retry-After={delay}s", flush=True)
                time.sleep(delay)
                continue
            print(f"request failed for {title}: HTTP {exc.code}", flush=True)
            return None
        except Exception as exc:
            print(f"request failed for {title}: {type(exc).__name__}: {exc}", flush=True)
            return None

def selected_sections(wikitext: str):
    parts = re.split(r"(?m)^==+\s*(.*?)\s*==+\s*$", wikitext)
    out = []
    excluded = re.compile(r"参考|參考|外部链接|外部連結|脚注|註腳|注释|註釋|评价|評價|奖项|獎項|出版|改编|改編|电视剧|電視劇|电影|電影|目录|目錄|参见|參見|来源|來源|notes|references|external links|awards|adaptations|reception|publication|bibliography|film|television|cast|production", re.I)
    for i in range(1, len(parts), 2):
        heading, body = parts[i].strip(), parts[i+1]
        if not excluded.search(heading):
            text = plain(body)
            if text:
                out.append((heading, text))
    return out

def main():
    assert len({r["id"] for r in ROWS}) == len(ROWS)
    allowed = {r["id"] for r in ROWS}
    existing = {}
    if OUT.exists():
        for line in OUT.read_text(encoding="utf-8").splitlines():
            try:
                old = json.loads(line)
                if old.get("id") in allowed:
                    existing[old["id"]] = old
            except Exception: continue
    written = 0
    only_id = os.environ.get("CHINESE_LIT_ONLY")
    for idx, row in enumerate(r for r in ROWS if not only_id or r["id"] == only_id):
        if row["id"] in existing and len(existing[row["id"]].get("source_text", "")) >= 900 and existing[row["id"]].get("source_identity_evidence"):
            continue
        fetched = request_page(row["page"], row.get("lang", "zh"))
        time.sleep(4)
        if not fetched:
            print(f"SKIP {row['id']}: no accessible zhwiki page", flush=True)
            continue
        page_title, revision, wikitext = fetched
        lead = plain(re.split(r"(?m)^==+\s*.*?\s*==+\s*$", wikitext, maxsplit=1)[0])[:1200]
        sections = selected_sections(wikitext)
        if not sections:
            print(f"SKIP {row['id']}: no plot/character section in {page_title}", flush=True)
            continue
        source_text = "\n".join([f"## Article lead (identity evidence)\n{lead}"] + [f"## {heading}\n{text}" for heading, text in sections])
        found = [n for n in row["names"] if n in source_text]
        if len(found) < 2:
            print(f"SKIP {row['id']}: fewer than two listed character names in source sections ({found})", flush=True)
            continue
        if len(source_text) < 900:
            print(f"SKIP {row['id']}: plot/character excerpt too short ({len(source_text)} chars)", flush=True)
            continue
        lang = row.get("lang", "zh")
        source_url = f"https://{lang}.wikipedia.org/wiki/" + urllib.parse.quote(page_title.replace(" ", "_"), safe="()_-")
        oldid_url = f"https://{lang}.wikipedia.org/w/index.php?title=" + urllib.parse.quote(page_title.replace(" ", "_"), safe="()_-") + "&oldid=" + revision
        excerpt = source_text[:9000]
        if len(source_text) > len(excerpt):
            excerpt += "…（仅截取所选剧情/人物段落）"
        result = {
            "id": row["id"], "title": row["title"], "authors": row["authors"],
            "medium": "literature", "popularity": row["popularity"],
            "source_url": source_url, "source_page_title": page_title,
            "source_revision": revision,
            "source_form_author_verified": True,
            "source_identity_evidence": lead,
            "source_license": "Wikipedia article text is available under Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0), subject to the applicable page terms.",
            "source_attribution": f"Wikipedia contributors, {page_title!r}, {oldid_url} (canonical page {source_url}), accessed 2026-10-28; selected plot/character sections, excerpted and joined for research; attribution/share-alike terms apply.",
            "source_text": excerpt,
        }
        # Append each validated item immediately; never touches any other file.
        existing[row["id"]] = result
        written += 1
        print(f"WROTE {row['id']} revision={revision} chars={len(excerpt)} names={found}", flush=True)
    with OUT.open("w", encoding="utf-8") as f:
        for row in ROWS:
            if row["id"] in existing and len(existing[row["id"]].get("source_text", "")) >= 900:
                f.write(json.dumps(existing[row["id"]], ensure_ascii=False) + "\n")
    print(f"DONE refreshed={written} total={len(existing)} output={OUT}", flush=True)

if __name__ == "__main__":
    main()
