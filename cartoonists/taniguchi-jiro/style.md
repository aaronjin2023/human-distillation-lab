# Jiro Taniguchi — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Jiro Taniguchi manga style, realistic fine line, quiet everyday life, large empty panels, slow time, black-and-white manga`
- ZH: 谷口治郎风格，写实细线，安静日常，大留白格，时间缓慢，黑白漫画

## (2) 线条、网点/色彩

- 线条：细腻写实的排线，轮廓精确，风景如素描。`verbatim`
- 网点/色彩：黑白为主，淡网点，留白多，明暗柔和。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数极少，大格作风景与散步，留白多，节奏极慢。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 中年男人、登山者，面孔平淡，体型真实，服装日常。`verbatim`
- 角色类型：散步者的街道与风景、遥远小镇的回乡、神之山岭的登山。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框极少，旁白如独白；拟声词几乎不用。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：散步者的街道与风景、遥远小镇的回乡、神之山岭的登山、日常的吃饭与行走、四季的风景、沉默的时间。`verbatim`
- 不该画：No exaggerated speed lines、no crowded small panels、no cartoon big eyes、no loud sound effects。`impression`
- Negative prompt: `No exaggerated speed lines, no crowded small panels, no cartoon big eyes, no loud sound effects`

## (7) 测试提示词示例（现代题材：一只小约克夏犬与中年男人走过安静的傍晚街道）

- Prompt: `In the style of Jiro Taniguchi, a small Yorkshire terrier walking with a middle-aged man through a quiet evening street, quiet manga page`
- 中文对照：谷口治郎风格，一只小约克夏犬与中年男人走过安静的傍晚街道，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
