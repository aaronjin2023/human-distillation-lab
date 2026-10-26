# Kenji Mizoguchi — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kenji Mizoguchi: one-shot long takes, the camera that follows women through suffering, water and mist, history as a woman's fate, no cuts to escape`
- ZH: 沟口风格：一镜到底的长镜头，跟随女性穿越苦难的镜头，水与雾，历史即女性的命运，无处可逃的剪切。

## (2) 镜头语言

- 景别：远景与全景为主，人物小，风景大；特写罕见。`verbatim`
- 机位：缓慢横移与推轨，机位跟随女性行走；一镜到底。`verbatim`
- 镜头：标准焦距，深焦，画面层次如浮世绘。`impression`

## (3) 场面调度

- 场面调度：女性在风景中行走，机位跟随；走位即命运。`verbatim`
- 演员：职业演员（田中绢代），表演克制而悲悯。`artifact`
- 空间：水边、雾中、古城，空间即女性的命运。`impression`

## (4) 剪辑节奏

- 剪辑：长镜头是基本单位，剪切极少；一镜到底。`verbatim`
- 转场：硬切，时间跳跃如命运。`impression`
- 声音：环境音（水、风）为主，音乐克制；对白平淡。`impression`

## (5) 色彩与光影

- 色彩：黑白为主，灰调温润；水面反光即光。`impression`
- 光影：自然光，雾即光；少强烈明暗。`impression`
- 画幅：1.37:1，横向风景构图。`impression`

## (6) 叙事结构

- 结构：女性一生的编年，线性而苦涩；结尾常为死亡或离去。`verbatim`
- 视点：全知而悲悯，观众与女性同行。`impression`
- 时间：历史时间，女性的一生即历史。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：女性、长镜头、水与雾、苦难、历史、妓女与艺伎。
- 该拍：湖边、雾、古城、茶屋、河流。
- 不该拍：不拍快速剪辑、不拍心理独白、不拍煽情高潮、不拍男性视角的猎奇。
- Negative prompt: `No fast cutting, no psychological monologue, no melodramatic climax, no male-gaze exoticism, no handheld shaky cam, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Kenji Mizoguchi, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, a very long take follows a woman through the carriage, water and mist outside, history as a woman's fate, no cuts to escape`
- 中文对照：沟口风格：一只约克夏犬坐在地铁座位上，一个极长的镜头跟随一位女性穿过车厢，窗外是水与雾，历史即女性的命运，无处可逃的剪切。
- Negative: `No fast cutting, no psychological monologue, no melodramatic climax, no male-gaze exoticism`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
