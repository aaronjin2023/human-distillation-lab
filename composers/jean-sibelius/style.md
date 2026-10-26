# Jean Sibelius — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Organic growth, Finnish landscape, modal melody, long pedal, sparse texture, single-movement symphony, nature in sound`
- ZH: 有机生长，芬兰风景，调式旋律，长音踏板，稀疏织体，单乐章交响曲，声音中的自然。

## (2) 旋律与和声

- 旋律：民间歌唱，短小动机；和声：调式和声，五声音阶。禁：瓦格纳式半音绵延。调性清晰，民间调式点缀。

## (3) 节奏与织体

- 节奏：稳健、缓慢；织体：稀疏，留白。

## (4) 配器与音色

- 乐器：管弦乐，弦乐与木管；音色：冷峻、清澈；力度：中弱为主。

## (5) 曲式与结构

- 曲式：交响诗、交响曲、协奏曲；结构：有机生长、单乐章；结尾：渐弱或悬置。

## (6) 该写什么 / 不该写什么

- 该写：有机生长、芬兰风景、调式旋律、稀疏织体、单乐章交响曲。
- 不该写：瓦格纳式半音绵延、无调性、厚重管弦乐、空洞炫技、煽情电影配乐式 swell、流行和弦循环。
- Negative prompt: `no Wagnerian chromatic sprawl, no atonal wandering, no thick orchestral mass, no empty virtuosity, no sentimental film-score swell, no pop chord loop`

## (7) 测试提示词示例（现代题材：深夜末班车窗外的雨）

- Prompt: `In the style of Jean Sibelius, rain on the window of a night bus crossing the city, Organic growth, Finnish landscape, modal melody, long pedal, sparse texture, single-movement symphony, nature in sound`
- 中文对照：让·西贝柳斯风格，深夜末班车窗外的雨，有机生长，芬兰风景，调式旋律，长音踏板，稀疏织体，单乐章交响曲，声音中的自然。
- Negative: `no Wagnerian chromatic sprawl, no atonal wandering, no thick orchestral mass, no empty virtuosity, no sentimental film-score swell, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
