# Alain Resnais — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alain Resnais: time folded, memory as architecture, tracking shots through corridors, past and present in one frame, love and war remembered`
- ZH: 雷乃风格：时间折叠，记忆即建筑，走廊中的推轨镜头，过去与现在同框，爱与战争被记忆。

## (2) 镜头语言

- 景别：全景与特写交替，走廊推轨；特写凝视面孔。`verbatim`
- 机位：缓慢推轨，机位在走廊与房间中移动；少用手持。`impression`
- 镜头：标准与广角，深焦，画面如记忆宫殿。`impression`

## (3) 场面调度

- 场面调度：走廊与房间中的人物游荡，走位即记忆。`verbatim`
- 演员：职业演员，表演克制，对白如独白。`impression`
- 空间：旅馆走廊、广岛街头、集中营遗址，空间即记忆。`impression`

## (4) 剪辑节奏

- 剪辑：时间折叠式剪辑，过去与现在硬切并置；节奏缓慢。`verbatim`
- 转场：硬切与叠化，记忆转场不加标记。`impression`
- 声音：画外音独白，音乐（乔瓦尼·富斯科）克制；环境音稀少。`artifact`

## (5) 色彩与光影

- 色彩：黑白时期高反差；彩色时期冷调，灰、蓝、米。`impression`
- 光影：室内柔光，明暗对比温和；阴影即记忆。`impression`
- 画幅：宽银幕，走廊构图。`impression`

## (6) 叙事结构

- 结构：时间折叠，过去与现在并置；结尾开放。`verbatim`
- 视点：限知视角，观众与人物同样不确定记忆是否真实。`impression`
- 时间：记忆时间，闪回与现在交织。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：时间折叠、走廊推轨、记忆、广岛与集中营、爱情与战争、画外音独白。
- 该拍：旅馆、废墟、雕塑、镜子、照片。
- 不该拍：不拍线性叙事、不拍明确答案、不拍煽情配乐、不拍动作场面。
- Negative prompt: `No linear narrative, no clear answers, no sentimental score, no action scenes, no fast cutting, no explanatory dialogue`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Alain Resnais, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, time folds, the carriage becomes a corridor of memory, past and present in one frame, tracking shot, love and war remembered`
- 中文对照：雷乃风格：一只约克夏犬坐在地铁座位上，时间折叠，车厢变成记忆的走廊，过去与现在同框，推轨镜头，爱与战争被记忆。
- Negative: `No linear narrative, no clear answers, no sentimental score, no action scenes`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
