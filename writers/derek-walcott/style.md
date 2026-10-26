# Derek Walcott — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Derek Walcott: Caribbean epic, Homer under a tropical sun, the sea as history, a fisherman's name carrying an epic, language that is English and not English, love after love`
- ZH: 沃尔科特风格：加勒比史诗，热带阳光下的荷马，大海即历史，一个渔夫的名字承载一部史诗，是英语又不是英语的语言，爱在爱之后。

## (2) 句式与节奏

句长：诗行长短不一，史诗体以长句盘旋，抒情短诗以短句收束；节奏靠海浪的起伏推进。节奏：缓慢、辽阔，靠大海与历史的潮汐推进；《奥梅罗斯》以渔夫阿喀琉斯为框架，靠加勒比的日常与荷马的对应推进。`impression`

## (3) 词汇与意象

词汇：英语日常词、加勒比方言词与荷马史诗词并置；‘海’‘渔夫’‘白鹭’是核心词。意象群：大海（历史之海）、渔夫（阿喀琉斯）、白鹭（白色的鸟）、热带阳光、甘蔗园；意象是史诗的零件。禁词/禁意象：不用抽象的哲理议论，不用冷静的旁观，不用直白的控诉。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第三人称史诗叙述与第一人称抒情‘我’交替；叙述者既是史诗的讲述者也是加勒比的见证者。结构：史诗的环形结构、抒情短诗的并置；开头多为一个大海的场景，结尾多为爱或和解的收束。对话：史诗中人物直接说话，渔夫的对话即史诗的对话。`impression`

## (5) 语气与距离

语气：辽阔、热烈、带史诗的庄重；与人物的距离是同情的凝视；与读者的距离是邀约式的——请读者进入加勒比。幽默是温和的，悲悯是主调。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：加勒比的史诗；热带阳光下的荷马；大海即历史；一个渔夫的名字承载一部史诗；爱在爱之后。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No abstract philosophising, no cool detachment, no direct accusation, no flat reportage, no ironic distance`

## (7) 测试提示词示例（现代题材：一个外卖骑手在深夜送餐）

- Prompt: `In the style of Derek Walcott, a food delivery rider works late at night. Caribbean epic: the city is a sea, the rider a fisherman. Homer under neon light. The sea as history. Love after love.`
- 中文对照：沃尔科特风格，一个外卖骑手深夜送餐。加勒比史诗：城市即大海，骑手即渔夫；霓虹灯下的荷马；大海即历史；爱在爱之后。
- Negative: `abstract philosophising, cool detachment, direct accusation, flat reportage, ironic distance`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
