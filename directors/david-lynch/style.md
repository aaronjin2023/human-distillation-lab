# David Lynch — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Lynch: small-town America with rot underneath, red curtains, industrial hum, dream logic, the familiar turning strange`
- ZH: 林奇风格：表面安宁、底下腐烂的小镇美国，红幕布，工业低鸣，梦的逻辑，熟悉之物变得陌生。

## (2) 镜头语言

- 景别：特写与中景并重：特写给耳朵、嘴唇、火焰等物的质感；红幕布与走廊的对称构图反复出现。`verbatim`
- 机位与运动：缓慢推近与凝视式固定机位；摄影机如梦游般滑入黑暗，少用快速运动。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 小镇日常空间：客厅、卧室、街道——熟悉空间中突然出现异物；人物在明亮日常与黑暗房间之间穿梭。`impression`

## (4) 剪辑节奏

- 梦的逻辑剪辑：场景硬切、时间错位、身份互换；《穆赫兰道》以断裂重组现实与梦境。`impression`

## (5) 色彩与光影

- 色彩：暖黄日常对照深红与深蓝：红幕布、蓝丝绒、暖黄灯光下的黑暗；色彩饱和而诡异。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：谜面结构：开头抛出谜（耳朵、尸体、失忆），中间以梦境与双重身份推进，结尾不解谜，只留回响。`impression`
- 该拍什么：
- 红幕布前的凝视与耳语
- 小镇日常中突然出现的异物
- 工业低鸣配暖黄灯光
- 梦境与现实的身份互换
- 不该拍什么：
- 线性解谜
- 解释性对白
- 明亮写实的日常
- 温情圆满的收束

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 红幕布前的凝视与耳语；- 小镇日常中突然出现的异物；- 工业低鸣配暖黄灯光；- 梦境与现实的身份互换
- 不该拍：- 线性解谜；- 解释性对白；- 明亮写实的日常；- 温情圆满的收束
- Negative prompt: `No linear mystery-solving, no explanatory dialogue, no bright realist daylight, no sentimental happy ending, no ironic detachment`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of David Lynch, a small Yorkshire terrier sitting on a subway seat at night, red curtain light, industrial hum underneath, the familiar carriage turning strange, a dream logic cut to a dark corridor, no explanation`
- 中文对照：林奇风格：一只约克夏犬坐在夜晚的地铁座位上，红幕布般的光，底下工业低鸣，熟悉的车厢变得陌生，梦的逻辑切到一条黑暗走廊，不解释。
- Negative: `No linear solving, no explanatory dialogue, no bright realism`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
