# Pyotr Ilyich Tchaikovsky — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Sweeping melody, ballet lyricism, lush orchestration, emotional climax, Russian folk colour within Western forms`
- ZH: 辽阔歌唱旋律，芭蕾抒情，浓烈配器，情感高潮，西方曲式中的俄国民间色彩。

## (2) 旋律与和声

- 旋律：长线条歌唱，级进与跳进并重；和声：功能和声，半音作情感色彩。禁：无调性。调性清晰，情感靠旋律与配器。

## (3) 节奏与织体

- 节奏：芭蕾舞曲节奏，圆舞曲；织体：主调为主，旋律突出。

## (4) 配器与音色

- 乐器：大管弦乐，弦乐歌唱，木管独奏；音色：浓烈、华丽；力度：极端对比，高潮饱满。

## (5) 曲式与结构

- 曲式：芭蕾、交响曲、协奏曲；结构：四乐章或舞剧分幕；结尾：辉煌或渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：芭蕾舞剧、歌唱性旋律、圆舞曲、管弦乐高潮、俄国民间色彩。
- 不该写：无调性、学院式枯燥对位、单薄室内乐织体、静态极简、冷漠疏离、流行和弦循环。
- Negative prompt: `no atonal wandering, no dry academic counterpoint, no thin chamber texture, no static minimalism, no ironic detachment, no pop chord loop`

## (7) 测试提示词示例（现代题材：现代城市街角小便利店的深夜场景）

- Prompt: `In the style of Pyotr Ilyich Tchaikovsky, a quiet night scene at a small convenience store in a modern city, Sweeping melody, ballet lyricism, lush orchestration, emotional climax, Russian folk colour within Western forms`
- 中文对照：彼得·伊里奇·柴可夫斯基风格，现代城市街角小便利店的深夜场景，辽阔歌唱旋律，芭蕾抒情，浓烈配器，情感高潮，西方曲式中的俄国民间色彩。
- Negative: `no atonal wandering, no dry academic counterpoint, no thin chamber texture, no static minimalism, no ironic detachment, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
