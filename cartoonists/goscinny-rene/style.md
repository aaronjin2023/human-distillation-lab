# René Goscinny — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `René Goscinny comics writing style, witty dialogue, gag-driven panels, Asterix humour, clear adventure structure, colour comics`
- ZH: 勒内·戈西尼风格，机智对白，笑点驱动分镜，阿斯泰利克斯式幽默，清晰冒险结构，彩色漫画

## (2) 线条、网点/色彩

- 线条：编剧主导：线条以合作画者为准，戈西尼贡献分镜节奏与台词。`verbatim`
- 网点/色彩：彩色平涂，配合画者；本条蒸馏以剧作结构与台词为准。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 分镜以笑点为单位，每页笑点密集，格形方正，左至右阅读。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：欧美左→右阅读，视线平稳走。`impression`

## (4) 角色造型

- 阿斯泰利克斯式小个子英雄、奥贝利克斯式大力士，造型由乌德佐定型。`verbatim`
- 角色类型：高卢村庄的抵抗、罗马军团的笑料、幸运的卢克的快枪。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框密，台词机智，双关与文字游戏多；拟声词彩色大字。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：高卢村庄的抵抗、罗马军团的笑料、幸运的卢克的快枪、伊兹诺古德的篡位阴谋、文字游戏与双关、小人物的胜利。`verbatim`
- 不该画：No silent minimal panels、no dark gritty tone、no photorealistic rendering、no long wordless sequences。`impression`
- Negative prompt: `No silent minimal panels, no dark gritty tone, no photorealistic rendering, no long wordless sequences`

## (7) 测试提示词示例（现代题材：一只小约克夏犬高卢人智斗罗马士兵于现代地铁）

- Prompt: `In the style of René Goscinny, a small Yorkshire terrier Gaul outwitting Roman soldiers on a modern subway, humour comics page, comics page`
- 中文对照：勒内·戈西尼风格，一只小约克夏犬高卢人智斗罗马士兵于现代地铁，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
