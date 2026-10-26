# Jafar Panahi — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jafar Panahi: the camera trapped in one small space, real life pressing in from outside, women and children against the rules, fiction filmed as if it were happening now`
- ZH: 帕纳西风格：摄影机困在一个小空间里，真实生活从外面压进来，女人与孩子对抗规则，虚构拍得像正在发生。

## (2) 镜头语言

- 景别：中景与近景为主，空间逼仄时用人物的面部与手部特写。`verbatim`
- 机位：固定机位与车内机位，摄影机常被困在出租车、房间、走廊里。`verbatim`
- 镜头：标准焦段，景深保留门里门外的两个世界。`impression`
- 运镜禁忌：几乎不用航拍、升降与花哨运镜，摄影机越受限越真实。`impression`

## (3) 场面调度

- 人物走位：人物在封闭空间里进出、等待、被拦下，门槛就是权力线。`verbatim`
- 景深与层次：前景是规则（门卫、警察、车窗），背景是想去的地方。`impression`
- 空间：出租车、公寓、街道，空间越小，外部世界的压力越大。`impression`
- 演员表演风格：非职业演员与真人出演，表演克制，情绪藏在等待里。`artifact`

## (4) 剪辑节奏

- 剪辑速度：中慢速，长镜头保留等待与僵持的完整时间。`impression`
- 转场：硬切为主，场景之间不解释，靠重复的遭遇推进。`impression`
- 段落结构：环形与接力式（《生命的圆圈》多位女性接力，命运循环）。`impression`
- 声音剪辑：车外人声、街头噪音不断渗入封闭空间，声音即外部世界。`verbatim`

## (5) 色彩与光影

- 色彩：德黑兰街头的灰黄与车内暖调并置，低饱和、实景色。`verbatim`
- 光影：自然光与车内顶光，阴影来自真实建筑而非布光。`impression`
- 胶片 / 画幅：数字拍摄为主（《出租车》车载小机器拍摄），质感粗粝而直接。`artifact`

## (6) 叙事结构

- 结构：环形与开放式：一个愿望受阻、换人、再受阻，结尾不解决。`impression`
- 视点：限知而贴近，镜头只跟得上人物走得动的范围。`impression`
- 时间：顺时，真实时间即影片时间，等待不被剪掉。`impression`
- 类型处理：以纪录片方法拍虚构故事，演员与导演本人的处境互为镜像（《出租车》导演本人开车）。`artifact`

## (7) 该拍什么 / 不该拍什么

- 该拍：被困的小空间、女性的日常抗争、等待与受阻、车内对话、环形接力结构、真实渗入虚构
- 不该拍：宏大场面、快速剪辑、煽情音乐、解释性对白、圆满解决、脱离现实的奇观
- Negative prompt: `No fast cutting, no grand spectacle, no sentimental music, no explanatory dialogue, no neat resolution, no studio gloss`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jafar Panahi, a small Yorkshire terrier sitting on a subway seat, fixed camera inside the carriage, the dog waits while passengers come and go, real street noise leaks in, no music, no explanation of where the dog is going`
- 中文对照：帕纳西风格：一只约克夏犬坐在地铁座位上，车厢内固定机位，犬等待着，乘客来来去去，真实的街头噪音渗入车厢，没有音乐，不解释犬要去哪里。
- Negative: `No fast cutting, no grand spectacle, no sentimental music, no explanatory voiceover, no neat ending`
- 检验点：受限空间感是否成立；等待是否被完整保留；真实感是否来自声音与空间而非表演。
