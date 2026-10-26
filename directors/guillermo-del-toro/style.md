# Guillermo del Toro — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guillermo del Toro: gothic fairy tale, amber and teal, monsters with tender hearts, clockwork creatures, childhood wonder inside horror`
- ZH: 德尔·托罗风格：哥特童话，琥珀色与青色，内心温柔的怪物，发条般的造物，恐怖之中的童年奇想。

## (2) 镜头语言

- 景别：中景与特写并重，特写给怪物与物件的质感；低机位仰拍让孩子视角主导世界。`verbatim`
- 机位与运动：缓慢推近与环绕为主，摄影机像在博物馆里踱步；怪物出场时用缓慢的揭示而非跳吓。`impression`
- 运镜禁忌：见第 (7) 节不该拍清单。

## (3) 场面调度

- 手工布景的封闭世界：迷宫、地窖、实验室；怪物与孩子在同一画框内对峙，成人世界在背景中崩塌。`impression`

## (4) 剪辑节奏

- 节奏舒缓，段落以童话章节推进；剪辑让位于美术与造型，奇观场面用长镜头展示手工质感。`impression`

## (5) 色彩与光影

- 色彩：琥珀金、深青与血红三色主导；冷绿的水下世界对照暖黄的童年记忆，怪物常为青灰或赭石。`verbatim`
- 光影：以影片本身的光影为准——自然光为主、人工光只作补光；明暗对比随场景而定，阴影带色彩而不死黑，高光克制不溢出。`verbatim`

## (6) 叙事结构

- 结构：童话结构：孩子进入异世界、完成三件考验、付出代价；开头以画外音或书页起笔，结尾以童话式收束、真假不辨。`impression`
- 该拍什么：
- 哥特迷宫与地窖中的童话考验
- 手工怪物与发条造物的特写
- 琥珀与青色交织的奇幻内景
- 孩子与怪物在同一画框内的对视
- 不该拍什么：
- 跳吓式剪辑
- 冷峻写实的纪录风格
- 怪物只作恐怖符号
- 过度明亮的商业奇幻光

## (7) 该拍什么 / 不该拍什么（Negative prompt）

- 该拍：- 哥特迷宫与地窖中的童话考验；- 手工怪物与发条造物的特写；- 琥珀与青色交织的奇幻内景；- 孩子与怪物在同一画框内的对视
- 不该拍：- 跳吓式剪辑；- 冷峻写实的纪录风格；- 怪物只作恐怖符号；- 过度明亮的商业奇幻光
- Negative prompt: `No jump-scare cutting, no cold documentary realism, no monsters as mere horror props, no bright commercial fantasy lighting, no ironic detachment`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Guillermo del Toro, a small Yorkshire terrier sitting on a subway seat at night, amber light against teal shadows, the carriage turning into a clockwork fairy-tale grotto, a gentle monster watching from the next seat, childhood wonder inside the dark`
- 中文对照：德尔·托罗风格：一只约克夏犬坐在夜晚的地铁座位上，琥珀光对着青色阴影，车厢化作发条童话洞窟，一只温柔的怪物坐在邻座注视，黑暗中的童年奇想。
- Negative: `No jump scares, no flat realism, no bright fantasy lighting`
- 检验点：镜头语言、场面调度、剪辑节奏、色彩光影、叙事结构是否都落在该导演的风格内；狗是否仍是画面主体。
