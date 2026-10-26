# Shotaro Ishinomori — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Shotaro Ishinomori manga style, dynamic hero poses, dense action panels, clean ink line, screentone, transforming hero manga`
- ZH: 石森章太郎风格，动态英雄姿态，密集动作格，干净墨线，网点，变身英雄漫画

## (2) 线条、网点/色彩

- 线条：干净有力的轮廓线，动作线密集，线条比手冢更硬朗。`verbatim`
- 网点/色彩：黑白为主，网点表现金属与夜色；彩色时红、蓝对比鲜明。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，动作分解细，跨页作变身与爆炸场面，格形方正间有斜切。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 改造人、骑士式英雄：紧身衣、面罩、披风，姿态夸张挺拔。`verbatim`
- 角色类型：九人改造人小队与各自异能、变身：腰带、姿势、光效、江户捕物：佐武与市的搭档破案。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框圆而密，拟声词大字出格，常与爆炸、变身音效同框。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：九人改造人小队与各自异能、变身：腰带、姿势、光效、江户捕物：佐武与市的搭档破案、群像英雄与牺牲、特摄式怪人与组织、历史与科幻并置。`verbatim`
- 不该画：No photorealistic rendering、no quiet slow slice-of-life pacing、no single-panel illustration without panels、no muted flat vector style。`impression`
- Negative prompt: `No photorealistic rendering, no quiet slow slice-of-life pacing, no single-panel illustration without panels, no muted flat vector style`

## (7) 测试提示词示例（现代题材：一个外卖骑手在雨夜街头变身成英雄）

- Prompt: `In the style of Shotaro Ishinomori, a food delivery rider transforming into a hero on a rainy city street at night, dynamic manga page`
- 中文对照：石森章太郎风格，一个外卖骑手在雨夜街头变身成英雄，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
