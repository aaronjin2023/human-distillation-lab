# Umm Kulthum — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Arabic classical vocal in the style of Umm Kulthum: powerful contralto, maqam microtones, long improvised ornamentation, tarab ecstasy, precise diction of classical Arabic poetry, orchestra of takht, a single line repeated and varied for an hour`
- ZH: 乌姆·库尔苏姆风格：有力的女中音，木卡姆微分音，长时即兴装饰，塔拉布狂喜，古典阿拉伯诗歌的精准咬字，塔赫特乐队伴奏，同一诗句反复变奏一小时。

## (2) 音色与音域

- 声部：女中音（contralto），音域宽。
- 音色：主音色：有力、温暖、富于穿透力的女中音；辅音色：微分音的细腻弯曲；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域宽，中音区最厚实，高音区以即兴装饰攀升。

## (3) 唱腔与发声技法

- 木卡姆微分音：四分之一音的弯曲精准，是声口标记。`verbatim`
- 长时即兴装饰：同一诗句反复变奏，每遍装饰不同。`verbatim`
- 塔拉布：以即兴召唤听众的狂喜状态。`impression`
- 古典诗歌咬字：阿拉伯语辅音与元音极清晰。`impression`
- 气息控制：长乐句一气呵成，换气极隐蔽。`impression`

## (4) 咬字与语言

- 音色即语言：有力音色本身就是塔拉布的召唤。`impression`
- 力度：由弱到强缓慢累积，高潮在长时延展后到达。`impression`
- 节奏：自由节奏，乐队定拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如诗行，换气在句间。`impression`
- 与伴奏的咬合：塔赫特乐队铺底，人声在其上即兴。`impression`
- 情感递进：由低语到狂喜，缓慢累积，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：古典阿拉伯爱情诗、同一诗句的长时反复变奏、木卡姆微分音即兴、月度音乐会的塔拉布演唱。
- 不该唱：No operatic roundness、no rock shouting、no short pop structure、no mumbled diction、no one-shot climax。
- Negative prompt: `No operatic roundness, no rock shouting, no short pop structure, no mumbled diction, no one-shot climax`

## (7) 测试提示词示例（现代题材：唱一首关于黄昏时分老妇人在邮局等一封信的歌）

- Prompt: `Sing in the style of Umm Kulthum, a song about an old woman waiting for a letter at a post office at dusk. Powerful contralto, maqam microtones, long improvised ornamentation, tarab ecstasy, precise diction, takht orchestra, a single line repeated and varied.`
- 中文对照：有力的女中音，木卡姆微分音，长时即兴装饰，塔拉布狂喜，古典阿拉伯诗歌的精准咬字，塔赫特乐队伴奏，同一诗句反复变奏一小时。 唱一首关于黄昏时分老妇人在邮局等一封信的歌。
- Negative: `No operatic roundness, no rock shouting, no short pop structure, no mumbled diction, no one-shot climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
