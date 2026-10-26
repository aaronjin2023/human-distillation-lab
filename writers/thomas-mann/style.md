# Thomas Mann — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thomas Mann: ironic distance, long reflective sentences, time stretched and examined, the bourgeois world observed with sympathy and judgement, art and sickness and death in slow conversation`
- ZH: 托马斯·曼风格：反讽的距离，绵长沉思的句子，时间被拉长、被审视，资产阶级世界被同情又被审判地观察，艺术、疾病与死亡在缓慢对话。

## (2) 句式与节奏

句长：长句为主，从句层层嵌套，间以精妙的反讽插入语；段落长，议论与叙事交织，一段可同时完成场景、心理与评论。节奏：缓慢、沉思，时间被刻意拉长（《魔山》七年写成一千页，一天可以写一章）；情节推进慢，靠对话与内心辩论推进。`impression`

## (3) 词汇与意象

词汇：德语书面语的典雅与精确，音乐、疾病、时间、艺术词汇反复出现；拉丁语与法语词点缀。意象群：时间（魔山的七年、威尼斯的夏天）、疾病与疗养院（高山、雪、体温）、艺术与堕落（威尼斯之死的美少年）、商人家族的衰落（布登勃洛克的房子与账本）。禁词/禁意象：不用短促的动作白描，不用直白的激情宣泄，不用通俗的悬念。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第三人称全知，但带反讽的距离——叙述者既同情人物又审判人物，常以‘我们’式的议论介入；《魔山》中叙述者直接与读者讨论‘时间’。结构：编年与沉思交织（《布登勃洛克一家》四代编年史）、封闭空间中的长对话（《魔山》疗养院）、中篇的凝练悲剧（《威尼斯之死》）。开头多为平静的日常切入，结尾多为死亡或衰落的收束。对话：长对话是思想的载体（塞特姆布里尼与纳夫塔的辩论），对话即论战。`impression`

## (5) 语气与距离

语气：庄重中带反讽，同情中带审判；与人物的距离是‘有距离的爱’；与读者的距离是邀约式的沉思——请读者与叙述者一起思考时间、艺术与死亡。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一个家族四代的衰落；疗养院或封闭空间中的长对话；时间如何被拉长、被浪费、被审视；艺术与疾病、美与死亡的纠缠；资产阶级的礼仪与内在空虚。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No short action-driven scenes, no direct emotional outpouring, no cheap suspense, no flat reportage, no unironic heroism`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Thomas Mann, a man buys oden at a convenience store late at night. Long reflective sentences. The steam, the fluorescent light, and time itself becomes the subject — how long is a night, how is a life measured. Ironic distance, sympathy and judgement together. A conversation with the clerk becomes a debate about modern life.`
- 中文对照：托马斯·曼风格，一个人在深夜便利店买关东煮。长句沉思；蒸汽、日光灯，而时间本身成为主题——一夜有多长，一生如何度量；反讽的距离，同情与审判并存；与店员的对话变成一场关于现代生活的辩论。
- Negative: `short action-driven scenes, direct emotional outpouring, cheap suspense, flat reportage, unironic heroism`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
