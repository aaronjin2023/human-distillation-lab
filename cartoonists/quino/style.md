# Quino — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Quino, Mafalda the little girl, simple expressive line, philosophical humour, one strip one question about the world`
- ZH: 基诺风格：玛法达小女孩，简练表情线，哲学幽默，一则一问世界。

## (2) 线条、网点/色彩

- 线条：简练的表现性线条，轮廓干净；玛法达圆脸短发，一笔可认；表情夸张而细腻。`impression`
- 色彩：黑白为主，彩色版平涂淡彩；色彩不抢线条。`impression`
- 质感：墨水线稿 / 淡彩 / 数码平涂，见上；不编造实测 HEX 值。`impression`

## (3) 分镜

- 分镜：报纸连环条漫，四至六格；笑点在末格；阅读自左而右，视线随玛法达走。`impression`
- 节奏：见 process.md 第 1 节；格间时间与留白按本节分镜习惯处理。`impression`

## (4) 角色造型

- 角色造型：玛法达——小女孩、圆脸、短发、蝴蝶结；配角小伙伴各有标志；成人多为类型化。`verbatim`
- 角色类型：反复出现的角色类型见第 (6) 节与 motifs.md；配角与主角的造型对比以作品画面为准。`impression`

## (5) 对话框与拟声词

- 对话框与拟声词：对白短、犀利，童言问世界；对话框圆润；拟声词小。`impression`
- 文字量：每页文字密度见上；旁白与对话的分配以作品画面为准。`impression`

## (6) 该画什么 / 不该画什么（Negative prompt）

- 该画：玛法达：小女孩问世界、童言哲学：战争、和平、汤、小伙伴：菲利普、苏珊、马诺林、成人世界：父母、老师、政客、阿根廷日常：家庭、学校、街道、一则一问：末格的哲学落点。`verbatim`
- 不该画：No photorealistic rendering、No crowded panels、No cynical cruelty、No long explanatory text。`impression`
- Negative prompt: `No photorealistic rendering, No crowded panels, No cynical cruelty, No long explanatory text`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Quino, a small Yorkshire terrier sitting on a subway seat, Mafalda style, simple expressive line, philosophical humour, one strip one question`
- 中文对照：基诺风格：一只小约克夏犬坐在地铁座位上，玛法达式简练表情线，哲学幽默，一则一问。
- Negative: `No photorealistic rendering, no crowded panels, no cynical cruelty, no long explanatory text`
- 检验点：风格是否一望可认；分镜与线条是否按本节习惯；禁区里的写法是否出现。
