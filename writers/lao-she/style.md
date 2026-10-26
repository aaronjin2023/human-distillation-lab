# Lao She — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lao She: Beijing vernacular with humour, ordinary people in a teahouse, laughter that turns bitter, fate told through daily life`
- ZH: 老舍风格：北京话的幽默，茶馆里的普通人，笑中带苦，命运写于日常。

## (2) 句式与节奏

- 小说：叙事从容、对话密、细节多；话剧《茶馆》：三幕三时代，对话即情节，节奏由慢入快、由笑入悲。`impression`

## (3) 词汇与意象

- 词汇：词域：北京口语、旗人话、市井俚语；用字生动、幽默，善用口语的节奏与歇后语；文言极少。`impression`
- 意象：骆驼祥子的人力车、茶馆、四世同堂的院落、北平的胡同；意象群的核心是“城”——北平即命运的舞台。`impression`
- 禁词/禁意象：不用文言的迂曲、不用空洞的豪言、不写与百姓无关的宏大叙事、不作板起面孔的说教（幽默代替说教）。

## (4) 叙事视角与结构

- 视角：第三人称全知而亲近：叙述者如胡同里的邻居，知人情、懂世故；话剧则完全让人物对话，不作旁白。`impression`
- 结构：小说：线性叙事、由小及大；《茶馆》：三幕式，每幕一时代，人物进出、时代变迁；结尾多为悲凉收束。`impression`
- 对话：京味对话推进情节，人物语言即性格；独白少，对话多，叙述者常退后。

## (5) 语气与距离

- 语气：幽默、温厚、悲凉；与小人物同情、与时代共感；笑是表，苦是里。`impression`（学界通说：幽默与悲凉）

## (6) 该写什么 / 不该写什么

- 该写：北京口语、茶馆众生、幽默、日常命运、笑中带苦。
- 不该写：文言迂曲、空洞豪言、宏大叙事、板脸说教。
- Negative prompt: `No convoluted classical prose, no empty bravado, no grand narrative detached from common people, no solemn lecturing`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Lao She, a man buys oden at a convenience store late at night. Beijing-flavoured vernacular dialogue, the shop as a small teahouse, laughter over small change, and a bitter undertone that arrives without preaching.`
- 中文对照：老舍风格：一个人在深夜便利店买关东煮。北京味口语对白，便利店如小茶馆，为几块钱说笑，苦味不声不响地来，不说教。
- Negative: `convoluted classical prose, empty bravado, grand narrative detached from people, solemn lecturing`
- 检验点：口语是否北京味而幽默；茶馆式众生相是否出现；苦味是否在笑后才来。
