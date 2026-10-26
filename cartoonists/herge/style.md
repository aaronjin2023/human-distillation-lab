# Hergé — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Hergé ligne claire style, clear line, flat colour, precise background, adventure comics album, left-to-right panels, colour comics`
- ZH: 埃尔热风格，明线派，清晰线条，平涂色彩，精确背景，冒险连环画，左至右分镜，彩色漫画

## (2) 线条、网点/色彩

- 线条：均匀清晰的明线，轮廓粗细一致，无阴影排线。`verbatim`
- 网点/色彩：平涂彩色，主色蓝、红、黄，辅色柔和，禁油画式渐变。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，方格整齐，左至右阅读，跨页少，大格作风景。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：欧美左→右阅读，视线平稳走。`impression`

## (4) 角色造型

- 丁丁式少年记者、米卢白狗，造型简洁，表情克制。`verbatim`
- 角色类型：丁丁与米卢的冒险、蓝莲花的中国风景、刚果与异国风情。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框椭圆，字体工整；拟声词彩色大字，常出格。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：丁丁与米卢的冒险、蓝莲花的中国风景、刚果与异国风情、船长与教授的搭档、精确的交通工具与建筑、冒险中的幽默。`verbatim`
- 不该画：No sketchy rough line、no dark gritty shading、no crowded tiny panels、no photorealistic rendering。`impression`
- Negative prompt: `No sketchy rough line, no dark gritty shading, no crowded tiny panels, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：一只小约克夏犬记者与白狗在现代城市地铁）

- Prompt: `In the style of Hergé, a small Yorkshire terrier reporter and his white dog on a subway in a modern city, ligne claire comics page, comics page`
- 中文对照：埃尔热风格，一只小约克夏犬记者与白狗在现代城市地铁，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
