# Masashi Kishimoto — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Masashi Kishimoto manga style, dynamic ninja action, speed lines, expressive faces, detailed costumes, black-and-white manga with screentone`
- ZH: 岸本齐史风格，动态忍者动作，速度线，表情丰富，服装精细，黑白漫画配网点

## (2) 线条、网点/色彩

- 线条：干净有力的线，忍者服装细节多，动作线密。`verbatim`
- 网点/色彩：黑白为主，网点表现阴影；彩色时橙、蓝主调。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，忍术对决分解细，跨页作忍术全貌，节奏快。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 鸣人式金发少年、忍者服装，护额、查克拉线。`verbatim`
- 角色类型：忍者的修行与对决、鸣人的成长与羁绊、忍术与查克拉。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框密，台词热血；拟声词大字，忍术音效粗黑。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：忍者的修行与对决、鸣人的成长与羁绊、忍术与查克拉、木叶村的日常与任务、师徒与对手、武士 8 的武士与机械。`verbatim`
- 不该画：No realistic fine line、no sparse slow panels、no dark gritty tone、no photorealistic rendering。`impression`
- Negative prompt: `No realistic fine line, no sparse slow panels, no dark gritty tone, no photorealistic rendering`

## (7) 测试提示词示例（现代题材：一只小约克夏犬忍者在夜城屋顶修行）

- Prompt: `In the style of Masashi Kishimoto, a small Yorkshire terrier ninja training on a rooftop above a night city, action manga page`
- 中文对照：岸本齐史风格，一只小约克夏犬忍者在夜城屋顶修行，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
