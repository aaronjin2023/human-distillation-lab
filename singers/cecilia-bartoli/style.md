# Cecilia Bartoli — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Coloratura mezzo-soprano in the style of Cecilia Bartoli: agile fiery mezzo, dazzling coloratura, Rossinian sparkle, Baroque revival energy, dramatic temperament`
- ZH: 芭托莉风格：灵活火热的花腔女中音，花腔耀眼，罗西尼式的闪烁，巴洛克复兴的能量，戏剧性的气质。

## (2) 音色与音域

- 花腔女中音，音色灵活火热；主音色为火热的花腔女中音，辅音色为弱音的轻盈，禁音色为沉重的戏剧音色与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息灵活，起音锋利，收尾多渐弱或跳音；唱腔：花腔跑动极快而清晰，跳音与颤音结合，装饰音丰富。`artifact`

## (4) 咬字与语言

- 意大利语咬字敏捷，辅音锋利；换气点藏在花腔间隙。`artifact`

## (5) 节奏与即兴

- 速度明快，节奏锋利；花腔段落节奏精确，慢板更沉。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：罗西尼花腔女中音（罗西娜、《灰姑娘》安杰丽娜）、巴洛克歌剧（亨德尔、维瓦尔第）、莫扎特女中音角色、音乐会咏叹调、古乐器伴奏下的花腔段落。
- 不该唱：`No heavy dramatic weight, no breathy pop tone, no slow legato wash, no jazz scat, no thin head voice`
- Negative prompt: `No heavy dramatic weight, no breathy pop tone, no slow legato wash, no jazz scat, no thin head voice`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Cecilia Bartoli, a song about a woman buying coffee at a convenience store late at night. Agile fiery mezzo, dazzling coloratura, Rossinian sparkle, dramatic temperament, light Baroque orchestra.`
- 中文对照：芭托莉风格：唱一首关于深夜在便利店买咖啡的女人的歌。灵活火热的花腔女中音，花腔耀眼，罗西尼式的闪烁，戏剧性的气质，轻型巴洛克乐队伴奏。
- Negative: `No heavy dramatic weight, no breathy pop tone, no slow legato wash, no jazz scat, no thin head voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
