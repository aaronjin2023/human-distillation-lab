# Wolfgang Amadeus Mozart — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Classical perfection, balanced sonata form, singing melody, clear tonal harmony, elegant counterpoint, opera and symphony in equal measure, effortless grace with hidden depth`
- ZH: 古典完美，均衡的奏鸣曲式，歌唱性旋律，清晰调性和声，优雅的对位，歌剧与交响曲并重，毫不费力的优雅与暗藏的深度。

## (2) 旋律与和声

- 旋律：旋律歌唱性极强，级进为主，乐句均衡完美；主题短小、富于发展。`artifact` 和声：功能和声明确，属—主收束清晰；半音作表情，转调优雅；禁用随意半音。调性：调性稳定，转调如行云流水。

## (3) 节奏与织体

- 节奏：节奏清晰，舞曲与歌剧节奏并重；小步舞曲优雅，终乐章活泼。织体：主调为主，复调为辅（《朱庇特》终乐章五主题赋格）；留白靠乐句呼吸。

## (4) 配器与音色

- 配器与音色：管弦乐队（弦乐、木管、铜管）与歌剧声乐并重；音色明亮、透明；力度靠配器对比；空间感来自维也纳宫廷与剧场。

## (5) 曲式与结构

- 曲式：歌剧（《唐·乔瓦尼》）、交响曲（《朱庇特》）、协奏曲、安魂曲并重；奏鸣曲式是骨架。结构：呈示—展开—再现，高潮在展开部；结尾以清晰终止收束。

## (6) 该写什么 / 不该写什么

- 该写：歌唱性旋律、奏鸣曲式、歌剧重唱与终曲、《朱庇特》终乐章五主题赋格、钢琴协奏曲的独奏—乐队对话。
- 不该写：无歌唱性的机械音型、随意半音与无调性、管弦乐盖过独唱、与结构无关的装饰、感伤的滥情。
- Negative prompt: `No unlyrical mechanical figuration, no random chromaticism, no orchestra covering voices, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`

## (7) 测试提示词示例（现代题材：深夜雨中行驶的一辆出租车）

- Prompt: `In the style of Wolfgang Amadeus Mozart, a 30-second piece for a taxi driving through rain late at night, classical perfection, balanced sonata form, singing melody, clear tonal harmony, elegant counterpoint, opera and symphony in equal measure, effortless grace with hidden depth`
- 中文对照：莫扎特风格，为深夜雨中行驶的一辆出租车写 30 秒配乐，古典完美，均衡的奏鸣曲式，歌唱性旋律，清晰调性和声，优雅的对位，歌剧与交响曲并重，毫不费力的优雅与暗藏的深度。
- Negative: `No unlyrical mechanical figuration, no random chromaticism, no orchestra covering voices, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
