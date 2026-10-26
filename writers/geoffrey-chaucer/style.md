# Geoffrey Chaucer — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chaucer: Middle English rhymed couplets, a pilgrimage frame holding many voices, vivid portraits in a few lines, irony gentle and sharp at once, high and low side by side`
- ZH: 乔叟风格：中古英语双韵体，朝圣框架容纳众声，寥寥数笔的人物速写，温和而锋利的反讽，雅俗并置。

## (2) 句式与节奏

- 句式：句长：双韵对句（rhymed couplets）为主，句式流畅而口语化；人物速写常以一长串并列短语完成。
- 节奏：节奏：朝圣路上的行进节奏——总序缓慢铺陈人物，故事各有快慢，巴斯妇的健谈与骑士的庄重形成对照。

## (3) 词汇与意象

- 词汇：词汇：中古英语，法语与拉丁借词并置；职业、服饰、身体细节极具体；爱用反讽的委婉语。
- 意象：意象群：四月春雨、朝圣之路、塔巴德客栈、马匹与服饰、梦境与命运、巴斯妇的红袜与宽帽。
- 禁词/禁意象：禁词/禁意象：不写单一的道德说教，不用现代英语的直白，不写脱离人物的抽象议论。

## (4) 叙事视角与结构

- 视角：叙事视角：第一人称朝圣者（乔叟本人）为框架叙述者，各故事由各自的讲者讲述；视角多层，叙述者时而天真、时而狡黠。
- 结构：结构：框架故事（朝圣 + 讲故事比赛）套住二十四个故事，计划约一百二十个、未完成；故事顺序在各抄本中不一，编排本身即是争议。`artifact`（大英图书馆梳理，本次搜索核对）

## (5) 语气与距离

- 语气：语气：温和、幽默而锋利；同情人物又不放过他们的虚伪；与读者的距离如旅伴，边走边说。

## (6) 该写什么 / 不该写什么

- 该写：该写：人物速写、框架与众声、雅俗并置、温和的反讽、朝圣之路。
- 不该写：不该写：单一道德说教、现代直白、脱离人物的抽象议论。
- Negative prompt: `No single moral sermon, no modern bluntness, no abstract digression detached from character`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Chaucer, a small Yorkshire terrier sits on a subway seat among pilgrims of the morning commute. Rhymed couplets. A vivid portrait in a few lines. Gentle irony. High and low side by side.`
- 中文对照：乔叟风格，一只小约克夏犬坐在地铁座位上，与早高峰的朝圣者们同行。双韵对句，寥寥数笔的人物速写，温和的反讽，雅俗并置。
- Negative: `single moral sermon, modern bluntness, abstract digression`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
