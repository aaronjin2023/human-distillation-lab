# Howard Hawks — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Howard Hawks: genre mastery, fast overlapping dialogue, professional groups under pressure, deep-focus staging, laconic heroes, action as character`
- ZH: 霍克斯风格：类型大师，快速重叠对白，压力下的职业群体，深焦调度，寡言英雄，行动即性格。

## (2) 镜头语言

- 深焦中景：人物在画面内分层站位，前景、中景、背景同时有动作；机位平稳，极少炫技运镜；对白场景用双人中景，动作场景用全景。`verbatim`

## (3) 场面调度

- 职业群体调度：牛仔、飞行员、记者、侦探在封闭空间内各司其职，对话重叠、动作并行；人物走位即职业分工，群戏如乐队合奏。`verbatim`

## (4) 剪辑节奏

- 对白剪辑：快速重叠对白靠剪辑保持节奏，句与句之间几乎无停顿；动作段落剪辑干净利落，追逐与枪战按空间逻辑切，不炫技。`verbatim`

## (5) 色彩与光影

- 黑白为主，硬光与深影服务于类型——黑色电影的夜街、西部片的尘土；彩色期《红河》用 Technicolor 的草原与牛群，色彩作职业世界的标示。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 快速重叠的职业对白
- 深焦群戏与分层站位
- 牛仔、飞行员、侦探的职业群体
- 追逐与枪战的空间逻辑
- 寡言英雄的和解结尾
- 不该拍：
- no slow contemplative pacing, no long-take stillness
- no psychological exposition, no inner monologue
- no handheld shakiness, no documentary roughness
- no sentimental melodrama, no tearful climax
- no ironic distance, no genre parody
- Negative prompt: `No slow contemplative pacing, no long-take stillness, psychological exposition, no inner monologue, handheld shakiness, no documentary roughness, sentimental melodrama, no tearful climax, ironic distance, no genre parody`

## (7) 叙事结构

- 职业群体受压：牛仔赶牛、飞行员冒险、侦探破案、记者抢新闻；故事是群体在压力下的协作，结尾常以群体的和解或胜利收束，英雄寡言。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Howard Hawks, a small Yorkshire terrier sits on a subway seat while a professional crew of commuters — a driver, a guard, a nurse — trade fast overlapping dialogue around it, deep-focus staging, laconic heroism, action as character`
- 中文对照：霍克斯风格：类型大师，快速重叠对白，压力下的职业群体，深焦调度，寡言英雄，行动即性格。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No slow contemplative pacing, no psychological exposition, no handheld shakiness, no sentimental melodrama, no ironic distance`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
