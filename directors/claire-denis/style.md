# Claire Denis — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Claire Denis: the body in close-up, postcolonial heat, desire without words, the camera touching skin like a hand`
- ZH: 德尼风格：特写中的身体，后殖民的热，欲望无需言语，镜头如手般触碰皮肤。

## (2) 镜头语言

- 景别：身体特写与中景并重：特写给皮肤、汗水、手；长镜头凝视身体的动作。`verbatim`
- 机位与运动：缓慢横移与手持结合：摄影机贴近身体运动，少用快速剪辑，运动即欲望的节奏。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 后殖民空间调度：非洲、军营、巴黎郊区——身体在热与尘土中相遇，调度以身体的接近与远离驱动。`impression`

## (4) 剪辑节奏

- 节奏舒缓，段落以身体动作与音乐连接；剪辑让位于凝视，省略多于交代。`impression`

## (5) 色彩与光影

- 色彩：暖黄与赭石主导：非洲的热黄、军营的土绿、巴黎的灰蓝；色彩写身体的温度。`impression`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：身体结构：开头以身体或空间切入，中间以欲望与记忆的纠缠推进，结尾以告别或舞蹈收束，不给解释。`impression`
- 该拍什么：
- 身体特写中的皮肤与汗水
- 后殖民空间中的身体相遇
- 缓慢横移中的欲望节奏
- 暖黄与赭石的身体温度
- 不该拍什么：
- 快速剪辑
- 解释性对白
- 冷峻的旁观
- 戏剧化高潮

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 身体特写中的皮肤与汗水；- 后殖民空间中的身体相遇；- 缓慢横移中的欲望节奏；- 暖黄与赭石的身体温度
- 不该拍：- 快速剪辑；- 解释性对白；- 冷峻的旁观；- 戏剧化高潮
- Negative prompt: `No fast cutting, no explanatory dialogue, no cold detached observation, no dramatic climax, no sentimental shortcut`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Claire Denis, a small Yorkshire terrier sitting on a subway seat, close-ups of skin and hands, the camera touching like a hand, postcolonial heat in the carriage, desire without words, a dance at the end`
- 中文对照：德尼风格：一只约克夏犬坐在地铁座位上，皮肤与手的特写，镜头如手般触碰，车厢里的后殖民热，欲望无需言语，结尾一支舞。
- Negative: `No fast cutting, no explanatory dialogue, no cold detachment`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
