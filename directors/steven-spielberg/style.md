# Steven Spielberg — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Steven Spielberg: wonder in a low-angle close-up, the oner that reveals the world, light breaking through darkness, ordinary people facing the extraordinary`
- ZH: 斯皮尔伯格风格：低角度特写中的惊奇，揭示世界的长镜头，穿透黑暗的光，普通人面对非凡之事。

## (2) 镜头语言

- 景别：低角度特写与反应镜头为主：先拍人物看，再拍人物所看之物；《大白鲨》以反应镜头写恐惧。`verbatim`
- 机位与运动：平稳推近与升降，少用手持；长镜头揭示空间，《拯救大兵瑞恩》开场以手持写混乱是例外而非惯例。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 家庭与群体调度：孩子在前、成人在后，人物在开阔空间中奔跑、寻找、团聚；调度以寻找与重逢驱动。`impression`

## (4) 剪辑节奏

- 经典连续性剪辑：视线匹配、动作匹配，节奏由悬念驱动；高潮段落加速，结尾以团聚或告别收束。`impression`

## (5) 色彩与光影

- 色彩：暖金阳光与深蓝夜色对照；《辛德勒的名单》黑白中一点红为标志；战争段落去饱和，家庭段落暖调。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：三幕冒险结构：日常—入侵—归来；开头以日常切入，中间以奇观推进，结尾以和解或告别收束，情感完整。`impression`
- 该拍什么：
- 低角度特写中的惊奇反应
- 长镜头揭示的奇观空间
- 暖金阳光下的家庭团聚
- 黑白中一点红的克制点缀
- 不该拍什么：
- 冷峻疏离的旁观
- 碎片化的跳切
- 犬儒的讽刺
- 无情感的奇观堆砌

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 低角度特写中的惊奇反应；- 长镜头揭示的奇观空间；- 暖金阳光下的家庭团聚；- 黑白中一点红的克制点缀
- 不该拍：- 冷峻疏离的旁观；- 碎片化的跳切；- 犬儒的讽刺；- 无情感的奇观堆砌
- Negative prompt: `No cold detached observation, no fragmented jump cutting, no cynical irony, no emotionless spectacle, no bleak hopeless ending`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Steven Spielberg, a small Yorkshire terrier sitting on a subway seat, low-angle close-up of wonder on a child's face, one long take revealing the whole carriage, warm light breaking through the windows, ordinary commute turning extraordinary`
- 中文对照：斯皮尔伯格风格：一只约克夏犬坐在地铁座位上，孩子脸上低角度特写的惊奇，一个长镜头揭示整节车厢，暖光穿透车窗，日常通勤化作非凡。
- Negative: `No cold detachment, no jump cutting, no cynical irony`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
