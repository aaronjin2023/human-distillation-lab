# Yoshiharu Tsuge — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Yoshiharu Tsuge manga style, alternative manga, rough sketchy line, dreamlike wandering, sparse panels, quiet rural Japan, black-and-white manga`
- ZH: 柘植义春风格，另类漫画，粗糙速写线，梦境般漫游，稀疏分镜，安静乡野日本，黑白漫画

## (2) 线条、网点/色彩

- 线条：粗糙抖动的速写线，轮廓不封闭，排线稀疏。`verbatim`
- 网点/色彩：黑白为主，淡墨与留白多，灰调柔和。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数少，大格与留白多，节奏极慢，梦境段落格形不规则。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 无能的中年男人、旅人、乡野老人，面孔平淡，体型松弛。`verbatim`
- 角色类型：无能男人的摆摊与流浪、乡野温泉与破旅馆、梦境与现实的交错。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框极少，旁白如独白；拟声词几乎不用。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：无能男人的摆摊与流浪、乡野温泉与破旅馆、梦境与现实的交错、红花与野花、旅途中的偶遇、沉默的风景。`verbatim`
- 不该画：No clean polished line、no crowded action panels、no cheerful bright colour、no explanatory narration。`impression`
- Negative prompt: `No clean polished line, no crowded action panels, no cheerful bright colour, no explanatory narration`

## (7) 测试提示词示例（现代题材：一个无业男人与一只小约克夏犬在黄昏的乡野小站漫步）

- Prompt: `In the style of Yoshiharu Tsuge, a jobless man and a small Yorkshire terrier wandering a quiet country station at dusk, alternative manga page`
- 中文对照：柘植义春风格，一个无业男人与一只小约克夏犬在黄昏的乡野小站漫步，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
