# Emily Dickinson — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emily Dickinson: short hymn-like stanzas, dashes, slant rhyme, capitalised nouns, death and eternity in a small room, compression`
- ZH: 狄金森风格：短小的赞美诗体，破折号，斜韵，大写名词，死亡与永恒在一间小屋里，极致的压缩。

## (2) 句式与节奏

- 短行、破折号多；句式压缩，一句即一世界；斜韵代替正韵。
- 节奏：段落长度与章节切分见 technique.md；诗的行断与韵律见 technique.md。

## (3) 词汇与意象

- 常用词域：死神、蜜蜂、花园、窗、永恒、心灵；名词大写，日常词被赋予重量。
- 意象：死神马车、蜜蜂、花园、窗、苍蝇；小屋即宇宙。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第一人称，时而旁观者；视角贴近内心。
- 结构：四行一节，赞美诗体；开头多为场景或命题切入，结尾常以悖论收束。
- 对话：诗中基本无人称对话；以自述、呼告与破折号的停顿代对话。

## (5) 语气与距离

- 冷静、锐利、神秘；既亲密又疏离。

## (6) 该写什么 / 不该写什么

- 该写：死神（绅士般的引路人）、蜜蜂与花园（自然与劳作）、窗与苍蝇（生死的边界）、可能（栖居之所）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No long narrative, no ornament, no explanation, no regular rhyme, no sentimentality`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Emily Dickinson, a letter to yourself ten years from now. Short hymn-like stanzas. Dashes. Slant rhyme. Death and Eternity in a small room. No explanation.`
- 中文对照：狄金森风格，一封写给十年后自己的信。短小的赞美诗体。破折号。斜韵。死亡与永恒在一间小屋里。不作解释。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
