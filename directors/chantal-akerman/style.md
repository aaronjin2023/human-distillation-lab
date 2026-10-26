# Chantal Akerman — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chantal Akerman: duration as meaning, the static camera watching a woman's daily labour, time itself as the subject`
- ZH: 阿克曼风格：时长即意义，固定机位注视女性的日常劳作，时间本身即主题。

## (2) 镜头语言

- 景别：固定机位长镜头为主：中景与全景写日常劳作，特写克制；《让娜·迪尔曼》以三小时写三日的家务。`verbatim`
- 机位与运动：几乎不动：固定机位是本体，摄影机拒绝运动，时间在静止中流淌。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 家庭内景调度：厨房、浴室、走廊——女性在固定画框内重复劳作，调度以日常动作驱动，空间即时间的牢笼。`impression`

## (4) 剪辑节奏

- 极少剪辑：长镜头内完成段落，剪辑点即时间的断裂；节奏由日常的重复驱动，越重复越紧张。`impression`

## (5) 色彩与光影

- 色彩：低饱和的日常色彩：厨房的米白、灰蓝、暗褐；色彩克制，光影写时间的流逝。`impression`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：日常时间结构：开头以日常切入，中间以重复推进，结尾以一次偏离（土豆烧焦、一次出走）收束，时间本身即高潮。`impression`
- 该拍什么：
- 固定机位下的日常劳作长镜头
- 女性在厨房与走廊中的重复动作
- 低饱和日常色彩的时间流逝
- 一次偏离日常的静默高潮
- 不该拍什么：
- 快速剪辑
- 戏剧化高潮
- 解释性对白
- 手持晃动

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 固定机位下的日常劳作长镜头；- 女性在厨房与走廊中的重复动作；- 低饱和日常色彩的时间流逝；- 一次偏离日常的静默高潮
- 不该拍：- 快速剪辑；- 戏剧化高潮；- 解释性对白；- 手持晃动
- Negative prompt: `No fast cutting, no dramatic climax, no explanatory dialogue, no handheld shaky cam, no sentimental music`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Chantal Akerman, a small Yorkshire terrier sitting on a subway seat, one static long take, the camera watching the dog and the passengers' daily labour of waiting, time itself as the subject, a small deviation at the end`
- 中文对照：阿克曼风格：一只约克夏犬坐在地铁座位上，一个固定长镜头，摄影机注视狗与乘客等待的日常劳作，时间本身即主题，结尾一次小小的偏离。
- Negative: `No fast cutting, no dramatic climax, no explanatory dialogue`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
