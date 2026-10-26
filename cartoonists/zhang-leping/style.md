# Zhang Leping — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Leping, Sanmao the street orphan, three hairs on a bare head, simple black ink line, wordless humour and deep compassion`
- ZH: 张乐平风格：三毛流浪儿，头顶三根发，简练墨线，无言幽默与深切同情。

## (2) 线条、网点/色彩

- 线条：简练的钢笔墨线，轮廓干净、略带稚气；人物造型极简，三毛三根发一笔可认。`verbatim`
- 色彩：黑白为主，偶有淡彩；明暗靠线条疏密，不靠网点。`verbatim`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：四格或多格连环，每格一景；节奏先慢后急，笑点与泪点同格；阅读自左而右，视线随三毛走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：三毛——光头三根发、瘦小、衣衫褴褛；成人多为类型化：阔人、兵、流氓，体型与三毛对照。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：多无对白，靠画面叙事；偶有短句对白，口语简短；拟声词小而少。`verbatim`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：三毛流浪：街头、码头、弄堂的流浪生活、三毛与狗、与小伙伴的温情、三毛从军：战争中的儿童、贫富对照：阔人与流浪儿同框、三毛的善良与机智、无言的幽默与眼泪。`verbatim`
- 不该画：No ornate decoration、No photorealistic detail、No cynical cruelty、No crowded dialogue balloons。`impression`
- Negative prompt: `No ornate decoration, No photorealistic detail, No cynical cruelty, No crowded dialogue balloons`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Zhang Leping, a small Yorkshire terrier sitting on a subway seat, Sanmao style, simple black ink line, wordless humour, deep compassion`
- 中文对照：张乐平风格：一只小约克夏犬坐在地铁座位上，三毛式简练墨线，无言幽默，深切同情。
- Negative: `No ornate decoration, no photorealistic detail, no cynical cruelty, no crowded dialogue balloons`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
