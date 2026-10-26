# Gabriela Mistral — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gabriela Mistral: maternal lyric, earth and child imagery, plain words carrying biblical weight, grief and tenderness in the same line`
- ZH: 加夫列拉·米斯特拉尔风格：母性抒情，大地与孩子意象，朴素词语承载圣经般的重量，悲痛与温柔在同一行里。

## (2) 意象

- 主意象：大地、孩子、母亲、面包、水、安第斯山；辅意象：摇篮、墓、麦田、夜；禁意象：华美异国想象、都市浮华；密度中等，意象多取自乡村日常与圣经，朴素而沉重。

## (3) 韵律与句式

- 自由体与民谣体并行，行长中等，句式以短句与排比为主；善用重复与叠咏，节奏如摇篮曲与挽歌交替；朗读时缓慢、庄重，有停顿。

## (4) 语言密度与词汇

- 词汇朴素而庄重：大地、孩子、面包、水等日常词承载大义；少用典雅大词；动词温柔而坚定；禁词：华丽形容词堆砌、都市俚语。

## (5) 结构习惯

- 诗集式结构：短诗成组，以母题（母性、死亡、大地）分组；开头多直入场景（孩子、大地），结尾多以祈祷或祝福收束；视角多为第一人称母亲/教师；推进靠意象重复与情感递进。

## (6) 该写什么 / 不该写什么

- 该写：大地与孩子、母性与死亡、面包与水；朴素而庄重的语言、摇篮曲式重复；悲痛与温柔同行。
- 不该写：风格上的禁区——ornate exotic imagery, no urban flashiness, no ironic detachment, no abstract discourse without earth, no sentimental sweetness。
- Negative prompt: `No ornate exotic imagery, no urban flashiness, no ironic detachment, no abstract discourse without earth, no sentimental sweetness`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Gabriela Mistral, a letter to oneself ten years from now. Maternal lyric, earth and child imagery, plain words carrying biblical weight, grief and tenderness in the same line.`
- 中文对照：加夫列拉·米斯特拉尔风格：一封写给十年后自己的信。母性抒情，大地与孩子意象，朴素词语承载重量，悲痛与温柔同行。
- Negative: `No ornate exotic imagery, no urban flashiness, no ironic detachment, no abstract discourse without earth, no sentimental sweetness`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
