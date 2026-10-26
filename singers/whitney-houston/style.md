# Whitney Houston — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop and R&B vocal in the style of Whitney Houston: powerful gospel-trained soprano, crystalline diction, effortless melisma, soaring sustained high notes, tender verses exploding into triumphant choruses, warmth inside power`
- ZH: 休斯顿风格：福音训练出的强力女高音，清澈咬字，毫不费力的转音，高亢延持的高音，温柔主歌炸裂为胜利式副歌，力量中有温暖。

## (2) 音色与音域

- 音色：明亮强力的女高音，高音区圆润开放；主音色为福音式胸声，辅音色为轻柔气声；禁音色为沙哑撕裂与含混低语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑极深，起音平稳滑入，收尾拖长渐弱；颤音自然而宽；《I Will Always Love You》以无伴奏起音与高音延持为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，元音饱满、辅音轻；重音落在情感词上；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 节奏：流行节拍上略拖后，副歌常以长音推进；即兴以转音与加花为主，现场版常拉长高音。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 强力抒情歌与福音式副歌（如《I Will Always Love You》一类）
- 温柔主歌接高亢副歌的能量对照
- 转音与加花的即兴点缀
- 无伴奏起音与高音延持
- 不该唱：`No raspy growl, no mumbled diction, no thin head voice, no flat monotone delivery, no operatic coloratura`
- Negative prompt: `No raspy growl, no mumbled diction, no thin head voice, no flat monotone delivery, no operatic coloratura`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `Sing in the style of Whitney Houston, a song about a cup of coffee left on a windowsill in a modern city. Powerful gospel-trained soprano, crystalline diction, effortless melisma, tender verses exploding into triumphant choruses, warmth inside power.`
- 中文对照：休斯顿风格：唱一首关于窗台上咖啡的歌。强力福音女高音，清澈咬字，毫不费力的转音，温柔主歌炸裂为胜利式副歌，力量中有温暖。
- Negative: `No raspy growl, no mumbled diction, no thin head voice, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
