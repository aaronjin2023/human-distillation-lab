# David Bowie — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Rock vocal in the style of David Bowie: theatrical chameleon tenor, shifting personas, clipped British diction, dramatic dynamic leaps, crooned intimacy against glam-rock swagger, alien and elegant at once`
- ZH: 鲍伊风格：戏剧化的变色龙男高音，身份不断切换，干脆的英式咬字，力度戏剧性跳跃，耳语式亲密对照华丽摇滚的派头，疏离而优雅。

## (2) 音色与音域

- 音色：多变男高音，可亮可暗、可冷可热；主音色为戏剧化的胸声，辅音色为假声与气声；禁音色为一成不变的“本色”与粗粝的蓝调嘶吼。`artifact`

## (3) 唱腔与发声技法

- 发声：按角色换发声方式，起音干脆或滑入皆可，收尾常带戏剧停顿；颤音克制；《Heroes》以渐强推进，《Life on Mars?》以钢琴式乐句起伏。`artifact`

## (4) 咬字与语言

- 咬字：英式发音清晰，辅音干脆，元音收紧；歌词如台词，重音落在意象词上；换气点制造悬念。`artifact`

## (5) 节奏与即兴

- 节奏：摇滚节拍上切分与停顿并用，副歌常以出其不意的重音进入；即兴少，以编曲与角色切换制造变化。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 戏剧化叙事歌与科幻、疏离主题的歌曲（如《Space Oddity》一类）
- 华丽摇滚的派头式副歌与戏剧性力度跳跃
- 耳语式亲密主歌接开放副歌的对照
- 钢琴或合成器铺底上的角色化演唱
- 不该唱：`No bluesy rasp, no mumbled delivery, no one-register monotony, no earnest folk plainness, no operatic vibrato`
- Negative prompt: `No bluesy rasp, no mumbled delivery, no one-register monotony, no earnest folk plainness, no operatic vibrato`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `Sing in the style of David Bowie, a song about a cup of coffee left on a windowsill in a modern city. Theatrical tenor, clipped British diction, dramatic dynamic leaps, crooned intimacy against glam-rock swagger, alien and elegant.`
- 中文对照：鲍伊风格：唱一首关于窗台上咖啡的歌。戏剧化男高音，干脆的英式咬字，力度戏剧性跳跃，耳语式亲密对照华丽摇滚派头，疏离而优雅。
- Negative: `No bluesy rasp, no mumbled delivery, no one-register monotony, no earnest folk plainness`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
