# Nikolai Gogol — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nikolai Gogol: grotesque realism, a nose that walks away, a clerk's overcoat that becomes a soul, laughter through tears, the petty official world inflated to the absurd`
- ZH: 果戈理风格：怪诞现实主义，一只自己走掉的鼻子，一件小公务员的大衣变成灵魂，含泪的笑，微末官僚世界被吹胀成荒诞。

## (2) 句式与节奏

句长：长句堆积、从句层层嵌套，间以短句的笑点；段落长，细节堆积，离题（对某条街、某道菜的长篇议论）本身就是结构。节奏：缓慢、堆积，靠细节与离题的密度推进；《死魂灵》以乞乞科夫的拜访为框架，靠一座座庄园的并置推进。`impression`

## (3) 词汇与意象

词汇：俄语日常词、官僚术语（官阶、公文、请愿）与食物词（饺子、鲟鱼、茶）并置；‘鼻子’‘大衣’‘死魂灵’是核心词。意象群：鼻子（自己走掉的鼻子）、大衣（阿卡基的大衣）、死魂灵（已死农奴的名单）、官僚的办公桌与请愿书；意象是荒诞的零件。禁词/禁意象：不用简洁的极简主义，不用冷静的旁观，不用直白的道德说教。`verbatim`/`artifact`

## (4) 叙事视角与结构

视角：全知叙述者直接介入，边讲故事边议论（‘读者啊’），叙述者与读者直接对话；视角在人物之间滑动，同一事件在不同人物意识中呈现不同形状。结构：拜访的框架 + 庄园的并置、短篇的顿悟式结尾；开头多为一个日常场景（彼得堡的街、办公室），结尾多为含泪的笑或抒情的离题。对话：对话是官僚式的讨价还价，人物靠言语的夸张暴露自己。`verbatim`

## (5) 语气与距离

语气：怪诞、夸张、含泪的笑；与人物的距离是同情的凝视；与读者的距离是直接的——叙述者直接对读者说话。幽默是黑色的，悲悯藏在笑声之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：微末官僚世界被吹胀成荒诞；一只自己走掉的鼻子；一件大衣变成灵魂；含泪的笑；离题的长篇议论。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No minimalist spareness, no cool detachment, no direct moral preaching, no flat reportage, no plain realism`

## (7) 测试提示词示例（现代题材：一个外卖骑手在深夜送餐）

- Prompt: `In the style of Nikolai Gogol, a food delivery rider works late at night. Grotesque realism: the rider's uniform becomes his soul. Laughter through tears. A long digression on the street, the rain, the price of noodles. The petty world inflated to the absurd.`
- 中文对照：果戈理风格，一个外卖骑手深夜送餐。怪诞现实主义：骑手的制服变成他的灵魂；含泪的笑；一段关于街道、雨、面价的长篇离题；微末世界被吹胀成荒诞。
- Negative: `minimalist spareness, cool detachment, direct moral preaching, flat reportage, plain realism`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
