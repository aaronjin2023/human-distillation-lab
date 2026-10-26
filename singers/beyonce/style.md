# Beyoncé — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop and R&B vocal in the style of Beyoncé: powerful agile mezzo-soprano, razor-sharp diction, intricate melisma, commanding belt against breathy intimacy, precision choreography in every phrase, regal and relentless`
- ZH: 碧昂丝风格：强力敏捷的女中音，刀锋般精准的咬字，复杂的转音，命令式强音对照气声亲密，每句都如编舞般精准，威严而不懈。

## (2) 音色与音域

- 音色：强力明亮的女中音，高音区开放有力；主音色为命令式胸声，辅音色为气声与假声；禁音色为含混低语与甜美圆润。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑极深，起音干脆有力，收尾短促或拖长；颤音自然；转音复杂而精准，《Crazy in Love》以号角式副歌为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，辅音干脆、元音亮；重音落在节奏点与宣言词上；换气短促精准。`artifact`

## (5) 节奏与即兴

- 节奏：R&B 节拍上精准切分，乐句如编舞般卡点；即兴以转音与尾段加花为主，现场版常拉长高音。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 强力 R&B 舞曲与宣言式流行歌曲（如《Crazy in Love》一类）
- 命令式强音与气声亲密的对照
- 复杂转音与精准卡点的乐句
- 抒情高音歌（如《Halo》一类）
- 不该唱：`No mumbled diction, no thin head voice, no flat monotone delivery, no operatic coloratura, no loose off-beat phrasing`
- Negative prompt: `No mumbled diction, no thin head voice, no flat monotone delivery, no operatic coloratura, no loose off-beat phrasing`

## (7) 测试提示词示例（现代题材：深夜加班的办公室）

- Prompt: `Sing in the style of Beyoncé, a song about working overtime in an office late at night. Powerful agile mezzo-soprano, razor-sharp diction, intricate melisma, commanding belt against breathy intimacy, precision in every phrase.`
- 中文对照：碧昂丝风格：唱一首关于深夜加班办公室的歌。强力敏捷的女中音，刀锋般精准的咬字，复杂的转音，命令式强音对照气声亲密，每句都精准如编舞。
- Negative: `No mumbled diction, no thin head voice, no flat monotone delivery, no operatic coloratura`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
