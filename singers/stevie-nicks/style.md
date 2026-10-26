# Stevie Nicks — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Rock vocal in the style of Stevie Nicks: husky mystical contralto, breathy phrasing, long sustained notes, witchy vibrato, intimate verses building into soaring choruses, shawl-and-moonlight storytelling`
- ZH: 尼克斯风格：沙哑神秘的女低音，气声乐句，长音延持，女巫式颤音，亲密主歌 渐强至高扬副歌，披巾与月光般的叙事。

## (2) 音色与音域

- 音色：沙哑而带雾感的女低音，中低音区最有辨识度；主音色为气声包裹的胸声，辅音色为高音区的清亮假声；禁音色为甜美圆润与学院式花腔。`artifact`

## (3) 唱腔与发声技法

- 发声：气息绵长，起音以气声滑入，收尾拖长渐弱；颤音宽而慢，是声口标记；《Rhiannon》以长音与颤音营造神秘感。`artifact`

## (4) 咬字与语言

- 咬字：美式发音，元音拉长、辅音轻；重音落在意象词上；换气点长，气口即氛围。`artifact`

## (5) 节奏与即兴

- 节奏：摇滚节拍上拖拍，乐句如波浪起伏；即兴以长音延持与尾段重复为主，现场版常拉长尾句。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 神秘叙事歌与女性、月光、命运主题的歌曲（如《Rhiannon》《Landslide》一类）
- 气声主歌接高扬副歌的波浪式推进
- 长音延持与宽颤音的氛围营造
- 民谣摇滚式的亲密独白
- 不该唱：`No sweet rounded pop tone, no operatic coloratura, no clipped staccato phrasing, no harsh shouting, no flat monotone delivery`
- Negative prompt: `No sweet rounded pop tone, no operatic coloratura, no clipped staccato phrasing, no harsh shouting, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：阳台上的绿植）

- Prompt: `Sing in the style of Stevie Nicks, a song about plants growing on a balcony in a modern city. Husky mystical contralto, breathy phrasing, long sustained notes, witchy vibrato, intimate verses building into soaring choruses.`
- 中文对照：尼克斯风格：唱一首关于阳台绿植的歌。沙哑神秘的女低音，气声乐句，长音延持，女巫式颤音，亲密主歌 渐强至高扬副歌。
- Negative: `No sweet rounded pop tone, no operatic coloratura, no clipped staccato phrasing, no harsh shouting`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
