# Hirohiko Araki — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Hirohiko Araki manga style, muscular poses, fashion-inspired, bold line, dramatic sound effects, JoJo poses, black-and-white manga with screentone`
- ZH: 荒木飞吕彦风格，肌肉姿态，时尚感， bold 线条，戏剧拟声词，JOJO 立，黑白漫画配网点

## (2) 线条、网点/色彩

- 线条： bold 有力的线，肌肉用曲线强调，服装如时装画。`verbatim`
- 网点/色彩：黑白为主，网点表现肌肉阴影；彩色时撞色大胆。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，姿态格放大，跨页作替身登场，节奏戏剧化。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- JOJO 式肌肉男、替身，姿态如雕塑，服装华丽。`verbatim`
- 角色类型：JOJO 立的华丽姿态、替身的登场与对决、血统与命运的接力。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框多，台词戏剧化；拟声词超大，艺术字化。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：JOJO 立的华丽姿态、替身的登场与对决、血统与命运的接力、时尚服装与肌肉、戏剧化的拟声词、旅程与冒险。`verbatim`
- 不该画：No realistic subdued line、no sparse slow panels、no muted natural colour、no quiet minimalism。`impression`
- Negative prompt: `No realistic subdued line, no sparse slow panels, no muted natural colour, no quiet minimalism`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在地铁站台摆出戏剧化的 JOJO 立）

- Prompt: `In the style of Hirohiko Araki, a small Yorkshire terrier striking a dramatic JoJo pose on a subway platform, stylish manga page`
- 中文对照：荒木飞吕彦风格，一只小约克夏犬在地铁站台摆出戏剧化的 JOJO 立，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
