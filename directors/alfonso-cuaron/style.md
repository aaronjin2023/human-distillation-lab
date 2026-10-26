# Alfonso Cuarón — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfonso Cuarón: long fluid takes, natural light, lived-in Mexico City and space, the camera as a witness that never looks away`
- ZH: 卡隆风格：绵长流畅的长镜头，自然光，充满生活气息的墨西哥城与太空，镜头是永不移开视线的见证者。

## (2) 镜头语言

- 景别：长镜头与中景为主，远景交代环境，特写克制、只在情绪顶点出现。`verbatim`
- 机位与运动：摄影机持续流动：缓慢横移、跟拍、升降，少用跳切；《地心引力》以长镜头模拟失重漂浮，《罗马》以横移展开街区生活。`verbatim`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 深焦与多层调度：前景有人物劳作、中景有对话、背景有街景同时发生；人物常在画框边缘出入，空间先于人物。`impression`

## (4) 剪辑节奏

- 长镜头内完成段落，剪辑点藏在运动与遮挡之后；节奏由镜头运动而非剪切驱动，段落之间以黑场或日常声过渡。`impression`

## (5) 色彩与光影

- 色彩：自然光主导：墨西哥城的暖灰、土黄与褪色白；《罗马》黑白摄影以灰阶层次代替色彩；太空段落为深黑与冷白的高反差。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：线性中嵌套记忆与闪回；开头常以日常场景切入，结尾收束于一个凝视或离别，不解释人物命运。`impression`
- 该拍什么：
- 绵长长镜头中的日常劳作与行走
- 自然光下的墨西哥街景与家庭内景
- 摄影机横移中多层同时发生的动作
- 失重或漂浮中的缓慢旋转
- 不该拍什么：
- 快速跳切
- 手持晃动
- 戏剧化特写堆砌
- 饱和的商业大片色彩

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 绵长长镜头中的日常劳作与行走；- 自然光下的墨西哥街景与家庭内景；- 摄影机横移中多层同时发生的动作；- 失重或漂浮中的缓慢旋转
- 不该拍：- 快速跳切；- 手持晃动；- 戏剧化特写堆砌；- 饱和的商业大片色彩
- Negative prompt: `No fast cutting, no handheld shaky cam, no pile-up of dramatic close-ups, no saturated blockbuster colour, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Alfonso Cuarón, a small Yorkshire terrier sitting on a subway seat in a modern city, one long fluid take, camera slowly tracking past fellow passengers, natural fluorescent light, everyday life unfolding in layers around the dog, no cutting away`
- 中文对照：卡隆风格：一只约克夏犬坐在现代城市的地铁座位上，一个绵长流畅的长镜头，摄影机缓缓横移掠过身旁乘客，自然荧光灯，日常生活在狗的周围分层展开，不切走。
- Negative: `No fast cutting, no handheld camera, no dramatic close-ups, no saturated colour`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
