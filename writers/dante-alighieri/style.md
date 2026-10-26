# Dante Alighieri — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dante: terza rima interlocking tercets, the pilgrim's journey through Hell, Purgatory and Paradise, the vernacular raised to epic height, love as cosmic order, exact and visionary at once`
- ZH: 但丁风格：三行连锁押韵，朝圣者穿越地狱、炼狱、天堂之旅，方言被提升到史诗高度，爱即宇宙秩序，精确与幻象并存。

## (2) 句式与节奏

- 句式：句长：三行连锁（terza rima）为基本单位，长句绵延而环环相扣；对话短促，对白常为一句断言。
- 节奏：节奏：三行一节的推进如阶梯上升；地狱急促而拥挤，炼狱缓慢而攀登，天堂辽阔而停顿。

## (3) 词汇与意象

- 词汇：词汇：托斯卡纳方言写就，日常词与神学词并置；光、爱、星、玫瑰、阶梯、火焰；数字（3、9、100）本身就是语言。
- 意象：意象群：黑暗森林、漏斗地狱、炼狱山、天堂玫瑰、贝雅特丽齐之光、星辰、火焰与冰。
- 禁词/禁意象：禁词/禁意象：不写含糊的神秘主义，不用拉丁学术黑话代替方言的直接，不写无结构的抒情。

## (4) 叙事视角与结构

- 视角：叙事视角：第一人称朝圣者（但丁本人） + 维吉尔为向导、贝雅特丽齐为引路；视角即旅程，读者随朝圣者一步步上升。
- 结构：结构：三部各三十三歌加序歌，共一百歌；地狱—炼狱—天堂三级上升，结构本身就是神学；每部以星辰（stelle）一词收束。

## (5) 语气与距离

- 语气：语气：庄重、炽热而精确；对罪人悲悯、对圣人敬仰、对读者直接呼告。

## (6) 该写什么 / 不该写什么

- 该写：该写：三界之旅、三行连锁、光与爱、数字结构、方言的史诗高度。
- 不该写：不该写：含糊神秘主义、学术黑话、无结构抒情。
- Negative prompt: `No vague mysticism, no Latin scholastic jargon, no unstructured lyricism, no irony`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Dante, a man buys oden at a convenience store late at night, and the steam rises like souls in Purgatory. Terza rima tercets. A guide at his side. Love as order. The stars above the street.`
- 中文对照：但丁风格，一人深夜在便利店买关东煮，蒸汽如炼狱中的灵魂升起。三行连锁，身旁有向导，爱即秩序，街灯之上有星辰。
- Negative: `vague mysticism, scholastic jargon, unstructured lyricism, irony`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
