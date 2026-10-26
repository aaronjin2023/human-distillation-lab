# Joost Swarte — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joost Swarte, precise geometric ligne claire, flat bright colour, architectural composition, deadpan absurd humour, Dutch clear-line comic page`
- ZH: 约斯特·斯瓦特风格，精确几何清晰线，明亮平涂，建筑式构图，冷面荒诞幽默，荷兰清晰线漫画页。

## (2) 线条、网点/色彩

- 线条：精确均匀的清晰线，几何感强，轮廓如建筑制图；线条不抖、不粗、不皴。`verbatim`
- 网点/色彩：平涂鲜亮，无渐变：红、黄、蓝三原色并置，间有黑块压住画面。
- 质感：墨水线稿 + 平涂；纸面干净如制图，无肌理。

## (3) 分镜

- 格数与格形：格数中等，方格为主，构图如建筑平面；整页大格展现建筑与街道。
- 节奏：节奏冷静均匀，荒诞靠情节不靠速度；一页一个冷笑话。
- 视线引导：欧式左→右阅读；视线沿建筑线条走，先看结构再看人物。

## (4) 角色造型

- 造型：约波·德·波约（Jopo de Pojo）：摇滚青年与荒诞冒险；安东·马卡萨尔：侦探式冷面主角；卡托恩与平巴尔：儿童双人组。
- 角色类型：冷面小人物、侦探、摇滚青年、儿童；主角面无表情，世界荒诞。
- 动作：动作少而准，行走、开门、跌落；动态靠构图不靠速度线。

## (5) 对话框与拟声词

- 对话框：对话框小而工整，文字冷静；笑点在图文反差。
- 拟声词：拟声词少而工整，字形如建筑标牌。
- 文字量：每页文字密度低，对话精简，画面自己讲荒诞。

## (6) 该画什么 / 不该画什么

- 该画：清晰线（ligne claire）、建筑与街道平面、约波·德·波约的摇滚冒险、安东·马卡萨尔的侦探冷面、卡托恩与平巴尔、《Modern Papier》杂志、《纽约客》式单幅冷笑话、错位与误会。`verbatim`
- 不该画：不画潦草抖线、不画渐变阴影、不画拥挤对话框、不画写实渲染、不画喧哗速度线。
- Negative prompt: `No sketchy rough line, no gradient shading, no crowded dialogue, no photorealistic rendering, no loud speed lines, no muted palette`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Joost Swarte, a small Yorkshire terrier on a subway seat drawn as a precise architectural elevation, ligne claire, flat bright colour, deadpan absurd humour, almost no words`
- 中文对照：约斯特·斯瓦特风格：一只小约克夏犬坐在地铁座位上，画成立面图般精确，清晰线，明亮平涂，冷面荒诞幽默，几乎无字。
- Negative: `No sketchy rough line, no gradient shading, no crowded dialogue`
- 检验点：线是否精确如制图；色彩是否平涂鲜亮；荒诞是否靠结构不靠表情。
