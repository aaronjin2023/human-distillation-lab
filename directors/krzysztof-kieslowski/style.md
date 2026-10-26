# Krzysztof Kieślowski — 导演风格规格 style.md（给图像 / 视频模型）

> 只描述影片，不描述人生。引用影片时只指认到具体影片与场景，不逐帧复述剧情。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Krzysztof Kieślowski: moral parables in grey Warsaw, chance as fate, faces in windows, colour as a code, the same soul twice`
- ZH: 基耶斯洛夫斯基风格：灰色华沙中的道德寓言，偶然即命运，窗中的面孔，色彩即密码，同一个灵魂两次。

## (2) 镜头语言

- 景别：中景与特写并重，窗与镜的特写；全景交代华沙公寓楼。`verbatim`
- 机位：固定机位，平视；机位常透过窗与镜拍摄。`impression`
- 镜头：标准焦距，浅焦，面孔明亮、背景虚化。`impression`

## (3) 场面调度

- 场面调度：公寓楼群戏，人物在楼道与窗前相遇；走位即偶然。`verbatim`
- 演员：职业演员，表演克制，沉默多。`impression`
- 空间：华沙公寓楼、巴黎街道，空间即命运。`impression`

## (4) 剪辑节奏

- 剪辑：节奏舒缓，段落式；剪切点藏在偶然相遇中。`verbatim`
- 转场：硬切与叠化，时间跳跃温柔。`impression`
- 声音：对白精确，音乐（普赖斯纳）克制而关键；环境音真实。`artifact`

## (5) 色彩与光影

- 色彩：早期灰调冷峻；《红白蓝》三色即密码，红为爱、白为平等、蓝为自由。`verbatim`
- 光影：自然光，柔和明暗；窗光即命运。`impression`
- 画幅：1.37:1 与宽银幕并用。`impression`

## (6) 叙事结构

- 结构：系列结构（《十诫》十部、《红白蓝》三部），每部一个道德困境；结尾开放。`verbatim`
- 视点：限知视角，观众与人物同样不知道偶然的含义。`impression`
- 时间：偶然的时间，一次相遇改变一生。`impression`

## (7) 该拍什么 / 不该拍什么

- 该拍：道德寓言、偶然、窗与镜、公寓楼、双重生活、色彩密码。
- 该拍：华沙、巴黎、电话、信件、狗（《十诫》第一诫）。
- 不该拍：不拍明确答案、不拍煽情高潮、不拍动作场面、不拍心理独白。
- Negative prompt: `No clear answers, no melodramatic climax, no action scenes, no psychological monologue, no fast cutting, no explanatory voiceover`

## (8) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Krzysztof Kieślowski, a small Yorkshire terrier sitting on a subway seat in a modern city, the terrier on a subway seat, a woman sees it through the window and misses her train, chance as fate, colour as a code, the same soul twice`
- 中文对照：基耶斯洛夫斯基风格：一只约克夏犬坐在地铁座位上，一位女性透过车窗看到它而错过了车，偶然即命运，色彩即密码，同一个灵魂两次。
- Negative: `No clear answers, no melodramatic climax, no action scenes, no psychological monologue`
- 检验点：风格一句话是否成立；镜头语言、场面调度、剪辑节奏是否可辨；Negative prompt 是否守住禁区。
