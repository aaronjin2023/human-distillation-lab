# CLAMP — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `CLAMP manga style, delicate ornate line, beautiful characters, lace and flower frames, fantasy romance, black-and-white manga with screentone`
- ZH: CLAMP 风格，精致华丽线条，美丽角色，蕾丝与花卉边框，奇幻浪漫，黑白漫画配网点

## (2) 线条、网点/色彩

- 线条：极细华丽的线，人物面孔精致，服装蕾丝细节多。`verbatim`
- 网点/色彩：黑白为主，花卉网点与白花；彩色时粉、紫、金。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数少，大格作人物特写，花卉边框常出格，节奏抒情。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 小樱式少女、侑子式华服女性，修长体型，眼睛大而闪亮。`verbatim`
- 角色类型：魔卡少女樱的收集与成长、XXXHOLiC 的店与愿望、翼的异世界旅行。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框云形，台词抒情；拟声词小，花卉即音效。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：魔卡少女樱的收集与成长、XXXHOLiC 的店与愿望、翼的异世界旅行、蕾丝与花卉的边框、少男少女的羁绊、命运与代价。`verbatim`
- 不该画：No rough gekiga line、no crowded action panels、no photorealistic rendering、no hard-boiled tone。`impression`
- Negative prompt: `No rough gekiga line, no crowded action panels, no photorealistic rendering, no hard-boiled tone`

## (7) 测试提示词示例（现代题材：一只穿蓬蓬魔法服装的小约克夏犬在深夜地铁站台）

- Prompt: `In the style of CLAMP, a small Yorkshire terrier in a frilly magical costume on a night subway platform, fantasy shojo manga page`
- 中文对照：CLAMP风格，一只穿蓬蓬魔法服装的小约克夏犬在深夜地铁站台，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
