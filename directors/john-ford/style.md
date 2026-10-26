# John Ford — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Ford: the American West, Monument Valley, doorframe compositions, community rituals, the lone rider on the horizon, elegiac landscapes, classical restraint`
- ZH: 福特风格：美国西部，纪念碑谷，门框式构图，社群仪式，地平线上的独行骑手，挽歌式风景，古典克制。

## (2) 镜头语言

- 门框式机位：《搜索者》开场与结尾的门框构图，人物在门框内望向荒野；远景拍纪念碑谷，中景拍社群仪式，特写只留给约翰·韦恩的眼神。`verbatim`

## (3) 场面调度

- 社群调度：驿站马车内各色人物分层，教堂、婚礼、葬礼的仪式调度；个人在社群中，社群在风景中，风景在门框中。`verbatim`

## (4) 剪辑节奏

- 古典剪辑：节奏平稳，场景间淡入淡出；追逐段落剪辑加速但不失控；《关山飞渡》马车追逐靠平行剪辑制造紧张，剪辑服务于故事而非炫技。`verbatim`

## (5) 色彩与光影

- 黑白西部片的硬光与深影，纪念碑谷的红岩在黑白中靠明暗呈现；彩色期《搜索者》用 Technicolor 的红岩与蓝天，色彩作美国神话的标示。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 纪念碑谷的远景与门框构图
- 马车追逐与社群仪式
- 地平线上的独行骑手
- 教堂、婚礼、葬礼的仪式调度
- 门框合上的挽歌结尾
- 不该拍：
- no handheld camera, no shaky realism
- no fast MTV cutting, no jump cuts
- no psychological exposition, no inner monologue
- no ironic revisionism, no cynical twist
- no muted desaturated palette, no grey realism
- Negative prompt: `No handheld camera, no shaky realism, fast MTV cutting, no jump cuts, psychological exposition, no inner monologue, ironic revisionism, no cynical twist, muted desaturated palette, no grey realism`

## (7) 叙事结构

- 西部史诗与社群挽歌：马车穿越荒野、独行骑手寻找家人、矿工社群的兴衰；故事是社群的仪式，结尾常以骑手独自离去收束，门框合上。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of John Ford, a small Yorkshire terrier sits on a subway seat framed by the carriage doorway like a Monument Valley doorframe, the community of commuters around it, elegiac landscape beyond the window, classical restraint, the lone rider's farewell`
- 中文对照：福特风格：美国西部，纪念碑谷，门框式构图，社群仪式，地平线上的独行骑手，挽歌式风景，古典克制。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No handheld camera, no fast MTV cutting, no psychological exposition, no ironic revisionism, no muted desaturated palette`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
