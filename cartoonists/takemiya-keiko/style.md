# Keiko Takemiya — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Keiko Takemiya shojo manga style, elegant line, beautiful boys, cosmic science fiction, flowing panels, black-and-white manga`
- ZH: 竹宫惠子风格，优雅线条，美少年，宇宙科幻，流动分镜，黑白少女漫画

## (2) 线条、网点/色彩

- 线条：优雅细线，人物修长，头发流动，星空用细网点。`verbatim`
- 网点/色彩：黑白为主，星空网点密；彩色时蓝、紫。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 分镜流动，格线斜切，跨页作宇宙，节奏抒情缓慢。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 美少年、宇宙少年，制服与长发，眼睛忧郁。`verbatim`
- 角色类型：风与木之诗的少年寄宿学校、奔向地球的宇宙流亡、少年的爱与死。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框云形，台词抒情；拟声词小。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：风与木之诗的少年寄宿学校、奔向地球的宇宙流亡、少年的爱与死、星空与飞船、变奏曲式的重复、青春的告别。`verbatim`
- 不该画：No rough gekiga line、no crowded action panels、no photorealistic rendering、no loud sound effects。`impression`
- Negative prompt: `No rough gekiga line, no crowded action panels, no photorealistic rendering, no loud sound effects`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在太空站花园与美少年们漂浮）

- Prompt: `In the style of Keiko Takemiya, a small Yorkshire terrier floating in a space station garden with beautiful boys, shojo sci-fi manga page`
- 中文对照：竹宫惠子风格，一只小约克夏犬在太空站花园与美少年们漂浮，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
