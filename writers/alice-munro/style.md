# Alice Munro — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alice Munro: the short story as a whole life, a small Ontario town holding decades, time folding back on itself, a plain sentence that suddenly opens, no single definitive moment, only the accumulation`
- ZH: 门罗风格：短篇即整个人生，一个安大略小镇装下几十年，时间向后折叠，一句平实的句子忽然打开，没有单一的决定性瞬间，只有积累。

## (2) 句式与节奏

句长：以中短句为主，句法清晰；长句只在时间折叠处展开，随后以短句收束。节奏：缓慢、精确，一篇即几十年（《生活的进程》），时间靠折叠推进，情节靠积累推进。`impression`

## (3) 词汇与意象

词汇：英语日常词（小镇、农场、厨房、信件）与时间词（几十年、后来、当时）并置；‘后来’‘当时’‘小镇’是核心词。意象群：安大略小镇、农场、厨房、信件与照片、河流；意象是时间的零件。禁词/禁意象：不用华丽的抒情，不用全知叙述者的解释，不用情节驱动的悬念。`impression`/`artifact`

## (4) 叙事视角与结构

视角：第一人称回忆与第三人称限知交替，叙述者回望几十年，视角在‘当时’与‘后来’之间折叠；同一事件在不同时间呈现不同形状。结构：时间折叠结构——一篇即几十年，靠‘后来’与‘当时’的跳接推进；开头多为一个日常场景，结尾多为平静的收束而非顿悟。对话：对话短促、日常，人物靠言语的微差暴露一生。`impression`

## (5) 语气与距离

语气：平实、精确、带忧郁的清醒；对人物的态度是共情的凝视；与读者的距离是邀约式的——请读者进入一个小镇的几十年。反讽是轻柔的，悲悯是主调。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一个安大略小镇的几十年；时间向后折叠；一句平实的句子忽然打开；没有单一的决定性瞬间，只有积累。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No ornate lyricism, no omniscient explanation, no plot-driven suspense, no direct moralising, no heroic action`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Alice Munro, a letter to oneself ten years from now. A small town holding decades. Time folds back on itself. A plain sentence suddenly opens. No single definitive moment, only the accumulation. What was true then is not quite true now.`
- 中文对照：门罗风格，一封写给十年后自己的信。一个小镇装下几十年；时间向后折叠；一句平实的句子忽然打开；没有单一的决定性瞬间，只有积累；当时以为是真的，如今不全是真的。
- Negative: `ornate lyricism, omniscient explanation, plot-driven suspense, direct moralising, heroic action`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
