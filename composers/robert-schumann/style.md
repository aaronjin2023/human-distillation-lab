# Robert Schumann — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Literary piano cycles, Florestan fire and Eusebius dream, short character pieces, songful melody, inner voices, harmonic detour`
- ZH: 文学性钢琴套曲，热情与梦幻两种性格对置，短小性格小品，歌唱性旋律，活跃的内声部，迂回的和声。

## (2) 旋律与和声

- 旋律：短小性格动机，歌唱中带朗诵；和声：功能和声加半音迂回，远关系转调。禁：瓦格纳式无终旋律。调性常游移，靠动机收束。

## (3) 节奏与织体

- 节奏：切分与交叉节奏；织体：内声部活跃，主调中藏复调。

## (4) 配器与音色

- 乐器：钢琴、艺术歌曲、交响乐；音色：钢琴中音区温暖，管弦乐偏厚；力度：突强与突弱对比。

## (5) 曲式与结构

- 曲式：钢琴套曲、艺术歌曲集、交响曲；结构：小品并置成套曲，标题作提示；结尾：余韵或突转。

## (6) 该写什么 / 不该写什么

- 该写：钢琴套曲小品、艺术歌曲、性格对比、标题小品、内声部复调。
- 不该写：瓦格纳式长线条、空洞炫技、无调性、单乐章绵延、煽情电影配乐式 swell、打击性粗暴。
- Negative prompt: `no long Wagnerian line, no empty virtuosity, no atonal wandering, no single-movement sprawl, no sentimental film-score swell, no percussive brutality`

## (7) 测试提示词示例（现代题材：现代城市街角小便利店的深夜场景）

- Prompt: `In the style of Robert Schumann, a quiet night scene at a small convenience store in a modern city, Literary piano cycles, Florestan fire and Eusebius dream, short character pieces, songful melody, inner voices, harmonic detour`
- 中文对照：罗伯特·舒曼风格，现代城市街角小便利店的深夜场景，文学性钢琴套曲，热情与梦幻两种性格对置，短小性格小品，歌唱性旋律，活跃的内声部，迂回的和声。
- Negative: `no long Wagnerian line, no empty virtuosity, no atonal wandering, no single-movement sprawl, no sentimental film-score swell, no percussive brutality`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
