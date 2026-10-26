# Sammy Cahn — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sammy Cahn: breezy invitation lyrics, crisp colloquial swing, travel and weather imagery, playful repetition, instantly singable hooks`
- ZH: 萨米·卡恩风格：轻快的邀约式歌词，利落的口语摇摆，旅行与天气的意象，俏皮的重复，一听就能跟着唱的副歌。

## (2) 意象

- 意象群：(1)旅行与远方——飞机、异国、喷泉、硬币，邀约即意象；(2)天气与季节——雪、雨、阳光，用天气写心情；(3)夜晚的城市——霓虹、酒吧、舞池，轻松的都市夜。意象密度中等，每句一两个具体意象，多明喻，用典极少。禁意象：沉重的苦难意象、晦涩的象征。

## (3) 韵律

- 押韵：句尾押韵工整，韵脚短促响亮；大量使用叠句与重复（Let It Snow! 三叠）制造记忆点；换韵多在桥段。音节与字数：每句字数短而整齐，与摇摆节拍严丝合缝，重音落在口语重音上，几乎没有拗口的长句。

## (4) 句式与口语密度

- 句式：短句、祈使句多（Come fly with me），像发出邀请；设问偶见，排比常用。口语密度很高：日常口语、俚语、重复语气词，书面语极少；对话体与独白体并存。

## (5) 情感弧线

- 情感弧线：起——一句邀约进场；转——列举远方的美好，情绪上扬；合——副歌重复邀约，收在轻快的肯定上。情感强度轻快明朗，与听众零距离；结尾常以叠句收束，余音即邀请。

## (6) 该写什么 / 不该写什么

- 该写：轻快的邀约句式、旅行、天气等具体意象、叠句与重复、短促响亮的韵脚、副歌一句即记忆点。
- 不该写：沉重的苦难意象、晦涩的象征、冗长的解释、阴郁的收束。
- Negative prompt: `No heavy suffering imagery, no obscure symbolism, no long explanatory lines, no gloomy ending, no forced rhyme`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Sammy Cahn, lyrics as a letter to oneself ten years from now, an invitation to travel light. Breezy colloquial swing, travel and weather imagery, playful repetition, verse, chorus, bridge. No gloom.`
- 中文对照：萨米·卡恩风格：轻快的邀约式歌词，利落的口语摇摆，旅行与天气的意象，俏皮的重复，一听就能跟着唱的副歌。以“一封写给十年后自己的信”为题写歌词，见英文提示词。
- Negative: `No heavy suffering imagery, no obscure symbolism, no long explanatory lines, no gloomy ending, no forced rhyme`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
