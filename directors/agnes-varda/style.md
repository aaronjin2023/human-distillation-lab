# Agnès Varda — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Agnès Varda: New Wave curiosity, real time and real faces, gleaning images from the margins, playful and political, the camera as a companion`
- ZH: 瓦尔达风格：新浪潮好奇心，实时与真实面孔，从边缘拾穗影像， playful 而政治，镜头即同伴。

## (2) 镜头语言

- 景别：中景与特写并重，面孔特写亲切；全景交代街头与田野。`verbatim`
- 机位：手持跟拍，机位亲切移动；少用固定机位。`impression`
- 镜头：标准焦距，自然光，画面明亮。`impression`

## (3) 场面调度

- 场面调度：实景街头与田野，人物自然行走；拾穗者即主角。`verbatim`
- 演员：职业与素人混用，表演自然；导演本人常出镜。`artifact`
- 空间：巴黎街头、田野、海滩，空间即生活。`impression`

## (4) 剪辑节奏

- 剪辑：节奏轻快，段落拼贴；剪切如拾穗，碎片并置。`verbatim`
- 转场：硬切与叠化并用，时间跳跃轻快。`impression`
- 声音：对白自然，画外音亲切；音乐轻快。`impression`

## (5) 色彩与光影

- 色彩：黑白时期灰调明亮；彩色时期饱和明快，红、蓝、黄。`impression`
- 光影：自然光，明亮均匀，少阴影。`impression`
- 画幅：1.37:1 与宽银幕并用。`impression`

## (6) 叙事结构

- 结构：实时结构（《克莱奥》两小时）与拾穗拼贴并存；结尾开放。`verbatim`
- 视点：女性视角，导演本人即向导。`impression`
- 时间：实时与记忆并置，拾穗的时间。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：拾穗、实时、女性视角、街头与田野、真实面孔、 playful 政治。
- 该拍：市场、海滩、村庄、墙面、镜子。
- 不该拍：不拍冷峻疏离、不拍男性凝视、不拍煽情高潮、不拍隐藏作者。
- Negative prompt: `No cold detachment, no male gaze, no melodramatic climax, no hidden author, no fast cutting, no studio sets`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Agnès Varda, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, a woman films it with curiosity, real commuters smile, gleaning images from the margins, playful and political, the camera as a companion`
- 中文对照：瓦尔达风格：一只约克夏犬坐在地铁座位上，一位女性好奇地拍摄它，真实乘客微笑，从边缘拾穗影像，playful 而政治，镜头即同伴。
- Negative: `No cold detachment, no male gaze, no melodramatic climax, no hidden author`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
