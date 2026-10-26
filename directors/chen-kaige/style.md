# Chen Kaige — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chen Kaige: the yellow earth as fate, grand landscape holding small people, opera and ritual, history as a long slow tragedy`
- ZH: 陈凯歌风格：黄土地即命运，宏大风景兜住渺小的人，戏曲与仪式，历史是一场漫长的缓慢悲剧。

## (2) 镜头语言

- 景别：大远景与全景为主，人物常是黄土地上的一点。`verbatim`
- 机位：固定机位与缓慢横移，摄影机讲究风景的仪式感。`impression`
- 镜头：广角拍风景，长焦压缩人物的渺小。`impression`
- 运镜禁忌：几乎不用手持晃动与快速剪辑，运镜服务于风景的重量。`impression`

## (3) 场面调度

- 人物走位：人物在黄土高原、戏台、山村之间缓慢移动，走位即命运。`verbatim`
- 景深与层次：前景黄土、中景人物、背景远山的层次是标志。`verbatim`
- 空间：黄土高原、戏台、山村，空间越开阔，人物越渺小。`impression`
- 演员表演风格：职业演员，表演克制而仪式化，情绪靠风景与戏曲外化。`impression`

## (4) 剪辑节奏

- 剪辑速度：慢速，长镜头保留风景与仪式的完整时间。`impression`
- 转场：叠化与淡入淡出为主，时代在叠化里过去。`impression`
- 段落结构：以仪式（婚礼、唱戏、祭祀）作章节，历史在仪式间流逝。`impression`
- 声音剪辑：民歌、戏曲与环境音构成声景，音乐即土地。`verbatim`

## (5) 色彩与光影

- 色彩：土黄、赭石、灰绿的黄土色谱，低饱和、自然光。`verbatim`
- 光影：强烈的自然光，阴影是黄土高原的形状。`impression`
- 胶片 / 画幅：彩色，画幅讲究风景的仪式感，色彩面积大。`impression`

## (6) 叙事结构

- 结构：线性为主，以个人命运写历史的漫长悲剧。`impression`
- 视点：全知而悲悯，镜头站在被历史碾过的人一边。`impression`
- 时间：顺时而漫长，时间在风景与仪式里流逝。`impression`
- 类型处理：以乡土史诗与戏曲写历史，类型成规被风景与仪式颠覆。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：黄土高原、大远景、戏曲与仪式、被历史碾过的个人、民歌与戏曲声、缓慢的悲剧
- 不该拍：快速剪辑、手持晃动、解释性对白、轻佻喜剧、都市奇观
- Negative prompt: `No fast cutting, no handheld shaky cam, no explanatory dialogue, no light comedy, no urban spectacle, no sentimental music`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Chen Kaige, a small Yorkshire terrier sitting on a subway seat, vast composition, the dog small against the carriage, slow long take, folk song in the distance, history pressing in, no explanation`
- 中文对照：陈凯歌风格：一只约克夏犬坐在地铁座位上，宏大的构图，犬在车厢中显得渺小，缓慢的长镜头，远处有民歌，历史压进来，不解释。
- Negative: `No fast cutting, no handheld camera, no explanatory voiceover, no light comedy, no urban spectacle`
- 检验点：风景与人物的比例是否成立；缓慢悲剧感是否在；仪式感是否来自空间而非台词。
