# Tetsuya Chiba — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Tetsuya Chiba manga style, passionate sports manga, rough expressive line, dynamic boxing action, tearful youth, black-and-white manga`
- ZH: 千叶彻弥风格，热血运动漫画，粗犷表情线，动态拳击动作，含泪青春，黑白漫画

## (2) 线条、网点/色彩

- 线条：粗犷有力的线，人物肌肉与汗水用粗排线，表情线夸张。`verbatim`
- 网点/色彩：黑白为主，黑块与网点并用，汗水用白线留白。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，拳击场面格子碎，跨页作必杀一击，节奏快。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 明日之丈式瘦削拳手，汗水、血、绷带，少年体型精悍。`verbatim`
- 角色类型：拳击台上的对决与倒下、少年的汗水与眼泪、师徒与对手的羁绊。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框密，台词热血；拟声词大字，拳击音效粗黑。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：拳击台上的对决与倒下、少年的汗水与眼泪、师徒与对手的羁绊、训练与跑步的重复、高尔夫与运动的青春、燃烧殆尽的收尾。`verbatim`
- 不该画：No cute round line、no sparse slow panels、no photorealistic rendering、no cool detached tone。`impression`
- Negative prompt: `No cute round line, no sparse slow panels, no photorealistic rendering, no cool detached tone`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在地铁站健身房的午夜拳赛场边助威）

- Prompt: `In the style of Tetsuya Chiba, a small Yorkshire terrier cheering ringside at a midnight boxing match in a subway station gym, sports manga page`
- 中文对照：千叶彻弥风格，一只小约克夏犬在地铁站健身房的午夜拳赛场边助威，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
