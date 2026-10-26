# Katherine Mansfield — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Katherine Mansfield: the short story as a moment, a garden party that reveals a whole class, free indirect thought in a single afternoon, light and flowers and a sudden shadow, no explanation, only the moment`
- ZH: 曼斯菲尔德风格：短篇即一个瞬间，一场花园茶会揭示整个阶级，一个下午的自由间接思想，光与花与忽然降临的阴影，不解释，只有瞬间。

## (2) 句式与节奏

句长：以中短句为主，句法清晰；长句只在顿悟处展开，随后以短句收束。节奏：轻快、精确，一篇即一个下午（《花园茶会》）、一个晚上（《幸福》）；时间靠意识的流动推进，情节极少。`impression`

## (3) 词汇与意象

词汇：英语日常词（花、帽子、茶、窗）与阶级词（花园、工人、穷人）并置；‘花’‘帽子’‘光’是核心词。意象群：花园（阶级的花园）、帽子（劳拉的帽子）、光（午后的光）、穷人的死（茶会之外的死亡）；意象是阶级的零件。禁词/禁意象：不用全知叙述者的解释，不用情节驱动的悬念，不用直白的道德评判。`impression`/`artifact`

## (4) 叙事视角与结构

视角：自由间接引语 + 第三人称限知，紧贴女主人公（劳拉、伯莎）的意识；视角不切换，意识在一个人身上流动。结构：单日、单场景的短篇结构；开头多为一个日常场景（筹备茶会），结尾多为顿悟或戛然而止。对话：对话短促、日常，人物靠言语的微差暴露阶级与内心。`impression`

## (5) 语气与距离

语气：抒情、敏锐、带忧郁的清醒；对人物的态度是共情的凝视；与读者的距离是邀约式的——请读者进入一个下午。反讽是轻柔的，悲悯是主调。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一个下午的意识流动；一场花园茶会揭示整个阶级；光与花与忽然降临的阴影；顿悟或戛然而止的结尾。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No omniscient explanation, no plot-driven suspense, no direct moralising, no flat reportage, no heroic action`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Katherine Mansfield, a small Yorkshire terrier sits on a subway seat. Free indirect thought in a single ride. Light through the window, a hat, a flower. A sudden shadow — the world outside the carriage. No explanation, only the moment.`
- 中文对照：曼斯菲尔德风格，一只小约克夏犬坐在地铁座位上。一个车程的自由间接思想；窗外的光、一顶帽子、一朵花；忽然降临的阴影——车厢之外的世界；不解释，只有瞬间。
- Negative: `omniscient explanation, plot-driven suspense, direct moralising, flat reportage, heroic action`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
