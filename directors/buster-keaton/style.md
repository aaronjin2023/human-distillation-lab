# Buster Keaton — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Buster Keaton: deadpan stone face, spectacular practical stunts, wide shots that prove the gag is real, trains and collapsing houses, engineering comedy, no smile`
- ZH: 基顿风格：扑克脸，实拍特技大场面，证明笑料真实的远景，火车与倒塌的房屋，工程式喜剧，绝不微笑。

## (2) 镜头语言

- 远景与全景为主：特技必须在全景里一次看清，证明没有替身与剪辑作弊；机位固定，极少特写；火车追逐用多机位远景交代空间。`verbatim`

## (3) 场面调度

- 工程式调度：火车、房屋、瀑布都是真实机关，基顿在机关中央完成动作；倒塌的房屋正好留出窗洞，火车头正好接住人，调度即工程计算。`verbatim`

## (4) 剪辑节奏

- 按特技段落剪辑：一个特技一个镜头，节奏由真实物理决定；追逐段落靠平行剪辑加速，但特技本身不切；《福尔摩斯二世》用剪辑玩梦境与银幕穿越。`verbatim`

## (5) 色彩与光影

- 黑白为主，火车黑铁、房屋白墙、基顿黑礼帽构成硬对比；外景自然光，室内戏用均匀布光，不作情绪性明暗。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 火车追逐与铁轨上的特技
- 倒塌房屋的窗洞奇迹
- 扑克脸面对灾难
- 银幕穿越与梦境剪辑
- 真实机关与全景证明
- 不该拍：
- no close-up reaction shots, no smiling at the gag
- no cutting inside a stunt, no cheating with editing
- no dialogue jokes, no verbal comedy
- no handheld camera, no shaky realism
- no sentimental music, no emotional close-ups
- Negative prompt: `No close-up reaction shots, no smiling at the gag, cutting inside a stunt, no cheating with editing, dialogue jokes, no verbal comedy, handheld camera, no shaky realism, sentimental music, no emotional close-ups`

## (7) 叙事结构

- 小人物对抗大机器与大自然：追火车救爱人、误入电影银幕、在豪华游轮上求生；故事是连串特技，结尾常以一个更大特技收束，面无表情。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Buster Keaton, a small Yorkshire terrier with a deadpan face sits on a subway seat as the carriage lurches, the dog stays perfectly still while passengers tumble around it, wide shot proving it is real, no smile, engineering comedy`
- 中文对照：基顿风格：扑克脸，实拍特技大场面，证明笑料真实的远景，火车与倒塌的房屋，工程式喜剧，绝不微笑。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No close-up reaction shots, no cutting inside a stunt, no dialogue jokes, no handheld camera, no sentimental music`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
