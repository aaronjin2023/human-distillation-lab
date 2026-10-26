# Charles M. Schulz — 漫画风格规格 style.md（给图像模型）

> 只描述画面，不描述人生。引用画面时只指认到具体作品与页/格，不整页复制。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles M. Schulz, minimal clean line, four-panel gag, children and a beagle, sparse backgrounds, newspaper comic strip`
- ZH: 舒尔茨风格，极简干净线，四格笑话，孩子与小猎犬，稀疏背景，报纸连环漫画。

## (2) 线条、网点/色彩

- 线条：极简干净的线，造型圆润；背景几乎空白。`verbatim`
- 网点/色彩：黑白日报版，彩色星期日版平涂柔和。
- 质感：墨水线稿 + 柔和彩色；纸面干净，无肌理。

## (3) 分镜

- 格数与格形：四格为主，方格；节奏靠停顿与留白。
- 节奏：节奏靠停顿与留白，四格一停顿，笑点在停顿里。
- 视线引导：美式阅读顺序左→右；视线在人脸与留白间移动。

## (4) 角色造型

- 造型：查理·布朗的圆头、露西的心理诊所、史努比的狗屋、伍德斯托克。
- 角色类型：失败的孩子、刻薄的女孩、幻想的小猎犬、黄鸟；主角失败，配角机智。
- 动作：动作极简，踢球、走路、躺狗屋；速度线全无。

## (5) 对话框与拟声词

- 对话框：对话框简短，哲学化童言。
- 拟声词：拟声词少；踢球声以画面代替。
- 文字量：每页文字密度低，对话简短，留白本身就是笑点。

## (6) 该画什么 / 不该画什么

- 该画：查理·布朗的失败、露西的心理诊所、史努比的幻想（王牌飞行员）、棒球与风筝、圣诞节与南瓜大王、伍德斯托克、狗狗屋顶。`verbatim`
- 不该画：不画细密背景、不画写实解剖、不画拥挤格子、不画冷酷讽刺、不画鲜亮饱和色。
- Negative prompt: `No detailed backgrounds, no realistic anatomy, no crowded panels, no cynical cruelty, no bright saturated colour`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Charles M. Schulz, a small Yorkshire terrier sitting on a subway seat, minimal clean line, four-panel gag, sparse background, gentle philosophy`
- 中文对照：舒尔茨风格：一只小约克夏犬坐在地铁座位上，极简干净线，四格笑话，稀疏背景，温和哲思。
- Negative: `No detailed backgrounds, no realistic anatomy, no cynical cruelty`
- 检验点：线是否极简干净；背景是否稀疏；停顿与留白是否还在；哲思是否温和。
