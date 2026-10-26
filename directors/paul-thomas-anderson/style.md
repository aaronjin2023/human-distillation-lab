# Paul Thomas Anderson — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Thomas Anderson: sweeping ensemble tracking shots, fathers and sons, oil and faith, the camera circling a charismatic ruin`
- ZH: 保罗·托马斯·安德森风格：横扫群像的跟踪长镜头，父与子，石油与信仰，摄影机环绕一个魅力十足的废墟。

## (2) 镜头语言

- 景别：长镜头跟踪与特写交替；《不羁夜》开场长镜头与《血色将至》荒漠全景为标志。`verbatim`
- 机位与运动：缓慢而坚定的跟踪与环绕：摄影机贴近人物行走，环绕 charismatic 人物，运动即权力的轨迹。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 群像调度：派对、片场、教堂——多人物在同一空间中交错，调度以行走与对峙驱动。`impression`

## (4) 剪辑节奏

- 长镜头内完成段落，剪辑点藏在运动之后；段落以音乐收束，节奏由人物情绪而非情节驱动。`impression`

## (5) 色彩与光影

- 色彩：暖金与土黄主导：《血色将至》荒漠的赭石与黑油对照；《大师》海蓝与暖黄对撞。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：人物史诗结构：开头以青年或外来者切入，中间以父子与师徒关系推进，结尾以决裂或孤独收束，不给和解。`impression`
- 该拍什么：
- 群像派对中的跟踪长镜头
- 荒漠与油田的宽全景
- 父子与师徒的对峙特写
- 暖金与赭石的史诗色调
- 不该拍什么：
- 快速跳切
- 扁平的类型化人物
- 温情圆满的收束
- 冷调低饱和的画面

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 群像派对中的跟踪长镜头；- 荒漠与油田的宽全景；- 父子与师徒的对峙特写；- 暖金与赭石的史诗色调
- 不该拍：- 快速跳切；- 扁平的类型化人物；- 温情圆满的收束；- 冷调低饱和的画面
- Negative prompt: `No fast cutting, no flat genre characters, no sentimental happy ending, no cold desaturated image, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Paul Thomas Anderson, a small Yorkshire terrier sitting on a subway seat, a sweeping tracking shot through the carriage party, a charismatic passenger circling the dog, father-and-son tension in close-up, warm gold against desert ochre light`
- 中文对照：保罗·托马斯·安德森风格：一只约克夏犬坐在地铁座位上，跟踪长镜头横扫车厢派对，一位魅力十足的乘客环绕着狗，父子张力写在特写里，暖金对荒漠赭石的光。
- Negative: `No fast cutting, no flat characters, no sentimental ending`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
