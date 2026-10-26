# Kaija Saariaho — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Spectral harmony, luminous orchestration, electronics blended with acoustic, voice as colour, slow transformation, dreamlike distance`
- ZH: 频谱和声，明亮配器，电子与原声融合，人声作音色，缓慢变形，梦幻距离感。

## (2) 旋律与和声

- 旋律：人声式长线，级进为主；小提琴独奏线条歌唱而富于泛音。`artifact`
- 和声：频谱和声——和弦源自泛音列；调性游移，色彩先于功能。`artifact`

## (3) 节奏与织体

- 节奏：缓慢流动，少用强拍；织体：多层音色叠加，密度渐变。

## (4) 配器与音色

- 配器：电子与管弦融合，竖琴、打击乐、弦乐泛音；人声作音色层。

## (5) 曲式与结构

- 曲式：歌剧、协奏曲、管弦乐；结构靠音色变形，高潮缓慢到达，结尾常渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：频谱和声、电子与原声融合、人声作音色、缓慢音色变形、明亮管弦配器、梦幻距离感。
- 不该写：functional harmony as structure、no Germanic motivic development、no regular metre throughout、no dense counterpoint、no sentimental swell、no loud climax without slow build。
- Negative prompt: `No functional harmony as structure, no Germanic motivic development, no regular metre throughout, no dense counterpoint, no sentimental swell, no loud climax without slow build`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Kaija Saariaho, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, spectral harmony, luminous strings and harp, slow timbral transformation, dreamlike distance`
- 中文对照：萨里亚霍风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，频谱和声，明亮弦乐与竖琴，缓慢音色变形，梦幻距离感。
- Negative: `No functional harmony as structure, no Germanic motivic development, no regular metre throughout, no dense counterpoint, no sentimental swell, no loud climax without slow build`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
