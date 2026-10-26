# Quentin Tarantino — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Quentin Tarantino: chapters and trunk shots, needle-drop pop music, long talky scenes exploding into stylized violence, genre pastiche with footnotes`
- ZH: 塔伦蒂诺风格：章节与后备箱镜头，流行金曲针落，长篇对话突然爆出风格化暴力，类型拼贴加脚注。

## (2) 镜头语言

- 景别：后备箱仰拍、特写与中景并重；对话场面以正反打长镜头拍到底，暴力场面以特写放大。`verbatim`
- 机位与运动：缓慢推近与环绕为主，对话时摄影机几乎不动，暴力时突然加速；运镜服务于对话的张力。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 餐厅、酒吧、后备箱等封闭空间的长对话：人物围坐、走位极少，调度以语言与眼神驱动。`impression`

## (4) 剪辑节奏

- 章节式非线性剪辑：时间打乱、标题卡分隔，段落以音乐针落收束；暴力场面剪辑突然加速。`impression`

## (5) 色彩与光影

- 色彩：高饱和流行色：红、黄、黑的漫画式对撞；《杀死比尔》以黄黑与血红为主，复古胶片颗粒感。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：章节体 + 非线性：开头常以长对话起笔，中间以标题卡分章，结尾以暴力或复仇收束，时间可倒可跳。`impression`
- 该拍什么：
- 封闭空间中的长篇对话
- 后备箱仰拍与章节标题卡
- 流行金曲针落的暴力场面
- 高饱和红黄黑的类型拼贴
- 不该拍什么：
- 简短功能性对白
- 平稳线性的时间
- 克制的写实暴力
- 冷调低饱和的画面

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 封闭空间中的长篇对话；- 后备箱仰拍与章节标题卡；- 流行金曲针落的暴力场面；- 高饱和红黄黑的类型拼贴
- 不该拍：- 简短功能性对白；- 平稳线性的时间；- 克制的写实暴力；- 冷调低饱和的画面
- Negative prompt: `No short functional dialogue, no flat linear time, no restrained realist violence, no cold desaturated image, no invisible genre`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Quentin Tarantino, a small Yorkshire terrier sitting on a subway seat, trunk-shot low angle up at the passengers, a long talky scene about the dog, needle-drop pop song, chapter title card, stylized violence of looks, saturated red and yellow`
- 中文对照：塔伦蒂诺风格：一只约克夏犬坐在地铁座位上，后备箱式低角度仰拍乘客，关于狗的长篇对话，流行金曲针落，章节标题卡，眼神的风格化暴力，饱和的红与黄。
- Negative: `No short dialogue, no linear time, no restrained violence`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
