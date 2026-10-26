# Ngũgĩ wa Thiong'o — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ngũgĩ wa Thiong'o: oral storytelling cadence, Gikuyu proverbs, the village and the land, plain forceful sentences, the coloniser's language turned back on itself`
- ZH: 恩古吉风格：口头讲故事的节奏，基库尤谚语，村落与土地，平实有力的句子，把殖民者的语言反过来用。

## (2) 句式与节奏

- 口头叙事节奏，重复与排比多；句式平实有力，短句作锤击。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：土地、河流、学校、监狱、茅屋、斗争；基库尤语词汇与谚语嵌入英语。
- 意象：土地、河流、学校、监狱、茅屋；土地即一切。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：全知视角，村落合唱；偶用第一人称。
- 结构：村落编年与群像；开头多为日常场景切入，结尾常以集会或审判收束。
- 对话：对话推进情节，吉库尤口语与英语交织；独白与集体合唱交替，议论借人物之口。

## (5) 语气与距离

- 坚定、悲悯；既控诉又怀抱希望。

## (6) 该写什么 / 不该写什么

- 该写：土地（得失之间即历史）、河流与学校（传统与现代的交汇）、监狱（写作与抵抗的场所）、一粒麦种（牺牲与新生）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No colonial romance, no detached irony, no ornamental lyricism, no single hero`

## (7) 测试提示词示例（现代题材：手机没电的一天）

- Prompt: `In the style of Ngũgĩ wa Thiong'o, a day without a charged phone. Plain forceful sentences. The village, the land, the school. A proverb closes the scene. The story is told aloud.`
- 中文对照：恩古吉风格，手机没电的一天。平实有力的句子。村落、土地、学校。一句谚语收束场景。故事是讲出来的。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
