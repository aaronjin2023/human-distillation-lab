# Yasunari Kawabata — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yasunari Kawabata: spare lyrical prose, haiku-like vignettes, snow, silence and the beauty of impermanence, suggestion over statement, endings left open`
- ZH: 川端康成风格：简净抒情的散文，俳句般的片段，雪、沉默与无常之美，以暗示代替说明，结尾开放。

## (2) 句式与节奏

- 短句为主，句与句之间留白大；景物先行，人物后至；段落短，场景如俳句般并置。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：雪、温泉、雾气、镜、茶碗、和服、指尖、火车、山；词性偏名词与感官动词，形容词克制。
- 意象：雪国、温泉雾气、车窗镜中人、千羽鹤茶碗、指尖的触感；每群只列文本意象，不作过度象征阐释。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第三人称限知，多贴近男主人公的内视角；偶用第一人称掌篇小说。
- 结构：片段并置、掌篇小说；开头多为场景切入（车窗、温泉、茶室），结尾收束松散、常戛然而止。
- 对话：对话极简、克制，多为日常寒暄与未说出口的话；沉默与停顿即对话的一部分。

## (5) 语气与距离

- 幽玄、物哀、克制；与人物保持温柔的距离，与读者保持含蓄的距离。

## (6) 该写什么 / 不该写什么

- 该写：雪与温泉（洁净、寒冷、短暂的美）、镜与倒影（虚实难分）、茶道器物（传统之美与人物命运并置）、掌篇小说（同一母题反复变奏）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No explicit explanation, no neat resolution, no loud emotion, no long analysis, no Western-style plot climax`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Yasunari Kawabata, a man buys oden at a convenience store late at night. Short spare sentences. Steam, glass, the reflection of his face in the window. Nothing explained. The night is cold and beautiful.`
- 中文对照：川端康成风格，一个人在深夜便利店买关东煮。短句，留白。蒸汽、玻璃、窗上映出的脸。什么都不解释。夜又冷又美。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
