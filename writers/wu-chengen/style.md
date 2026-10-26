# Wu Cheng'en — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wu Cheng'en: gods and demons in playful vernacular, eighty-one tribulations as a road, comic bickering among pilgrims, the marvellous told as everyday travel`
- ZH: 吴承恩风格：白话写神魔，八十一难成一路，取经人一路拌嘴，奇幻写成日常行旅。

## (2) 句式与节奏

- 章回体而节奏轻快：每回一难、每难一故事；打斗与变化详写、行路略写；语言幽默，对话密。`impression`

## (3) 词汇与意象

- 词汇：词域：白话为主，神魔名目、道佛术语与市井口语并存；善用谐音双关与喜剧绰号；诗赞穿插，雅俗并存。`impression`
- 意象：金箍棒、筋斗云、火焰山、蟠桃、人参果、白骨精；意象群的核心是“变”——七十二变与人心之变。`impression`
- 禁词/禁意象：不用沉重的历史写实、不用板起面孔的说教、不写与取经无关的宫廷权谋、不作冷峻的悲剧收束。

## (4) 叙事视角与结构

- 视角：说书人视角：全知而幽默，时而调侃师徒、时而点破妖怪；视角随取经路走，不潜入内心。`impression`
- 结构：章回体：百回线性西行，八十一难为节；每难自成单元、又前后呼应；开头大闹天宫、结尾取经成功、封号收束。`impression`
- 对话：神魔小说以对话推进取经路上的冲突，孙悟空与妖魔的斗口、师徒问答是主要推进方式。

## (5) 语气与距离

- 语气：幽默、诙谐、讽而不刻；与孙悟空亲近、与妖怪调侃；喜剧底色下藏着修行的严肃。`impression`（学界通说：神魔小说）

## (6) 该写什么 / 不该写什么

- 该写：神魔白话、八十一难、师徒拌嘴、变化打斗、幽默收束。
- 不该写：沉重历史写实、板脸说教、宫廷权谋、冷峻悲剧。
- Negative prompt: `No heavy historical realism, no solemn preaching, no court intrigue, no bleak tragic ending`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Wu Cheng'en, a small Yorkshire terrier sits on a subway seat. Chapter form: the dog as a little pilgrim with a magic cudgel of a leash, the carriage as one tribulation among eighty-one, comic bickering with fellow passengers, the marvellous told as an ordinary ride.`
- 中文对照：吴承恩风格：一只约克夏犬坐在地铁座位上。章回体：犬如小行者，牵引绳如金箍棒，车厢是八十一难中的一难，与乘客一路拌嘴，奇幻写成日常乘车。
- Negative: `heavy historical realism, solemn preaching, court intrigue, bleak tragic ending`
- 检验点：神魔意象是否转入现代场景；师徒式拌嘴是否出现；喜剧底色是否在。
