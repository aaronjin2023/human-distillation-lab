# Katsuhiro Otomo — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Katsuhiro Otomo manga style, hyper-detailed city, dense line, cinematic panels, apocalyptic science fiction, black-and-white manga`
- ZH: 大友克洋风格，超精细城市，密集线条，电影式分镜，末世科幻，黑白漫画

## (2) 线条、网点/色彩

- 线条：极细密的线，城市建筑如图纸，人物线干净硬朗。`verbatim`
- 网点/色彩：黑白为主，黑白对比强，网点细腻；彩色时红、黑主调。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，电影式分镜，跨页作城市全景，节奏如电影。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 阿基拉式少年、超能力者，摩托车、城市废墟。`verbatim`
- 角色类型：新东京的废墟与重建、超能力少年的暴走、摩托车队的夜驰。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框密，台词冷峻；拟声词大字，爆炸音效粗黑。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：新东京的废墟与重建、超能力少年的暴走、摩托车队的夜驰、城市全景与细节、童梦的公寓异能、末世的秩序与崩坏。`verbatim`
- 不该画：No cute round line、no sparse empty panels、no bright cheerful colour、no simple cartoon background。`impression`
- Negative prompt: `No cute round line, no sparse empty panels, no bright cheerful colour, no simple cartoon background`

## (7) 测试提示词示例（现代题材：一只小约克夏犬骑摩托穿过深夜霓虹废墟城市）

- Prompt: `In the style of Katsuhiro Otomo, a small Yorkshire terrier riding a motorcycle through a neon ruined city at night, cinematic manga page`
- 中文对照：大友克洋风格，一只小约克夏犬骑摩托穿过深夜霓虹废墟城市，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
