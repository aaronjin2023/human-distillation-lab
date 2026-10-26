# Yoichi Takahashi — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Yoichi Takahashi manga style, passionate soccer manga, dynamic kicks, speed lines, heroic poses, black-and-white manga`
- ZH: 高桥阳一风格，热血足球漫画，动态射门，速度线，英雄姿态，黑白漫画

## (2) 线条、网点/色彩

- 线条：干净有力的线，射门动作线密集，人物肌肉简洁。`verbatim`
- 网点/色彩：黑白为主，网点表现球场；彩色时绿、蓝主调。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，射门分解细，跨页作必杀射门，节奏快。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 大空翼式少年球员，射门姿态夸张，球衣号码清晰。`verbatim`
- 角色类型：足球小将的射门与必杀技、世青篇的国际对决、少年的梦想与努力。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框密，台词热血；拟声词大字，射门音效粗黑。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：足球小将的射门与必杀技、世青篇的国际对决、少年的梦想与努力、球队的羁绊、球场全景、逆转的进球。`verbatim`
- 不该画：No cute round line、no sparse slow panels、no photorealistic rendering、no quiet minimalism。`impression`
- Negative prompt: `No cute round line, no sparse slow panels, no photorealistic rendering, no quiet minimalism`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在地铁站上方的屋顶球场射门得分）

- Prompt: `In the style of Yoichi Takahashi, a small Yorkshire terrier scoring a goal on a rooftop soccer field above a subway station, sports manga page`
- 中文对照：高桥阳一风格，一只小约克夏犬在地铁站上方的屋顶球场射门得分，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
