# Hafez — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hafez: polished ghazals, wine, rose and nightingale, love sacred and profane at once, wit, ambiguity, the couplet that turns on its last line`
- ZH: 哈菲兹风格：精致的伽扎尔，酒、玫瑰与夜莺，神圣与世俗之爱同体，机智、暧昧，尾联翻转全诗。

## (2) 句式与节奏

- 对句为单位，句式工整；双关密集；尾联常突然翻转，前文意义随之改写。
- 节奏：段落长度与章节切分见 technique.md；诗的行断与韵律见 technique.md。

## (3) 词汇与意象

- 常用词域：酒、玫瑰、夜莺、月亮、酒馆、爱人、晨风；词汇华美而克制。
- 意象：酒、玫瑰、夜莺、月亮、酒馆；同一意象既可世俗解，也可苏菲解。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第一人称抒情者，时而自嘲，时而训诫。
- 结构：伽扎尔：每联独立成意，联与联之间跳跃，尾联点题或翻转。
- 对话：抒情诗中基本无人称对话；以呼告（对酒、对友人、对爱人）与自问自答代对话。

## (5) 语气与距离

- 机智、暧昧、欢愉中带忧伤；从不板起面孔。

## (6) 该写什么 / 不该写什么

- 该写：酒与玫瑰（爱与欢愉）、夜莺与玫瑰（恋人与被恋者）、酒馆与隐修（世俗与神圣的对峙与互通）、月亮与晨风（夜与黎明的过渡）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No plain moralising, no single fixed meaning, no prosaic narration, no formlessness`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Hafez, a letter to yourself ten years from now. Wine, rose and nightingale. Every couplet complete in itself. Let the last couplet turn the whole letter around.`
- 中文对照：哈菲兹风格，一封写给十年后自己的信。酒、玫瑰与夜莺。每联自足。让最后一联翻转整封信。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
