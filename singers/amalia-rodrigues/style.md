# Amália Rodrigues — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Fado vocal in the style of Amália Rodrigues: dark contralto, saudade lament, restrained vibrato, Portuguese guitar, precise Portuguese diction, dramatic pause, fate accepted rather than fought`
- ZH: 阿玛莉亚·罗德里格斯风格：暗沉的女中音，萨乌达德式的哀诉，克制的颤音，葡萄牙吉他，精准的葡语咬字，戏剧性停顿，接受命运而不反抗。

## (2) 音色与音域

- 声部：女中音（contralto），常用中低音区。
- 音色：主音色：暗沉、温暖、富于穿透力的女中音；辅音色：叹息般的气声；禁音色：明亮高音、摇滚喊腔、甜腻颤音。音域以中低音区为叙事主场，高音区以克制收束。

## (3) 唱腔与发声技法

- 萨乌达德式哀诉：以叹息而非哭诉表达宿命。`impression`
- 克制颤音：颤音窄而均匀，句尾轻现。`verbatim`
- 戏剧性停顿：停顿即意义，沉默也是语言。`impression`
- 葡语咬字：辅音与元音极清晰，重音落在词义上。`impression`
- 葡萄牙吉他：双吉他铺底，人声在其上叙事。`artifact`

## (4) 咬字与语言

- 音色即语言：暗沉音色本身就是宿命的距离感。`impression`
- 力度：中弱力度为主，高潮只抬半格，克制是法朵的底色。`impression`
- 节奏：自由节奏，吉他定拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如叹息，换气在句间。`impression`
- 与伴奏的咬合：双吉他只铺底，不抢人声。`impression`
- 情感递进：由平静到哀诉，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：宿命与大海的法朵、家园主题的抒情、萨乌达德式的叹息、葡萄牙吉他伴奏的叙事。
- 不该唱：No bright high notes、no rock shouting、no sentimental outburst、no wide operatic vibrato、no fast patter delivery。
- Negative prompt: `No bright high notes, no rock shouting, no sentimental outburst, no wide operatic vibrato, no fast patter delivery`

## (7) 测试提示词示例（现代题材：唱一首关于深夜渔港边渔民遗孀补网的歌）

- Prompt: `Sing in the style of Amália Rodrigues, a song about a fisherman's widow mending a net by the harbour at night. Dark contralto, saudade lament, restrained vibrato, Portuguese guitar, precise Portuguese diction, dramatic pause, fate accepted rather than fought.`
- 中文对照：暗沉的女中音，萨乌达德式的哀诉，克制的颤音，葡萄牙吉他，精准的葡语咬字，戏剧性停顿，接受命运而不反抗。 唱一首关于深夜渔港边渔民遗孀补网的歌。
- Negative: `No bright high notes, no rock shouting, no sentimental outburst, no wide operatic vibrato, no fast patter delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
