# Jean-Luc Godard — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Luc Godard: New Wave rupture, jump cuts, direct address, quotation and collage, cinema that thinks aloud, colour as argument`
- ZH: 戈达尔风格：新浪潮断裂，跳切，直视镜头，引文与拼贴，会思考的电影，色彩即论证。

## (2) 镜头语言

- 景别：中景与特写交替，特写直视镜头；全景少。`verbatim`
- 机位：手持跟拍，机位自由移动，拒绝固定机位。`impression`
- 镜头：标准焦距，浅焦，画面常失焦或过曝。`impression`

## (3) 场面调度

- 场面调度：街头即兴走位，演员看镜头说话；空间即巴黎街头。`verbatim`
- 演员：职业与素人混用，表演即兴，台词常即兴。`artifact`
- 空间：巴黎街头、公寓、汽车，空间即兴而真实。`impression`

## (4) 剪辑节奏

- 剪辑：跳切为标志，时间断裂；节奏忽快忽慢。`verbatim`
- 转场：跳切与硬切，字幕卡打断叙事。`verbatim`
- 声音：对白与音乐并置，声画常不同步；画外音评论。`impression`

## (5) 色彩与光影

- 色彩：黑白时期高反差；彩色时期原色并置，红、蓝、黄如论证。`verbatim`
- 光影：自然光，少修饰；过曝与欠曝并存。`impression`
- 画幅：1.37:1 与宽银幕并用。`impression`

## (6) 叙事结构

- 结构：去情节化，引文拼贴，字幕卡打断；结尾常为死亡或离去。`verbatim`
- 视点：直视镜头，作者现身，观众被直接质问。`impression`
- 时间：跳切的时间，过去与现在并置。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：跳切、直视镜头、引文拼贴、巴黎街头、字幕卡、原色并置。
- 该拍：汽车、公寓、书店、电影院、政治口号。
- 不该拍：不拍无缝叙事、不拍隐藏作者、不拍煽情配乐、不拍闭合结局。
- Negative prompt: `No seamless narrative, no hidden author, no sentimental score, no closed ending, no invisible editing, no psychological realism`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jean-Luc Godard, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, jump cuts, the dog looks straight into the camera, quotation cards interrupt, Paris street immediacy, colour as argument`
- 中文对照：戈达尔风格：一只约克夏犬坐在地铁座位上，跳切，狗直视镜头，引文字幕卡打断叙事，巴黎街头的即时性，色彩即论证。
- Negative: `No seamless narrative, no hidden author, no sentimental score, no closed ending`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
