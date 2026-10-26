# Yoshihiro Tatsumi — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `Yoshihiro Tatsumi manga style, gekiga, stark black ink, sparse panels, lonely salaryman, postwar urban alienation, black-and-white manga`
- ZH: 辰巳嘉裕风格，剧画，冷峻黑墨，稀疏分镜，孤独上班族，战后都市疏离，黑白漫画

## (2) 线条、网点/色彩

- 线条：粗黑短促的线，轮廓硬，阴影用大黑块与粗排线。`verbatim`
- 网点/色彩：黑白为主，黑白对比极端，灰网点少，夜色多。`verbatim`
- 质感：墨水线稿为主，网点与平涂并用；不编造实测 HEX 值。`artifact`

## (3) 分镜

- 每页格数少，大格多，留白与沉默格多，节奏慢。`verbatim`
- 节奏：格间时间按作品节奏走，详见 process.md。`impression`
- 视线引导：日式右→左阅读，视线随动作线走。`impression`

## (4) 角色造型

- 中年男人、推人、工人，面孔疲惫，体型佝偻，表情少。`verbatim`
- 角色类型：深夜街头的独行者、推人与被推的劳工、战后废墟与出租屋。`verbatim`
- 动作：动作线与动态姿势按该人作品惯例处理，表情与姿态先行，静止造型亦有张力。`impression`

## (5) 对话框与拟声词

- 对话框少而短，沉默格无字；拟声词几乎不用，寂静即语言。`verbatim`
- 文字量：每页文字密度按作品惯例，旁白与对话的分配见 language.md。`impression`

## (6) 该画什么 / 不该画什么

- 该画：深夜街头的独行者、推人与被推的劳工、战后废墟与出租屋、上班族的通勤与加班、告别与错过、城市角落的性与暴力。`verbatim`
- 不该画：No cute round line、no crowded action panels、no cheerful bright colour、no explanatory narration。`impression`
- Negative prompt: `No cute round line, no crowded action panels, no cheerful bright colour, no explanatory narration`

## (7) 测试提示词示例（现代题材：一个疲惫的上班族与一只小约克夏犬在深夜地铁里共享沉默）

- Prompt: `In the style of Yoshihiro Tatsumi, a tired office worker and a small Yorkshire terrier sharing silence on a late-night subway, gekiga manga page`
- 中文对照：辰巳嘉裕风格，一个疲惫的上班族与一只小约克夏犬在深夜地铁里共享沉默，漫画页。
- Negative: `No photorealistic rendering, no crowded tiny panels, no flat vector illustration, no smooth academic blending`
- 检验点：风格是否迁移到现代题材而不丢分镜、线条与角色造型；背景是否按该人惯例处理；拟声词与对话框是否符合该人习惯。
