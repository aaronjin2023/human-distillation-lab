# Louis Armstrong — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz vocal in the style of Louis Armstrong: gravelly warm voice, trumpet-like phrasing, behind-the-beat swing, scat invention, joyful growl`
- ZH: 阿姆斯特朗风格：沙哑温暖的嗓音，小号般的乐句，拖拍摇摆，拟声即兴，欢快的低吼。

## (2) 音色与音域

- 沙哑温暖，音色带颗粒感，如小号；主音色为沙哑温暖的爵士嗓音，辅音色为拟声的乐器感，禁音色为圆润的美声与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：胸声为主，起音带滑入，收尾多渐弱或低吼；唱腔：拟声唱法（scat），滑音与装饰音，小号式乐句。`artifact`

## (4) 咬字与语言

- 美式英语咬字松弛，口语化；辅音轻，元音带新奥尔良口音；换气点随乐句呼吸。`artifact`

## (5) 节奏与即兴

- 摇摆感强，拖在拍子后面；乐句如小号独奏，与乐队呼应。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：爵士标准曲（《What a Wonderful World》《Hello, Dolly!》）、新奥尔良爵士（《West End Blues》）、拟声即兴段落、与小号呼应的演唱段落、口语化叙事句式。
- 不该唱：`No smooth croon, no straight on-beat phrasing, no operatic vibrato, no sweet rounded tone, no clipped diction`
- Negative prompt: `No smooth croon, no straight on-beat phrasing, no operatic vibrato, no sweet rounded tone, no clipped diction`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Louis Armstrong, a song about a night-shift worker buying coffee at a convenience store. Gravelly warm voice, trumpet-like phrasing, behind-the-beat swing, scat invention, joyful growl, small jazz combo.`
- 中文对照：阿姆斯特朗风格：唱一首关于夜班工人在便利店买咖啡的歌。沙哑温暖的嗓音，小号般的乐句，拖拍摇摆，拟声即兴，欢快的低吼，小型爵士乐队伴奏。
- Negative: `No smooth croon, no straight on-beat phrasing, no operatic vibrato, no sweet rounded tone, no clipped diction`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
