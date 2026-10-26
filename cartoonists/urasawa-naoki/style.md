# Naoki Urasawa — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Naoki Urasawa manga style, realistic line, suspense thriller, dense dialogue, cinematic panels, black-and-white manga`
- ZH: 浦泽直树风格，写实线条，悬疑惊悚，对话密集，电影式分镜，黑白漫画

## (2) 线条、网点/色彩

- 线条：干净写实的线，人物面孔精致，表情细腻。`verbatim`
- 网点/色彩：黑白为主，网点细腻，明暗靠排线。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，电影式分镜，悬念格放大，节奏张弛有度。`verbatim`
- 节奏：切分格子、定视线与节奏（分镜稿（name）、格线、对话框位置）；分镜示例：切 5 格——全景、特写、侧脸、对视、留白格；对话框只留一句。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 天马医生式正直者、约翰式冷面少年，群像多，面孔各异。`verbatim`
- 角色类型：怪物的追逐与对峙、20 世纪少年的预言与阴谋、冥王的机器人与人性。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框密，台词多，悬念靠对话推进；拟声词克制。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：怪物的追逐与对峙、20 世纪少年的预言与阴谋、冥王的机器人与人性、医生的抉择、群像的交错、悬念的反转。`verbatim`
- 不该画：No cute round line、no sparse slow panels、no loud sound effects、no simple good-versus-evil cartoon。`impression`
- Negative prompt: `No cute round line, no sparse slow panels, no loud sound effects, no simple good-versus-evil cartoon`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在深夜地铁目击神秘男子）

- Prompt: `In the style of Naoki Urasawa, a small Yorkshire terrier witnessing a mysterious man on a late-night subway, suspense manga page`
- 中文对照：浦泽直树风格，一只小约克夏犬在深夜地铁目击神秘男子，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
