# Alfonso Wong — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfonso Wong, Old Master Q, four to six panels, visual slapstick, minimal dialogue, Hong Kong everyday life`
- ZH: 王泽风格：老夫子，四至六格，视觉滑稽，极少对白，香港日常生活。

## (2) 线条、网点/色彩

- 线条：简洁利落的钢笔线，轮廓干净；老夫子瓜皮帽、马褂一笔可认。`verbatim`
- 色彩：黑白为主，彩色版平涂淡彩；色彩不抢线条。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：四至六格定式，每格一景；笑点在末格；阅读自左而右，视线随老夫子走。`verbatim`
- 节奏：切 4–6 格、定笑点落格（分镜稿（name））；分镜示例：切 4 格——车厢、犬、乘客、犬把座位让出。`impression`

## (4) 角色造型

- 角色造型：老夫子——瓜皮帽、马褂、八字胡；大番薯、秦先生、陈小姐、老赵各有标志；体型对照生笑点。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：多为默片式，画面下方配四字成语标题；对白极少、口语简短；拟声词小。`verbatim`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：老夫子：瓜皮帽马褂的滑稽主角、大番薯、秦先生、陈小姐、老赵的搭档戏、香港日常生活：茶楼、街市、巴士、水浒、西游等古典改编、四字成语标题、中西文化碰撞的笑话。`verbatim`
- 不该画：No long dialogue、No photorealistic rendering、No dark cynical satire、No crowded panels。`impression`
- Negative prompt: `No long dialogue, No photorealistic rendering, No dark cynical satire, No crowded panels`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Alfonso Wong, a small Yorkshire terrier sitting on a subway seat, Old Master Q style, four to six panels, visual slapstick, minimal dialogue`
- 中文对照：王泽风格：一只小约克夏犬坐在地铁座位上，老夫子式四至六格，视觉滑稽，极少对白。
- Negative: `No long dialogue, no photorealistic rendering, no dark cynical satire, no crowded panels`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
