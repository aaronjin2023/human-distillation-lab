# Arnold Schoenberg — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Twelve-tone row, Sprechstimme, expressionist intensity, developing variation, atonal freedom, row as unity`
- ZH: 十二音序列，朗诵调，表现主义强度，发展变奏，无调性自由，音列即统一。

## (2) 旋律与和声

- 旋律：序列变形，跳进为主；和声：十二音序列、无调性。禁：功能和声。调性缺席，序列即统一。

## (3) 节奏与织体

- 节奏：自由、表现主义；织体：复调与主调交织。

## (4) 配器与音色

- 乐器：室内乐、管弦乐、人声；音色：冷峻、紧张；力度：极端对比。

## (5) 曲式与结构

- 曲式：组曲、清唱剧、室内乐；结构：序列变形组织；结尾：悬置或收束。

## (6) 该写什么 / 不该写什么

- 该写：十二音序列、朗诵调、表现主义强度、发展变奏、序列变形。
- 不该写：功能和声、调性解决、浪漫旋律、过度煽情、流行和弦循环、节拍器式僵硬。
- Negative prompt: `no functional harmony, no tonal resolution, no Romantic melody, no sentimental excess, no pop chord loop, no metronomic rigidity`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，晨光中）

- Prompt: `In the style of Arnold Schoenberg, a cup of coffee sitting on a windowsill in the morning light, Twelve-tone row, Sprechstimme, expressionist intensity, developing variation, atonal freedom, row as unity`
- 中文对照：阿诺德·勋伯格风格，一杯放在窗台上的咖啡，晨光中，十二音序列，朗诵调，表现主义强度，发展变奏，无调性自由，音列即统一。
- Negative: `no functional harmony, no tonal resolution, no Romantic melody, no sentimental excess, no pop chord loop, no metronomic rigidity`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
