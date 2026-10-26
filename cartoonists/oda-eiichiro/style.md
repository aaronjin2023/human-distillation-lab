# Eiichiro Oda — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Eiichiro Oda manga style, lively pirate adventure, round expressive characters, dense detailed panels, dynamic action, black-and-white manga`
- ZH: 尾田荣一郎风格，活泼海贼冒险，圆润表情角色，密集精细分镜，动态动作，黑白漫画

## (2) 线条、网点/色彩

- 线条：圆润有力的线，人物造型夸张，背景细节极密。`verbatim`
- 网点/色彩：黑白为主，网点表现阴影；彩色时红、蓝、黄跳色。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数极多，格子密，跨页作冒险全景，节奏快而密。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 路飞式草帽少年、海贼群像，服装各异，表情夸张。`verbatim`
- 角色类型：草帽海贼团的冒险、海贼的梦想与宝藏、岛屿与海洋的奇观。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框极多，台词快；拟声词超大出格。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：草帽海贼团的冒险、海贼的梦想与宝藏、岛屿与海洋的奇观、伙伴的羁绊、战斗与笑料并置、世界观的层层展开。`verbatim`
- 不该画：No sparse empty panels、no realistic fine line、no quiet minimalism、no photorealistic rendering。`impression`
- Negative prompt: `No sparse empty panels, no realistic fine line, no quiet minimalism, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：一只小约克夏犬海贼船长驾船航行于夜城地铁之上）

- Prompt: `In the style of Eiichiro Oda, a small Yorkshire terrier pirate captain on a ship sailing above a night subway city, adventure manga page`
- 中文对照：尾田荣一郎风格，一只小约克夏犬海贼船长驾船航行于夜城地铁之上，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
