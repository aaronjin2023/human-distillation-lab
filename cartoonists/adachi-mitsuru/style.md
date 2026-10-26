# Mitsuru Adachi — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Mitsuru Adachi manga style, clean simple line, understated youth, baseball, quiet emotion, sparse panels, black-and-white manga`
- ZH: 安达充风格，干净简洁线条，克制的青春，棒球，安静情感，稀疏分镜，黑白漫画

## (2) 线条、网点/色彩

- 线条：干净简洁的细线，人物造型简单，表情克制。`verbatim`
- 网点/色彩：黑白为主，网点淡，留白多；彩色时淡蓝、淡绿。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数少，大格作投球与击球，留白多，节奏安静。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 棒球少年、少女，体型修长，表情淡，制服简洁。`verbatim`
- 角色类型：棒球的投球与击球、少年的暗恋与告别、四叶草与幸运。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框少，台词短；拟声词小，投球音效克制。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：棒球的投球与击球、少年的暗恋与告别、四叶草与幸运、日常的训练与放学路、兄弟与对手、安静的青春。`verbatim`
- 不该画：No exaggerated big eyes、no crowded action panels、no loud sound effects、no melodramatic shouting。`impression`
- Negative prompt: `No exaggerated big eyes, no crowded action panels, no loud sound effects, no melodramatic shouting`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在地铁站灯光下看深夜棒球练习）

- Prompt: `In the style of Mitsuru Adachi, a small Yorkshire terrier watching a night baseball practice under subway station lights, quiet sports manga page`
- 中文对照：安达充风格，一只小约克夏犬在地铁站灯光下看深夜棒球练习，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
