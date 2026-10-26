# Akira Kurosawa — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Akira Kurosawa: epic humanism, weather as fate, multiple cameras, axial cuts, rain wind and fire, the individual against the crowd`
- ZH: 黑泽明风格：史诗人文主义，天气即命运，多机位，轴线剪切，雨风火，个人对抗人群。

## (2) 镜头语言

- 景别：远景与全景为主，天气中的人群；特写在情感顶点出现。`verbatim`
- 机位：多机位同时拍摄，机位移动果断；长焦压缩空间。`artifact`
- 镜头：长焦为主，景深浅，人物与背景分离。`artifact`

## (3) 场面调度

- 场面调度：群戏如战场，人物在雨风中移动；走位即冲突。`verbatim`
- 演员：职业演员（三船敏郎、志村乔），表演幅度大而精确。`artifact`
- 空间：村庄、城堡、荒原，空间即战场。`impression`

## (4) 剪辑节奏

- 剪辑：轴线剪切（axial cut），同一轴线跳切拉近；节奏果断。`verbatim`
- 转场：硬切与划像（wipe），段落衔接如画卷。`artifact`
- 声音：环境音（雨、风）为主，音乐（早坂文雄）关键。`artifact`

## (5) 色彩与光影

- 色彩：黑白时期高反差，雨与泥；彩色时期（《乱》）浓烈原色，红、黄、蓝。`verbatim`
- 光影：天气即光，雨、雾、火的光影。`impression`
- 画幅：宽银幕，横向史诗构图。`impression`

## (6) 叙事结构

- 结构：多视角（《罗生门》）与史诗线性并存；结尾常为雨中的希望。`verbatim`
- 视点：多视角切换，真相不确定。`impression`
- 时间：史诗时间，季节与天气标记。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：多视角、天气、群戏、武士、村庄、雨风火、个人对抗人群。
- 该拍：城堡、荒原、森林、雨中的战斗、旗帜。
- 不该拍：不拍室内心理剧、不拍克制留白、不拍即兴手持、不拍煽情独白。
- Negative prompt: `No chamber psychological drama, no restrained minimalism, no improvised handheld, no sentimental monologue, no flat lighting, no slow empty takes`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Akira Kurosawa, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat in the rain, multiple cameras, axial cuts, weather as fate, the individual against the crowd, epic humanism`
- 中文对照：黑泽明风格：一只约克夏犬坐在地铁座位上，窗外是雨，多机位，轴线剪切，天气即命运，个人对抗人群，史诗人文主义。
- Negative: `No chamber psychological drama, no restrained minimalism, no improvised handheld, no sentimental monologue`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
