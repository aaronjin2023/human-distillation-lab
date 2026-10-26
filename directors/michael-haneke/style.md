# Michael Haneke — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michael Haneke: cold long takes, violence off-screen, the bourgeois interior as a trap, the audience forced to watch without relief`
- ZH: 哈内克风格：冷峻的长镜头，画外暴力，中产内景即陷阱，观众被迫注视而无处可逃。

## (2) 镜头语言

- 景别：固定机位长镜头为主：中景与全景写中产内景，特写克制；暴力常在画外，只留声音。`verbatim`
- 机位与运动：几乎不动：固定机位是本体，摄影机拒绝运动与安慰，时间在静止中压迫。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 中产内景调度：客厅、钢琴房、走廊——人物在体面空间中冷漠对峙，调度以静默与等待驱动。`impression`

## (4) 剪辑节奏

- 极少剪辑：长镜头内完成段落，剪辑点即时间的断裂；节奏由静默驱动，越静越紧张。`impression`

## (5) 色彩与光影

- 色彩：低饱和的冷灰与米白主导：中产内景的冷白、灰蓝、暗褐；色彩克制，光影写体面的寒冷。`impression`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：冷峻寓言结构：开头以日常切入，中间以暴力或偏离推进，结尾以静默或灾难收束，不给解释与安慰。`impression`
- 该拍什么：
- 固定机位下的中产内景长镜头
- 画外暴力的声音设计
- 静默对峙中的冷峻凝视
- 低饱和冷灰的体面空间
- 不该拍什么：
- 快速剪辑
- 煽情音乐
- 解释性对白
- 温情圆满的收束

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 固定机位下的中产内景长镜头；- 画外暴力的声音设计；- 静默对峙中的冷峻凝视；- 低饱和冷灰的体面空间
- 不该拍：- 快速剪辑；- 煽情音乐；- 解释性对白；- 温情圆满的收束
- Negative prompt: `No fast cutting, no sentimental music, no explanatory dialogue, no warm happy ending, no comforting camera movement`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Michael Haneke, a small Yorkshire terrier sitting on a subway seat, one cold static long take, the violence happening off-screen, only sound remaining, bourgeois passengers watching without relief, no comfort`
- 中文对照：哈内克风格：一只约克夏犬坐在地铁座位上，一个冷峻的固定长镜头，暴力发生在画外，只剩声音，中产乘客注视而无处可逃，不给安慰。
- Negative: `No fast cutting, no sentimental music, no explanatory dialogue`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
