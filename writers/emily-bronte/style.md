# Emily Brontë — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emily Brontë: the moor as a soul, passion without apology, nested narrators, the house as a body, weather as feeling, no reconciliation offered`
- ZH: 艾米莉·勃朗特风格：荒原即灵魂，毫不道歉的激情，嵌套的叙述者，房子即身体，天气即情感，不提供和解。

## (2) 句式与节奏

- 句式：句长：长短交错——荒原描写长句绵延，对话短促如风暴；独白长句如歌。
- 节奏：节奏：风暴的节奏——平静、突起、狂暴、回落；嵌套叙述让时间层层折叠。

## (3) 词汇与意象

- 词汇：词汇：荒原、风、雨、石楠、房子与窗、灵魂与鬼魂；爱用强烈的自然词。
- 意象：意象群：呼啸山庄与画眉山庄、荒原与风、窗与鬼魂、希斯克利夫的眼睛、凯瑟琳的灵魂。
- 禁词/禁意象：禁词/禁意象：不写温和的和解，不用礼貌的反讽，不写小世界的精确。

## (4) 叙事视角与结构

- 视角：叙事视角：嵌套叙述——洛克伍德听耐莉讲，耐莉转述他人；叙述的层数即是怀疑的深度；真相在版本之间。
- 结构：结构：两代人的环形结构，第一代激情、第二代和解的可能；开头多为一个场景（雪夜投宿），结尾以墓地收束。

## (5) 语气与距离

- 语气：语气：炽热、冷峻而悲悯；与人物的距离极近（爱他们），与读者的距离如荒原——不迎合。

## (6) 该写什么 / 不该写什么

- 该写：该写：荒原、激情、嵌套叙述、房子与窗、天气即情感。
- 不该写：不该写：温和和解、礼貌反讽、小世界精确。
- Negative prompt: `No gentle reconciliation, no polite irony, no small-world precision, no sentimental comfort`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Emily Brontë, a woman buys oden at a convenience store late at night, and the steam is the moor wind. Passion without apology. Nested narrators. Weather as feeling. No reconciliation offered.`
- 中文对照：艾米莉·勃朗特风格，一位女子深夜在便利店买关东煮，蒸汽即荒原的风。毫不道歉的激情，嵌套的叙述者，天气即情感，不提供和解。
- Negative: `gentle reconciliation, polite irony, small-world precision, sentimental comfort`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
