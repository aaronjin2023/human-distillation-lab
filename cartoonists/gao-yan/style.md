# Gao Yan — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gao Yan, quiet youth comics, soft digital line, green light and night train, gentle loneliness and warmth`
- ZH: 高妍风格：安静青年漫画，柔和数码线，绿灯与夜车，温柔的孤独与暖意。

## (2) 线条、网点/色彩

- 线条：柔和的数码线，轮廓干净、略带手绘感；人物造型简练，表情含蓄。`impression`
- 色彩：淡彩为主，绿灯的绿、夜车的蓝是标志色；色彩淡雅，氛围重于情节。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：大格抒情与小格叙事交错；节奏舒缓，留白多；阅读自右而左或竖屏，视线随主角走。`impression`
- 节奏：竖屏长条切格、定下滑节奏（竖屏分镜稿）；分镜示例：大格抒情——犬立车厢，小格叙事。`impression`

## (4) 角色造型

- 角色造型：青年男女造型简练、面容清秀；丘丘等小动物配角圆润；表情含蓄而细腻。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白少、文雅；旁白抒情；拟声词小而少；沉默也是语言。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：绿灯：绿灯下的等待与相遇、丘丘的奇妙日常：小动物的日常、夜车：深夜列车与远方、青年孤独：温柔的孤独、城市夜景：便利店、车站、街道、日常抒情：小确幸。`verbatim`
- 不该画：No loud action lines、No photorealistic rendering、No crowded panels、No cynical humour。`impression`
- Negative prompt: `No loud action lines, No photorealistic rendering, No crowded panels, No cynical humour`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Gao Yan, a small Yorkshire terrier sitting on a subway seat, quiet youth comics, soft digital line, night train, gentle loneliness and warmth`
- 中文对照：高妍风格：一只小约克夏犬坐在地铁座位上，安静青年漫画，柔和数码线，夜车，温柔的孤独与暖意。
- Negative: `No loud action lines, no photorealistic rendering, no crowded panels, no cynical humour`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
