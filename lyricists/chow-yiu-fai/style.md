# Chow Yiu-fai — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chow Yiu-fai: city as text, wordplay and homophones, wry distance, Cantonese colloquial rhythm, love observed from the street corner`
- ZH: 周耀辉风格：城市即文本，谐音与双关，冷眼旁观的疏离，粤语口语节奏，爱情写在街角。

## (2) 意象

- 城市意象群：囍帖街、旧区、招牌、街角、电车——城市变迁即感情变迁；身体与空间意象：座位、窗、门、楼梯，把抽象关系写成具体位置；时间意象：旧物、昨日、下一站，用地点写时间。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 粤语九声填词，韵脚贴合旋律；主歌韵脚较松、副歌收紧；善用同音与近音双关，换韵处常是语义转折处；长短句交错，短句收束如点题。 `impression`

## (4) 句式与口语密度

- 口语密度中高：粤语口语入词自然，书面语只作点缀；多用设问与反问，少用直抒；对话感弱、旁白感强，像站在街边讲别人的故事。 `impression`

## (5) 情感弧线

- 起：一个城市场景进场（街、店、车站）；转：场景里的旧物或旧人被点破，感情翻面；合：副歌收在冷静的判断句上，不煽情，留一个回望的结尾。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：城市变迁与感情对照、谐音双关与一语双关、冷静旁白、街角视角、短句点题式收束、旧物写时间。
- 不该写：直白口号、廉价煽情与哭诉、无城市落点的抽象抒情、顺口的廉价排比、解释性议论。
- Negative prompt: `No plain slogans, no cheap sentimentality, no abstract lyricism without a city anchor, no forced rhyme, no explanatory commentary`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Chow Yiu-fai, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：周耀辉风格：城市即文本，谐音与双关，冷眼旁观的疏离，粤语口语节奏，爱情写在街角。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No plain slogans, no cheap sentimentality, no abstract lyricism without a city anchor, no forced rhyme, no explanatory commentary`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
