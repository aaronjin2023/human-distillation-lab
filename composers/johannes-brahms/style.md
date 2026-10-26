# Johannes Brahms — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Developing variation, classical forms, dense counterpoint, autumnal harmony, cross-rhythm, warm orchestral colour`
- ZH: 发展变奏，古典曲式，密集对位，秋意和声，交叉节奏，温暖的管弦乐色彩。

## (2) 旋律与和声

- 旋律：长线条，级进中带大跳；和声：功能和声，半音柔和，远关系转调。禁：瓦格纳式无终旋律。调性稳定，不协和按规则解决。

## (3) 节奏与织体

- 节奏：交叉节奏、切分；织体：复调与主调交织，声部密度高。

## (4) 配器与音色

- 乐器：管弦乐、室内乐、钢琴；音色：温暖、厚实，中音区浓；力度：中强为主，极少极端。

## (5) 曲式与结构

- 曲式：交响曲、协奏曲、变奏曲、安魂曲；结构：奏鸣曲式、帕萨卡里亚；结尾：庄重收束。

## (6) 该写什么 / 不该写什么

- 该写：发展变奏、古典曲式、帕萨卡里亚、交叉节奏、室内乐式管弦乐。
- 不该写：瓦格纳式无终旋律、无调性、空洞炫技、标题音乐图解、单薄织体、煽情电影配乐式 swell。
- Negative prompt: `no Wagnerian endless line, no atonal wandering, no empty virtuosity, no programmatic illustration, no thin texture, no sentimental film-score swell`

## (7) 测试提示词示例（现代题材：为一只坐在地铁座位上的小约克夏犬写 30 秒配乐）

- Prompt: `In the style of Johannes Brahms, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Developing variation, classical forms, dense counterpoint, autumnal harmony, cross-rhythm, warm orchestral colour`
- 中文对照：约翰内斯·勃拉姆斯风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，发展变奏，古典曲式，密集对位，秋意和声，交叉节奏，温暖的管弦乐色彩。
- Negative: `no Wagnerian endless line, no atonal wandering, no empty virtuosity, no programmatic illustration, no thin texture, no sentimental film-score swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
