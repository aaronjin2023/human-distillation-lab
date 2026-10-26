# Hildegard von Bingen — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Medieval plainchant, soaring melismatic lines, wide leaps of fourths and fifths, modal, free rhythm, single unaccompanied female voices, ecstatic and luminous`
- ZH: 中世纪素歌，翱翔的 melisma 长句，四度五度大跳，调式，自由节奏，无伴奏女声，狂喜而明亮。

## (2) 音高与和声方向

- 主：教会调式（多利亚等），单声线条，无和声进行；音高围绕一个中心音盘旋、扩展。禁：功能和声、属—主解决、三和弦堆叠。调性：调式中心稳定，但旋律游移幅度大；不协和几乎不存在，解决靠回到中心音。

## (3) 旋律与节奏

- 旋律：级进中突然大跳（四度、五度、八度），音域宽（常超八度），长 melisma（一音多音节），呼吸长、拱形线条。节奏：自由节奏，无固定拍子，跟随歌词音节。织体：单声；偶有简单平行（四度/五度）与应答。

## (4) 配器与音色

- 人声：无伴奏女声合唱 / 独唱；魔鬼角色只说不唱（传说如此，见 conflicts）。音色：清亮、素净、无乐器装饰；泛音靠人声共鸣。力度：弱—中，靠旋律高低起伏而非力度对比。

## (5) 曲式与结构

- 曲式：应答轮唱（antiphon / responsory）与连祷式结构；《美德剧》为道德剧，17 种美德依次出场。结构：旋律公式反复变奏，同一公式加音、减音、移位。高潮在音域最高点而非和声高潮。结尾：回到中心音，平静收束。

## (6) 该写什么 / 不该写什么

- 该写：素歌长句、调式 melisma、宽音域拱形旋律、应答式圣咏、灵性题材的声乐。
- 不该写：功能和声、固定节拍、乐队配器、半音化泛滥、世俗舞曲节奏。
- Negative prompt: `functional harmony, fixed metre, orchestral accompaniment, rampant chromaticism, dance rhythm, sentimental film-score swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Hildegard von Bingen, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, medieval plainchant, soaring melismatic lines, wide leaps of fourths and fifths, modal, free rhythm, unaccompanied female voices, luminous and ecstatic`
- 中文对照：希尔德加德风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，中世纪素歌，翱翔的 melisma 长句，四五度大跳，调式，自由节奏，无伴奏女声，明亮狂喜。
- Negative: `functional harmony, fixed metre, orchestral accompaniment, chromaticism, dance rhythm`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
