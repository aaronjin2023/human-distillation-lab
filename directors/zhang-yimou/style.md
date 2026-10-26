# Zhang Yimou — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Yimou: saturated colour as fate, grand compositions of red and yellow, ritual and enclosure, the individual crushed by history`
- ZH: 张艺谋风格：饱和色彩即命运，红与黄的大构图，仪式与围合，个人被历史碾过。

## (2) 镜头语言

- 景别：全景与大远景为主，人物常是色彩海洋中的一点。`verbatim`
- 机位：固定机位与缓慢横移，摄影机讲究构图的对称与仪式感。`impression`
- 镜头：广角与长焦并用，色彩的面积本身就是叙事。`impression`
- 运镜禁忌：几乎不用手持晃动与碎切，运镜服务于画面的仪式感。`impression`

## (3) 场面调度

- 人物走位：人物在院落、城墙、高粱地之间被空间围合，走位即命运。`verbatim`
- 景深与层次：前景红灯笼、中景人物、背景灰墙的三层结构是标志。`verbatim`
- 空间：封闭院落与开阔高粱地并置，空间越封闭，色彩越浓烈。`impression`
- 演员表演风格：职业演员，表演外放而克制并存，情绪靠色彩与仪式外化。`impression`

## (4) 剪辑节奏

- 剪辑速度：中速，仪式段落用长镜头保留完整过程。`impression`
- 转场：硬切与叠化并用，季节与时代在叠化里过去。`impression`
- 段落结构：以仪式（婚礼、点灯、祭祀）作章节，历史在仪式间流逝。`impression`
- 声音剪辑：唢呐、锣鼓与环境音构成声景，音乐即命运。`verbatim`

## (5) 色彩与光影

- 色彩：高饱和红、黄、绿，红高粱、红灯笼、大红棉袄是标志。`verbatim`
- 光影：强烈的自然光与暖调，阴影是灰墙的形状。`impression`
- 胶片 / 画幅：彩色，画幅讲究对称与满幅，色彩面积大。`impression`

## (6) 叙事结构

- 结构：线性为主，以家庭 / 家族的兴衰写历史。`impression`
- 视点：全知而悲悯，镜头站在被历史碾过的人一边。`impression`
- 时间：顺时而漫长，时间在仪式与季节里流逝。`impression`
- 类型处理：以乡土史诗写历史，类型成规被色彩与仪式颠覆。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：高饱和红黄、封闭院落、仪式章节、高粱地与城墙、被历史碾过的个人、唢呐与锣鼓
- 不该拍：低饱和灰调、快速剪辑、手持晃动、解释性对白、轻佻喜剧
- Negative prompt: `No muted grey palette, no fast cutting, no handheld shaky cam, no explanatory dialogue, no light comedy, no loose improvisation`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Zhang Yimou, a small Yorkshire terrier sitting on a subway seat, saturated red and yellow, ritual composition, the dog small against a grand coloured frame, long take, fate pressing in, no music beyond a single reed note`
- 中文对照：张艺谋风格：一只约克夏犬坐在地铁座位上，高饱和红与黄，仪式感构图，犬在宏大的色彩画框中显得渺小，长镜头，命运压进来，除了一声唢呐没有别的音乐。
- Negative: `No muted grey palette, no fast cutting, no handheld camera, no explanatory voiceover, no light comedy`
- 检验点：色彩面积是否成为叙事；仪式感构图是否成立；个人被压迫感是否来自空间而非台词。
