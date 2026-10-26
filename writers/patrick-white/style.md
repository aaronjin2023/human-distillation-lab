# Patrick White — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Patrick White: epic of the Australian interior, vast landscapes holding small souls, symbolic realism, a visionary outsider against a philistine town, sentences that swell like weather`
- ZH: 怀特风格：澳大利亚内陆的史诗，辽阔的风景装下渺小的灵魂，象征现实主义，一个 visionary 的局外人对抗庸俗的小镇，句子如天气般涨落。

## (2) 句式与节奏

句长：长句为主，从句层层嵌套，间以短句的顿悟；段落长，一段可同时完成风景、人物与象征。节奏：缓慢、史诗，靠内陆的辽阔与时间的绵延推进；《沃斯》以探险为框架，靠沙漠的并置推进。`impression`

## (3) 词汇与意象

词汇：英语日常词、澳大利亚内陆词（沙漠、桉树、尘土）与象征词（眼睛、风暴、树）并置；‘眼睛’‘风暴’‘树’是核心词。意象群：沙漠（内陆的荒漠）、风暴之眼（平静的核心）、树（人树）、眼睛（ visionary 的眼睛）；意象是象征的零件。禁词/禁意象：不用简洁的极简主义，不用冷静的旁观，不用直白的道德评判。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第三人称全知，叙述者直接介入，边讲故事边议论；视角在人物之间滑动，同一事件在不同人物意识中呈现不同形状。结构：探险的框架 + 内陆的并置、家族编年；开头多为一个辽阔的风景，结尾多为顿悟或死亡的收束。对话：对话是象征的载体，人物靠言语的夸张暴露自己。`impression`

## (5) 语气与距离

语气：庄重、象征、带 visionary 的热情；与人物的距离是同情的凝视；与读者的距离是邀约式的——请读者进入内陆。幽默是干冷的，悲悯藏在象征之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：澳大利亚内陆的辽阔；一个 visionary 的局外人对抗庸俗的小镇；象征现实主义；句子如天气般涨落。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No minimalist spareness, no cool detachment, no direct moralising, no flat reportage, no plain realism`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Patrick White, a man buys oden at a convenience store late at night. Epic of the interior: the store is a desert, the fluorescent light a harsh sun. A visionary outsider against a philistine town. Sentences that swell like weather. The ordinary holds a symbol.`
- 中文对照：怀特风格，一个人在深夜便利店买关东煮。内陆的史诗：便利店即沙漠，日光灯即烈日；一个 visionary 的局外人对抗庸俗的小镇；句子如天气般涨落；日常装下一个象征。
- Negative: `minimalist spareness, cool detachment, direct moralising, flat reportage, plain realism`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
