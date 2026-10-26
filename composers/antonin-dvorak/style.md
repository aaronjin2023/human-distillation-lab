# Antonín Dvořák — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Bohemian folk melody, dance rhythms, warm orchestration, pentatonic colour, classical forms with folk soul`
- ZH: 波希米亚民间旋律，舞曲节奏，温暖配器，五声音阶色彩，古典曲式中的民间灵魂。

## (2) 旋律与和声

- 旋律：民间歌唱性，级进为主；和声：功能和声，五声音阶作色彩。禁：无调性、瓦格纳式绵延。调性清晰，民间调式点缀。

## (3) 节奏与织体

- 节奏：波尔卡、弗里安特舞曲节奏；织体：主调为主，旋律突出。

## (4) 配器与音色

- 乐器：管弦乐，木管与弦乐并重；音色：温暖、明亮；力度：中强为主。

## (5) 曲式与结构

- 曲式：交响曲、协奏曲、舞曲集；结构：四乐章或舞曲并置；结尾：明朗收束。

## (6) 该写什么 / 不该写什么

- 该写：波希米亚民间旋律、斯拉夫舞曲、五声音阶、古典曲式、温暖管弦乐。
- 不该写：无调性、瓦格纳式半音绵延、学院式枯燥对位、单薄织体、冷漠疏离、流行和弦循环。
- Negative prompt: `no atonal wandering, no Wagnerian chromatic sprawl, no dry academic counterpoint, no thin texture, no ironic detachment, no pop chord loop`

## (7) 测试提示词示例（现代题材：午夜空街上亮着灯的自动售货机）

- Prompt: `In the style of Antonín Dvořák, a vending machine glowing at midnight on an empty street, Bohemian folk melody, dance rhythms, warm orchestration, pentatonic colour, classical forms with folk soul`
- 中文对照：安东宁·德沃夏克风格，午夜空街上亮着灯的自动售货机，波希米亚民间旋律，舞曲节奏，温暖配器，五声音阶色彩，古典曲式中的民间灵魂。
- Negative: `no atonal wandering, no Wagnerian chromatic sprawl, no dry academic counterpoint, no thin texture, no ironic detachment, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
