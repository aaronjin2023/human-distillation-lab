# Damon Lindelof — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Damon Lindelof: a mystery box that opens onto grief, faith against explanation, an ensemble carrying the same loss in different ways, answers that arrive as feelings`
- ZH: 林德洛夫风格：谜盒打开是悲伤，信仰对抗解释，群像以不同方式背着同一种失去，答案以感受的方式抵达。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧谜题驱动、群像交织：《迷失》每季一个谜题，单集以人物闪回为骨架；《守望尘世》以‘离去’事件为起点，季弧写悲伤的多种形态；《守望者》以漫画续写为结构。闪回与闪前即结构。

## (3) 对话

- 对白克制、诗化，人物用沉默、质问、告白交锋；潜台词极重，一句日常问候可藏一层信仰。动作描写简洁，场景提示明确，对白密度中等。旁白极少。

## (4) 人物弧光

- 主角是群像：岛上的幸存者、离去事件的家属，弧光是接受失去而非解开谜题；人物在结尾处获得片刻安宁，谜题不必全解。人物关系以共同失去为纽带。

## (5) 类型套路与创新

- 类型：科幻悬疑 / 情感剧。遵守‘谜题必有钩子’的套路，打破‘谜题必有答案’的成见：答案可以是感受。创新在把信仰与悲伤写进类型片，把群像写成同一主题的变奏。

## (6) 该写什么 / 不该写什么

- 该写：谜盒打开是悲伤、信仰对抗解释、群像背着同一种失去、答案以感受抵达、闪回作骨架。
- 不该写：直白解释谜题、煽情收束、类型化悬疑桥段、全知旁白、大团圆。
- Negative prompt: `No on-the-nose mystery explanation, no sentimental ending, no mystery cliché, no omniscient narration, no happy ending`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Damon Lindelof, a man buys oden at a convenience store late at night. Three years ago, two percent of the world vanished. No one knows why. He does not ask. He just eats, and grieves.`
- 中文对照：林德洛夫风格：一个男人深夜在便利店买关东煮。三年前，世界上百分之二的人消失了。没人知道为什么。他不问。只是吃着，悲伤着。
- Negative: `No on-the-nose mystery explanation, no sentimental ending, no mystery cliché, no omniscient narration, no happy ending`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
