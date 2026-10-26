# Richard Wagner — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Endless melody, leitmotif, Tristan chromaticism, huge orchestra, music drama, long-range harmonic tension without resolution`
- ZH: 无终旋律，主导动机，特里斯坦式半音，超大管弦乐，乐剧，长程和声张力而不解决。

## (2) 旋律与和声

- 旋律：无终旋律，长线条无呼吸点；和声：半音化功能和声，推迟解决，属和弦绵延。禁：规整乐句收束。调性游移，解决一再推迟。

## (3) 节奏与织体

- 节奏：自由律动，管弦乐驱动；织体：管弦乐主导，人声为声部之一。

## (4) 配器与音色

- 乐器：超大管弦乐，瓦格纳大号、竖琴、铜管；音色：浓烈、绵密；力度：极端对比，持续高潮。

## (5) 曲式与结构

- 曲式：乐剧、主导动机网络；结构：多幕长篇，动机贯穿；结尾：解决或升华。

## (6) 该写什么 / 不该写什么

- 该写：主导动机、无终旋律、半音和声、超大管弦乐、乐剧长篇结构。
- 不该写：方正乐句、分曲咏叹调形式、快速解决、单薄室内乐织体、轻娱乐、无调性。
- Negative prompt: `no square phrasing, no closed aria form, no quick resolution, no thin chamber texture, no light entertainment, no atonal wandering`

## (7) 测试提示词示例（现代题材：现代城市街角小便利店的深夜场景）

- Prompt: `In the style of Richard Wagner, a quiet night scene at a small convenience store in a modern city, Endless melody, leitmotif, Tristan chromaticism, huge orchestra, music drama, long-range harmonic tension without resolution`
- 中文对照：理查德·瓦格纳风格，现代城市街角小便利店的深夜场景，无终旋律，主导动机，特里斯坦式半音，超大管弦乐，乐剧，长程和声张力而不解决。
- Negative: `no square phrasing, no closed aria form, no quick resolution, no thin chamber texture, no light entertainment, no atonal wandering`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
