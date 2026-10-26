# Kurt Cobain — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Grunge vocal in the style of Kurt Cobain: Raw cracked tenor, quiet verses exploding into shredded choruses, mumbled intimacy against cathartic screaming, melody buried in noise, sincerity over polish`
- ZH: 柯本风格：粗糙开裂的男高音，安静主歌炸裂为撕碎的副歌，含混亲密对照宣泄式嘶喊，旋律埋在噪声里，真诚压倒精致。

## (2) 音色与音域

- 音色：粗糙沙哑的男高音，中音区带裂感；主音色为撕裂的胸声，辅音色为含混的气声低语；禁音色为圆润美声与精致的转音。`artifact`

## (3) 唱腔与发声技法

- 发声：胸声带撕裂边缘，起音含混、收尾常拖成嘶喊；颤音几乎不用；《Smells Like Teen Spirit》以安静—爆发对照为结构。`artifact`

## (4) 咬字与语言

- 咬字：美式发音含混，元音扁、辅音轻；重音落在情绪词上，词义常让位于音色；换气短促。`artifact`

## (5) 节奏与即兴

- 节奏：垃圾摇滚节拍上拖拍与抢拍并用，副歌常突然加速；即兴少，以音量对照制造变化，现场版常更粗粝直白。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 安静主歌接爆发副歌的垃圾摇滚歌曲（如《Smells Like Teen Spirit》一类）
- 含混低语与撕裂嘶喊的对照
- 旋律埋在失真吉他里的演唱
- 不插电式的脆弱亲密演唱
- 不该唱：`No polished belting, no sweet crooning, no operatic vibrato, no ornate melisma, no detached cool delivery`
- Negative prompt: `No polished belting, no sweet crooning, no operatic vibrato, no ornate melisma, no detached cool delivery`

## (7) 测试提示词示例（现代题材：深夜加班的办公室）

- Prompt: `Sing in the style of Kurt Cobain, a song about working overtime in an office late at night. Raw cracked tenor, quiet verses exploding into shredded choruses, mumbled intimacy against cathartic screaming, melody buried in noise.`
- 中文对照：柯本风格：唱一首关于深夜加班办公室的歌。粗糙开裂的男高音，安静主歌炸裂为撕碎副歌，含混亲密对照宣泄嘶喊，旋律埋在噪声里。
- Negative: `No polished belting, no sweet crooning, no operatic vibrato, no ornate melisma`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
