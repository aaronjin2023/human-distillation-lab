# Qu Yuan — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Qu Yuan: Chuci sao-style verse, long cascading lines broken by the sigh-particle 'xi', fragrant herbs and river gods, heaven-questioning, loyal exile lament, ecstatic and desolate at once`
- ZH: 屈原风格：楚辞骚体，长行奔涌、兮字咏叹，香草美人，江河神明，天问式发问，忠而被谤的放逐之叹，激越而苍凉。

## (2) 意象

- 主意象：香草（兰、蕙、芷、椒）、江河（湘水、沅水）、日月星辰、神灵（山鬼、湘君）
- 辅意象：美人、佩玉、鸾凤、舟楫
- 禁意象：市井琐碎、田园闲适、轻佻艳情
- 密度：高密度：神话、典故、香草层层叠加，一句多典
- 来源：神话、楚地风物、典故
`impression`

## (3) 韵律与句式

- 韵律：楚辞体：长短句，以兮字句中停顿，六言为主、参差错落，换韵自由
- 句式：长句奔涌，兮字断句，叠词与呼告并用，《天问》式连珠设问
- 节奏：缓急相间，咏叹长调，顿挫落在兮字处，朗读如长歌
`impression`

## (4) 语言密度与词汇

- 词汇：香草名、神名、地名密集；动词多采、佩、搴、扈；不用口语俗词
- 密度：每行信息量极高，一字一典，意象堆叠
- 禁词：白话口语、琐碎日常、轻佻艳情、工整律句
`impression`

## (5) 结构习惯

- 诗体：长篇抒情 / 问体；《离骚》三段式（自述—求索—决绝）；《九歌》祭神组诗；《天问》连珠发问
- 开头：自述身世或直入神境
- 结尾：以决绝或归隐收束，不留和解
- 视角：第一人称抒情主体，兼祭祀代言
- 推进：自述 → 求索 → 受谗 → 决绝，层层递进
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 香草美人
- 江河神明
- 天问式发问
- 兮字咏叹
- 长行奔涌
- 不该写：
- 琐碎日常
- 工整律句
- 直白说教
- 温情和解
- 口语俗词
- Negative prompt: `No mundane daily chatter, no neat regulated couplets, no direct moralising, no sentimental reconciliation, no plain prosaic diction`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Qu Yuan, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. Chuci sao-style verse, long cascading lines broken by the sigh-particle 'xi', fragrant herbs and river gods, heaven-questioning, loyal exile lament, ecstatic and desolate at once`
- 中文对照：屈原风格：一只约克夏犬深夜坐在地铁座位上，乘客们看着它。屈原风格：楚辞骚体，长行奔涌、兮字咏叹，香草美人，江河神明，天问式发问，忠而被谤的放逐之叹，激越而苍凉。
- Negative: `No mundane daily chatter, no neat regulated couplets, no direct moralising, no sentimental reconciliation, no plain prosaic diction`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
