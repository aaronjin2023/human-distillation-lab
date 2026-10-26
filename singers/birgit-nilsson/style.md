# Birgit Nilsson — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Dramatic soprano in the style of Birgit Nilsson: steely brilliant soprano, huge power over full orchestra, laser high notes, Wagnerian stamina, cool Nordic clarity`
- ZH: 尼尔森风格：钢铁般明亮的戏剧女高音，盖过整个乐队的力量，激光般的高音，瓦格纳式的耐力，北欧式的冷静清晰。

## (2) 音色与音域

- 戏剧女高音，音色钢亮，穿透力强，高音如激光；主音色为钢亮的戏剧女高音，辅音色为弱音的冷静，禁音色为轻飘的花腔与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息极长，胸声支撑，高音稳定，弱音仍带芯；唱腔：乐句宏大，颤音适中，装饰音克制。`artifact`

## (4) 咬字与语言

- 德语咬字硬朗清晰，元音集中；意大利语咬字同样清晰；换气点留在长乐句的呼吸处。`artifact`

## (5) 节奏与即兴

- 速度稳健，乐句宏大，耐力型长线条；高潮处不抢拍。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：瓦格纳女主角（布伦希尔德、伊索尔德）、施特劳斯戏剧女高音、普契尼《图兰朵》图兰朵、威尔第戏剧角色、瓦格纳乐剧长独白与爱之死段落。
- 不该唱：`No light coloratura flutter, no breathy intimacy, no soft crooning, no jazz swing, no small-scale lyricism`
- Negative prompt: `No light coloratura flutter, no breathy intimacy, no soft crooning, no jazz swing, no small-scale lyricism`

## (7) 测试提示词示例（现代题材：凌晨机场）

- Prompt: `Sing in the style of Birgit Nilsson, a song about a traveller waiting alone at an airport before dawn. Steely brilliant soprano, huge power, laser high notes, long Wagnerian line, cool Nordic clarity, full orchestra.`
- 中文对照：尼尔森风格：唱一首关于黎明前独自在机场等候的旅人的歌。钢铁般明亮的戏剧女高音，力量宏大，激光般的高音，瓦格纳式长线条，北欧式冷静清晰，管弦乐伴奏。
- Negative: `No light coloratura flutter, no breathy intimacy, no soft crooning, no jazz swing, no small-scale lyricism`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
