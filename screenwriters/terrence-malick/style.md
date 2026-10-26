# Terrence Malick — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Terrence Malick: poetic whispered voiceover, nature as the real protagonist, elliptical time, violence glimpsed through grass and light, dialogue sparse as prayer`
- ZH: 泰伦斯·马力克风格：诗意的低语旁白，自然是真正的主角，省略的时间，透过草与光瞥见的暴力，对白稀少如祈祷。

## (2) 结构：三幕 / 序列 / 节拍

- 诗性省略结构：三幕被打散成碎片，时间跳跃、场景并置，靠旁白与自然意象组织而非靠情节。第一幕立下人物与风景，第二幕让人物在风景中游荡、相爱、犯罪，第三幕在自然的注视之下收束——不是结局，而是消散。

## (3) 对话

- 对白极少：短句、低语、画外音，旁白是诗意的自问而非叙事。动作描写写自然：草、光、水、天空，自然本身就是人物。对话少，沉默多。

## (4) 人物弧光

- 主角多为局外人：逃犯、农工、士兵。弧光不是成长而是消散——人物在自然面前变得渺小，爱与暴力同样短暂。对手是自然与时间，人类只是过客。

## (5) 类型套路与创新

- 诗电影 / 剧情片 / 战争片。他遵守剧情片的人物与情感，但打破了“剧本必须情节完整”的成见：情节被打散，只留碎片与旁白。创新在自然即主角——剧本为风景留出篇幅。禁套路：几乎不用解释性对白，不写紧凑的悬念。

## (6) 该写什么 / 不该写什么

- 该写：诗意低语旁白与省略结构、自然即真正的主角、透过草与光瞥见的暴力、稀少如祈祷的对白。
- Negative prompt: `No explanatory dialogue, no tight suspense plotting, no fast cutting, no witty banter, no sentimental climax`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Terrence Malick, a small Yorkshire terrier sits on a subway seat while the city passes like weather. Poetic whispered voiceover, nature as the real protagonist, elliptical time. What is this life? The train moves on. The dog watches the light.`
- 中文对照：泰伦斯·马力克风格：一只约克夏犬坐在地铁座位上，城市如天气般掠过。诗意的低语旁白，自然是真正的主角，省略的时间。这生命是什么？列车继续前行，狗注视着光。
- Negative: `No explanatory dialogue, no tight suspense plotting, no fast cutting, no witty banter, no sentimental climax`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
