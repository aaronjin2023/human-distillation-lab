# Madonna — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop vocal in the style of Madonna: cool detached alto, talk-sung verses, precise rhythmic diction, whispered intimacy against defiant choruses, reinvention in every era, provocation delivered deadpan`
- ZH: 麦当娜风格：冷峻疏离的女低音，说唱式主歌，精准的节奏咬字，耳语亲密对照挑衅副歌，每个时代都重塑自我，挑衅以面无表情的方式送出。

## (2) 音色与音域

- 音色：冷峻的女低音，中音区带鼻音；主音色为说唱式胸声，辅音色为耳语气声；禁音色为甜美圆润与歌剧式颤音。`artifact`

## (3) 唱腔与发声技法

- 发声：气息平稳，起音直接，收尾短促；颤音极少；《Vogue》以说唱式乐句为标记，《Like a Virgin》以轻快的跳跃感为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音清晰，辅音干脆；重音落在节奏点与挑衅词上；换气短促。`artifact`

## (5) 节奏与即兴

- 节奏：舞曲节拍上精准切分，说唱式主歌与旋律副歌对照；即兴少，以编曲与形象切换制造变化。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 舞曲与说唱式主歌接旋律副歌的流行歌曲（如《Vogue》一类）
- 冷峻疏离的挑衅式演唱
- 耳语亲密与副歌宣言的对照
- 每个时代重塑自我的风格切换
- 不该唱：`No sweet rounded tone, no operatic vibrato, no earnest ballad sincerity throughout, no mumbled diction, no bluesy rasp`
- Negative prompt: `No sweet rounded tone, no operatic vibrato, no earnest ballad sincerity throughout, no mumbled diction, no bluesy rasp`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `Sing in the style of Madonna, a song about riding a shared bicycle through a modern city at night. Cool detached alto, talk-sung verses, precise rhythmic diction, whispered intimacy against defiant choruses, provocation delivered deadpan.`
- 中文对照：麦当娜风格：唱一首关于深夜骑共享单车的歌。冷峻疏离的女低音，说唱式主歌，精准的节奏咬字，耳语亲密对照挑衅副歌，挑衅以面无表情送出。
- Negative: `No sweet rounded tone, no operatic vibrato, no earnest ballad sincerity throughout, no mumbled diction`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
