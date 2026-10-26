# Freddie Mercury — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Rock vocal in the style of Freddie Mercury: powerful tenor, operatic range, theatrical drama, fearless falsetto, rock anthem climax, camp grandeur`
- ZH: 默丘里风格：有力的男高音，歌剧般的音域，戏剧性的张力，无畏的假声，摇滚圣歌的高潮，华丽的宏大。

## (2) 音色与音域

- 男高音有力，音域极宽，音色带歌剧与摇滚的双重质感；主音色为有力的摇滚男高音，辅音色为假声的高音，禁音色为气声耳语与单薄的头声。`artifact`

## (3) 唱腔与发声技法

- 发声：胸声与假声切换自如，起音果断，收尾或渐弱或辉煌；唱腔：歌剧式高音，颤音适中，装饰音丰富。`artifact`

## (4) 咬字与语言

- 英语咬字清晰，带戏剧性的重音；换气点随乐句呼吸。`artifact`

## (5) 节奏与即兴

- 戏剧节奏，乐句随剧情起伏；慢板更沉，快板更烈。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：华丽摇滚史诗（《Bohemian Rhapsody》）、体育场圣歌（《We Are the Champions》）、灵魂式抒情（《Somebody to Love》）、歌剧式多声部段落与假声高音、现场互动的呼喊段落。
- 不该唱：`No breathy whisper, no thin head voice, no straight stiff phrasing, no mumbled diction, no small-scale intimacy`
- Negative prompt: `No breathy whisper, no thin head voice, no straight stiff phrasing, no mumbled diction, no small-scale intimacy`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Freddie Mercury, a song about a night-shift worker buying coffee at a convenience store. Powerful tenor, operatic range, theatrical drama, fearless falsetto, rock anthem climax, rock band and choir.`
- 中文对照：默丘里风格：唱一首关于夜班工人在便利店买咖啡的歌。有力的男高音，歌剧般的音域，戏剧性的张力，无畏的假声，摇滚圣歌的高潮，摇滚乐队与合唱伴奏。
- Negative: `No breathy whisper, no thin head voice, no straight stiff phrasing, no mumbled diction, no small-scale intimacy`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
