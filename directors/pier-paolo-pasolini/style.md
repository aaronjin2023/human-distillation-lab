# Pier Paolo Pasolini — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pier Paolo Pasolini: poetic cinema, sacred and profane in one frame, non-actors as icons, frontal tableaux, ancient myth in modern slums`
- ZH: 帕索里尼风格：诗意电影，神圣与亵渎同框，非职业演员如圣像，正面构图，现代贫民窟中的古代神话。

## (2) 镜头语言

- 景别：正面中景与全景为主，人物如圣像般直面镜头。`verbatim`
- 机位：固定机位，正面构图，少用运动；机位如祭坛前的凝视。`impression`
- 镜头：标准焦距，深焦，画面如文艺复兴绘画。`impression`

## (3) 场面调度

- 场面调度：正面群戏，人物排成圣像画般的构图；贫民窟即舞台。`verbatim`
- 演员：非职业演员，面孔如圣像，表演静默而庄严。`artifact`
- 空间：罗马贫民窟、沙漠、古城，神话空间与现实空间重叠。`impression`

## (4) 剪辑节奏

- 剪辑：节奏缓慢，段落式；剪切如诗行断句。`impression`
- 转场：硬切，神话与现实之间不加过渡。`impression`
- 声音：巴赫与古典音乐，环境音稀少；音乐即神圣。`artifact`

## (5) 色彩与光影

- 色彩：黑白时期粗粝神圣；彩色时期浓烈，土黄、赭红、深蓝如壁画。`verbatim`
- 光影：强烈的正面光，面孔被照亮如圣像；阴影深沉。`impression`
- 画幅：1.37:1 与宽银幕并用，正面构图。`impression`

## (6) 叙事结构

- 结构：寓言式，神话重述（《马太福音》《美狄亚》），结尾常为暴力或死亡。`verbatim`
- 视点：全知而神圣，诗人视角俯瞰俗世。`impression`
- 时间：神话时间，古代与现代并置。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：贫民窟圣像、神话重述、正面构图、神圣与亵渎、沙漠与古城。
- 该拍：非职业演员的面孔、巴赫音乐、仪式化的暴力。
- 不该拍：不拍心理现实主义、不拍中产室内剧、不拍即兴手持、不拍煽情配乐。
- Negative prompt: `No psychological realism, no bourgeois interior drama, no improvised handheld, no sentimental score, no fast cutting, no ironic distance`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Pier Paolo Pasolini, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat like a small sacred icon, frontal tableau, commuters as a fresco, Bach on the soundtrack, ancient myth in a modern carriage`
- 中文对照：帕索里尼风格：一只约克夏犬坐在地铁座位上，如同一尊小小的圣像，正面构图，乘客如壁画，巴赫配乐，现代车厢中的古代神话。
- Negative: `No psychological realism, no bourgeois interior drama, no improvised handheld, no sentimental score`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
