# Fujio Akatsuka — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Fujio Akatsuka manga style, gag manga, loose round line, exaggerated faces, chaotic panels, slapstick comedy, black-and-white manga`
- ZH: 赤冢不二夫风格，搞笑漫画，松散圆线，夸张表情，混乱分镜，闹剧喜剧，黑白漫画

## (2) 线条、网点/色彩

- 线条：松散圆润的粗线，轮廓抖动，表情线夸张拉长。`verbatim`
- 网点/色彩：黑白为主，网点少，黑块作强调；彩色时红、黄跳色。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，格形不规则，笑点格突然放大，节奏快而乱。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 笨蛋爸爸式大鼻子、阿松六胞胎、魔法少女，表情极端。`verbatim`
- 角色类型：六胞胎的集体闹剧、笨蛋爸爸的暴走、魔法少女的变身失误。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框多而大，拟声词超大出格，常与表情同框。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：六胞胎的集体闹剧、笨蛋爸爸的暴走、魔法少女的变身失误、日常小事的无限放大、夸张的哭与笑、无厘头的结尾。`verbatim`
- 不该画：No realistic fine line、no sparse slow panels、no dark gritty gekiga tone、no photorealistic rendering。`impression`
- Negative prompt: `No realistic fine line, no sparse slow panels, no dark gritty gekiga tone, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在便利店制造混乱）

- Prompt: `In the style of Fujio Akatsuka, a small Yorkshire terrier causing chaos in a convenience store, gag manga page`
- 中文对照：赤冢不二夫风格，一只小约克夏犬在便利店制造混乱，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
