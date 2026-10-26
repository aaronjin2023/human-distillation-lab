# Taylor Swift — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Taylor Swift: diary-like narrative lyrics, small telling detail as evidence, scarf and kitchen-light imagery, chorus as a reframed memory`
- ZH: 泰勒·斯威夫特风格：日记般的叙事歌词，一个有说服力的细节即证据，围巾与冰箱灯的意象，副歌即换一个角度重述记忆。

## (2) 意象

- 意象群：(1)日常细节——围巾、冰箱灯、楼梯，细节即证据；(2)时间与季节——秋天、十年、午夜，时间即情感；(3)童话与反童话——城堡、王子、空白，反童话即自嘲。意象密度高，每句多个细节意象，多明喻，用典克制（童话、流行文化轻触即止）。禁意象：抽象的议论、直白的说教、廉价的流行隐喻。

## (3) 韵律

- 押韵：句尾押韵工整流畅，韵脚多为柔和的口语尾音；常以叠韵与内韵制造歌唱感；换韵处即记忆翻转处。音节与字数：每句字数中等，长短句交错，贴合流行旋律的呼吸；重音即口语重音。

## (4) 句式与口语密度

- 句式：中句为主，长短交错；多用第一人称叙事与第二人称对话交错，设问偶见，排比常用。口语密度高：日记般的口语、细节句，书面语极少；叙事体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个细节进场（围巾、冰箱灯）；转——记忆层层展开，细节累积；合——副歌收在重述的记忆上，清醒而不煽情。情感强度真诚克制，与听众零距离；结尾常收束在一个细节上。

## (6) 该写什么 / 不该写什么

- 该写：日常细节即证据、日记般的叙事、围巾与冰箱灯意象、记忆的重述、副歌换角度再看。
- 不该写：抽象的议论、直白的说教、廉价的流行隐喻、生硬的押韵。
- Negative prompt: `No abstract commentary, no direct preaching, no cheap pop metaphors, no forced rhyme, no grand slogans`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Taylor Swift, lyrics about a small Yorkshire terrier sitting on a subway seat, a commuter remembering a lost scarf. Diary-like detail, chorus that reframes the memory. No preaching.`
- 中文对照：泰勒·斯威夫特风格：日记般的叙事歌词，一个有说服力的细节即证据，围巾与冰箱灯的意象，副歌即换一个角度重述记忆。以“一只坐在地铁里的约克夏犬”为题写歌词，见英文提示词。
- Negative: `No abstract commentary, no direct preaching, no cheap pop metaphors, no forced rhyme, no grand slogans`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
