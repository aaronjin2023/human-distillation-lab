# Orijit Sen — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Orijit Sen, River of Stories, India's first graphic novel, folk art and reportage, Narmada dam and Adivasi life`
- ZH: 森风格：《故事之河》，印度首部图像小说，民间艺术与纪实，纳尔默达大坝与阿迪瓦西生活。

## (2) 线条、网点/色彩

- 线条：民间艺术味的线条，轮廓简练有力；人物造型带印度民间画味。`impression`
- 色彩：淡彩与平涂并行；色彩取自民间艺术，淡雅而有力。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：多格连环，格数中等；节奏舒缓，民间故事与纪实交错；阅读自左而右，视线随河流走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：阿迪瓦西人物造型写实而民间化；河流与大坝是主角；表情坚毅。`impression`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：旁白多、纪实与民间故事交错；对白简短；拟声词少。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：故事之河：纳尔默达河与大坝、阿迪瓦西：原住民生活与民间故事、德里漫画：德里都市、民间艺术：印度民间画味、河流：河即叙事、抗争：大坝与 displacement。`verbatim`
- 不该画：No photorealistic rendering、No bright saturated colour、No exaggerated action lines、No crowded small panels。`impression`
- Negative prompt: `No photorealistic rendering, No bright saturated colour, No exaggerated action lines, No crowded small panels`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Orijit Sen, a small Yorkshire terrier sitting on a subway seat, River of Stories style, folk art and reportage, river and dam`
- 中文对照：森风格：一只小约克夏犬坐在地铁座位上，《故事之河》式民间艺术与纪实，河流与大坝。
- Negative: `No photorealistic rendering, no bright saturated colour, no exaggerated action lines, no crowded small panels`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
