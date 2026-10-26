# Lat — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lat, Kampung Boy, lively Malaysian village life, quick ink caricature, gentle humour`
- ZH: 拉特风格：甘榜小子，马来西亚乡村生活，快捷墨水漫画，温和幽默。

## (2) 线条、网点/色彩

- 线条：快捷的墨水漫画线，轮廓流畅、带速写感；甘榜人物造型夸张而亲切。`impression`
- 色彩：黑白为主，彩色版淡彩；色彩不抢线条。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：报纸连环与图像小说并行；格数中等，节奏轻快；阅读自左而右，视线随小拉特走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：甘榜小子——圆脸、短发、赤脚；乡村人物造型各有标志；表情生动。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白短、口语化，带马来味；对话框圆润；拟声词小。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：甘榜小子：马来西亚乡村童年、拉特的城市：吉隆坡都市生活、拉特与朋友们：乡村与都市朋友、乡村风光：甘榜、稻田、河流、多元族群：马来、华人、印度人、童年与成长。`verbatim`
- 不该画：No dark satire、No photorealistic rendering、No crowded panels、No cynical humour。`impression`
- Negative prompt: `No dark satire, No photorealistic rendering, No crowded panels, No cynical humour`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Lat, a small Yorkshire terrier sitting on a subway seat, Kampung Boy style, lively Malaysian village life, quick ink caricature, gentle humour`
- 中文对照：拉特风格：一只小约克夏犬坐在地铁座位上，甘榜小子式马来西亚乡村生活，快捷墨水漫画，温和幽默。
- Negative: `No dark satire, no photorealistic rendering, no crowded panels, no cynical humour`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
