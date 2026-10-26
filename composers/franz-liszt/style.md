# Franz Liszt — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Thematic transformation, virtuoso piano, symphonic poem, chromatic harmony, Hungarian verbunkos colour, single-movement architecture`
- ZH: 主题变形，炫技钢琴，交响诗，半音和声，匈牙利 verbunkos 色彩，单乐章结构。

## (2) 旋律与和声

- 旋律：主题变形，长线条与炫技音型交替；和声：半音化功能和声，增和弦、全音阶作色彩。禁：无调性。调性游移，靠主题变形收束。

## (3) 节奏与织体

- 节奏：匈牙利切分、自由节奏；织体：钢琴交响化，单乐器写全乐队。

## (4) 配器与音色

- 乐器：钢琴、管弦乐；音色：钢琴音域全开，管弦乐色彩浓烈；力度：ppp 到 fff 的极端对比。

## (5) 曲式与结构

- 曲式：交响诗、单乐章奏鸣曲、狂想曲；结构：主题变形贯穿全曲；结尾：辉煌收束。

## (6) 该写什么 / 不该写什么

- 该写：主题变形、交响诗、匈牙利狂想曲、单乐章奏鸣曲、钢琴炫技、半音和声。
- 不该写：无调性、静态重复、单薄沙龙小品、节拍器式僵硬、煽情电影配乐式 swell、流行和弦循环。
- Negative prompt: `no atonal wandering, no static repetition, no thin salon miniature, no metronomic rigidity, no sentimental film-score swell, no pop chord loop`

## (7) 测试提示词示例（现代题材：为一只坐在地铁座位上的小约克夏犬写 30 秒配乐）

- Prompt: `In the style of Franz Liszt, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Thematic transformation, virtuoso piano, symphonic poem, chromatic harmony, Hungarian verbunkos colour, single-movement architecture`
- 中文对照：弗朗茨·李斯特风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，主题变形，炫技钢琴，交响诗，半音和声，匈牙利 verbunkos 色彩，单乐章结构。
- Negative: `no atonal wandering, no static repetition, no thin salon miniature, no metronomic rigidity, no sentimental film-score swell, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
