# Bernie Taupin — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bernie Taupin: cinematic story lyrics, American road and small-town imagery, plain words with a novelist's eye, chorus as a single glowing image`
- ZH: 伯尼·陶平风格：电影般的叙事歌词，美国公路与小镇的意象，平实的字句带着小说家的眼睛，副歌即一个发光的意象。

## (2) 意象

- 意象群：(1)公路与小镇——公路、汽车旅馆、小镇，行走即故事；(2)星与烛——星星、蜡烛、风，微光即挽歌；(3)舞者与音乐——小舞者、钢琴、蓝眼睛，人物即画面。意象密度中等偏高，每句一两个意象，明喻多，用典克制。禁意象：直白的煽情、廉价的流行隐喻、抽象的议论。

## (3) 韵律

- 押韵：句尾押韵工整，韵脚多为柔和的尾音；常以叠韵与内韵制造歌唱感；换韵处即叙事转折处。音节与字数：每句字数中等，长短句交错，贴合 Elton John 旋律的呼吸；重音即口语重音。

## (4) 句式与口语密度

- 句式：中句为主，长短交错；多用第一人称叙事与第二人称对话交错，设问偶见，排比克制。口语密度中等：日常口语打底，小说般的书面语点睛；叙事体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个画面进场（小舞者、蜡烛）；转——叙事推进，细节累积；合——副歌收在一个发光的意象上，温和而不煽情。情感强度克制而深沉，与听众保持叙事的距离；结尾常收束在一个意象上。

## (6) 该写什么 / 不该写什么

- 该写：公路与小镇意象、电影般的叙事句式、星与烛的微光意象、平实的观察、副歌一个发光的意象。
- 不该写：直白的煽情、廉价的流行隐喻、抽象的议论、生硬的押韵。
- Negative prompt: `No blunt sentimentality, no cheap pop metaphors, no abstract commentary, no forced rhyme, no grand slogans`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Bernie Taupin, lyrics about a small Yorkshire terrier sitting on a subway seat. Cinematic small-town imagery, plain words with a novelist's eye, chorus as a single glowing image. No sentimentality.`
- 中文对照：伯尼·陶平风格：电影般的叙事歌词，美国公路与小镇的意象，平实的字句带着小说家的眼睛，副歌即一个发光的意象。以“一只坐在地铁里的约克夏犬”为题写歌词，见英文提示词。
- Negative: `No blunt sentimentality, no cheap pop metaphors, no abstract commentary, no forced rhyme, no grand slogans`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
