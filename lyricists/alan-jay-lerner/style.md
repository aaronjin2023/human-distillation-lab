# Alan Jay Lerner — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alan Jay Lerner: elegant musical-theatre lyrics, romantic wit, London and Paris street imagery, chorus as a rapturous declaration`
- ZH: 阿兰·杰伊·勒纳风格：优雅的音乐剧歌词，浪漫的机智，伦敦与巴黎街头的意象，副歌即一句陶醉的宣言。

## (2) 意象

- 意象群：(1)伦敦与巴黎——街道、雨、夜晚，城市即浪漫；(2)舞蹈与夜晚——舞蹈、夜晚、灯光，舞蹈即心动；(3)花与春天——花、春天、微笑，春天即爱情。意象密度中等，每句一两个意象，多明喻，用典克制。禁意象：俚语的粗粝、直白的煽情、晦涩的象征。

## (3) 韵律

- 押韵：句尾押韵工整优雅，韵脚多为长元音；常以叠韵制造歌唱感；换韵处即情绪转折处。音节与字数：每句字数中等偏整齐，贴合音乐剧旋律的呼吸；重音即口语重音。

## (4) 句式与口语密度

- 句式：中句为主，长短交错；多用第一人称独白与第二人称称呼交错，设问偶见。口语密度中等：优雅口语打底，书面语点睛；独白体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个浪漫场景进场；转——一句机智把情绪推向陶醉；合——副歌收在陶醉的宣言上，不滥情。情感强度优雅浓烈，与听众保持浪漫的距离；结尾常收束在一个意象上。

## (6) 该写什么 / 不该写什么

- 该写：伦敦与巴黎街头意象、浪漫的机智、舞蹈与夜晚意象、优雅的句式、副歌一句陶醉的宣言。
- 不该写：俚语的粗粝、直白的煽情、晦涩的象征、生硬的押韵。
- Negative prompt: `No coarse slang, no blunt sentimentality, no obscure symbolism, no forced rhyme, no cynical irony`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Alan Jay Lerner, lyrics about a small Yorkshire terrier sitting on a subway seat, a commuter falling in love with the city again. Elegant romantic wit, Paris street imagery, chorus as a rapturous declaration. No cynicism.`
- 中文对照：阿兰·杰伊·勒纳风格：优雅的音乐剧歌词，浪漫的机智，伦敦与巴黎街头的意象，副歌即一句陶醉的宣言。以“一只坐在地铁里的约克夏犬”为题写歌词，见英文提示词。
- Negative: `No coarse slang, no blunt sentimentality, no obscure symbolism, no forced rhyme, no cynical irony`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
