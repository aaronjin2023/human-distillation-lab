# Éric Rohmer — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Éric Rohmer: moral tales in words, long conversations in sunlight, seasons as structure, desire debated not shown, the camera that listens`
- ZH: 侯麦风格：言语中的道德故事，阳光下的长对话，季节即结构，欲望被辩论而非展示，倾听的镜头。

## (2) 镜头语言

- 景别：中景与全景为主，对话双方的中景；特写罕见。`verbatim`
- 机位：固定机位，平视，机位如倾听者。`impression`
- 镜头：标准焦距，自然光，画面明亮。`impression`

## (3) 场面调度

- 场面调度：室内与海滩对话，人物并坐或对坐；走位即辩论。`verbatim`
- 演员：职业与素人混用，表演自然，对白精确。`artifact`
- 空间：海滩、公寓、咖啡馆，季节标记空间。`impression`

## (4) 剪辑节奏

- 剪辑：节奏缓慢，对话的完整时长被保留；剪切点藏在对白中。`verbatim`
- 转场：硬切与淡入淡出，季节更替标记时间。`impression`
- 声音：对白主导，音乐极少；环境音（海浪、风）为主。`impression`

## (5) 色彩与光影

- 色彩：彩色为主，明亮自然，蓝天、绿树、米色室内。`impression`
- 光影：自然阳光，柔和明暗，少阴影。`impression`
- 画幅：1.37:1 与宽银幕并用，中景构图。`impression`

## (6) 叙事结构

- 结构：系列结构（六个道德故事、四季），每部一个道德困境；结尾开放。`verbatim`
- 视点：限知视角，观众与人物同样辩论。`impression`
- 时间：季节时间，夏天与冬天标记欲望。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：长对话、道德困境、季节、海滩、阳光、欲望的辩论。
- 该拍：咖啡馆、公寓、海边别墅、自行车、绿光。
- 不该拍：不拍动作场面、不拍心理独白、不拍煽情音乐、不拍明确答案。
- Negative prompt: `No action scenes, no psychological monologue, no sentimental score, no clear answers, no fast cutting, no camera movement`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Éric Rohmer, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, two commuters debate whether to adopt it, long conversation in sunlight, seasons as structure, desire debated not shown, the camera that listens`
- 中文对照：侯麦风格：一只约克夏犬坐在地铁座位上，两位乘客辩论是否收养它，阳光下的长对话，季节即结构，欲望被辩论而非展示，倾听的镜头。
- Negative: `No action scenes, no psychological monologue, no sentimental score, no clear answers`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
