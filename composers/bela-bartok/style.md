# Béla Bartók — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Folk modes, arch form, night music, polymodality, percussive piano, rhythmic drive, folk song as structure`
- ZH: 民间调式，拱形结构，夜音乐，多调性，打击性钢琴，节奏驱动，民歌即结构。

## (2) 旋律与和声

- 旋律：民间歌唱，短小动机；和声：民间调式、多调性。禁：功能和声主导。调性游移，民间调式为根。

## (3) 节奏与织体

- 节奏：不规则、民间舞曲；织体：复调与主调交织。

## (4) 配器与音色

- 乐器：管弦乐、弦乐四重奏、钢琴；音色：打击性、冷峻；力度：极端对比。

## (5) 曲式与结构

- 曲式：协奏曲、弦乐四重奏、组曲；结构：拱形结构；结尾：辉煌或渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：民间调式、拱形结构、夜音乐、打击性节奏、民间旋律。
- 不该写：功能和声主导、德国式动机发展、无调性、过度煽情、单薄沙龙织体、流行和弦循环。
- Negative prompt: `no functional harmony dominance, no Germanic motivic development, no atonal wandering, no sentimental excess, no thin salon texture, no pop chord loop`

## (7) 测试提示词示例（现代题材：现代城市街角小便利店的深夜场景）

- Prompt: `In the style of Béla Bartók, a quiet night scene at a small convenience store in a modern city, Folk modes, arch form, night music, polymodality, percussive piano, rhythmic drive, folk song as structure`
- 中文对照：贝拉·巴托克风格，现代城市街角小便利店的深夜场景，民间调式，拱形结构，夜音乐，多调性，打击性钢琴，节奏驱动，民歌即结构。
- Negative: `no functional harmony dominance, no Germanic motivic development, no atonal wandering, no sentimental excess, no thin salon texture, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
