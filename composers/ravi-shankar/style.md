# Ravi Shankar — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Hindustani composition, raga melody, tala rhythm cycles, sitar-led alap to jhala arc, improvisation within fixed framework`
- ZH: 北印度古典作曲，拉格旋律，塔拉节奏循环，西塔琴主导的阿拉普到加拉弧线，固定框架内的即兴。

## (2) 旋律与和声

- 旋律：拉格音阶长线，滑音与装饰音丰富，音域宽，呼吸长，歌唱性与器乐性兼备。
- 和声：持续低音（坦普拉）上的旋律，无功能和声；主：拉格调式；禁：西方功能和声；不协和靠装饰音解决。

## (3) 节奏与织体

- 节奏：塔拉循环，自由阿拉普到固定节拍；织体：西塔琴独奏加坦普拉与塔布拉，密度由稀到密。

## (4) 配器与音色

- 配器：西塔琴、坦普拉、塔布拉，间或管弦乐；音色：共鸣丰富、带泛音；力度：由极弱渐强到极强。

## (5) 曲式与结构

- 曲式：阿拉普—焦尔—加拉弧线；结构：自由引子—节奏进入—加速；高潮在加拉最密处；结尾常以主音收束。

## (6) 该写什么 / 不该写什么

- 该写：拉格旋律与滑音、塔拉节奏循环、阿拉普到加拉的弧线、持续低音上的即兴。
- 不该写：西方功能和声、固定曲式的短曲、无拉格的即兴、管弦铺陈盖过西塔琴。
- Negative prompt: `No Western functional harmony, no fixed short song form, no improvisation without a raga, no orchestral padding over the sitar, no climax without the alap-to-jhala arc`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Ravi Shankar, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a raga melody on sitar, a slow alap opening, a tala cycle entering, sliding ornaments, drone underneath`
- 中文对照：拉维·香卡风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，西塔琴拉格旋律，缓慢阿拉普开场，塔拉循环进入，滑音装饰，持续低音衬底。。
- Negative: `No Western functional harmony, no fixed short song form, no improvisation without a raga, no orchestral padding over the sitar, no climax without the alap-to-jhala arc`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
