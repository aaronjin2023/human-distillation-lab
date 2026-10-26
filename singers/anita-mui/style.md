# Anita Mui — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Cantopop vocal in the style of Anita Mui: husky contralto, theatrical delivery, precise Cantonese diction, dramatic phrasing, cabaret glamour with street-wise grit, a song as a stage play rather than a melody`
- ZH: 梅艳芳风格：沙哑的女中音，戏剧化演唱，精准的粤语咬字，戏剧化乐句，歌舞厅华丽与街头韧劲并存，歌如舞台剧而非旋律。

## (2) 音色与音域

- 声部：女中音（contralto），常用中低音区。
- 音色：主音色：沙哑、富于弹性、辨识度极高的女中音；辅音色：戏剧化的高音；禁音色：甜腻颤音、美声式圆润、摇滚喊腔。音域以中低音区为叙事主场，高音区以戏剧攀升。

## (3) 唱腔与发声技法

- 沙哑声口：沙哑是声口标记，辨识度极高。`verbatim`
- 戏剧化乐句：乐句如舞台台词，停顿即意义。`impression`
- 粤语咬字：辅音清晰，元音饱满，重音落在词义上。`impression`
- 舞台感：现场演唱带走位与造型，声音即舞台。`artifact`
- 换气藏于句间：长乐句气息平稳，换气点在戏剧停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：沙哑音色本身就是舞台的距离感。`impression`
- 力度：中强力度为主，高潮处抬高，不煽情。`impression`
- 节奏：稳健的流行节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如台词，换气在句间。`impression`
- 与伴奏的咬合：乐队只铺底，不抢人声。`impression`
- 情感递进：由平静到戏剧，层层推进。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：女性主题的粤语流行、戏剧化舞台歌曲、夕阳与故人的抒情、沙哑声口的叙事。
- 不该唱：No sweet pop vibrato、no operatic roundness、no mumbled diction、no rock shouting、no flat monotone delivery。
- Negative prompt: `No sweet pop vibrato, no operatic roundness, no mumbled diction, no rock shouting, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于午夜最后一次关上花店门的女人的歌）

- Prompt: `Sing in the style of Anita Mui, a song about a woman closing her flower shop for the last time at midnight. Husky contralto, theatrical delivery, precise Cantonese diction, dramatic phrasing, cabaret glamour with street-wise grit, a song as a stage play.`
- 中文对照：沙哑的女中音，戏剧化演唱，精准的粤语咬字，戏剧化乐句，歌舞厅华丽与街头韧劲并存，歌如舞台剧而非旋律。 唱一首关于午夜最后一次关上花店门的女人的歌。
- Negative: `No sweet pop vibrato, no operatic roundness, no mumbled diction, no rock shouting, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
