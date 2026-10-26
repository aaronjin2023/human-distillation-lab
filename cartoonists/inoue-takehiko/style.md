# Takehiko Inoue — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Takehiko Inoue manga style, dynamic sports and samurai, expressive ink line, realistic anatomy, emotional faces, black-and-white manga`
- ZH: 井上雄彦风格，动态运动与武士，表情墨线，写实解剖，情感面孔，黑白漫画

## (2) 线条、网点/色彩

- 线条：有力而富表情的墨线，肌肉与汗水用粗线，武士用书法感线。`verbatim`
- 网点/色彩：黑白为主，墨色浓淡分明；彩色时水墨感强。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，篮球动作分解细，武士对决用大格，节奏张弛。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 樱木式红发少年、宫本武藏式武士，体型真实，表情强烈。`verbatim`
- 角色类型：灌篮高手的篮球对决、浪客行的武士修行、REAL 的轮椅篮球。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框密，台词热血；拟声词大字，篮球与刀光音效粗黑。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：灌篮高手的篮球对决、浪客行的武士修行、REAL 的轮椅篮球、汗水与眼泪、师徒与对手、胜负与成长。`verbatim`
- 不该画：No cute round line、no sparse slow panels、no photorealistic rendering、no flat vector style。`impression`
- Negative prompt: `No cute round line, no sparse slow panels, no photorealistic rendering, no flat vector style`

## (7) 测试提示词示例（现代题材：一只小约克夏犬在深夜体育馆看轮椅篮球赛）

- Prompt: `In the style of Takehiko Inoue, a small Yorkshire terrier watching a wheelchair basketball game in a night gym, emotional sports manga page`
- 中文对照：井上雄彦风格，一只小约克夏犬在深夜体育馆看轮椅篮球赛，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
