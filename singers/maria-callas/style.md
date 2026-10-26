# Maria Callas — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Dramatic soprano in the style of Maria Callas: dark-edged soprano, searing chest voice, fearless coloratura, dramatic phrasing, words first, beauty second`
- ZH: 卡拉斯风格：带暗色边缘的戏剧女高音，胸声灼热，花腔无畏，戏剧化乐句，词义先于音色之美。

## (2) 音色与音域

- 女高音音色带暗色边缘，胸声有力，高音穿透，花腔锋利；主音色为戏剧性的暗亮女高音，辅音色为弱音的私语，禁音色为甜美的圆润轻声。`artifact`

## (3) 唱腔与发声技法

- 发声：胸声与头声对比强烈，起音果断，收尾或渐弱或戛然而止；唱腔：美声花腔与戏剧力度并存，颤音快而窄，弱音（pianissimo）与爆发对比极端。`artifact`

## (4) 咬字与语言

- 意大利语咬字如念白，重音落在词义上，宣叙调式处理；辅音锋利，元音随情绪变色；换气点即戏剧停顿。`artifact`

## (5) 节奏与即兴

- rubato 戏剧化，乐句呼吸长，停顿制造张力；速度随剧情起伏，慢板更慢，快板更急。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：美声歌剧女主角（诺尔玛、露琪亚）、威尔第与普契尼悲剧女主角（托斯卡、薇奥莱塔）、贝里尼长线条咏叹调（《圣洁的女神》）、现场录音中的戏剧高潮与弱音段落、宣叙调与咏叹调的对照。
- 不该唱：`No sweet rounded tone, no even pretty phrasing, no soft whisper, no detached coloratura, no light soubrette charm`
- Negative prompt: `No sweet rounded tone, no even pretty phrasing, no soft whisper, no detached coloratura, no light soubrette charm`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Maria Callas, a song about a woman buying coffee at a convenience store late at night. Dark-edged soprano, searing chest voice, dramatic phrasing, words first, long line with sudden pianissimo, small orchestra.`
- 中文对照：卡拉斯风格：唱一首关于深夜在便利店买咖啡的女人的歌。带暗色边缘的女高音，胸声灼热，戏剧化乐句，词义先行，长线条中突然出现弱音，小型管弦乐伴奏。
- Negative: `No sweet rounded tone, no even pretty phrasing, no soft whisper, no detached coloratura, no light soubrette charm`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
