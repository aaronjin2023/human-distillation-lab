# Elvis Presley — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Rock vocal in the style of Elvis Presley: warm baritone-tenor, gospel fire, country hiccup, rockabilly swagger, intimate croon to full-throated shout`
- ZH: 普雷斯利风格：温暖的男中—男高音，福音的火焰，乡村的打嗝式唱腔，摇滚比利的派头，亲密的低吟到全力的喊叫。

## (2) 音色与音域

- 男中—男高音温暖，音色带福音与乡村的双重质感；主音色为温暖的摇滚男声，辅音色为福音式的高潮，禁音色为学院式的美声与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：胸声为主，起音带滑入，收尾或渐弱或喊叫；唱腔：乡村打嗝式装饰音（hiccup），福音式高潮，颤音适中。`artifact`

## (4) 咬字与语言

- 美式英语咬字带南方口音，口语化；换气点随乐句呼吸。`artifact`

## (5) 节奏与即兴

- 摇滚比利的摇摆，乐句如身体摆动；慢板更沉，快板更烈。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：摇滚与摇滚比利（《Jailhouse Rock》《Suspicious Minds》）、抒情情歌（《Can't Help Falling in Love》）、福音式高潮段落、现场演出的呼喊与互动段落、乡村打嗝式装饰音段落。
- 不该唱：`No operatic vibrato, no breathy whisper, no straight stiff phrasing, no jazz scat, no thin head voice`
- Negative prompt: `No operatic vibrato, no breathy whisper, no straight stiff phrasing, no jazz scat, no thin head voice`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `Sing in the style of Elvis Presley, a song about a small Yorkshire terrier sitting on a subway seat. Warm baritone-tenor, gospel fire, country hiccup, rockabilly swagger, intimate croon to full-throated shout, rock band.`
- 中文对照：普雷斯利风格：唱一首关于一只约克夏犬坐在地铁座位上的歌。温暖的男中—男高音，福音的火焰，乡村的打嗝式唱腔，摇滚比利的派头，亲密的低吟到全力的喊叫，摇滚乐队伴奏。
- Negative: `No operatic vibrato, no breathy whisper, no straight stiff phrasing, no jazz scat, no thin head voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
