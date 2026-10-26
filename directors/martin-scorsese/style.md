# Martin Scorsese — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Martin Scorsese: restless tracking shots, freeze frames, voiceover confession, rock music driving the cut, New York streets as a moral arena`
- ZH: 斯科塞斯风格：不安的跟踪长镜头，定格，画外音自白，摇滚乐驱动剪辑，纽约街头即道德竞技场。

## (2) 镜头语言

- 景别：跟踪长镜头与特写交替；《好家伙》夜总会一镜跟拍为标志性调度。`verbatim`
- 机位与运动：摄影机紧贴人物行走：长镜头跟拍、急推、急拉，运动即欲望的速度。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 街头与酒吧群戏：人物在狭窄空间中游走、争吵、背叛；调度以行走与围坐驱动，权力在移动中转移。`impression`

## (4) 剪辑节奏

- 音乐驱动剪辑：摇滚乐切点即剪辑点，定格与跳切并用；画外音自白与画面并行，时间靠音乐压缩。`impression`

## (5) 色彩与光影

- 色彩：霓虹红与街灯暖黄对照深夜蓝黑；《愤怒的公牛》黑白摄影以灰阶写暴力与孤独。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：自白式传记结构：开头画外音交代人物，中间以欲望上升、暴力失控推进，结尾以审判或孤独收束，不给救赎。`impression`
- 该拍什么：
- 摇滚乐驱动的街头跟踪长镜头
- 画外音自白配定格
- 酒吧与夜总会中的群戏游走
- 霓虹红与深夜蓝黑的城市夜景
- 不该拍什么：
- 平稳冷漠的旁观机位
- 无音乐的干剪辑
- 温情圆满的收束
- 扁平明亮的喜剧光

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 摇滚乐驱动的街头跟踪长镜头；- 画外音自白配定格；- 酒吧与夜总会中的群戏游走；- 霓虹红与深夜蓝黑的城市夜景
- 不该拍：- 平稳冷漠的旁观机位；- 无音乐的干剪辑；- 温情圆满的收束；- 扁平明亮的喜剧光
- Negative prompt: `No detached static camera, no dry music-free cutting, no sentimental happy ending, no flat bright comedy lighting, no moralizing voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Martin Scorsese, a small Yorkshire terrier sitting on a subway seat, a long tracking shot gliding down the carriage to rock music, freeze frame on the dog's face, voiceover confession from a passenger, neon red against night blue`
- 中文对照：斯科塞斯风格：一只约克夏犬坐在地铁座位上，摇滚乐中长镜头滑过车厢，定格在狗的脸上，乘客画外音自白，霓虹红对深夜蓝。
- Negative: `No static camera, no music-free cutting, no sentimental ending`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
