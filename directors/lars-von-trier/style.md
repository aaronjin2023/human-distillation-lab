# Lars von Trier — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lars von Trier: handheld Dogme rawness, a suffering heroine, provocation as method, the camera shaking with the character's faith`
- ZH: 冯·提尔风格：手持道格玛的粗粝，受难的女主角，挑衅即方法，摄影机随人物的信念而颤抖。

## (2) 镜头语言

- 景别：手持中景与特写并重：特写给受难的面孔；《破浪》以手持写信仰的颤抖。`verbatim`
- 机位与运动：手持晃动是本体：摄影机如呼吸般颤抖，运动即人物的内心失序。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 封闭空间调度：小岛、工厂、庄园——女主角在封闭空间中受难，调度以身体与信仰驱动。`impression`

## (4) 剪辑节奏

- 跳切与手持剪辑：段落以音乐章节分隔，《黑暗中的舞者》以歌舞对照现实；节奏由受难驱动，越痛越快。`impression`

## (5) 色彩与光影

- 色彩：低饱和的冷灰与暗褐主导：北欧的冷光、工厂的灰绿；歌舞段落以饱和色彩对照现实的灰暗。`impression`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：受难结构：开头以善良的女主角切入，中间以牺牲与误解推进，结尾以死亡或毁灭收束，不给救赎。`impression`
- 该拍什么：
- 手持晃动中的受难面孔特写
- 封闭空间中的信仰与牺牲
- 歌舞段落对照现实的灰暗
- 章节标题分隔的挑衅结构
- 不该拍什么：
- 平稳的三脚架
- 温情圆满的收束
- 解释性对白
- 冷峻的旁观

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 手持晃动中的受难面孔特写；- 封闭空间中的信仰与牺牲；- 歌舞段落对照现实的灰暗；- 章节标题分隔的挑衅结构
- 不该拍：- 平稳的三脚架；- 温情圆满的收束；- 解释性对白；- 冷峻的旁观
- Negative prompt: `No smooth tripod shots, no sentimental happy ending, no explanatory dialogue, no cold detached observation, no comforting resolution`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Lars von Trier, a small Yorkshire terrier sitting on a subway seat, handheld camera shaking with the dog's faith, a suffering passenger's close-up, chapters dividing the ride, a musical number against grey reality, no comfort`
- 中文对照：冯·提尔风格：一只约克夏犬坐在地铁座位上，手持摄影机随狗的信念颤抖，受难乘客的特写，章节分隔这趟车，歌舞段落对照灰暗现实，不给安慰。
- Negative: `No smooth tripod shots, no sentimental ending, no explanatory dialogue`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
