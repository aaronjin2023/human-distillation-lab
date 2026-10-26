# Kyu Sakamoto — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Kayokyoku vocal in the style of Kyu Sakamoto: bright warm tenor, clear Japanese diction, gentle vibrato, upbeat optimism, whistling interlude, a song as a smile held back from tears rather than a lament`
- ZH: 坂本九风格：明亮温暖的男高音，清晰的日语咬字，轻柔颤音，昂扬的乐观，口哨间奏，歌如忍住眼泪的微笑而非哀诉。

## (2) 音色与音域

- 声部：男高音（tenor），常用中音区。
- 音色：主音色：明亮、温暖、富于亲和力的男高音；辅音色：口哨间奏；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域以中音区为叙事主场，高音区明亮收束。

## (3) 唱腔与发声技法

- 明亮演唱：音色明亮大方，是声口标记。`verbatim`
- 轻柔颤音：颤音窄而均匀，句尾轻现。`impression`
- 日语咬字：辅音清晰，元音饱满，重音落在词义上。`impression`
- 口哨间奏：《昂首向前走》的口哨间奏是声口标记。`artifact`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：明亮音色本身就是乐观的距离感。`impression`
- 力度：中强力度为主，高潮处抬高，不煽情。`impression`
- 节奏：稳健的歌谣曲节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如微笑，换气在句间。`impression`
- 与伴奏的咬合：乐队只铺底，不抢人声。`impression`
- 情感递进：由平静到昂扬，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：明亮乐观的歌谣曲、口哨间奏的抒情、夜星与明天的叙事、忍住眼泪的微笑。
- 不该唱：No operatic roundness、no rock shouting、no sweet pop vibrato、no mumbled diction、no sentimental outburst。
- Negative prompt: `No operatic roundness, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`

## (7) 测试提示词示例（现代题材：唱一首关于黎明时分夜班工人吹着口哨回家的歌）

- Prompt: `Sing in the style of Kyu Sakamoto, a song about a night-shift worker whistling on the way home at dawn. Bright warm tenor, clear Japanese diction, gentle vibrato, upbeat optimism, whistling interlude, a song as a smile held back from tears.`
- 中文对照：明亮温暖的男高音，清晰的日语咬字，轻柔颤音，昂扬的乐观，口哨间奏，歌如忍住眼泪的微笑而非哀诉。 唱一首关于黎明时分夜班工人吹着口哨回家的歌。
- Negative: `No operatic roundness, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
