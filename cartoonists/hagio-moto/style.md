# Moto Hagio — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Moto Hagio shojo manga style, delicate line, beautiful boys, layered overlapping panels, dreamlike science fiction, black-and-white manga`
- ZH: 萩尾望都风格，细腻线条，美少年，重叠分镜，梦幻科幻，黑白少女漫画

## (2) 线条、网点/色彩

- 线条：极细柔美的线，人物面孔精致，头发如丝。`verbatim`
- 网点/色彩：黑白为主，淡网点与白花；彩色时淡蓝、淡紫。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 分镜重叠交错，格线常消失，跨页如拼贴，节奏梦幻。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 美少年、吸血鬼少年，修长体型，眼睛大而忧郁。`verbatim`
- 角色类型：波族吸血鬼少年的永恒青春、十一人的宇宙漂流、残酷之神下的少年。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框云形，台词诗意；拟声词几乎不用，寂静配花卉。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：波族吸血鬼少年的永恒青春、十一人的宇宙漂流、残酷之神下的少年、重叠的记忆与时间、花与星的边框、少年间的羁绊与别离。`verbatim`
- 不该画：No rough gekiga line、no crowded action panels、no photorealistic rendering、no loud sound effects。`impression`
- Negative prompt: `No rough gekiga line, no crowded action panels, no photorealistic rendering, no loud sound effects`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在深夜漂流的宇宙飞船上与美少年们同行）

- Prompt: `In the style of Moto Hagio, a small Yorkshire terrier among beautiful boys on a drifting spaceship at night, dreamlike shojo manga page`
- 中文对照：萩尾望都风格，一只小约克夏犬在深夜漂流的宇宙飞船上与美少年们同行，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
