# Diana Ross — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul and pop vocal in the style of Diana Ross: light silky soprano, breathy intimacy, precise diction, graceful melisma, glamorous ease, tenderness against disco lift`
- ZH: 罗斯风格：轻盈丝滑的女高音，气声亲密感，咬字精准，优雅的转音，华丽的轻松感，温柔对照迪斯科上扬。

## (2) 音色与音域

- 音色：轻盈丝滑的女高音，中高音区清澈；主音色为气声包裹的胸声，辅音色为假声点缀；禁音色为沙哑嘶吼与强力呐喊。`artifact`

## (3) 唱腔与发声技法

- 发声：气息轻柔，起音以气声滑入，收尾拖长渐弱；颤音自然而窄；《Ain't No Mountain High Enough》以层层推进的副歌为标记，《Endless Love》以对唱的亲密感为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，辅音轻、元音亮；重音落在情感词上；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 节奏：灵魂与迪斯科节拍上略拖后，乐句优雅起伏；即兴以转音与尾段加花为主。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 灵魂流行歌与迪斯科歌曲（如《Upside Down》一类）
- 气声亲密的抒情演唱（如《Endless Love》）
- 层层推进的副歌（如《Ain't No Mountain High Enough》）
- 优雅转音与轻盈高音
- 不该唱：`No raspy shouting, no operatic coloratura, no mumbled diction, no harsh distortion, no flat monotone delivery`
- Negative prompt: `No raspy shouting, no operatic coloratura, no mumbled diction, no harsh distortion, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：深夜加班的办公室）

- Prompt: `Sing in the style of Diana Ross, a song about working overtime in an office late at night. Light silky soprano, breathy intimacy, precise diction, graceful melisma, glamorous ease, tenderness against disco lift.`
- 中文对照：罗斯风格：唱一首关于深夜加班办公室的歌。轻盈丝滑的女高音，气声亲密感，咬字精准，优雅的转音，华丽的轻松感，温柔对照迪斯科上扬。
- Negative: `No raspy shouting, no operatic coloratura, no mumbled diction, no harsh distortion`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
