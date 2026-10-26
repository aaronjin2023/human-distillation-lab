# Gustav Mahler — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Vast symphony, song and symphony fused, irony and folk song, huge orchestra, long-range climax, world in sound`
- ZH: 宏大交响曲，歌曲与交响融合，反讽与民歌，超大管弦乐，长程高潮，声音中的世界。

## (2) 旋律与和声

- 旋律：歌唱性长线条，民间旋律与艺术歌曲交织；和声：晚期浪漫功能和声，半音浓烈。禁：无调性。调性游移，靠动机收束。

## (3) 节奏与织体

- 节奏：进行曲、兰德勒舞曲；织体：管弦乐主导，声部密度高。

## (4) 配器与音色

- 乐器：超大管弦乐，独奏乐器突出；音色：浓烈、对比强烈；力度：极端对比。

## (5) 曲式与结构

- 曲式：交响曲、交响声乐；结构：五乐章或多乐章；结尾：升华或渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：超大交响曲、歌曲与交响融合、民间旋律、进行曲节奏、长程高潮。
- 不该写：无调性、单薄室内乐织体、冷漠疏离、短小品、流行和弦循环、节拍器式僵硬。
- Negative prompt: `no atonal wandering, no thin chamber texture, no ironic detachment, no short miniature, no pop chord loop, no metronomic rigidity`

## (7) 测试提示词示例（现代题材：现代城市街角小便利店的深夜场景）

- Prompt: `In the style of Gustav Mahler, a quiet night scene at a small convenience store in a modern city, Vast symphony, song and symphony fused, irony and folk song, huge orchestra, long-range climax, world in sound`
- 中文对照：古斯塔夫·马勒风格，现代城市街角小便利店的深夜场景，宏大交响曲，歌曲与交响融合，反讽与民歌，超大管弦乐，长程高潮，声音中的世界。
- Negative: `no atonal wandering, no thin chamber texture, no ironic detachment, no short miniature, no pop chord loop, no metronomic rigidity`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
