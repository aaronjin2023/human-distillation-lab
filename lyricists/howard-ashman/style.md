# Howard Ashman — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Howard Ashman: character-driven musical lyrics, longing as the engine, small telling detail as a wish, chorus as a single yearning image`
- ZH: 霍华德·阿什曼风格：角色驱动的音乐剧歌词，渴望即引擎，一个有说服力的细节即愿望，副歌即一个渴望的意象。

## (2) 意象

- 意象群：(1)渴望与世界——世界、海洋、陆地，渴望即主题；(2)美女与野兽——玫瑰、城堡、烛台，爱即转变；(3)朋友与魔法——朋友、精灵、魔法，友谊即魔法。意象密度中等，每句一两个意象，多明喻，用典克制（童话轻触即止）。禁意象：直白的说教、晦涩的象征、廉价的流行隐喻。

## (3) 韵律

- 押韵：句尾押韵工整流畅，韵脚多为柔和的口语尾音；常以叠韵制造歌唱感；换韵处即渴望转折处。音节与字数：每句字数中等偏整齐，贴合迪士尼旋律的呼吸；重音即口语重音。

## (4) 句式与口语密度

- 句式：中句为主，长短交错；多用第一人称独白（I want）与第二人称对话交错，设问偶见。口语密度高：平实口语打底，童话书面语点睛；独白体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个角色的渴望进场（I want）；转——细节累积，渴望升温；合——副歌收在一个渴望的意象上，温和而不滥情。情感强度真诚浓烈，与听众零距离；结尾常收束在一个意象上。

## (6) 该写什么 / 不该写什么

- 该写：角色的渴望、I want 句式、童话意象、细节即愿望、副歌一个渴望的意象。
- 不该写：直白的说教、晦涩的象征、廉价的流行隐喻、生硬的押韵。
- Negative prompt: `No direct preaching, no obscure symbolism, no cheap pop metaphors, no forced rhyme, no cynical irony`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Howard Ashman, lyrics about a small Yorkshire terrier sitting on a subway seat, longing to be part of the human world. Character-driven longing, small telling detail, chorus as a single yearning image. No preaching.`
- 中文对照：霍华德·阿什曼风格：角色驱动的音乐剧歌词，渴望即引擎，一个有说服力的细节即愿望，副歌即一个渴望的意象。以“一只坐在地铁里的约克夏犬”为题写歌词，见英文提示词。
- Negative: `No direct preaching, no obscure symbolism, no cheap pop metaphors, no forced rhyme, no cynical irony`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
