# Sanpei Shirato — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Sanpei Shirato manga style, gekiga, heavy black ink, dense hatching, dynamic ninja action, class struggle historical drama, black-and-white manga`
- ZH: 白土三平风格，剧画，浓重黑墨，密排线，动态忍者动作，阶级斗争历史剧，黑白漫画

## (2) 线条、网点/色彩

- 线条：粗黑有力的轮廓线，排线密而硬，黑块面积大。`verbatim`
- 网点/色彩：黑白为主，黑白对比强烈，网点少，靠排线与黑块明暗。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数多，动作分解细，斜格与跨页并用，战斗场面格子碎。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 忍者体型精悍，动作如武术分解，农民与武士造型对比鲜明。`verbatim`
- 角色类型：忍者卡姆依的逃亡与反抗、阶级压迫下的农民与武士、武艺对决的分解动作。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框方圆并用，旁白多，字体密；拟声词粗黑大字。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：忍者卡姆依的逃亡与反抗、阶级压迫下的农民与武士、武艺对决的分解动作、江户时代的村落与山林、师徒与同伴的背叛、历史中的底层视角。`verbatim`
- 不该画：No cute round Tezuka line、no empty white background、no photorealistic rendering、no light cheerful comedy tone。`impression`
- Negative prompt: `No cute round Tezuka line, no empty white background, no photorealistic rendering, no light cheerful comedy tone`

## (7) 测试提示词示例（现代题材：一个外卖骑手忍者跃过现代地铁站上方的屋顶）

- Prompt: `In the style of Sanpei Shirato, a delivery rider ninja leaping across rooftops above a modern subway station, gekiga manga page`
- 中文对照：白土三平风格，一个外卖骑手忍者跃过现代地铁站上方的屋顶，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
