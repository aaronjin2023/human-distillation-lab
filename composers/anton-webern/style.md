# Anton Webern — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Pointillist brevity, twelve-tone crystal, Klangfarbenmelodie, silence as structure, palindrome form, extreme concision`
- ZH: 点描式简洁，十二音水晶，音色旋律，静默即结构，回文形式，极致简洁。

## (2) 旋律与和声

- 旋律：点描式，短音点；和声：十二音序列。禁：功能和声。调性缺席，序列即结构。

## (3) 节奏与织体

- 节奏：稀疏、静默；织体：点描，留白。

## (4) 配器与音色

- 乐器：小型管弦乐、室内乐、合唱；音色：晶莹、透明；力度：极弱为主。

## (5) 曲式与结构

- 曲式：小品、交响曲、康塔塔；结构：回文、对称；结尾：渐弱或悬置。

## (6) 该写什么 / 不该写什么

- 该写：点描式简洁、十二音序列、音色旋律、静默结构、回文形式。
- 不该写：功能和声、浪漫长线条、厚重配器、响亮高潮、过度煽情、流行和弦循环。
- Negative prompt: `no functional harmony, no long Romantic line, no thick orchestration, no loud climax, no sentimental excess, no pop chord loop`

## (7) 测试提示词示例（现代题材：午夜空街上亮着灯的自动售货机）

- Prompt: `In the style of Anton Webern, a vending machine glowing at midnight on an empty street, Pointillist brevity, twelve-tone crystal, Klangfarbenmelodie, silence as structure, palindrome form, extreme concision`
- 中文对照：安东·韦伯恩风格，午夜空街上亮着灯的自动售货机，点描式简洁，十二音水晶，音色旋律，静默即结构，回文形式，极致简洁。
- Negative: `no functional harmony, no long Romantic line, no thick orchestration, no loud climax, no sentimental excess, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
