# Fritz Lang — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fritz Lang: monumental architecture, geometric compositions, the hunted outsider, fate as a machine, chiaroscuro, precise editing, paranoia in the modern city`
- ZH: 朗风格：纪念碑式建筑，几何构图，被追捕的局外人，命运如机器，明暗对比，精确剪辑，现代都市中的偏执。

## (2) 镜头语言

- 几何构图机位：对称的建筑线条、楼梯与走廊的纵深，人物在巨大空间中渺小；《M就是凶手》用俯拍追踪凶手，用阴影标示其存在；机位精确如建筑图纸。`verbatim`

## (3) 场面调度

- 建筑式调度：大都会的摩天楼与地下工人城上下对照，人物在楼梯与走廊间被追捕；群众如零件般排列，个人在机器中挣扎。`verbatim`

## (4) 剪辑节奏

- 精确剪辑：平行线索冷静交替，节奏均匀而不煽情；《M就是凶手》靠声音（口哨）而非画面追踪凶手，声画剪辑先于画面；高潮段落剪辑加速但不失控。`verbatim`

## (5) 色彩与光影

- 黑白表现主义：硬光深影，摩天楼的冷光与地下城的暗调对照；《大都会》用金属光泽与阴影区隔阶层；色彩缺席时靠明暗与几何制造压迫。`verbatim`

## (6) 该拍什么 / 不该拍什么

- 该拍：
- 摩天楼与地下城的上下对照
- 几何楼梯与走廊的追捕
- 口哨声追踪凶手
- 群众如零件的排列
- 法庭与群众审判的收束
- 不该拍：
- no loose improvisation, no warm sentimentality
- no handheld camera, no shaky realism
- no fast MTV cutting, no chaotic montage
- no bright cheerful lighting, no soft focus
- no happy resolution without a trial
- Negative prompt: `No loose improvisation, no warm sentimentality, handheld camera, no shaky realism, fast MTV cutting, no chaotic montage, bright cheerful lighting, no soft focus, happy resolution without a trial`

## (7) 叙事结构

- 被追捕者与机器命运：凶手、间谍、复仇者皆为现代都市的局外人；故事是追捕与审判，结尾常以法庭或群众审判收束，命运如机器般不可逃。`verbatim`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Fritz Lang, a small Yorkshire terrier sits on a subway seat while a whistled tune follows it down a geometric corridor, monumental station architecture, chiaroscuro, precise cutting, paranoia in the modern city, fate as a machine`
- 中文对照：朗风格：纪念碑式建筑，几何构图，被追捕的局外人，命运如机器，明暗对比，精确剪辑，现代都市中的偏执。一只约克夏犬坐在地铁座位上，按本导演的镜头、调度与剪辑拍成现代短片。
- Negative: `No loose improvisation, no handheld camera, no fast MTV cutting, no bright cheerful lighting, no happy resolution without a trial`
- 检验点：镜头语言是否成立；场面调度是否可辨；剪辑节奏是否符合本导演；Negative 清单是否被遵守。
