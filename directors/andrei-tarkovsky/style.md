# Andrei Tarkovsky — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Andrei Tarkovsky: sculpting in time, long takes as prayer, water fire earth air, the Zone as faith, colour drained to gold and earth`
- ZH: 塔可夫斯基风格：雕刻时间，长镜头即祈祷，水火土气，区即信仰，色彩褪至金与土。

## (2) 镜头语言

- 景别：远景与全景为主，人物小，自然大；特写罕见。`verbatim`
- 机位：极缓慢的推轨与横移，机位如祈祷般移动。`impression`
- 镜头：标准焦距，深焦，画面如圣像画。`impression`

## (3) 场面调度

- 场面调度：人物在自然与废墟中缓慢行走，走位即朝圣。`verbatim`
- 演员：职业演员，表演克制，沉默多。`impression`
- 空间：森林、河流、废墟、区，空间即信仰。`impression`

## (4) 剪辑节奏

- 剪辑：节奏极慢，长镜头是基本单位；剪切极少。`verbatim`
- 转场：硬切，时间跳跃如梦境。`impression`
- 声音：环境音（水、风、脚步）为主，音乐（巴赫）克制。`artifact`

## (5) 色彩与光影

- 色彩：黑白与彩色并置（《鲁布廖夫》结尾彩色圣像）；彩色时期土色与金色。`verbatim`
- 光影：自然光，阴天漫射；水面反光即圣光。`impression`
- 画幅：宽银幕，横向自然构图。`impression`

## (6) 叙事结构

- 结构：朝圣式线性，时间绵延；结尾常为一个长镜头。`verbatim`
- 视点：全知而神圣，诗人视角。`impression`
- 时间：雕刻的时间，长镜头即时间本身。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：长镜头、水火土气、区与朝圣、废墟与自然、梦境与童年、圣像。
- 该拍：河流、雨、火、镜子、马、教堂。
- 不该拍：不拍快速剪辑、不拍解释性对白、不拍类型化高潮、不拍心理分析。
- Negative prompt: `No fast cutting, no explanatory dialogue, no genre climax, no psychological analysis, no handheld shaky cam, no sentimental score`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Andrei Tarkovsky, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, a very long take, rain on the window, the carriage as the Zone, time sculpted, water and gold light, a prayer not a plot`
- 中文对照：塔可夫斯基风格：一只约克夏犬坐在地铁座位上，一个极长的镜头，窗上的雨，车厢即区，雕刻的时间，水与金光，一场祈祷而非情节。
- Negative: `No fast cutting, no explanatory dialogue, no genre climax, no psychological analysis`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
