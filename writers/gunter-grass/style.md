# Günter Grass — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Günter Grass: grotesque picaresque, a tin drum beating against history, the fantastic erupting from the everyday, Danzig as a lost world, language that piles up and spills over`
- ZH: 格拉斯风格：怪诞的流浪汉小说，一面铁皮鼓敲打历史，幻想从日常中迸发，但泽作为失落的世界，语言堆积、溢出。

## (2) 句式与节奏

句长：长句堆积、从句层层嵌套，间以短句的鼓点（‘咚、咚、咚’）；段落长，细节堆积如山，一段可同时完成场景、历史与幻想。节奏：缓慢、堆积，靠细节的密度推进；《铁皮鼓》以奥斯卡的回忆为框架，时间跳接，节奏靠‘鼓声’的反复驱动。`verbatim`

## (3) 词汇与意象

词汇：德语日常词、但泽方言词、食物与身体词（鳗鱼、土豆、鼓）与历史词（战争、纳粹、流亡）并置；‘鼓’是核心词。意象群：铁皮鼓（敲打历史的工具）、鳗鱼（但泽的海味与死亡）、土豆与食物、侏儒与巨人、但泽的街道与港口；意象靠堆积获得重量。禁词/禁意象：不用简洁的极简主义，不用冷静的旁观，不用直白的道德评判。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第一人称回忆（奥斯卡的自述）与第三人称的史诗叙述交替；叙述者不可靠——奥斯卡自称三岁决定不再长大，读者自行判断真假。结构：回忆的框架 + 插曲的堆积，时间跳接，靠鼓声与母题回环；开头多为一个怪诞的前提（‘我三岁决定不再长大’），结尾多为历史的收束而非个人的解决。对话：对话是流浪汉式的讨价还价，人物靠夸张与谎言暴露自己。`verbatim`

## (5) 语气与距离

语气：怪诞、夸张、带讽刺的热情；与人物的距离是同情的凝视；与读者的距离是邀约式的——请读者听鼓声，而不是读历史教科书。幽默是黑色的，悲悯藏在夸张之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一个怪诞的前提（不再长大的孩子、一面铁皮鼓）；但泽作为失落的世界；幻想从日常中迸发；历史靠细节的堆积显形；语言的溢出与夸张。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No minimalist spareness, no cool detachment, no direct moralising, no flat reportage, no plain realism`

## (7) 测试提示词示例（现代题材：一个外卖骑手在深夜送餐）

- Prompt: `In the style of Günter Grass, a food delivery rider works late at night. Grotesque picaresque: the rider beats a tin drum against the city's history. Details pile up — the food, the rain, the streets. The fantastic erupts from the everyday. Language piles up and spills over.`
- 中文对照：格拉斯风格，一个外卖骑手深夜送餐。怪诞的流浪汉小说：骑手敲着一面铁皮鼓对抗城市的历史；细节堆积——食物、雨、街道；幻想从日常中迸发；语言堆积、溢出。
- Negative: `minimalist spareness, cool detachment, direct moralising, flat reportage, plain realism`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
