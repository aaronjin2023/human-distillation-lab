# Johann Sebastian Bach — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Baroque counterpoint, strict fugue, walking bass, clear tonal harmony, ornamented melodic lines, balanced phrases, sacred and secular forms in equal measure`
- ZH: 巴洛克对位，严格赋格，行走低音，清晰调性和声，装饰性旋律线条，均衡乐句，圣俗体裁并重。

## (2) 旋律与和声

- 旋律：级进为主，跳进后弥补；装饰音丰富；主题短小、富于发展可能。`artifact` 和声：大调—小调功能和声，属—主收束明确；半音化为转调服务；赋格中的对位和声；禁用功能和声之外的随意半音。调性：调性稳定，转调靠模进与半音。

## (3) 节奏与织体

- 节奏：行走低音驱动，节奏稳定；舞曲节奏清晰。织体：复调为主，四—五声部；主调为辅；留白靠声部减至二声部。

## (4) 配器与音色

- 配器与音色：管风琴、羽管键琴、小提琴、弦乐、管乐、合唱并重；音色均衡、庄严、富于层次；力度靠声部与配器对比。

## (5) 曲式与结构

- 曲式：赋格、卡农、变奏曲、组曲、协奏曲、弥撒、受难曲、康塔塔并重。结构：主题—答题—对题—展开—再现；高潮在赋格展开最密处；结尾庄重收束，常以属—主完全终止。

## (6) 该写什么 / 不该写什么

- 该写：赋格与卡农、行走低音、变奏曲（《哥德堡变奏曲》）、弥撒与受难曲、大协奏曲与组曲。
- 不该写：无对位的单声旋律堆砌、功能和声之外的随意半音、无调性、流行和弦循环、感伤的电影配乐式高潮。
- Negative prompt: `No free atonal wandering, no random dissonance, no pop chord loop, no counterpoint-free melody, no sentimental film-score swell`

## (7) 测试提示词示例（现代题材：深夜只亮着一盏台灯的空办公室）

- Prompt: `In the style of Johann Sebastian Bach, a 30-second piece for an empty office late at night with one desk lamp on, baroque counterpoint, strict fugue, walking bass, clear tonal harmony, ornamented melodic lines, balanced phrases, sacred and secular forms in equal measure`
- 中文对照：约翰·塞巴斯蒂安·巴赫风格，为深夜只亮着一盏台灯的空办公室写 30 秒配乐，巴洛克对位，严格赋格，行走低音，清晰调性和声，装饰性旋律线条，均衡乐句，圣俗体裁并重。
- Negative: `No free atonal wandering, no random dissonance, no pop chord loop, no counterpoint-free melody, no sentimental film-score swell`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
