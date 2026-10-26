# Lynn Ahrens — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lynn Ahrens: clear storytelling lyrics, a character's memory as the engine, plain words carrying history, chorus as a homecoming, warm and unadorned`
- ZH: 阿伦斯风格：清晰的叙事歌词，以角色的记忆为引擎，平实的词承载历史，副歌是一次归家，温暖而不加装饰。

## (2) 意象

- 记忆意象（旧照片、八音盒、十二月的雪、圣彼得堡的宫殿）／旅途意象（火车、河流、远方的城市）／家庭意象（母亲的手、故乡的街道）；意象密度中等，每句一个意象；多用具体名词，少用抽象大词。 `impression`
- 意象密度：意象密度中等，每句一个意象 `impression`
- 禁意象：华丽辞藻、抽象口号、与剧情无关的抒情、故作艰深的隐喻。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音，换韵处即记忆的转折处；主歌—副歌—桥段各换一次韵；音节与旋律贴合，换气点留在乐句末尾。 `impression`
- 音节与字数：句式整齐，每句字数接近，副歌比主歌更齐整；长短句交错少，求的是唱得稳、记得住。 `impression`

## (4) 句式与口语密度

- 句式：句式以中短句为主，叙事句与抒情句交替；口语密度中等，书面语与口语各半；多用第一人称回忆体，偶用第二人称召唤。 `impression`
- 口语密度：口语密度中等：对话自然但不俚俗，语气词少；书面语用于历史与记忆段落，口语用于当下对话；独白体为主，对话体为辅。 `impression`

## (5) 情感弧线

- 起于一句记忆的召唤，中段沿旅途推进、记忆渐次清晰，副歌收在归家或认出自己的时刻，结尾常是开放的希望而非定论；情感克制而温暖。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：记忆与旅途意象、清晰的叙事推进、副歌归家感、平实而准确的词。
- 不该写：华丽辞藻、抽象口号、与剧情无关的抒情、故作艰深的隐喻。
- Negative prompt: `No ornate diction, no abstract slogans, no decorative lyricism unrelated to the plot, no wilfully obscure metaphor`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Lynn Ahrens, lyrics about a small Yorkshire terrier sitting on a subway seat, remembering a home it has not seen for years. Clear storytelling, memory as engine, chorus as homecoming. Verse, chorus, bridge. No ornate diction.`
- 中文对照：阿伦斯风格：歌词写一只约克夏犬坐在地铁座位上，回忆多年未见的家。叙事清晰，记忆是引擎，副歌是一次归家。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no decorative lyricism, no obscure metaphor`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
