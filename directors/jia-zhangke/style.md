# Jia Zhangke — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jia Zhangke: the Chinese county town in long takes, pop songs leaking from radios, demolition and construction, ordinary people left behind by change`
- ZH: 贾樟柯风格：县城长镜头，流行歌从收音机里漏出来，拆迁与建设，被变化抛下的普通人。

## (2) 镜头语言

- 景别：中景与全景为主，人物常是县城街景中的一部分。`verbatim`
- 机位：固定机位与缓慢横移，摄影机静观县城的日常。`verbatim`
- 镜头：标准焦段，深焦保留街景的多层生活。`impression`
- 运镜禁忌：几乎不用航拍奇观与快速剪辑，运镜克制而现实。`impression`

## (3) 场面调度

- 人物走位：人物在街头、工地、拆迁现场之间行走，空间即变化。`verbatim`
- 景深与层次：前景拆迁废墟、中景人物、背景新楼的三层结构是标志。`impression`
- 空间：县城、工地、江边，空间在拆与建之间。`impression`
- 演员表演风格：非职业与职业演员并用，表演生活化，不煽情。`artifact`

## (4) 剪辑节奏

- 剪辑速度：慢速，长镜头保留县城生活的完整时间。`impression`
- 转场：硬切为主，场景之间不解释，靠时间跳接。`impression`
- 段落结构：以生活段落并置推进，时代在段落间流逝。`impression`
- 声音剪辑：流行歌、收音机、工地噪音构成声景，音乐即时代。`verbatim`

## (5) 色彩与光影

- 色彩：灰黄与冷调的县城色谱，低饱和、实景色。`verbatim`
- 光影：自然光与室内 practical 光，阴影来自真实建筑。`impression`
- 胶片 / 画幅：数字与胶片并用，画幅克制，质感粗粝而直接。`impression`

## (6) 叙事结构

- 结构：线性而松散，生活段落并置，时代在边缘发生。`impression`
- 视点：全知而克制，镜头站在被变化抛下的人一边。`impression`
- 时间：顺时而漫长，时间在拆迁与建设里流逝；《山河故人》横跨三段时代。`impression`
- 类型处理：以纪录片方法拍虚构故事，虚构与纪录互相渗透。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：县城长镜头、拆迁与建设、流行歌与收音机、被抛下的普通人、江边与工地、时间的跳接
- 不该拍：宏大场面、快速剪辑、煽情音乐、解释性对白、圆满收束、脱离现实的奇观
- Negative prompt: `No grand spectacle, no fast cutting, no sentimental music, no explanatory dialogue, no neat resolution, no studio gloss`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jia Zhangke, a small Yorkshire terrier sitting on a subway seat, fixed long take, pop song leaking from a passenger radio, demolition outside the window, the dog stays, no music beyond the radio, time passes`
- 中文对照：贾樟柯风格：一只约克夏犬坐在地铁座位上，固定长镜头，流行歌从乘客收音机里漏出来，窗外是拆迁，犬一直坐在那里，除了收音机没有别的音乐，时间过去了。
- Negative: `No grand spectacle, no fast cutting, no sentimental music, no explanatory voiceover, no neat ending`
- 检验点：县城现实感是否成立；流行歌是否来自环境而非配乐；时间感是否来自跳接而非剪辑。
