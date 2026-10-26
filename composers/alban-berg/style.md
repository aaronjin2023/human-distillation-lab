# Alban Berg — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Second Viennese School twelve-tone lyricism, expressive row, Romantic warmth inside serial order, vocal declamation, arch form`
- ZH: 第二维也纳乐派十二音抒情，富于表现力的音列，序列秩序中的浪漫温情，声乐宣叙，拱形结构。

## (2) 旋律与和声

- 旋律：音列派生的长线条，半音级进与大跳交替，声乐线条近于说话—歌唱之间；器乐旋律常由音列的细胞变形而来。`artifact`
- 和声：十二音序列组织音高，保留三和弦残响与调性暗示；不协和是结构性的，非装饰性的；解决靠音列完成而非属—主。`artifact`

## (3) 节奏与织体

- 节奏：自由而富于呼吸，歌剧中按台词节奏组织；管弦乐以动机节奏细胞统一全曲；织体：复调与主调交替，室内乐式透明与全奏爆发并置。

## (4) 配器与音色

- 配器：歌剧大编制与室内乐编制并用；《小提琴协奏曲》独奏小提琴对大管弦乐，音色柔和而集中；善用弱音器、泛音与低声部铺垫。

## (5) 曲式与结构

- 曲式：歌剧用严格曲式框架（帕萨卡利亚、赋格、回旋曲）承载自由剧情；《小提琴协奏曲》两乐章拱形；高潮常在结构中点，结尾收束于音列的完整陈述。

## (6) 该写什么 / 不该写什么

- 该写：十二音音列的抒情变形、歌剧宣叙—咏叹交替、帕萨卡利亚与赋格等严格曲式、室内乐式透明配器、小提琴协奏曲式的长线条独奏。
- 不该写：tonal functional cadences as structural pillars、no diatonic folk melody、no free atonal wandering without a row、no lush Romantic climax without serial control、no operatic aria detached from the row。
- Negative prompt: `No tonal functional cadences as structural pillars, no diatonic folk melody, no free atonal wandering without a row, no lush Romantic climax without serial control, no operatic aria detached from the row`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Alban Berg, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, twelve-tone row turned into a lyrical vocal-like line, muted strings, restrained climax, arch form`
- 中文对照：贝尔格风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，十二音列化为抒情声乐线条，弱音弦乐，克制的高潮，拱形结构。
- Negative: `No tonal functional cadences as structural pillars, no diatonic folk melody, no free atonal wandering without a row, no lush Romantic climax without serial control, no operatic aria detached from the row`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
