# Hal David — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hal David: plainspoken conversational lyrics, everyday detail as emotion, gentle understatement, Burt Bacharach's melodies carried by unadorned words`
- ZH: 哈尔·大卫风格：平实的谈话体歌词，日常细节即情感，温和的克制，不加修饰的字句托着旋律走。

## (2) 意象

- 意象群：(1)日常细节——雨滴、街道、信、电话，细节即情感；(2)行走与离开——走开、走过、雨中前行，动作即态度；(3)世界与爱——世界需要爱，把大命题落到一句平实的话上。意象密度低，每句至多一个意象，多明喻，用典极少。禁意象：华丽的古风意象、宏大的象征、苦情的自怜。

## (3) 韵律

- 押韵：句尾押韵自然松散，韵脚多为日常口语的尾音；常以重复与排比推进，不靠密韵；换韵处即情绪转折处。音节与字数：每句字数中等，长短句交错，贴合 Bacharach 旋律的不规则乐句，留出换气口；重音即口语重音。

## (4) 句式与口语密度

- 句式：中短句为主，像说话；多用第二人称劝慰与第一人称独白交错，设问偶见。口语密度很高：日常口语、简单句、语气词少，书面语极少；对话体多，独白体温和。

## (5) 情感弧线

- 情感弧线：起——一个日常细节进场（雨、街道）；转——一句劝慰或自省把情绪推开；合——副歌收在温和的接受上，不煽情。情感强度温和克制，与听众如朋友谈心；结尾常收束在一句平实的话上。

## (6) 该写什么 / 不该写什么

- 该写：日常细节意象、平实的谈话句式、温和的劝慰、松散自然的韵脚、副歌一句平实的话。
- 不该写：华丽的古风意象、宏大的象征、直白的煽情、密韵的炫技。
- Negative prompt: `No ornate archaic imagery, no grand symbolism, no blunt sentimentality, no rhyme-for-rhyme's-sake, no explanatory commentary`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Hal David, lyrics about a small Yorkshire terrier sitting on a subway seat, commuters pretending not to notice. Plainspoken conversational lines, everyday detail, gentle understatement, verse, chorus, bridge. No sentimentality.`
- 中文对照：哈尔·大卫风格：平实的谈话体歌词，日常细节即情感，温和的克制，不加修饰的字句托着旋律走。以“一只坐在地铁里的约克夏犬”为题写歌词，见英文提示词。
- Negative: `No ornate archaic imagery, no grand symbolism, no blunt sentimentality, no rhyme-for-rhyme's-sake, no explanatory commentary`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
