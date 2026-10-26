# Mei Lanfang — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处；本文件不引无法核对的台词原文。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mei Lanfang: Peking opera dan roles: flowing water sleeves, orchid fingers, circular stage walks, rounded singing voice, restrained sorrow beneath grace`
- ZH: 梅兰芳风格：京剧旦角，唱念做打，水袖流转、兰花指、圆场台步，嗓音圆润，端庄之下藏着克制的悲哀。

## (2) 形体

- 身体语言：水袖如水，舒展而不甩脱；台步圆场，小碎步平稳无声；身段讲究三弯（颈、腰、膝），动中有静。
- 镜头 / 舞台尺度：舞台尺度：后排观众可读的身段放大，但不失细腻；特写（影像记录）下手指与眼神的微小变化仍完整。
- 禁忌形体：不用大开大合的武生动作，不用生活化的随意步态，不用夸张的面部扭曲。

## (3) 台词

- 声音：嗓音甜润圆厚，行腔委婉；念白分京白与韵白，字头清晰、归韵讲究；唱段讲究气口与顿挫。
- 台词处理：唱念做打四功并重：唱是骨架，念白虚实相生，做是身段，打开合有度；独白式念白少，多用对白与唱段推进。
- 沉默的使用：停顿在唱腔的气口里：一个长拖腔后的静默，比念白更重；身段停住时，眼神不停。

## (4) 表情与眼神

- 表情：淡妆不浓，面部以眼神与眉梢传情；哭不皱眉、不张口，以水袖半掩面、肩头微颤代之。
- 眼神：眼波流转：看人先低垂、再缓缓抬起；凝视对手时目光定住，余光扫向观众。

## (5) 角色类型

- 常演角色：旦角为主：贵妃（《贵妃醉酒》）、虞姬（《霸王别姬》）、赵艳容（《宇宙锋》）、穆桂英；多为端庄、痴情、刚烈的女性。
- 类型突破：晚年演《穆桂英挂帅》，旦角而带帅气，身段在端庄中加入挂帅的英气；早年男旦演女性，以身段化去性别痕迹。
- 禁演类型：几乎不演生行、净行、丑行；不演市井泼辣的丑旦。

## (6) 该演什么 / 不该演什么

- 该演：京剧旦角行当、贵妃醉酒式独舞身段、水袖功、圆场台步、唱段中的克制悲哀
- 不该演：自然主义对白戏、生活化随意步态、夸张面部表情、西方舞台调度
- Negative prompt: `no naturalistic dialogue, no casual everyday gait, no exaggerated facial distortion, no Western stage blocking, no improvised lines, no realistic makeup`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Mei Lanfang, a man buys oden at a convenience store late at night. water sleeves half-covering the face, small circular steps to the counter, a long held note of hesitation before choosing, sorrow held beneath grace`
- 中文对照：一个人在深夜便利店买关东煮。水袖半掩面，小圆场步走到柜台前，选关东煮前拖一个长腔般的迟疑，端庄之下藏着悲哀。
- Negative: `No naturalistic mumbling, no exaggerated gestures, no casual slouching, no Western blocking`
- 检验点：水袖与圆场是否成立；唱腔式停顿是否代替了解释性台词；悲哀是否收着而不外露。
