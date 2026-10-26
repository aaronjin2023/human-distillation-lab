# Céline Dion — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Adult contemporary vocal in the style of Céline Dion: powerful French-Canadian soprano, crystalline diction in English and French, soaring sustained high notes, tender verses rising to triumphant choruses, sincerity without irony`
- ZH: 迪翁风格：强力的法裔加拿大女高音，英法双语清澈咬字，高亢延持的高音，温柔主歌升至胜利式副歌，真诚而不反讽。

## (2) 音色与音域

- 音色：明亮强力的女高音，高音区圆润开放；主音色为抒情胸声，辅音色为轻柔气声；禁音色为沙哑撕裂与含混低语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑极深，起音平稳，收尾拖长渐弱；颤音自然而宽；《My Heart Will Go On》以长音推进与高音延持为标记。`artifact`

## (4) 咬字与语言

- 咬字：英语与法语双语，元音饱满、辅音清晰；法语演唱时鼻音与连诵自然；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 节奏：抒情节拍上略拖后，副歌以长音推进；即兴以加花与高音延持为主，现场版常拉长尾段。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 强力抒情歌与电影主题曲（如《My Heart Will Go On》一类）
- 温柔主歌接胜利副歌的能量对照
- 英法双语的抒情演唱
- 高音延持与长音推进
- 不该唱：`No raspy growl, no mumbled diction, no detached irony, no operatic coloratura, no flat monotone delivery`
- Negative prompt: `No raspy growl, no mumbled diction, no detached irony, no operatic coloratura, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：凌晨的机场）

- Prompt: `Sing in the style of Céline Dion, a song about waiting at an airport in the early morning. Powerful French-Canadian soprano, crystalline diction, soaring sustained high notes, tender verses rising to triumphant choruses, sincerity without irony.`
- 中文对照：迪翁风格：唱一首关于凌晨机场等候的歌。强力法裔加拿大女高音，清澈咬字，高亢延持的高音，温柔主歌升至胜利式副歌，真诚而不反讽。
- Negative: `No raspy growl, no mumbled diction, no detached irony, no operatic coloratura`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
