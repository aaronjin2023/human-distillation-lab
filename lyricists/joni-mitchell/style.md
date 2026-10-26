# Joni Mitchell — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joni Mitchell: painterly lyrics, colour and weather as emotion, lucid self-examination, open-tuned phrasing, chorus as a reframed view`
- ZH: 琼尼·米切尔风格：画家般的歌词，色彩与天气即情感，清醒的自我审视，开放调弦般的句法，副歌即换一个角度再看。

## (2) 意象

- 意象群：(1)色彩与天气——蓝、黄色出租车、云、雪，色彩即情感；(2)天堂与停车场——天堂、停车场、树，失去即主题；(3)酒与地图——酒、地图、星，醉与清醒并置。意象密度高，每句多个意象，明喻多，用典克制（文学典故轻触即止）。禁意象：直白的煽情、廉价的流行隐喻。

## (3) 韵律

- 押韵：句尾押韵工整而自由，常以叠韵与内韵制造歌唱感；换韵处即视角转换处。音节与字数：每句字数中等，长短句交错，贴合开放调弦吉他的呼吸；重音即口语重音。

## (4) 句式与口语密度

- 句式：中句为主，长短交错；多用第一人称自白与第二人称对话交错，设问偶见，排比克制。口语密度中等：日常口语打底，画家般的书面语点睛；独白体多，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个画面进场（云、天堂）；转——视角翻转，同一事物两面看；合——副歌收在清醒的接受上，不煽情。情感强度清醒而深沉，与听众保持审视的距离；结尾常收束在一个意象上。

## (6) 该写什么 / 不该写什么

- 该写：色彩与天气意象、天堂与停车场的对照、清醒的自我审视、视角翻转结构、画家般的观察句式。
- 不该写：直白的煽情、廉价的流行隐喻、解释性的议论、生硬的押韵。
- Negative prompt: `No blunt sentimentality, no cheap pop metaphors, no explanatory commentary, no forced rhyme, no grand slogans`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Joni Mitchell, lyrics about a small Yorkshire terrier sitting on a subway seat. Painterly colour and weather imagery, lucid self-examination, chorus that reframes the view. No sentimentality.`
- 中文对照：琼尼·米切尔风格：画家般的歌词，色彩与天气即情感，清醒的自我审视，开放调弦般的句法，副歌即换一个角度再看。以“一只坐在地铁里的约克夏犬”为题写歌词，见英文提示词。
- Negative: `No blunt sentimentality, no cheap pop metaphors, no explanatory commentary, no forced rhyme, no grand slogans`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
