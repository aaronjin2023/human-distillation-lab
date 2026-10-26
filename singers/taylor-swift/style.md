# Taylor Swift — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop vocal in the style of Taylor Swift: clear conversational soprano, diary-like diction, catchy melodic hooks, intimate verses building into anthemic choruses, storytelling in every line, sincerity over vocal display`
- ZH: 斯威夫特风格：清澈口语化的女高音，日记式咬字，抓耳的旋律钩子，亲密主歌 渐强至颂歌式副歌，每句都在讲故事，真诚压倒炫技。

## (2) 音色与音域

- 音色：清澈明亮的女高音，中音区最有叙事感；主音色为口语化胸声，辅音色为气声；禁音色为沙哑撕裂与歌剧式颤音。`artifact`

## (3) 唱腔与发声技法

- 发声：气息平稳，起音如说话般直接，收尾短促或拖长；颤音少；《Love Story》以叙事乐句为标记，《Shake It Off》以轻快的跳跃感为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，辅音干脆；重音落在叙事关键词上；换气点留在句尾。`artifact`

## (5) 节奏与即兴

- 节奏：流行节拍上稳而带摇摆感，副歌常以钩子乐句进入；即兴少，以词义与编曲制造变化。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 叙事流行歌与日记式抒情歌曲（如《Love Story》一类）
- 口语化主歌接颂歌式副歌的对照
- 抓耳的旋律钩子与副歌重复
- 乡村与流行交界的叙事演唱
- 不该唱：`No operatic vibrato, no raspy growl, no mumbled diction, no ornate melisma, no flat monotone delivery`
- Negative prompt: `No operatic vibrato, no raspy growl, no mumbled diction, no ornate melisma, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `Sing in the style of Taylor Swift, a song about riding a shared bicycle through a modern city at night. Clear conversational soprano, diary-like diction, catchy melodic hooks, intimate verses building into anthemic choruses, storytelling in every line.`
- 中文对照：斯威夫特风格：唱一首关于深夜骑共享单车的歌。清澈口语化的女高音，日记式咬字，抓耳的旋律钩子，亲密主歌 渐强至颂歌式副歌，每句都在讲故事。
- Negative: `No operatic vibrato, no raspy growl, no mumbled diction, no ornate melisma`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
