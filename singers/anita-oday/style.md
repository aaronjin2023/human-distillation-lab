# Anita O'Day — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz vocal in the style of Anita O'Day: cool swinging alto, bebop phrasing, crisp diction, rhythmic daring, dry wit`
- ZH: 奥黛风格：冷静摇摆的女低音，比波普式乐句，咬字干脆，节奏大胆，冷幽默。

## (2) 音色与音域

- 女低音冷静，音色带干脆的颗粒感；主音色为冷静的爵士女低音，辅音色为拟声的乐器感，禁音色为甜美的圆润与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：胸声为主，起音干脆，收尾多戛然而止；唱腔：比波普式乐句，装饰音精确，颤音稀疏。`artifact`

## (4) 咬字与语言

- 美式英语咬字干脆，辅音清晰；换气点随乐句呼吸。`artifact`

## (5) 节奏与即兴

- 节奏大胆，乐句如比波普独奏；摇摆感强，拖拍与抢拍并存。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：比波普标准曲（《Sweet Georgia Brown》《Tea for Two》《Honeysuckle Rose》）、与大乐队合作的摇摆曲、快速拟声段落、冷爵士抒情曲、节奏大胆的即兴段落。
- 不该唱：`No sweet rounded tone, no breathy whisper, no straight stiff phrasing, no operatic vibrato, no shouted climax`
- Negative prompt: `No sweet rounded tone, no breathy whisper, no straight stiff phrasing, no operatic vibrato, no shouted climax`

## (7) 测试提示词示例（现代题材：手机没电）

- Prompt: `Sing in the style of Anita O'Day, a song about a phone running out of battery on a long journey home. Cool swinging alto, bebop phrasing, crisp diction, rhythmic daring, dry wit, big band.`
- 中文对照：奥黛风格：唱一首关于长途回家路上手机没电的歌。冷静摇摆的女低音，比波普式乐句，咬字干脆，节奏大胆，冷幽默，大乐队伴奏。
- Negative: `No sweet rounded tone, no breathy whisper, no straight stiff phrasing, no operatic vibrato, no shouted climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
