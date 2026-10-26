# Vittorio De Sica — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vittorio De Sica: neorealist compassion, a child's gaze, ordinary people in real Rome, long takes that wait, quiet dignity without sentimentality`
- ZH: 德·西卡风格：新现实主义的悲悯，儿童视角，真实罗马中的普通人，等待的长镜头，不煽情的尊严。

## (2) 镜头语言

- 景别：中景与全景为主，跟随人物行走；特写只在情感顶点短暂出现。`verbatim`
- 机位：平视，机位高度与儿童视线齐平；少用仰拍与俯拍。`impression`
- 镜头：标准焦距，深焦呈现罗马街景层次。`impression`

## (3) 场面调度

- 场面调度：实景街道，父子并排行走，人物在人群中穿行；群众场面自然。`verbatim`
- 演员：非职业演员（《偷自行车的人》父子均为素人），表演克制。`artifact`
- 空间：罗马街头、市场、教堂，空间即生活本身。`impression`

## (4) 剪辑节奏

- 剪辑：节奏舒缓，长镜头等待人物走完一段路；省略少，时间近乎实时。`verbatim`
- 转场：硬切与淡入淡出并用，段落衔接平缓。`impression`
- 声音：现场音，少配乐；音乐只在片头片尾出现。`impression`

## (5) 色彩与光影

- 色彩：黑白为主，灰调温润；阳光下的罗马街道明亮而不刺眼。`impression`
- 光影：自然光，柔和明暗，阴影不压迫人物。`impression`
- 画幅：1.37:1，纪录片式画幅。`impression`

## (6) 叙事结构

- 结构：单线跟随（父子找车的一天），线性时间，结尾开放而苦涩。`verbatim`
- 视点：儿童视角与父亲视角交替，观众与人物同行而非俯视。`impression`
- 时间：一天之内的时间压缩，近乎实时。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：父子同行、儿童视角、罗马街头日常、寻找与失落、普通人的尊严。
- 该拍：市场、教堂、雨中的街道、等待的长镜头。
- 不该拍：不拍明星特写、不拍煽情配乐、不拍戏剧化高潮、不拍道德说教。
- Negative prompt: `No star close-ups, no sentimental score, no melodramatic climax, no moral preaching, no studio sets, no fast cutting`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Vittorio De Sica, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat beside a tired father and his son, real commuters, child's eye-level camera, long waiting takes, quiet dignity, Rome street immediacy`
- 中文对照：德·西卡风格：一只约克夏犬坐在地铁座位上，旁边是一位疲惫的父亲和他的儿子，真实乘客，儿童视线高度的镜头，等待的长镜头，安静的尊严。
- Negative: `No star close-ups, no sentimental music, no melodramatic climax, no moral preaching`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
