# Alejandro G. Iñárritu — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alejandro G. Iñárritu: interwoven fates, restless handheld camera, raw emotion, one apparent continuous take, life colliding across a city`
- ZH: 伊纳里图风格：多线交织的命运，不安的手持摄影， raw 的情绪，貌似一镜到底，生命在城市中相撞。

## (2) 镜头语言

- 景别：中近景与特写交替，手持贴近人物面部；《鸟人》以貌似一镜到底的运动串联全片。`verbatim`
- 机位与运动：手持跟拍与急促推近为主，摄影机像喘息一样贴近人物；长镜头用于制造无法逃脱的连续感。`verbatim`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 人物在狭窄空间中冲撞：车祸现场、后台走廊、荒野；调度以身体冲突与追逐驱动，空间越收越紧。`impression`

## (4) 剪辑节奏

- 多线交叉剪辑：时间打乱、因果后置，几条线索在一次事故或一次相遇处交汇；《21克》以碎片重组时间。`impression`

## (5) 色彩与光影

- 色彩：冷峻的城市灰蓝与血色暖调对撞；《荒野猎人》以自然光下的雪原灰白与血红为主；肤色偏冷、阴影偏重。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：多线交织 + 非线性：开头常抛出一场事故或死亡，结尾多条线索收束于同一时刻，留下一个未解的道德问题。`impression`
- 该拍什么：
- 多条命运线在一次事故处交汇
- 手持贴近面部的情绪特写
- 貌似一镜到底的走廊与街道跟拍
- 荒野或城市边缘的求生行走
- 不该拍什么：
- 平稳的三脚架全景
- 线性平铺直叙
- 温情圆满的收束
- 干净的棚拍光

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 多条命运线在一次事故处交汇；- 手持贴近面部的情绪特写；- 貌似一镜到底的走廊与街道跟拍；- 荒野或城市边缘的求生行走
- 不该拍：- 平稳的三脚架全景；- 线性平铺直叙；- 温情圆满的收束；- 干净的棚拍光
- Negative prompt: `No static tripod wide shots, no linear flat storytelling, no sentimental happy ending, no clean studio lighting, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Alejandro G. Iñárritu, a small Yorkshire terrier sitting on a subway seat, handheld camera close on its face, three passengers' separate stories colliding around it, apparent single continuous take, raw city light, no escape from the carriage`
- 中文对照：伊纳里图风格：一只约克夏犬坐在地铁座位上，手持摄影机贴近它的脸，三位乘客各自的故事在它周围相撞，貌似一镜到底，粗粝的城市光，逃不出这节车厢。
- Negative: `No static wide shots, no linear storytelling, no sentimental ending`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
