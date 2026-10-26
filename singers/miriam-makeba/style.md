# Miriam Makeba — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `World vocal in the style of Miriam Makeba: warm South African contralto, Xhosa click consonants, joyful dance rhythm, clear diction in Xhosa and English, call-and-response with chorus, celebration rather than lament`
- ZH: 米丽亚姆·玛凯巴风格：温暖的南非女中音，科萨语搭嘴音，欢快的舞曲节奏，科萨语与英语咬字清晰，与合唱队呼应，欢庆而非哀诉。

## (2) 音色与音域

- 声部：女中音（contralto），常用中音区。
- 音色：主音色：温暖、圆润、富于弹性的南非女中音；辅音色：科萨语搭嘴音的颗粒感；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域以中音区为叙事主场，高音区轻收。

## (3) 唱腔与发声技法

- 搭嘴音：科萨语的 click 辅音是声口标记，颗粒清晰。`verbatim`
- 呼应式演唱：主唱与合唱队一呼一应。`verbatim`
- 舞曲节奏：人声踩在节奏上，身体感强。`impression`
- 双语咬字：科萨语与英语切换自然，重音各归其位。`impression`
- 现场一次成形：现场录音少补录，欢庆感即真实。`impression`

## (4) 咬字与语言

- 音色即语言：温暖音色本身就是南非的欢庆与尊严。`impression`
- 力度：中强力度为主，欢庆时抬高，不煽情。`impression`
- 节奏：舞曲节拍，人声与打击乐咬合紧密。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如呼喊，句尾自然收束。`impression`
- 与伴奏的咬合：打击乐与合唱队构成呼应，人声居中。`impression`
- 情感递进：由欢庆到深情，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：南非舞曲与欢庆歌曲、科萨语搭嘴音歌曲、主唱与合唱队的呼应、思乡与爱情的双语抒情。
- 不该唱：No operatic roundness、no rock shouting、no sentimental outburst、no mumbled diction、no flat monotone delivery。
- Negative prompt: `No operatic roundness, no rock shouting, no sentimental outburst, no mumbled diction, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于夜市水果摊贩边卖边跳舞的歌）

- Prompt: `Sing in the style of Miriam Makeba, a song about a street vendor dancing while selling fruit at a night market. Warm South African contralto, Xhosa click consonants, joyful dance rhythm, clear diction, call-and-response with chorus, celebration.`
- 中文对照：温暖的南非女中音，科萨语搭嘴音，欢快的舞曲节奏，科萨语与英语咬字清晰，与合唱队呼应，欢庆而非哀诉。 唱一首关于夜市水果摊贩边卖边跳舞的歌。
- Negative: `No operatic roundness, no rock shouting, no sentimental outburst, no mumbled diction, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
