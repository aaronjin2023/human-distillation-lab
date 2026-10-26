# Shigeru Mizuki — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Shigeru Mizuki manga style, detailed yokai world, dense background hatching, cute round characters against eerie scenery, black-and-white manga`
- ZH: 水木茂风格，细密妖怪世界，浓密背景排线，圆润角色配阴森景色，黑白漫画

## (2) 线条、网点/色彩

- 线条：人物线圆润简洁，背景线极细密，排线与点描并用。`verbatim`
- 网点/色彩：黑白为主，背景黑块与网点浓重；彩色时绿、褐主调。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数中等，背景大格多，妖怪登场用跨页，格形方正。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 鬼太郎式独眼少年、眼珠老爹、猫女，妖怪造型取材民间，形态各异。`verbatim`
- 角色类型：妖怪横丁与妖怪集会、鬼太郎与眼珠老爹的父子搭档、河童与水的世界。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框圆，妖怪台词常配特殊字体感；拟声词手写，夜行场面拟声词大。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：妖怪横丁与妖怪集会、鬼太郎与眼珠老爹的父子搭档、河童与水的世界、墓场与夜路、战争记忆与妖怪、民间传说再编。`verbatim`
- 不该画：No clean empty background、no photorealistic rendering、no sleek modern vector line、no bright cheerful colour flat。`impression`
- Negative prompt: `No clean empty background, no photorealistic rendering, no sleek modern vector line, no bright cheerful colour flat`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在深夜地铁站台遇见独眼妖怪少年）

- Prompt: `In the style of Shigeru Mizuki, a small Yorkshire terrier meeting a one-eyed yokai boy on a night subway platform, eerie manga page`
- 中文对照：水木茂风格，一只小约克夏犬在深夜地铁站台遇见独眼妖怪少年，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
