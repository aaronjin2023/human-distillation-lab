# Mikio Naruse — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mikio Naruse: women's quiet endurance, small rooms and staircases, rain and bars, no escape and no complaint, the camera that stays`
- ZH: 成濑风格：女性安静的忍耐，小房间与楼梯，雨与酒吧，无处可逃亦无抱怨，停留的镜头。

## (2) 镜头语言

- 景别：中景与全景为主，室内中景；特写罕见。`verbatim`
- 机位：固定机位，平视，机位停留；少用运动。`impression`
- 镜头：标准焦距，深焦，画面如室内静物。`impression`

## (3) 场面调度

- 场面调度：女性在小房间与楼梯间移动，走位即忍耐。`verbatim`
- 演员：职业演员（高峰秀子、原节子），表演克制。`artifact`
- 空间：小酒吧、公寓、楼梯，空间越收越紧。`impression`

## (4) 剪辑节奏

- 剪辑：节奏舒缓，段落式；剪切点藏在日常中。`verbatim`
- 转场：硬切与叠化，时间跳跃温柔。`impression`
- 声音：环境音（雨、街声）为主，音乐克制；对白平淡。`impression`

## (5) 色彩与光影

- 色彩：黑白为主，灰调温润；雨夜的灰与灯光的暖。`impression`
- 光影：室内柔光，均匀明亮；少强烈明暗。`impression`
- 画幅：1.37:1 与宽银幕并用，中景构图。`impression`

## (6) 叙事结构

- 结构：女性一生的编年，线性而苦涩；结尾开放而无奈。`verbatim`
- 视点：限知视角，观众与女性同样无处可逃。`impression`
- 时间：日常时间，雨季标记忍耐。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：女性忍耐、小房间、楼梯、雨、酒吧、日常、无处可逃。
- 该拍：银座、公寓、火车、茶杯、雨伞。
- 不该拍：不拍戏剧化高潮、不拍煽情音乐、不拍明确答案、不拍男性拯救。
- Negative prompt: `No melodramatic climax, no sentimental score, no clear answers, no male rescue, no fast cutting, no camera movement`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Mikio Naruse, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, a tired woman beside it, rain on the window, small room and staircase, no escape and no complaint, the camera that stays`
- 中文对照：成濑风格：一只约克夏犬坐在地铁座位上，旁边是一位疲惫的女性，窗上的雨，小房间与楼梯，无处可逃亦无抱怨，停留的镜头。
- Negative: `No melodramatic climax, no sentimental score, no clear answers, no male rescue`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
