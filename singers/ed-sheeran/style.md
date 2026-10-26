# Ed Sheeran — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop vocal in the style of Ed Sheeran: warm conversational tenor, loop-pedal rhythmic phrasing, intimate ballad delivery, rapid-fire verses against soaring choruses, sincerity over polish`
- ZH: 希兰风格：温暖口语化的男高音，循环踏板式的节奏乐句，亲密的抒情演唱，快嘴主歌对照高扬副歌，真诚压倒精致。

## (2) 音色与音域

- 音色：温暖的男高音，中音区最有叙事感；主音色为口语化胸声，辅音色为假声点缀；禁音色为沙哑撕裂与歌剧式颤音。`artifact`

## (3) 唱腔与发声技法

- 发声：气息平稳，起音如说话般直接，收尾拖长渐弱；真假声切换平滑；《Thinking Out Loud》以平稳连音为标记，《Shape of You》以节奏型乐句为标记。`artifact`

## (4) 咬字与语言

- 咬字：英式发音清晰，辅音干脆；快嘴段落咬字仍清晰；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 节奏：流行节拍上稳而带摇摆感，快嘴段落如说唱；即兴以循环踏板叠加人声与吉他为主，现场版常拉长尾段。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 吉他伴奏的抒情歌与节奏型流行歌曲（如《Thinking Out Loud》一类）
- 快嘴主歌接高扬副歌的对照
- 循环踏板式的人声叠加
- 亲密独白式的叙事演唱
- 不该唱：`No operatic vibrato, no raspy shouting, no mumbled diction, no ornate melisma, no flat monotone delivery`
- Negative prompt: `No operatic vibrato, no raspy shouting, no mumbled diction, no ornate melisma, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `Sing in the style of Ed Sheeran, a song about a cup of coffee left on a windowsill in a modern city. Warm conversational tenor, loop-pedal rhythmic phrasing, intimate ballad delivery, rapid-fire verses against soaring choruses.`
- 中文对照：希兰风格：唱一首关于窗台上咖啡的歌。温暖口语化的男高音，循环踏板式节奏乐句，亲密的抒情演唱，快嘴主歌对照高扬副歌，真诚压倒精致。
- Negative: `No operatic vibrato, no raspy shouting, no mumbled diction, no ornate melisma`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
