# Takao Saito — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Takao Saito manga style, hard-boiled gekiga, realistic fine line, precise gun and landscape detail, sparse dialogue, black-and-white manga`
- ZH: 齐藤隆夫风格，硬派剧画，写实细线，枪械与风景精确描绘，对话稀疏，黑白漫画

## (2) 线条、网点/色彩

- 线条：细腻写实的排线，轮廓精确，枪械与建筑如图纸。`verbatim`
- 网点/色彩：黑白为主，网点细腻，明暗靠排线层次。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数中等，大格作风景与狙击视线，节奏冷峻缓慢。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 骷髅 13 式冷面杀手，西装、墨镜、狙击枪，表情极少。`verbatim`
- 角色类型：狙击手的瞄准与等待、异国风景与城市、生存与荒野。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框极少，台词短；拟声词克制，枪声一格独占。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：狙击手的瞄准与等待、异国风景与城市、生存与荒野、武士与暗杀、一枪一格的冷峻、职业杀手的日常。`verbatim`
- 不该画：No cute round line、no crowded comedy panels、no cheerful bright colour、no explanatory narration。`impression`
- Negative prompt: `No cute round line, no crowded comedy panels, no cheerful bright colour, no explanatory narration`

## (7) 测试提示词示例（现代题材：一个沉默狙击手与一只小约克夏犬在夜城屋顶等待）

- Prompt: `In the style of Takao Saito, a silent sniper and a small Yorkshire terrier waiting on a rooftop above a night city, hard-boiled manga page`
- 中文对照：齐藤隆夫风格，一个沉默狙击手与一只小约克夏犬在夜城屋顶等待，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
