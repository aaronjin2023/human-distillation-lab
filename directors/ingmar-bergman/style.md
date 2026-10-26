# Ingmar Bergman — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ingmar Bergman: existential chamber drama, faces in close-up, silence as dialogue, God and death in one room, light that interrogates`
- ZH: 伯格曼风格：存在主义室内剧，面孔特写，沉默即对话，上帝与死亡同处一室，审问般的光。

## (2) 镜头语言

- 景别：面孔特写为主，特写即风景；全景罕见。`verbatim`
- 机位：固定机位，正面特写，机位与人物面孔齐平。`impression`
- 镜头：标准与长焦，特写景深浅，面孔之外皆虚。`impression`

## (3) 场面调度

- 场面调度：室内剧，两人对峙，人物在房间内缓慢移动；走位即心理。`verbatim`
- 演员：固定班底（冯·西多、安德森、乌尔曼），表演精确而内敛。`artifact`
- 空间：封闭室内、海岛、教堂，空间越收越紧。`impression`

## (4) 剪辑节奏

- 剪辑：节奏缓慢，特写之间硬切；沉默的时长即剪辑。`verbatim`
- 转场：硬切与淡入淡出，梦境与现实之间不加标记。`impression`
- 声音：对白精确，沉默漫长；音乐稀少，环境音克制。`impression`

## (5) 色彩与光影

- 色彩：黑白时期高反差，面孔明亮、背景深黑；彩色时期冷调，灰、蓝、米。`verbatim`
- 光影：斯文·尼科维斯特的柔光，面孔被光审问；阴影深沉。`artifact`
- 画幅：1.37:1 与宽银幕并用，特写构图。`impression`

## (6) 叙事结构

- 结构：室内剧线性，时间常为一天或一夜；结尾开放而苦涩。`verbatim`
- 视点：限知视角，观众与人物同样不知道上帝是否在场。`impression`
- 时间：梦境与闪回交织，过去侵入现在。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：面孔特写、两人对峙的室内剧、上帝之死、死亡化身、沉默与梦境。
- 该拍：海岛、教堂、棋盘、镜子、母女对峙。
- 不该拍：不拍群戏奇观、不拍快速剪辑、不拍煽情配乐、不拍明确答案。
- Negative prompt: `No crowd spectacle, no fast cutting, no sentimental score, no clear answers, no handheld shaky cam, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Ingmar Bergman, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat in close-up, its face interrogated by light, a silent commuter opposite, God and death in one carriage, chamber drama`
- 中文对照：伯格曼风格：一只约克夏犬坐在地铁座位上的特写，面孔被光审问，对面是一位沉默的乘客，上帝与死亡同处一节车厢，室内剧。
- Negative: `No crowd spectacle, no fast cutting, no sentimental score, no clear answers`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
