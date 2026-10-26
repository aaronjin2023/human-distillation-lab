# Robert Bresson — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Bresson: radical minimalism, hands and feet instead of faces, models not actors, ellipsis as structure, grace in the smallest gesture`
- ZH: 布列松风格：极致极简主义，以手与脚代替面孔，用模特而非演员，省略即结构，最小动作中的恩典。

## (2) 镜头语言

- 景别：手、脚、物件的特写为主，面孔特写罕见。`verbatim`
- 机位：固定机位，平视，拒绝运镜；机位如旁观者。`impression`
- 镜头：标准焦距，景深浅，画面极简。`impression`

## (3) 场面调度

- 场面调度：人物走位精确如仪式，手与脚的动作即戏剧。`verbatim`
- 演员：非职业“模特”，表演去戏剧化，声音平板。`artifact`
- 空间：监狱、乡村、街道，空间极简，物件即意义。`impression`

## (4) 剪辑节奏

- 剪辑：省略式剪辑，删去过渡与高潮，只留动作的碎片。`verbatim`
- 转场：硬切，时间跳跃不作交代。`impression`
- 声音：环境音（脚步、门、纸）为主，音乐极少；画外音日记体。`artifact`

## (5) 色彩与光影

- 色彩：黑白为主，灰调极简；彩色时期仍克制，低饱和。`impression`
- 光影：均匀自然光，无戏剧性明暗；光即恩典。`impression`
- 画幅：1.37:1，极简构图。`impression`

## (6) 叙事结构

- 结构：线性而省略，事件只留碎片；结尾常为一句画外音或一个动作。`verbatim`
- 视点：限知视角，观众只看到手与脚，不知道内心。`impression`
- 时间：省略的时间，动作之间留白。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：手与脚的特写、监狱与乡村、省略、画外音日记、最小动作、恩典。
- 该拍：门、楼梯、纸、钱、驴（《驴子巴特萨》）。
- 不该拍：不拍面孔特写、不拍心理独白、不拍煽情音乐、不拍戏剧化高潮。
- Negative prompt: `No face close-ups, no psychological monologue, no sentimental score, no melodramatic climax, no camera movement, no explanatory dialogue`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Robert Bresson, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, only its paws and the commuter's hands in close-up, ellipsis, silence, grace in the smallest gesture, no face, no psychology`
- 中文对照：布列松风格：一只约克夏犬坐在地铁座位上，只有它的爪子和乘客的手的特写，省略，沉默，最小动作中的恩典，没有面孔，没有心理。
- Negative: `No face close-ups, no psychological monologue, no sentimental score, no melodramatic climax`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
