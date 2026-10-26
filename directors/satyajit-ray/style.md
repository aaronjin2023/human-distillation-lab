# Satyajit Ray — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Satyajit Ray: lyrical humanism, Bengal village and city, Apu's journey, music as memory, the camera that watches with love`
- ZH: 雷伊风格：抒情人文主义，孟加拉乡村与城市，阿普的旅程，音乐即记忆，以爱观看的镜头。

## (2) 镜头语言

- 景别：全景与中景为主，乡村风景；特写温柔。`verbatim`
- 机位：固定与缓慢移动并存，机位如注视者。`impression`
- 镜头：标准焦距，深焦，画面层次如水彩。`impression`

## (3) 场面调度

- 场面调度：乡村与城市中的人物行走，走位即成长。`verbatim`
- 演员：职业与素人混用，表演自然。`artifact`
- 空间：孟加拉乡村、加尔各答，空间即成长。`impression`

## (4) 剪辑节奏

- 剪辑：节奏舒缓，段落式；剪切点藏在日常中。`verbatim`
- 转场：叠化与硬切，时间流逝如季节。`impression`
- 声音：音乐（拉维·香卡）关键，环境音真实；对白自然。`artifact`

## (5) 色彩与光影

- 色彩：黑白时期灰调温润；彩色时期暖调，土黄、绿。`impression`
- 光影：自然光，柔和明暗；阳光透过树叶。`impression`
- 画幅：1.37:1 与宽银幕并用。`impression`

## (6) 叙事结构

- 结构：成长编年（阿普三部曲），线性而抒情；结尾开放。`verbatim`
- 视点：儿童与作者视角，温柔而同情。`impression`
- 时间：季节时间，成长标记时间。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：阿普的成长、孟加拉乡村、音乐、火车、季节、家庭。
- 该拍：田野、河流、城市、音乐室、火车。
- 不该拍：不拍歌舞奇观、不拍煽情高潮、不拍快速剪辑、不拍类型化反派。
- Negative prompt: `No song-and-dance spectacle, no melodramatic climax, no fast cutting, no stereotyped villains, no studio sets, no sentimental score`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Satyajit Ray, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, a boy watches it with wonder, lyrical humanism, Bengal village and city, music as memory, the camera that watches with love`
- 中文对照：雷伊风格：一只约克夏犬坐在地铁座位上，一个男孩惊奇地望着它，抒情人文主义，孟加拉乡村与城市，音乐即记忆，以爱观看的镜头。
- Negative: `No song-and-dance spectacle, no melodramatic climax, no fast cutting, no stereotyped villains`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
