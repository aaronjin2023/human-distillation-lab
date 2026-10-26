# Kim Dong-hwa — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kim Dong-hwa, lyrical Korean manhwa, soft watercolour, a girl growing up in the countryside, seasons and first love`
- ZH: 金东华风格：抒情韩国漫话，柔和水彩，乡下少女的成长，四季与初恋。

## (2) 线条、网点/色彩

- 线条：柔和的水彩线，轮廓淡雅；少女造型清秀，线条不硬。`impression`
- 色彩：水彩淡彩，大地、水、天空三色是标志；色彩淡雅，季节感强。`verbatim`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：大格抒情与小格叙事交错；节奏舒缓，留白多；阅读自左而右，视线随少女走。`impression`
- 节奏：切格：抒情大格与叙事小格交错（分镜稿（name））；分镜示例：大格抒情——犬立车厢，小格叙事。`impression`

## (4) 角色造型

- 角色造型：少女面容清秀、长发；乡下人物造型朴素；表情细腻含蓄。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白少、文雅；旁白抒情；拟声词小而少；沉默也是语言。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：大地的颜色：乡下少女的成长、水的颜色：青春与初恋、天空的颜色：告别与远方、四季：春夏秋冬的色彩、乡下风光：田野、河流、天空、少女心境：成长与抉择。`verbatim`
- 不该画：No loud action lines、No photorealistic rendering、No crowded panels、No cynical humour。`impression`
- Negative prompt: `No loud action lines, No photorealistic rendering, No crowded panels, No cynical humour`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Kim Dong-hwa, a small Yorkshire terrier sitting on a subway seat, lyrical Korean manhwa, soft watercolour, seasons, first love`
- 中文对照：金东华风格：一只小约克夏犬坐在地铁座位上，抒情韩国漫话，柔和水彩，四季，初恋。
- Negative: `No loud action lines, no photorealistic rendering, no crowded panels, no cynical humour`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
