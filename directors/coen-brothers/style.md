# Coen brothers — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of the Coen brothers: deadpan wide shots, snow and blood, ordinary fools undone by one bad decision, fate as a laconic killer`
- ZH: 科恩兄弟风格：冷面全景，雪与血，普通人因一个坏决定而毁灭，命运是个寡言的杀手。

## (2) 镜头语言

- 景别：宽全景与中景为主，特写克制；人物在辽阔雪原或荒漠中显得渺小。`verbatim`
- 机位与运动：平稳推近与横移，少用手持；摄影机冷静旁观，拒绝煽情的运动。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 空旷空间中的小人物：雪原、荒漠、小镇街道——调度以行走与等待驱动，暴力突然降临。`impression`

## (4) 剪辑节奏

- 冷静的硬切与长镜头并存；节奏由对话的停顿驱动，暴力场面剪辑突然加速又迅速收住。`impression`

## (5) 色彩与光影

- 色彩：雪白与血红、荒漠土黄与深黑对照；色彩低饱和，唯独血与雪的反差强烈。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：犯罪寓言结构：开头一个坏决定，中间连锁反应，结尾命运收束、主角不解其意；视点冷静旁观，不给道德评判。`impression`
- 该拍什么：
- 雪原与荒漠中的宽全景小人物
- 冷面长对话中的停顿
- 一个坏决定引发的连锁反应
- 雪白与血红的强烈反差
- 不该拍什么：
- 煽情的特写
- 快速跳切
- 温情圆满的收束
- 解释性对白

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 雪原与荒漠中的宽全景小人物；- 冷面长对话中的停顿；- 一个坏决定引发的连锁反应；- 雪白与血红的强烈反差
- 不该拍：- 煽情的特写；- 快速跳切；- 温情圆满的收束；- 解释性对白
- Negative prompt: `No sentimental close-ups, no fast cutting, no warm happy ending, no explanatory dialogue, no moralizing voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of the Coen brothers, a small Yorkshire terrier sitting on a subway seat, deadpan wide shot down the snowy-white carriage, one bad decision by a passenger, laconic dialogue with long pauses, fate waiting at the next stop`
- 中文对照：科恩兄弟风格：一只约克夏犬坐在地铁座位上，冷面宽全景望向雪白的车厢，一位乘客的一个坏决定，寡言对话中的长停顿，命运在下一站等着。
- Negative: `No sentimental close-ups, no fast cutting, no warm ending`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
