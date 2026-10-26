# Marcel Proust — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marcel Proust: long sinuous sentences, involuntary memory, minute sensory detail, social observation through the narrator's consciousness, time regained through a madeleine, a church bell, a cobblestone`
- ZH: 普鲁斯特风格：绵延的长句，非自主记忆，极细微的感觉细节，叙述者意识中的社交观察，靠玛德莱娜小蛋糕、教堂钟声、一块铺路石找回时间。

## (2) 句式与节奏

句长：极长句为主，一个句子可绵延半页以上，从句套从句，以分号、逗号层层推进，间以括号插入的联想；段落亦长，一段常占整页。节奏：缓慢、迂回、停顿多，叙事时间被心理时间拉长；一个下午的茶会可以写几十页，而几年一笔带过。`impression`

## (3) 词汇与意象

词汇：法语贵族沙龙词汇与日常器物词并置（茶、蛋糕、山楂花、睡衣、窗帘），抽象词（时间、记忆、习惯、嫉妒）反复出现；感官词极密，尤其是气味、味道、光线与声音。意象群：玛德莱娜与椴树茶（味觉记忆）、贡布雷的山楂花与教堂、威尼斯的石路、斯万家的睡莲；意象不是装饰，是记忆的触发器。禁词/禁意象：几乎不用短促的动作白描与情节驱动的悬念句；不用粗粝的口语与直白的控诉。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第一人称回忆性叙述，成年叙述者回望童年与青年；视角在叙述者与人物之间滑动，自由间接引语与内心独白交织。结构：环形而非线性——全书以‘醒来’始、以‘动笔写作’终，时间靠联想跳接而非编年推进；开头多为场景或感觉的切入（失眠、茶香），结尾多为顿悟式的收束而非情节解决。对话：对话常被叙述者的长篇心理分析打断、包裹，社交谈话本身就是观察对象。`verbatim`

## (5) 语气与距离

语气：沉静、精微、略带忧郁的审视；对人物的态度是理解多于审判，连对势利的斯万与盖尔芒特夫人也以同情的细致写之；与读者的距离是邀约式的——请读者把自己的记忆放进叙述者的记忆里对照。反讽是温和的、内省的，不是尖刻的。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：童年住所与故乡小镇、沙龙与社交礼仪、一段气味或味道触发的回忆、爱情中的嫉妒与等待、睡前与醒来之间的意识、艺术与时间的顿悟。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No short telegram-style sentences, no fast plot-driven action, no plain reportage, no direct moralising, no sentimental happy ending`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Marcel Proust, a man buys oden at a convenience store late at night in a modern city. One long sinuous sentence after another. The steam, the smell of dashi, and suddenly a childhood winter kitchen returns whole. Social observation of the night-shift clerk through the narrator's consciousness. Time regained, not plot advanced.`
- 中文对照：普鲁斯特风格，一个人在深夜便利店买关东煮。长句绵延，蒸汽与高汤的气味忽然带回整个童年冬天的厨房；通过叙述者的意识观察夜班店员；找回的是时间，不是推进情节。
- Negative: `short telegram-style sentences, fast plot-driven action, plain reportage, direct moralising`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
