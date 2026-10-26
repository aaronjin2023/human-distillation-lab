# Johnny Mercer — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Johnny Mercer: Southern vernacular warmth, conversational drawl, moon and river imagery, plain words carrying ache, melody-hugging phrasing`
- ZH: 约翰尼·默瑟风格：南方口语的暖意，闲谈般的拖腔，月亮与河流的意象，平实的字句藏着隐痛，词句贴着旋律走。

## (2) 意象

- 意象群：(1)月亮与河流——月河、宽阔的河、彩虹的尽头，远方与归乡的双重指向；(2)南方日常——乡间小路、门廊、夏夜、旧歌，口音即意象；(3)酒与玫瑰——花与酒、逝去的时光，怀旧而不沉溺。意象密度中等偏低，每句一个意象，多明喻，用典少。禁意象：都市的冷硬意象、抽象的哲学概念。

## (3) 韵律

- 押韵：句尾押韵为主，韵脚多为开口长元音（moon / soon / river / dream），唱起来拖得长；常以叠词与重复制造摇摆感；换韵处即情绪转折处。音节与字数：每句字数中等，长短句交错，重音与爵士节拍对位，留出换气口，南方拖音即节奏。

## (4) 句式与口语密度

- 句式：中短句为主，像闲谈；多用第二人称与第一人称交错，设问偶见，排比克制。口语密度高：南方口语、俚语、缩略语自然入词，语气词少；书面语只在副歌点睛处出现。

## (5) 情感弧线

- 情感弧线：起——一个温柔的画面进场（月河、夏夜）；转——一句怀旧把情绪轻轻推向远方；合——副歌收在渴望与安慰之间，不绝望。情感强度温和克制，与听众如老友闲谈；结尾常收束在远方的一个意象上。

## (6) 该写什么 / 不该写什么

- 该写：月亮、河流、南方日常意象、口语化的闲谈句式、开口长元音韵脚、温柔的怀旧、副歌一句远方。
- 不该写：冷硬的都市意象、抽象的哲学议论、直白的煽情、生硬的押韵。
- Negative prompt: `No cold urban imagery, no abstract philosophising, no blunt sentimentality, no forced rhyme, no ornate diction`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Johnny Mercer, lyrics about a man buying oden at a convenience store late at night. Southern conversational drawl, moon and river imagery, plain words, gentle nostalgia, verse, chorus, bridge. No sentimentality.`
- 中文对照：约翰尼·默瑟风格：南方口语的暖意，闲谈般的拖腔，月亮与河流的意象，平实的字句藏着隐痛，词句贴着旋律走。以“一个人在深夜便利店买关东煮”为题写歌词，见英文提示词。
- Negative: `No cold urban imagery, no abstract philosophising, no blunt sentimentality, no forced rhyme, no ornate diction`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
