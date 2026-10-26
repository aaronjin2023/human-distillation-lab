# Frank Loesser — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frank Loesser: street-smart American vernacular, character songs that argue with themselves, a chorus that lands like a punchline, warmth under the slang`
- ZH: 洛瑟风格：街头智慧的美式口语，角色与自己辩论的歌曲，副歌像一句妙语落点，俚语之下是温情。

## (2) 意象

- 街头意象（骰子、酒吧、街角、霓虹）／赌博意象（运气、骰子、牌桌）／日常意象（寒夜、壁炉、旧外套）；意象密度中等；多用口语明喻，少用典。 `impression`
- 意象密度：意象密度中等 `impression`
- 禁意象：华丽辞藻、抽象口号、书面抒情、与角色无关的风景。`impression`

## (3) 韵律

- 句尾韵工整，韵脚口语化，常押俚语韵；换韵处即辩论的转折处；音节与节拍贴合，讲究唱得顺、说得像。 `impression`
- 音节与字数：句式以中短句为主，对话句与独白句交错；副歌短促有力，长短句随辩论换。 `impression`

## (4) 句式与口语密度

- 句式：句式以对话与自辩为主，设问与自答交替；口语密度极高，俚语与街头用语是本体；多用第一人称与第二人称对话。 `impression`
- 口语密度：口语密度极高：俚语、街头用语、感叹词自然入词；书面语极少；对话体为主。 `impression`

## (5) 情感弧线

- 起于一句街头开场，中段角色与自己或对方辩论，副歌收在妙语落点上，结尾常是温柔的让步；情感外冷内热。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：街头口语与俚语、角色自辩、赌博与运气意象、副歌的妙语落点。
- 不该写：华丽辞藻、抽象口号、书面抒情、与角色无关的风景。
- Negative prompt: `No ornate diction, no abstract slogans, no bookish lyricism, no scenery unrelated to the character`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Frank Loesser, lyrics about a small Yorkshire terrier sitting on a subway seat, while a gambler argues with himself about luck. Street-smart vernacular, chorus landing like a punchline. Verse, chorus, bridge. No ornate diction.`
- 中文对照：洛瑟风格：歌词写一只约克夏犬坐在地铁座位上，一位赌徒与自己辩论运气。街头口语，副歌像妙语落点。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no bookish lyricism, no scenery unrelated to the character`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
