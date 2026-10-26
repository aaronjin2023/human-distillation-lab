# Zhu Deyong — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhu Deyong, urban comics, sharp one-liners, simple line, men and women in the city, bittersweet humour`
- ZH: 朱德庸风格：都市漫画，犀利金句，简笔线条，城市男女，苦涩幽默。

## (2) 线条、网点/色彩

- 线条：简笔线条，轮廓干净、略带涂鸦感；人物造型极简，表情一笔点出。`impression`
- 色彩：黑白与淡彩并行；色彩淡雅，偶用一色点题。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：四格或多格，每格一景；金句在末格；阅读自左而右，视线随人物走。`impression`
- 节奏：切格：场景—转折—点题（分镜稿（name））；分镜示例：切 4 格——车厢、犬、低头族、金句收尾。`impression`

## (4) 角色造型

- 角色造型：涩女郎四位女主角各有标志；都市男女类型化，体型与打扮对照；表情冷峻而幽默。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白短、犀利，金句式；对话框圆润；拟声词小。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：涩女郎：四位都市女性的生活、双响炮：夫妻与家庭的笑话、都市男女：爱情、婚姻、职场、什么事都在发生：都市荒诞、金句：犀利的一句话点题、中年与人生的苦涩幽默。`verbatim`
- 不该画：No gentle poetic blank space、No photorealistic rendering、No long explanatory text、No sweet romantic cliché。`impression`
- Negative prompt: `No gentle poetic blank space, No photorealistic rendering, No long explanatory text, No sweet romantic cliché`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Zhu Deyong, a small Yorkshire terrier sitting on a subway seat, urban comics, sharp one-liners, simple line, bittersweet humour`
- 中文对照：朱德庸风格：一只小约克夏犬坐在地铁座位上，都市漫画，犀利金句，简笔线条，苦涩幽默。
- Negative: `No gentle poetic blank space, no photorealistic rendering, no long explanatory text, no sweet romantic cliché`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
