# Shen Zhi — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shen Zhi: elegant restrained Mandarin, night and parting imagery, long sighing lines, soft rhyme, tender melancholy, no outburst`
- ZH: 慎芝风格：典雅克制的国语，夜与离别意象，长句如叹息，韵脚柔和，温柔的惆怅，不写宣泄。

## (2) 意象

- 意象群：夜、街灯、雨、酒、最后一夜、意难忘的往事；意象密度中等，明喻为主，用典少；禁意象：喧闹都市、华丽古风、直白的肉欲。 `impression`

## (3) 韵律

- 押韵：句尾押韵，韵脚多为柔和的闭口与鼻音（en、in、ang），换韵处即情绪下沉处；句长中等偏长，留出换气口，旋律先行。 `impression`

## (4) 句式与口语密度

- 句式：中长句为主，排比少，设问与感叹并用；口语密度中等，书面语典雅；人称多为第一人称独白，偶有第二人称倾诉。 `impression`

## (5) 情感弧线

- 情感弧线：起于夜色与回忆—中段一声叹息—副歌收在温柔的认命上；结尾开放而克制，不写决绝。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：夜与离别意象、长句叹息、温柔惆怅、克制收束。
- 不该写：宣泄式高喊、喧闹与华丽意象、直白的议论。
- Negative prompt: `No shouting outburst, no noisy urban imagery, no ornate classical display, no direct moralising, no forced happy ending`

## (7) 测试提示词示例

- Prompt: `In the style of Shen Zhi, lyrics about a man buying oden at a convenience store late at night, remembering someone. Elegant restrained Mandarin, night imagery, long sighing lines, tender melancholy. Verse, chorus.`
- 中文对照：慎芝风格：写一个深夜在便利店买关东煮的男人，想起一个人。典雅克制，夜的意象，长句如叹息，温柔惆怅。
- Negative: `No shouting outburst, no noisy urban imagery, no ornate classical display, no direct moralising, no forced happy ending`
- 检验点：意象是否对位；韵脚是否顺口；副歌是否收在该作词人的情感弧线上；禁区写法是否出现。
