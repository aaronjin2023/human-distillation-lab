# Johann Sebastian Bach — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Baroque counterpoint, strict fugue, walking bass, clear tonal harmony, ornamented melodic lines, balanced phrases, sacred and secular forms in equal measure`
- ZH: 巴洛克对位，严格赋格，行走低音，清晰调性和声，装饰性旋律线条，均衡乐句，圣俗体裁并重。

## (2) 音高与和声方向

- 主：大调—小调功能和声；属—主收束明确；半音化为转调服务；赋格中的对位和声。禁：无调性、半音滥用、功能和声之外的随意半音。调性：调性稳定，转调靠模进与半音；不协和按规则解决。

## (3) 旋律与节奏

- 旋律：级进为主，跳进后弥补；装饰音丰富；主题短小、富于发展可能。节奏：行走低音驱动，节奏稳定；舞曲节奏清晰。织体：复调为主，四—五声部；主调为辅。

## (4) 配器与音色

- 乐器：管风琴、羽管键琴、小提琴、弦乐、管乐、合唱。音色：均衡、庄严、富于层次。力度：靠声部与配器对比。

## (5) 曲式与结构

- 曲式：赋格、卡农、变奏曲、组曲、协奏曲、弥撒、受难曲、康塔塔。结构：主题—答题—对题—展开—再现；高潮在赋格展开最密处。结尾：庄重收束，常以属—主完全终止。

## (6) 该写什么 / 不该写什么

- 该写：赋格、卡农、变奏曲、行走低音、弥撒与受难曲、协奏曲。
- 不该写：无对位的单声旋律堆砌、功能和声之外的随意半音、无调性、流行和弦循环。
- Negative prompt: `free atonal wandering, random dissonance, pop chord loop, no counterpoint, sentimental film-score swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of J. S. Bach, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, strict counterpoint, walking bass, clear tonal harmony, ornamented melody, balanced phrases, harpsichord and strings`
- 中文对照：巴赫风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，严格对位，行走低音，清晰调性和声，装饰性旋律，均衡乐句，羽管键琴与弦乐。
- Negative: `free atonal wandering, random dissonance, pop chord loop, no counterpoint, sentimental film-score swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
