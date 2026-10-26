# Carl Philipp Emanuel Bach — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Empfindsamer Stil, sudden contrasts, sighing appoggiaturas, free fantasy, expressive keyboard writing, the bridge from Baroque to Classical`
- ZH: 情感风格，突然对比，叹息倚音，自由幻想曲，表现性键盘写作，巴洛克向古典的桥梁。

## (2) 音高与和声方向

- 主：功能和声 + 表现性半音；倚音（appoggiatura）为表情；突然转调。禁：无调性、半音滥用。调性：调性清晰，但转调突然；不协和为表情。

## (3) 旋律与节奏

- 旋律：歌唱性强，倚音与叹息音型；幻想曲旋律自由、断续。节奏：突然停顿、自由节奏（幻想曲）；奏鸣曲节奏清晰。织体：主调为主，复调为辅。

## (4) 配器与音色

- 乐器：羽管键琴 / 古钢琴、长笛、弦乐。音色：细腻、富于对比。力度：靠突然强弱对比（terraced dynamics 的细腻化）。

## (5) 曲式与结构

- 曲式：奏鸣曲、幻想曲、协奏曲、交响曲。结构：奏鸣曲式早期形态；幻想曲自由结构；高潮在突然对比处。结尾：明确收束。

## (6) 该写什么 / 不该写什么

- 该写：情感风格、倚音、幻想曲、键盘奏鸣曲、突然对比。
- 不该写：无调性、半音滥用、复调的失控堆砌、机械均衡。
- Negative prompt: `atonality, aimless chromaticism, uncontrolled dense counterpoint, mechanical symmetry, sentimental swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of C. P. E. Bach, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Empfindsamer Stil, sudden contrasts, sighing appoggiaturas, free fantasy, expressive keyboard, harpsichord and fortepiano, tender and surprising`
- 中文对照：C.P.E.巴赫风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，情感风格，突然对比，叹息倚音，自由幻想曲，表现性键盘，羽管键琴与古钢琴，温柔而出人意料。
- Negative: `atonality, aimless chromaticism, uncontrolled dense counterpoint, mechanical symmetry, sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
