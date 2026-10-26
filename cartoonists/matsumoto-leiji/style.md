# Leiji Matsumoto — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Leiji Matsumoto manga style, romantic space opera, tall slender characters, detailed spaceship, starry screentone, black-and-white manga`
- ZH: 松本零士风格，浪漫太空歌剧，修长角色，精细宇宙飞船，星空网点，黑白漫画

## (2) 线条、网点/色彩

- 线条：细长优雅的线，人物修长，飞船用硬线精细描绘。`verbatim`
- 网点/色彩：黑白为主，星空用密网点与黑块；彩色时蓝、紫主调。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数中等，大格作星空与飞船，跨页多，节奏浪漫缓慢。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 修长美少年、美女，哈洛克式披风船长，列车与飞船。`verbatim`
- 角色类型：银河铁道与列车旅行、宇宙海盗的披风与骷髅旗、战舰大和号的出航。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框抒情，旁白多；拟声词小，星空寂静。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：银河铁道与列车旅行、宇宙海盗的披风与骷髅旗、战舰大和号的出航、星空与行星、少年与少女的告别、浪漫的牺牲。`verbatim`
- 不该画：No cute round line、no crowded tiny panels、no photorealistic rendering、no hard-boiled gritty tone。`impression`
- Negative prompt: `No cute round line, no crowded tiny panels, no photorealistic rendering, no hard-boiled gritty tone`

## (7) 测试提示词示例（现代题材：一只小约克夏犬乘坐太空列车飞越夜城）

- Prompt: `In the style of Leiji Matsumoto, a small Yorkshire terrier riding a space train above a night city, romantic space manga page`
- 中文对照：松本零士风格，一只小约克夏犬乘坐太空列车飞越夜城，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
