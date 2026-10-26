# Park Chan-wook — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Park Chan-wook: elegant cruelty, symmetrical compositions, revenge as ritual, the camera as a trap, beauty and violence in one frame`
- ZH: 朴赞郁风格：优雅的残酷，对称构图，复仇即仪式，摄影机即陷阱，美与暴力在同一画框里。

## (2) 镜头语言

- 景别：中景与特写并用，对称构图是标志。`verbatim`
- 机位：固定机位与缓慢横移，摄影机讲究画面的对称与陷阱感。`impression`
- 镜头：标准焦段，深焦保留前景与背景的双重陷阱。`impression`
- 运镜禁忌：几乎不用手持晃动，运镜服务于设计的精确。`impression`

## (3) 场面调度

- 人物走位：人物在走廊、楼梯、房间之间被空间困住，走位即陷阱。`verbatim`
- 景深与层次：前景门框、中景人物、背景镜面的三层结构是标志。`verbatim`
- 空间：监禁室、豪宅、山与海，空间越美，陷阱越深。`impression`
- 演员表演风格：职业演员，表演克制而精确，情绪靠构图与剪辑外化。`impression`

## (4) 剪辑节奏

- 剪辑速度：中速，复仇段落用快速剪辑制造冲击，日常段落用长镜头。`impression`
- 转场：匹配剪辑与硬切并用，时间在匹配剪辑里跳跃。`impression`
- 段落结构：以复仇章节推进，真相在段落间翻转。`impression`
- 声音剪辑：古典音乐与环境音构成声景，音乐即仪式。`verbatim`

## (5) 色彩与光影

- 色彩：高饱和红、绿、蓝，色彩即欲望与暴力。`verbatim`
- 光影：强烈的 practical 光与阴影，人物半张脸常隐入阴影。`impression`
- 胶片 / 画幅：彩色，画幅讲究对称与满幅，色彩面积大。`impression`

## (6) 叙事结构

- 结构：环形与多视角，真相在视角切换中翻转。`impression`
- 视点：多视角与不可靠叙述，镜头即陷阱。`impression`
- 时间：顺时与闪回交错，时间在复仇里压缩。`impression`
- 类型处理：以复仇片写人性，类型成规被对称与仪式颠覆。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：对称构图、复仇仪式、美与暴力、镜面与门框、多视角翻转、古典音乐
- 不该拍：手持晃动、线性直叙、煽情音乐、解释性对白、圆满收束
- Negative prompt: `No handheld shaky cam, no flat linear narrative, no sentimental music, no explanatory dialogue, no neat resolution, no loose improvisation`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Park Chan-wook, a small Yorkshire terrier sitting on a subway seat, symmetrical composition, the carriage as a trap, beauty and menace in one frame, classical music, revenge in the waiting`
- 中文对照：朴赞郁风格：一只约克夏犬坐在地铁座位上，对称构图，车厢即陷阱，美与威胁在同一画框里，古典音乐，等待即复仇。
- Negative: `No handheld shaky cam, no flat linear narrative, no sentimental music, no explanatory voiceover, no neat ending`
- 检验点：对称与陷阱感是否成立；美与暴力是否同框；翻转是否在而非直叙。
