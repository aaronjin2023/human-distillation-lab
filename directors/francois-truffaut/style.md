# François Truffaut — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of François Truffaut: New Wave humanism, childhood and love in close-up, tracking shots that follow, literature on screen, tenderness without sentimentality`
- ZH: 特吕弗风格：新浪潮人文主义，童年与爱情的特写，跟随的推轨镜头，文学上银幕，不煽情的温情。

## (2) 镜头语言

- 景别：中景与特写并重，面孔特写温柔；全景交代巴黎。`verbatim`
- 机位：推轨跟随人物行走，机位温柔移动；少用手持。`impression`
- 镜头：标准焦距，浅焦，面孔明亮。`impression`

## (3) 场面调度

- 场面调度：巴黎街头行走，人物并行；室内剧温柔。`verbatim`
- 演员：固定班底（让-皮埃尔·莱奥），表演自然。`artifact`
- 空间：巴黎街头、公寓、电影院，空间即记忆。`impression`

## (4) 剪辑节奏

- 剪辑：节奏流畅，推轨与剪切衔接自然；省略温柔。`verbatim`
- 转场：叠化与硬切并用，时间流逝如季节。`impression`
- 声音：对白自然，音乐温柔（乔治·德勒吕）；画外音旁白。`artifact`

## (5) 色彩与光影

- 色彩：黑白时期灰调温润；彩色时期暖调，米、棕、蓝。`impression`
- 光影：自然光，柔和明暗，面孔被温柔照亮。`impression`
- 画幅：1.37:1 与宽银幕并用。`impression`

## (6) 叙事结构

- 结构：线性而松散，童年与爱情的编年；结尾开放。`verbatim`
- 视点：儿童与作者视角，温柔而同情。`impression`
- 时间：编年时间，季节标记成长。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：童年、爱情三角、巴黎街头、电影自指、文学改编、推轨跟随。
- 该拍：海滩、电影院、书店、公寓、自行车。
- 不该拍：不拍冷峻疏离、不拍跳切断裂、不拍煽情高潮、不拍政治口号。
- Negative prompt: `No cold detachment, no jump-cut rupture, no melodramatic climax, no political slogans, no handheld shaky cam, no ironic distance`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of François Truffaut, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, a boy watches it with wonder, tracking shot follows them through Paris streets, tenderness without sentimentality, literature on screen`
- 中文对照：特吕弗风格：一只约克夏犬坐在地铁座位上，一个男孩惊奇地望着它，推轨镜头跟随他们穿过巴黎街头，不煽情的温情，文学上银幕。
- Negative: `No cold detachment, no jump-cut rupture, no melodramatic climax, no political slogans`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
