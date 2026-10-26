# Bong Joon-ho — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bong Joon-ho: genre bent until it breaks, upstairs and downstairs, the joke that turns into horror, meticulous design hiding class rage`
- ZH: 奉俊昊风格：类型被掰弯直到断裂，楼上与楼下，笑话翻成恐怖，精密的设计藏着阶级愤怒。

## (2) 镜头语言

- 景别：中景与全景并用，空间（楼梯、半地下室）的纵深感是标志。`verbatim`
- 机位：固定机位与缓慢横移，摄影机讲究空间的精确调度。`impression`
- 镜头：标准焦段，深焦保留楼上楼下的两个世界。`impression`
- 运镜禁忌：几乎不用手持晃动，运镜服务于设计的精确。`impression`

## (3) 场面调度

- 人物走位：人物在楼梯上下穿行，走位即阶级。`verbatim`
- 景深与层次：前景楼梯、中景人物、背景窗外雨的三层结构是标志。`verbatim`
- 空间：半地下室、豪宅、雨夜街道，空间即阶级。`impression`
- 演员表演风格：职业演员，表演在喜剧与悲剧之间快速切换。`impression`

## (4) 剪辑节奏

- 剪辑速度：中速，类型转折处用硬切制造断裂感。`impression`
- 转场：硬切为主，喜剧与恐怖在硬切处翻转。`impression`
- 段落结构：以类型段落并置推进，笑话段落后接恐怖段落。`impression`
- 声音剪辑：雨声、楼梯声与音乐构成声景，声音即阶级。`verbatim`

## (5) 色彩与光影

- 色彩：冷调与暖调并置，半地下室的绿灰与豪宅的暖黄对撞。`verbatim`
- 光影：自然光与室内 practical 光，阴影是楼梯的形状。`impression`
- 胶片 / 画幅：彩色，画幅讲究空间的纵深与对称。`impression`

## (6) 叙事结构

- 结构：类型混合：喜剧—悬疑—恐怖—悲剧，四段式翻转。`impression`
- 视点：全知而冷峻，镜头站在穷人一边而不煽情。`impression`
- 时间：顺时，时间在雨季与季节里流逝。`impression`
- 类型处理：遵守类型成规再掰弯它，类型翻转即主题。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：楼梯与半地下室、类型翻转、雨夜、阶级空间、笑话变恐怖、精密的设计
- 不该拍：单一类型、快速剪辑、煽情音乐、解释性对白、圆满收束
- Negative prompt: `No single-genre comfort, no fast cutting, no sentimental music, no explanatory dialogue, no neat resolution, no handheld shaky cam`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Bong Joon-ho, a small Yorkshire terrier sitting on a subway seat, upstairs and downstairs in one carriage, a joke that turns into dread, rain on the window, meticulous design, class in the seating`
- 中文对照：奉俊昊风格：一只约克夏犬坐在地铁座位上，同一节车厢里的楼上与楼下，笑话翻成恐惧，车窗上有雨，精密的设计，座位即阶级。
- Negative: `No single-genre comfort, no fast cutting, no sentimental music, no explanatory voiceover, no neat ending`
- 检验点：类型翻转是否成立；空间即阶级是否在；笑话变恐怖的断裂感是否在。
