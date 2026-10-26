# Stanley Kubrick — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Stanley Kubrick: symmetrical one-point perspective, slow Steadicam glides, cold precision, the human dwarfed by vast designed space`
- ZH: 库布里克风格：对称的一点透视，缓慢的斯坦尼康滑行，冷峻的精确，人在宏大设计空间中显得渺小。

## (2) 镜头语言

- 景别：一点透视的对称构图为主，广角镜头拉深空间；特写克制，用于凝视与疯狂的瞬间。`verbatim`
- 机位与运动：斯坦尼康缓慢前推与跟拍，运镜平稳如机器；《闪灵》走廊跟拍与《2001》旋转空间站皆为匀速运动。`verbatim`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 人物被置于巨大对称空间的中心或尽头：走廊、太空舱、舞厅；调度以几何秩序压迫人物，人物越小空间越大。`impression`

## (4) 剪辑节奏

- 剪辑冷静克制，长镜头与硬切并存；段落之间以音乐与黑场分隔，节奏由空间与音乐而非对白驱动。`impression`

## (5) 色彩与光影

- 色彩：冷白、深黑与原色点缀：太空舱的冷白、《发条橙》的艳色、《闪灵》地毯的橙红；高反差、少中间调。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：环形与对称结构：开头与结尾呼应，中间以章节推进；视点全知而冷漠，结尾常为开放的谜，不给答案。`impression`
- 该拍什么：
- 一点透视的对称走廊与大厅
- 斯坦尼康缓慢前推的跟拍
- 人在巨大空间尽头的渺小身影
- 冷白与原色点缀的几何内景
- 不该拍什么：
- 手持晃动
- 即兴松散的表演
- 暖调煽情
- 快速跳切

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 一点透视的对称走廊与大厅；- 斯坦尼康缓慢前推的跟拍；- 人在巨大空间尽头的渺小身影；- 冷白与原色点缀的几何内景
- 不该拍：- 手持晃动；- 即兴松散的表演；- 暖调煽情；- 快速跳切
- Negative prompt: `No handheld shaky cam, no loose improvisation, no warm sentimental tone, no fast cutting, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Stanley Kubrick, a small Yorkshire terrier sitting on a subway seat, perfect one-point perspective down the carriage, slow Steadicam glide towards the dog, cold fluorescent white, the dog tiny at the vanishing point, vast symmetrical space`
- 中文对照：库布里克风格：一只约克夏犬坐在地铁座位上，车厢完美的一点透视，斯坦尼康缓慢滑向狗，冷白荧光，狗在灭点处显得渺小，宏大对称的空间。
- Negative: `No handheld camera, no warm sentimentality, no fast cutting`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
