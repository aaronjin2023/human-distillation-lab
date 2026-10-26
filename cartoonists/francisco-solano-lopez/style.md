# Francisco Solano López — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Francisco Solano López, El Eternauta, realistic ink line, Buenos Aires under snow, ordinary people against invasion`
- ZH: 索拉诺·洛佩斯风格：《永恒者》，写实墨线，雪落布宜诺斯艾利斯，普通人对抗入侵。

## (2) 线条、网点/色彩

- 线条：写实的钢笔墨线，轮廓清晰、带速写感；人物造型写实，雪景线条细腻。`impression`
- 色彩：黑白为主；雪的白与夜的黑对照强烈；明暗对比强。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：多格连环，格数中等；节奏先慢后急，雪落一格一格推进；阅读自左而右，视线随主角走。`impression`
- 节奏：切格：纪实节奏慢、留白多（分镜稿（name））；分镜示例：多格连环，雪落一格一格推进。`impression`

## (4) 角色造型

- 角色造型：胡安·萨尔沃等普通人造型写实；外星入侵者造型怪异；人物表情坚毅。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白简短有力；旁白多、纪实味；拟声词小。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：永恒者：雪落布宜诺斯艾利斯、普通人对抗入侵、雪：致命的雪、布宜诺斯艾利斯都市、死亡之鹰：战争与飞行、睡美人：梦境与现实。`verbatim`
- 不该画：No cute cartoon simplification、No bright cheerful colour、No crowded small panels、No wordless ambiguity。`impression`
- Negative prompt: `No cute cartoon simplification, No bright cheerful colour, No crowded small panels, No wordless ambiguity`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Francisco Solano López, a small Yorkshire terrier sitting on a subway seat, El Eternauta style, realistic ink line, city under snow, ordinary people`
- 中文对照：索拉诺·洛佩斯风格：一只小约克夏犬坐在地铁座位上，《永恒者》式写实墨线，雪落都市，普通人。
- Negative: `No cute cartoon simplification, no bright cheerful colour, no crowded small panels, no wordless ambiguity`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
