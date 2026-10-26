# Igor Stravinsky — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Irregular accent, ostinato, bitonality, rhythmic drive, folk fragments, neoclassical clarity, block juxtaposition`
- ZH: 不规则重音，固定音型，多调性，节奏驱动，民间碎片，新古典清晰，块状并置。

## (2) 旋律与和声

- 旋律：民间碎片，短小动机；和声：多调性、民间调式。禁：功能和声主导。调性并置，不协和直给。

## (3) 节奏与织体

- 节奏：不规则重音、固定音型；织体：块状并置。

## (4) 配器与音色

- 乐器：大管弦乐，打击乐突出；音色：原始、锐利；力度：极端对比。

## (5) 曲式与结构

- 曲式：芭蕾、组曲；结构：块状并置；结尾：突强或渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：不规则重音、固定音型、多调性、民间碎片、块状并置。
- 不该写：功能和声主导、圆滑浪漫长线条、无调性、过度煽情、节拍器式僵硬、流行和弦循环。
- Negative prompt: `no functional harmony dominance, no smooth Romantic line, no atonal wandering, no sentimental excess, no metronomic rigidity, no pop chord loop`

## (7) 测试提示词示例（现代题材：为一只坐在地铁座位上的小约克夏犬写 30 秒配乐）

- Prompt: `In the style of Igor Stravinsky, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Irregular accent, ostinato, bitonality, rhythmic drive, folk fragments, neoclassical clarity, block juxtaposition`
- 中文对照：伊戈尔·斯特拉文斯基风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，不规则重音，固定音型，多调性，节奏驱动，民间碎片，新古典清晰，块状并置。
- Negative: `no functional harmony dominance, no smooth Romantic line, no atonal wandering, no sentimental excess, no metronomic rigidity, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
