# George Herriman — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George Herriman, shifting desert landscapes, poetic dialect, Krazy Kat and Ignatz Mouse, surreal newspaper comic page`
- ZH: 赫里曼风格，变幻沙漠风景，诗意方言，疯狂猫与老鼠，超现实报纸连环画页。

## (2) 线条、网点/色彩

- 线条：线条简洁而富有诗意，沙漠背景每格变幻；造型极简。`verbatim`
- 网点/色彩：黑白为主，彩色星期日版用色柔和。
- 质感：墨水线稿 + 柔和彩色；纸面干净，背景每格不同。

## (3) 分镜

- 格数与格形：格数少，方格为主；背景每格不同；节奏如诗。
- 节奏：节奏如诗，背景变幻即时间；一页可讲一个黄昏。
- 视线引导：美式阅读顺序左→右；视线在猫、鼠、狗三角间移动，背景每格都是新画。

## (4) 角色造型

- 造型：疯狂猫（雌雄莫辨）、伊格纳茨老鼠（砖头）、奥菲瑟·帕普警犬；沙漠中的仙人掌与月亮。
- 角色类型：疯狂猫、扔砖老鼠、警犬；三角即世界。
- 动作：动作极简，扔砖、追逐、凝视；速度线全无。

## (5) 对话框与拟声词

- 对话框：对话框多，诗意方言；疯狂猫的独特英语。
- 拟声词：拟声词轻；砖头声以画面代替。
- 文字量：每页文字密度中等，对话诗意，旁白少。

## (6) 该画什么 / 不该画什么

- 该画：沙漠与月亮、砖头与爱情、猫鼠狗三角、变幻的背景、诗意方言、西班牙语点缀、孤独与温柔。`verbatim`
- 不该画：不画细密背景、不画写实解剖、不画快速动作、不画现代俚语、不画黑色阴郁。
- Negative prompt: `No dense detailed backgrounds, no realistic anatomy, no fast action, no modern slang, no dark noir mood`

## (7) 测试提示词示例（现代题材：深夜便利店外的流浪猫）

- Prompt: `In the style of George Herriman, a stray cat outside a convenience store late at night, shifting desert-like backgrounds, poetic dialect, gentle surreal humour`
- 中文对照：赫里曼风格：深夜便利店外的流浪猫，变幻的沙漠式背景，诗意方言，温柔超现实幽默。
- Negative: `No dense detailed backgrounds, no realistic anatomy, no fast action`
- 检验点：背景是否每格变幻；方言是否诗意；砖头梗是否还在（哪怕换成现代物）。
