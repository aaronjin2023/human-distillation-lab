# Christopher Nolan — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Christopher Nolan: nested time, practical spectacle on IMAX, a ticking clock, the puzzle that is also an emotion`
- ZH: 诺兰风格：嵌套的时间，IMAX 实拍奇观，滴答作响的时钟，谜题本身即情感。

## (2) 镜头语言

- 景别：IMAX 大全景与特写交替：大全景写奇观，特写写时间的焦虑；交叉剪辑在不同时间线间跳跃。`verbatim`
- 机位与运动：平稳推近与航拍：摄影机庄重而精确，实拍奇观用缓慢揭示而非快速剪辑。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 多时间线调度：梦境层层嵌套、城市折叠，人物在不同时间层中同时行动；调度以时间结构驱动。`impression`

## (4) 剪辑节奏

- 交叉剪辑与时间嵌套：多条时间线并行加速，剪辑点即时间的切换；节奏由时钟驱动，越近高潮越快。`impression`

## (5) 色彩与光影

- 色彩：冷蓝与暖金对照：梦境冷蓝、现实暖金；《星际穿越》以尘土黄与太空黑为主。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：嵌套与倒叙结构：开头抛出谜面（失忆、梦、时间），中间以时间线交织推进，结尾以情感收束谜面。`impression`
- 该拍什么：
- 多时间线交叉剪辑的嵌套结构
- IMAX 实拍的奇观大全景
- 滴答时钟驱动的加速节奏
- 冷蓝与暖金的时间对照
- 不该拍什么：
- 线性平铺
- 数字特效堆砌的奇观
- 无情感的谜题
- 手持晃动

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 多时间线交叉剪辑的嵌套结构；- IMAX 实拍的奇观大全景；- 滴答时钟驱动的加速节奏；- 冷蓝与暖金的时间对照
- 不该拍：- 线性平铺；- 数字特效堆砌的奇观；- 无情感的谜题；- 手持晃动
- Negative prompt: `No flat linear plotting, no CGI-only spectacle, no emotionless puzzle, no handheld shaky cam, no sentimental shortcut`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Christopher Nolan, a small Yorkshire terrier sitting on a subway seat, nested time lines crossing in the carriage, IMAX wide shot of the folding city, a ticking clock, the dog at the centre of the puzzle, cold blue against warm gold`
- 中文对照：诺兰风格：一只约克夏犬坐在地铁座位上，多条时间线在车厢中交错，IMAX大全景中的折叠城市，滴答的时钟，狗在谜题中心，冷蓝对暖金。
- Negative: `No linear plotting, no CGI-only spectacle, no handheld camera`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
