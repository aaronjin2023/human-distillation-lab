# Sheldon Harnick — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sheldon Harnick: warm character comedy, plain words that turn suddenly tender, a chorus that marks time passing, tradition held lightly`
- ZH: 哈尼克风格：温暖的角色喜剧，平实的词忽然转入温柔，副歌标记时间的流逝，传统举重若轻。

## (2) 意象

- 传统意象（婚礼、烛台、村庄、安息日）／时间意象（日出日落、四季、孩子的长大）／日常意象（屋顶、提琴、集市）；意象密度中等，每句一个意象；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度中等，每句一个意象 `impression`
- 禁意象：华丽辞藻、抽象口号、刻薄的讽刺、与角色无关的抒情。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音；喜剧段落韵脚俏皮，温柔段落韵脚舒缓；换韵处即情绪的转折处；音节与旋律贴合。 `impression`
- 音节与字数：句式整齐，喜剧段落短句多，温柔段落长句多；主歌叙事、副歌抒情，长短句随情绪换。 `impression`

## (4) 句式与口语密度

- 句式：句式以中短句为主，喜剧的问答与抒情的独白交替；口语密度高，像角色在说话；多用第一人称与第二人称对话。 `impression`
- 口语密度：口语密度高：角色口语自然，语气词与感叹自然；书面语只在仪式与传统段落出现；对话体为主。 `impression`

## (5) 情感弧线

- 起于日常的喜剧场景，中段由笑转入时间的感慨，副歌收在日出日落的流逝感上，结尾常是温柔的接受而非反抗；情感克制而温暖。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：角色喜剧与温柔转折、时间流逝意象、传统与日常、副歌的流逝感。
- 不该写：华丽辞藻、抽象口号、刻薄的讽刺、与角色无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no cruel satire, no lyricism unrelated to the character`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Sheldon Harnick, lyrics about a small Yorkshire terrier sitting on a subway seat, while an old man watches the city pass like sunrise and sunset. Warm character comedy turning tender, chorus marking time. Verse, chorus, bridge. No ornate diction.`
- 中文对照：哈尼克风格：歌词写一只约克夏犬坐在地铁座位上，一位老人看着城市如日出日落般流过。温暖的角色喜剧转入温柔，副歌标记时间。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no cruel satire, no lyricism unrelated to the character`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
