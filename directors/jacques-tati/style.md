# Jacques Tati — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jacques Tati: visual comedy without dialogue, Monsieur Hulot lost in modernity, wide shots where the gag hides in the corner, sound as joke`
- ZH: 塔蒂风格：无对白的视觉喜剧，于洛先生迷失于现代性，全景中笑点藏在角落，声音即笑话。

## (2) 镜头语言

- 景别：全景与远景为主，人物小，空间大；特写罕见。`verbatim`
- 机位：固定机位，平视，机位远离人物，拒绝跟拍。`impression`
- 镜头：标准与广角，深焦，全景一次呈现多层笑点。`impression`

## (3) 场面调度

- 场面调度：于洛先生在现代建筑中笨拙行走，笑点在画面角落同时发生。`verbatim`
- 演员：塔蒂本人饰于洛，肢体喜剧，少对白。`artifact`
- 空间：现代主义建筑、度假海滩、巴黎，空间即笑话。`impression`

## (4) 剪辑节奏

- 剪辑：节奏缓慢，长镜头等待笑点；剪切点藏在动作中。`verbatim`
- 转场：硬切，场景之间留白。`impression`
- 声音：环境音与音效即对白，音乐稀少；声音设计即喜剧。`artifact`

## (5) 色彩与光影

- 色彩：黑白时期灰调温润；彩色时期（《游戏时间》）冷灰与霓虹。`verbatim`
- 光影：均匀自然光，无戏剧性明暗。`impression`
- 画幅：宽银幕，全景构图。`impression`

## (6) 叙事结构

- 结构：段落式，松散串联，无主线情节；结尾开放。`verbatim`
- 视点：全知而疏离，观众俯瞰于洛的笨拙。`impression`
- 时间：度假时间，缓慢而循环。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：于洛先生、现代建筑、海滩度假、全景中的笑点、声音喜剧。
- 该拍：玻璃门、电梯、喷泉、汽车、巴黎街头。
- 不该拍：不拍对白喜剧、不拍特写煽情、不拍快速剪辑、不拍心理分析。
- Negative prompt: `No dialogue comedy, no sentimental close-ups, no fast cutting, no psychological analysis, no handheld shaky cam, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jacques Tati, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, Monsieur Hulot lost in the modern carriage, the gag hides in the corner of a wide shot, sound as joke, no dialogue`
- 中文对照：塔蒂风格：一只约克夏犬坐在地铁座位上，于洛先生在现代车厢中迷失，笑点藏在全景的角落，声音即笑话，没有对白。
- Negative: `No dialogue comedy, no sentimental close-ups, no fast cutting, no psychological analysis`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
