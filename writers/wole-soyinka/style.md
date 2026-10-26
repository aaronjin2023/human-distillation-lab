# Wole Soyinka — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wole Soyinka: dense poetic drama, Yoruba myth and ritual, proverb and riddle, language that is ceremonial and combative at once`
- ZH: 索因卡风格：稠密的诗剧，约鲁巴神话与仪式，谚语与谜语，语言既是仪式的，又是战斗的。

## (2) 句式与节奏

- 长句、排比、谜语式短句交错；诗剧语言密度高，节奏如仪式。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：森林、面具、死亡、道路、鼓、祭祀；约鲁巴神话词汇与英语并置。
- 意象：森林、面具、死亡、道路、鼓声；仪式场景即世界。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：剧场多声部；人物以仪式语言对话，合唱队作评。
- 结构：仪式结构：开场—祭祀—冲突—献祭/和解；时间可循环，不必线性。
- 对话：剧作全以对话与独白构成，对白夹杂约鲁巴谚语与歌谣；独白多为神话式咏叹。

## (5) 语气与距离

- 庄严、讽刺；既敬神，又骂人。

## (6) 该写什么 / 不该写什么

- 该写：森林（神灵与凡人相遇之所）、死亡与侍从（生死之间的过渡仪式）、道路与面具（旅程与身份的变换）、鼓与歌（仪式的时间感）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No plain realism, no easy resolution, no naturalistic dialogue, no single voice`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Wole Soyinka, a letter to yourself ten years from now. Dense poetic sentences. A proverb, a riddle, a forest. Ceremony and combat in the same breath.`
- 中文对照：索因卡风格，一封写给十年后自己的信。稠密的诗句。一句谚语，一个谜语，一片森林。仪式与战斗在同一口气里。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
