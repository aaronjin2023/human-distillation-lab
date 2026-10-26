# Yasujirō Ozu — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yasujiro Ozu: low tatami-level camera, static shots, 50mm lens, everyday family interiors, quiet ellipses, no camera movement, muted colours, contemplative pacing`
- ZH: 小津风格：榻榻米高度的低机位，固定镜头，50mm 镜头，日常家庭室内，安静的省略，无运镜，低饱和色彩，沉思的节奏。

## (2) 镜头语言

- 景别：中景与全景为主，人物并坐；特写罕见。`verbatim`
- 机位：榻榻米高度的固定机位，平视，机位从不动。`verbatim`
- 镜头：50mm 标准镜头，深焦，画面如室内静物。`artifact`

## (3) 场面调度

- 场面调度：人物在室内并坐或对坐，走位极简；出画入画即转场。`verbatim`
- 演员：固定班底（笠智众、原节子），表演克制。`artifact`
- 空间：家庭室内、走廊、庭院，空间即日常。`impression`

## (4) 剪辑节奏

- 剪辑：省略式剪辑，删去过渡；枕头镜头（空镜头）连接场景。`verbatim`
- 转场：枕头镜头（风景、器物空镜）+ 硬切。`verbatim`
- 声音：环境音（火车、风）为主，音乐极少；对白平淡。`impression`

## (5) 色彩与光影

- 色彩：黑白时期灰调温润；彩色时期低饱和，米、棕、灰蓝。`verbatim`
- 光影：室内柔光，均匀明亮；少强烈明暗。`impression`
- 画幅：1.37:1，方形构图。`impression`

## (6) 叙事结构

- 结构：线性而松散，家庭日常的编年；结尾戛然而止。`verbatim`
- 视点：全知而克制，观众与人物同样安静。`impression`
- 时间：季节时间，省略的时间。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：家庭室内、榻榻米机位、枕头镜头、省略、季节、父女、出嫁。
- 该拍：走廊、庭院、火车、茶杯、烟囱。
- 不该拍：不拍大幅度运镜、不拍戏剧化高潮、不拍快速剪辑、不拍煽情音乐。
- Negative prompt: `No camera movement, no melodramatic climax, no fast cutting, no sentimental score, no close-ups, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Yasujiro Ozu, a small Yorkshire terrier sitting on a subway seat in a modern city, low static camera at seat height, 50mm lens, quiet everyday moment, muted colours, no camera movement, long take, contemplative, family-like warmth without sentimentality`
- 中文对照：小津风格：一只约克夏犬坐在地铁座位上，座位高度的低固定镜头，50mm 镜头，安静的日常瞬间，低饱和色彩，无运镜，长镜头，沉思，家庭般的温暖而不煽情。
- Negative: `No camera movement, no melodramatic climax, no fast cutting, no sentimental score`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
