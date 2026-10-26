# Tite Kubo — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Tite Kubo manga style, stylish shonen, sharp fashion line, large empty panels, dramatic poses, black-and-white manga with bold black`
- ZH: 久保带人风格，时尚少年，锋利时装线，大留白格，戏剧姿态，黑白漫画配大黑块

## (2) 线条、网点/色彩

- 线条：锋利干净的线，人物修长，服装如时装画，黑块面积大。`verbatim`
- 网点/色彩：黑白为主，黑白对比强，网点少；彩色时黑、白、红。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数少，大格作姿态与斩击，留白多，节奏时尚缓慢。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 死神式黑袍少年、斩魄刀，姿态如时装，面孔冷峻。`verbatim`
- 角色类型：死神的斩击与卍解、尸魂界的秩序、时尚的黑袍与斩魄刀。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框少，台词酷；拟声词大字，斩击音效粗黑。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：死神的斩击与卍解、尸魂界的秩序、时尚的黑袍与斩魄刀、大留白的姿态格、少年的成长与责任、魔女与龙的都市奇幻。`verbatim`
- 不该画：No cute round line、no crowded tiny panels、no bright cheerful colour、no explanatory narration。`impression`
- Negative prompt: `No cute round line, no crowded tiny panels, no bright cheerful colour, no explanatory narration`

## (7) 测试提示词示例（现代题材：一只小约克夏犬死神站在夜城屋顶）

- Prompt: `In the style of Tite Kubo, a small Yorkshire terrier soul reaper standing on a rooftop above a night city, stylish manga page`
- 中文对照：久保带人风格，一只小约克夏犬死神站在夜城屋顶，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
