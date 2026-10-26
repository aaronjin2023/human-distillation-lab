# Caetano Veloso — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Tropicalia vocal in the style of Caetano Veloso: soft intimate tenor, conversational delivery, Brazilian Portuguese diction, bossa-nova phrasing with rock and avant-garde collage, gentle irony, poetry whispered rather than sung loud`
- ZH: 卡埃塔诺·维罗索风格：柔和亲密的男高音，口语化演唱，巴西葡语咬字，波萨诺瓦乐句与摇滚先锋拼贴，温和的反讽，诗是耳语而非高唱。

## (2) 音色与音域

- 声部：男高音（tenor），常用中音区。
- 音色：主音色：柔和、亲密、富于弹性的男高音；辅音色：口语化的低语；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域以中音区为叙事主场，高音区轻收。

## (3) 唱腔与发声技法

- 口语化演唱：像说话一样唱歌，旋律服从葡语重音。`verbatim`
- 波萨诺瓦乐句：轻盈的桑巴节奏型，人声拖拍。`impression`
- 拼贴式编曲：摇滚、先锋与巴西传统并置，人声居中。`artifact`
- 温和反讽：以轻柔口吻唱尖锐内容。`impression`
- 葡语咬字：辅音轻柔，元音饱满，重音落在词义上。`impression`

## (4) 咬字与语言

- 音色即语言：柔和音色本身就是反讽的距离感。`impression`
- 力度：弱力度为主，全曲几乎不抬高潮，克制是反讽的底色。`impression`
- 节奏：轻盈的桑巴节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如谈话，换气在句间。`impression`
- 与伴奏的咬合：吉他与键盘只铺底，不抢歌词。`impression`
- 情感递进：由低语到倾诉，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：热带主义拼贴歌曲、圣保罗城市叙事、波萨诺瓦乐句的诗性演唱、温和反讽的民谣。
- 不该唱：No operatic roundness、no rock shouting、no sentimental outburst、no mumbled diction、no wide vibrato。
- Negative prompt: `No operatic roundness, no rock shouting, no sentimental outburst, no mumbled diction, no wide vibrato`

## (7) 测试提示词示例（现代题材：唱一首关于晚高峰地铁站台上弹吉他的街头艺人的歌）

- Prompt: `Sing in the style of Caetano Veloso, a song about a street musician playing guitar on a subway platform at rush hour. Soft intimate tenor, conversational delivery, Brazilian Portuguese diction, bossa-nova phrasing with rock collage, gentle irony, poetry whispered rather than sung loud.`
- 中文对照：柔和亲密的男高音，口语化演唱，巴西葡语咬字，波萨诺瓦乐句与摇滚先锋拼贴，温和的反讽，诗是耳语而非高唱。 唱一首关于晚高峰地铁站台上弹吉他的街头艺人的歌。
- Negative: `No operatic roundness, no rock shouting, no sentimental outburst, no mumbled diction, no wide vibrato`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
