# Camille Saint-Saëns — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `French clarity, classical balance, witty orchestration, elegant melody, brilliant piano and organ writing`
- ZH: 法国式清晰，古典均衡，机智配器，优雅旋律，辉煌的钢琴与管风琴写作。

## (2) 旋律与和声

- 旋律：优雅歌唱，级进为主；和声：功能和声，清晰转调。禁：瓦格纳式半音绵延、无调性。调性稳定。

## (3) 节奏与织体

- 节奏：清晰、机智；织体：主调为主，声部清晰。

## (4) 配器与音色

- 乐器：管弦乐、管风琴、钢琴；音色：明亮、透明；力度：中强为主。

## (5) 曲式与结构

- 曲式：交响曲、交响诗、组曲；结构：古典四乐章或组曲并置；结尾：明朗收束。

## (6) 该写什么 / 不该写什么

- 该写：法国式清晰、古典均衡、机智配器、优雅旋律、管风琴交响曲。
- 不该写：瓦格纳式半音绵延、无调性、厚重德式配器、过度煽情、无形式绵延、流行和弦循环。
- Negative prompt: `no Wagnerian chromatic sprawl, no atonal wandering, no thick Germanic mass, no sentimental excess, no formless sprawl, no pop chord loop`

## (7) 测试提示词示例（现代题材：现代城市街角小便利店的深夜场景）

- Prompt: `In the style of Camille Saint-Saëns, a quiet night scene at a small convenience store in a modern city, French clarity, classical balance, witty orchestration, elegant melody, brilliant piano and organ writing`
- 中文对照：卡米尔·圣-桑风格，现代城市街角小便利店的深夜场景，法国式清晰，古典均衡，机智配器，优雅旋律，辉煌的钢琴与管风琴写作。
- Negative: `no Wagnerian chromatic sprawl, no atonal wandering, no thick Germanic mass, no sentimental excess, no formless sprawl, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
