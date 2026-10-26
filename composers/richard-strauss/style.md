# Richard Strauss — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Lush orchestration, tone poem, waltz elegance, soaring vocal line, horn and violin solos, late-Romantic opulence`
- ZH: 华丽配器，交响诗，圆舞曲优雅，高扬声乐线条，圆号与小提琴独奏，晚期浪漫的丰盈。

## (2) 旋律与和声

- 旋律：歌唱性长线条，圆舞曲；和声：晚期浪漫功能和声，半音浓烈。禁：无调性。调性清晰，色彩靠配器。

## (3) 节奏与织体

- 节奏：圆舞曲、进行曲；织体：管弦乐主导，旋律突出。

## (4) 配器与音色

- 乐器：大管弦乐，圆号与小提琴独奏；音色：华丽、浓烈；力度：极端对比。

## (5) 曲式与结构

- 曲式：交响诗、歌剧、艺术歌曲；结构：单乐章或分幕；结尾：辉煌或渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：华丽配器、交响诗、圆舞曲、歌唱性旋律、圆号独奏。
- 不该写：无调性、单薄室内乐织体、学院式枯燥对位、冷漠疏离、流行和弦循环、节拍器式僵硬。
- Negative prompt: `no atonal wandering, no thin chamber texture, no dry academic counterpoint, no ironic detachment, no pop chord loop, no metronomic rigidity`

## (7) 测试提示词示例（现代题材：午夜空街上亮着灯的自动售货机）

- Prompt: `In the style of Richard Strauss, a vending machine glowing at midnight on an empty street, Lush orchestration, tone poem, waltz elegance, soaring vocal line, horn and violin solos, late-Romantic opulence`
- 中文对照：理查·施特劳斯风格，午夜空街上亮着灯的自动售货机，华丽配器，交响诗，圆舞曲优雅，高扬声乐线条，圆号与小提琴独奏，晚期浪漫的丰盈。
- Negative: `no atonal wandering, no thin chamber texture, no dry academic counterpoint, no ironic detachment, no pop chord loop, no metronomic rigidity`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
