# Terrence Malick — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Terrence Malick: magic-hour light, whispered voiceover, nature dwarfing history, the camera wandering like a wondering eye`
- ZH: 马力克风格：魔幻时刻的光，耳语般的画外音，自然压倒历史，摄影机如一双沉思的眼睛般游荡。

## (2) 镜头语言

- 景别：广角远景与自然特写交替：草原、天空、水流的大全景对照草叶与昆虫的特写。`verbatim`
- 机位与运动：手持与斯坦尼康结合的游荡运动：摄影机绕人物缓慢环行，少固定机位，多跟随自然光走。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 人物在自然中渺小：麦田、丛林、草原中的行走；调度以自然元素（风、水、光）驱动，人物只是过客。`impression`

## (4) 剪辑节奏

- 联想式剪辑：自然空镜插入叙事，时间跳跃，段落以画外音与音乐连接，节奏舒缓而断续。`impression`

## (5) 色彩与光影

- 色彩：魔幻时刻的金黄与青绿主导：日出日落的暖金、草原的青绿、天空的淡蓝，低饱和而明亮。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：散文式结构：线性叙事中插入自然沉思与哲学画外音；开头以自然空镜起笔，结尾以和解或轮回收束，不给因果。`impression`
- 该拍什么：
- 魔幻时刻的草原与天空远景
- 耳语画外音配自然空镜
- 人物在自然中渺小的行走
- 金黄与青绿的低饱和光影
- 不该拍什么：
- 快速剪辑
- 解释性对白
- 戏剧化高潮
- 棚拍人造光

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 魔幻时刻的草原与天空远景；- 耳语画外音配自然空镜；- 人物在自然中渺小的行走；- 金黄与青绿的低饱和光影
- 不该拍：- 快速剪辑；- 解释性对白；- 戏剧化高潮；- 棚拍人造光
- Negative prompt: `No fast cutting, no explanatory dialogue, no dramatic climax, no studio artificial light, no linear cause-and-effect plotting`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Terrence Malick, a small Yorkshire terrier sitting on a subway seat, magic-hour light through the windows, whispered voiceover wondering about the world, cutaways to sky and leaves, the dog small inside a vast wondering gaze`
- 中文对照：马力克风格：一只约克夏犬坐在地铁座位上，魔幻时刻的光穿透车窗，耳语画外音沉思世界，插入天空与树叶的空镜，狗在宏大的沉思目光中显得渺小。
- Negative: `No fast cutting, no explanatory dialogue, no studio light`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
