# Lady Gaga — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop vocal in the style of Lady Gaga: theatrical mezzo-soprano, dramatic dynamic leaps, talk-sung verses against anthemic choruses, Raw belt and vulnerable whisper in one voice, reinvention in every era`
- ZH: Lady Gaga 风格：戏剧化女中音，力度戏剧性跳跃，说唱式主歌对照颂歌式副歌， 粗粝强音与脆弱耳语集于一身，每个时代都重塑自我。

## (2) 音色与音域

- 音色：戏剧化的女中音，可亮可暗；主音色为强力胸声，辅音色为耳语气声；禁音色为甜美圆润与一成不变的本色。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音直接或滑入，收尾拖长或戛然而止；颤音自然；《Bad Romance》以戏剧化副歌为标记，《Shallow》以耳语到强音的推进为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音清晰，辅音干脆；重音落在宣言词上；换气点制造悬念。`artifact`

## (5) 节奏与即兴

- 节奏：舞曲节拍上精准切分，说唱式主歌与旋律副歌对照；即兴以尾段加花为主，现场版常拉长高音。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 戏剧化舞曲与颂歌式流行歌曲（如《Bad Romance》一类）
- 耳语主歌接强音副歌的戏剧对照
- 电影抒情歌的脆弱与爆发（如《Shallow》）
- 每个时代重塑自我的风格切换
- 不该唱：`No sweet rounded tone, no operatic coloratura, no mumbled diction, no detached cool delivery throughout, no flat monotone delivery`
- Negative prompt: `No sweet rounded tone, no operatic coloratura, no mumbled diction, no detached cool delivery throughout, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Lady Gaga, a song about a man buying coffee at a convenience store late at night. Theatrical mezzo-soprano, dramatic dynamic leaps, talk-sung verses against anthemic choruses, Raw belt and vulnerable whisper in one voice.`
- 中文对照：Lady Gaga 风格：唱一首关于深夜便利店买咖啡的歌。戏剧化女中音，力度戏剧性跳跃，说唱式主歌对照颂歌式副歌，粗粝强音与脆弱耳语集于一身。
- Negative: `No sweet rounded tone, no operatic coloratura, no mumbled diction, no detached cool delivery throughout`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
