# Kathryn Bigelow — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kathryn Bigelow: kinetic handheld immersion, the body under pressure, dust and sweat, tension held until it snaps`
- ZH: 毕格罗风格：动感手持的沉浸，压力下的身体，尘土与汗水，张力绷到断裂。

## (2) 镜头语言

- 景别：手持中景与特写并重：特写给手、汗、引线等细节；多机位覆盖动作，景别在混乱中切换。`verbatim`
- 机位与运动：手持跟拍与急推：摄影机贴近身体运动，冲浪、拆弹、追捕皆以身体的速度运动。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 压力空间调度：拆弹现场、突袭小队、冲浪海面——人物在危险空间中协作与对峙，调度以身体动作驱动。`impression`

## (4) 剪辑节奏

- 多机位快速剪辑：动作段落剪辑加速，静默段落拉长；节奏由心跳驱动，张力在剪辑中绷紧。`impression`

## (5) 色彩与光影

- 色彩：尘土黄与军绿、夜视绿与血红对照；色彩去饱和，汗水与尘土的质感写在画面上。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：任务结构：开头以任务或行动切入，中间以压力递增推进，结尾以任务完成或失败收束，不给道德评判。`impression`
- 该拍什么：
- 手持贴近身体的动作场面
- 拆弹与突袭中的多机位剪辑
- 尘土与汗水的质感特写
- 张力绷到断裂的静默段落
- 不该拍什么：
- 平稳冷漠的旁观
- 浪漫化的战争
- 温情圆满的收束
- 扁平的棚拍动作

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 手持贴近身体的动作场面；- 拆弹与突袭中的多机位剪辑；- 尘土与汗水的质感特写；- 张力绷到断裂的静默段落
- 不该拍：- 平稳冷漠的旁观；- 浪漫化的战争；- 温情圆满的收束；- 扁平的棚拍动作
- Negative prompt: `No detached static observation, no romanticized war, no sentimental happy ending, no flat studio action, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Kathryn Bigelow, a small Yorkshire terrier sitting on a subway seat, handheld camera close on trembling hands, multi-camera cutting around the carriage, dust and sweat, tension held until it snaps, no romance`
- 中文对照：毕格罗风格：一只约克夏犬坐在地铁座位上，手持摄影机贴近颤抖的手，多机位剪辑环绕车厢，尘土与汗水，张力绷到断裂，不浪漫化。
- Negative: `No static observation, no romanticized war, no sentimental ending`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
