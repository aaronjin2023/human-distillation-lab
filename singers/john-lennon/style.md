# John Lennon — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Rock vocal in the style of John Lennon: Raw confessional tenor, nasal edge, conversational phrasing, sudden shifts from tenderness to anger, plain diction, minimal vibrato, voice close to the microphone`
- ZH: 列侬风格：坦白直率的男高音，鼻音锋利，口语化乐句，温柔与愤怒之间骤然切换，咬字平实，颤音极少，人声贴近话筒。

## (2) 音色与音域

- 音色：偏亮的男高音，带鼻音与轻微沙哑，中音区最有辨识度；主音色为直白坦率的胸声，辅音色为轻柔的气声（如《Imagine》主歌）；禁音色为圆润的美声与油滑的颤音。`artifact`

## (3) 唱腔与发声技法

- 发声：胸声为主，起音直接，收尾常戛然而止或拖一个短音；颤音窄而少，愤怒时用喊腔边缘；《Come Together》用含混的低声絮语，《Imagine》用平稳的连音。`artifact`

## (4) 咬字与语言

- 咬字：利物浦口音底色的英式发音，辅音清晰、元音扁平；重音落在词义上，歌词与旋律咬合紧密；换气点留在句尾，停顿即表态。`artifact`

## (5) 节奏与即兴

- 节奏：摇滚节拍上略拖后，副歌常抢拍推进；即兴少而精，以重复乐句加压为主，现场版常拉长尾句、加重尾音。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 坦白式叙事歌与反战、和平主题的直抒歌曲（如《Imagine》一类）
- 口语化摇滚乐句，短句重复、层层加压的副歌
- 温柔主歌接愤怒副歌的情绪对照
- 贴近话筒的亲密独白式演唱
- 不该唱：`No operatic vibrato, no sweet rounded crooning, no polished belting, no ornate melisma, no detached cool delivery`
- Negative prompt: `No operatic vibrato, no sweet rounded crooning, no polished belting, no ornate melisma, no detached cool delivery`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of John Lennon, a song about a man buying coffee at a convenience store late at night. Raw confessional tenor, nasal edge, conversational phrasing, plain diction, minimal vibrato, voice close to the microphone, tenderness turning suddenly to anger.`
- 中文对照：列侬风格：唱一首关于深夜便利店里买咖啡的男人的歌。坦白的男高音，鼻音锋利，口语化乐句，咬字平实，颤音极少，人声贴近话筒，温柔骤然转为愤怒。
- Negative: `No operatic vibrato, no sweet rounded crooning, no polished belting, no ornate melisma, no detached cool delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
