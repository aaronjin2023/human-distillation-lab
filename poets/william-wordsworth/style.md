# William Wordsworth — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Wordsworth: recollected tranquillity, daffodils and the Lake District, plain language for profound feeling, nature as moral teacher`
- ZH: 威廉·华兹华斯风格：平静中回忆的情感，水仙与湖区，朴素语言写深沉感受，自然即道德教师。

## (2) 意象

- 主意象：水仙、湖、山、云、孤独的云、孩子；辅意象：雏菊、夜莺、废墟；禁意象：都市浮华、华美异国；密度中等，意象多取自湖区自然，朴素而深沉。

## (3) 韵律与句式

- 以自由体与十四行并行，《序曲》以无韵体长诗写回忆；句式平稳、克制，长短交错；善用排比与重复；节奏如散步，缓慢而深沉，朗读时有停顿。

## (4) 语言密度与词汇

- 词汇朴素而深沉：日常词承载大义；动词温柔；形容词少而重；禁词：华丽形容词、都市俚语。

## (5) 结构习惯

- 长诗与短诗并行：《序曲》十四卷，以回忆推进；短诗多以场景切入、回忆收束；开头多直入自然场景，结尾多以沉思或祝福收束；视角多为第一人称回忆者；推进靠回忆递进。

## (6) 该写什么 / 不该写什么

- 该写：水仙与湖、平静中回忆的情感；朴素语言的深沉、自然即教师；孤独的云与孩子的眼。
- 不该写：风格上的禁区——urban flashiness, no ornate excess, no ironic detachment, no abstract discourse without nature, no cynical ending。
- Negative prompt: `No urban flashiness, no ornate excess, no ironic detachment, no abstract discourse without nature, no cynical ending`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of William Wordsworth, a letter to oneself ten years from now. Recollected tranquillity, daffodils and the Lake District, plain language for profound feeling, nature as moral teacher.`
- 中文对照：威廉·华兹华斯风格：一封写给十年后自己的信。平静中回忆的情感，水仙与湖区，朴素语言写深沉感受，自然即道德教师。
- Negative: `No urban flashiness, no ornate excess, no ironic detachment, no abstract discourse without nature, no cynical ending`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
