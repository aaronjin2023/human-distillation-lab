# Cai Zhizhong — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cai Zhizhong, philosophical comics, simple round figures, big head and small body, classical wisdom in everyday scenes`
- ZH: 蔡志忠风格：哲理漫画，简笔圆润人物，大头小身，古典智慧入日常生活。

## (2) 线条、网点/色彩

- 线条：简笔圆润线，轮廓干净、略带童趣；老子、庄子大头小身，一笔可认。`impression`
- 色彩：黑白与淡彩并行；色彩淡雅，不抢线条。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：多格连环，每格一景；节奏舒缓，哲理在末格点出；阅读自左而右，视线随主角走。`impression`
- 节奏：切格：场景—转折—点题（分镜稿（name））；分镜示例：切 4 格——车厢、犬、乘客、犬让座点题。`impression`

## (4) 角色造型

- 角色造型：老子、庄子、孔子等圣贤大头小身、圆润可爱；配角小人物简省；表情温和。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：旁白多、对白少；旁白为典籍白话译文，简短易懂；对话框圆润、文字少。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：老子说：道家智慧入生活、庄子说：逍遥与齐物、孔子、孟子等儒家圣贤、菜根谭：处世哲理、禅宗公案与幽默、古典智慧的现代生活化。`verbatim`
- 不该画：No dark satire、No photorealistic rendering、No crowded panels、No long academic text。`impression`
- Negative prompt: `No dark satire, No photorealistic rendering, No crowded panels, No long academic text`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Cai Zhizhong, a small Yorkshire terrier sitting on a subway seat, philosophical comics, simple round figures, classical wisdom in everyday scenes`
- 中文对照：蔡志忠风格：一只小约克夏犬坐在地铁座位上，哲理漫画，简笔圆润人物，古典智慧入日常生活。
- Negative: `No dark satire, no photorealistic rendering, no crowded panels, no long academic text`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
