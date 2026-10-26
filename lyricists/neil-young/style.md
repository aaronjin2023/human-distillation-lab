# Neil Young — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Neil Young: plainspoken prairie lyrics, harvest and highway imagery, raw unadorned address, chorus as a simple repeated plea`
- ZH: 尼尔·杨风格：平实的草原歌词，丰收与公路的意象，粗粝而不加修饰的称呼，副歌即一句简单的重复恳求。

## (2) 意象

- 意象群：(1)丰收与田野——丰收、月亮、麦田，土地即情感；(2)公路与卡车——公路、流浪，行走即命运；(3)老人与黄金——老人、黄金之心，时间即主题。意象密度低，每句至多一个意象，多明喻，用典极少。禁意象：华丽的都市意象、晦涩的象征、直白的煽情。

## (3) 韵律

- 押韵：句尾押韵简单工整，韵脚多为短促的口语尾音；常以重复推进，不靠密韵；换韵处即情绪转折处。音节与字数：每句字数短而整齐，贴合民谣吉他的呼吸；重音即口语重音，唱起来粗粝直接。

## (4) 句式与口语密度

- 句式：短句为主，长短交错；多用第一人称独白与第二人称对话交错，设问偶见。口语密度很高：日常口语、简单句，书面语极少；独白体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个画面进场（丰收月、老人）；转——一句自省把情绪推开；合——副歌收在简单的恳求上，不煽情。情感强度粗粝而真诚，与听众零距离；结尾常收束在一个意象上。

## (6) 该写什么 / 不该写什么

- 该写：丰收与田野意象、平实的短句、老人与黄金之心、简单的重复副歌、粗粝的真诚。
- 不该写：华丽的都市意象、晦涩的象征、直白的煽情、密韵的炫技。
- Negative prompt: `No ornate urban imagery, no obscure symbolism, no blunt sentimentality, no rhyme-for-rhyme's-sake, no explanatory commentary`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Neil Young, lyrics about a small Yorkshire terrier sitting on a subway seat. Plainspoken prairie imagery, harvest moon, raw unadorned address, chorus as a simple repeated plea. No sentimentality.`
- 中文对照：尼尔·杨风格：平实的草原歌词，丰收与公路的意象，粗粝而不加修饰的称呼，副歌即一句简单的重复恳求。以“一只坐在地铁里的约克夏犬”为题写歌词，见英文提示词。
- Negative: `No ornate urban imagery, no obscure symbolism, no blunt sentimentality, no rhyme-for-rhyme's-sake, no explanatory commentary`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
