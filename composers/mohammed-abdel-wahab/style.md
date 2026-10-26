# Mohammed Abdel Wahab — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Arabic song composition, maqam melody, tarab long lines, oud-led ornamentation, Western orchestra fused with Arabic modes`
- ZH: 阿拉伯歌曲作曲，玛卡姆旋律，塔拉布长线，乌德主导装饰，西方管弦融合阿拉伯调式。

## (2) 旋律与和声

- 旋律：玛卡姆音阶长线，装饰音与滑音丰富，音域宽，呼吸长，歌唱性极强。
- 和声：玛卡姆调式为主，西方和声为辅；主：玛卡姆；禁：纯西方功能和声；不协和靠装饰音解决。

## (3) 节奏与织体

- 节奏：自由塔拉布与规整节拍交替；织体：乌德与人声主导加管弦，密度中，留白靠长装饰。

## (4) 配器与音色

- 配器：乌德、人声、管弦、打击；音色：温暖、共鸣丰富；力度：由弱渐强，塔拉布高潮在装饰最密处。

## (5) 曲式与结构

- 曲式：长歌曲式，主题—装饰变奏—再现；结构：引子—长线展开—高潮；结尾常以主音长音收束。

## (6) 该写什么 / 不该写什么

- 该写：玛卡姆长线旋律、乌德装饰、塔拉布高潮、西方管弦与阿拉伯调式融合。
- 不该写：纯西方功能和声、短曲式流行歌、无装饰的直白旋律、无玛卡姆的即兴。
- Negative prompt: `No pure Western functional harmony, no short pop song form, no plain melody without ornament, no improvisation without a maqam, no climax without tarab build-up`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Mohammed Abdel Wahab, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a maqam melody, oud ornamentation, a long tarab line, warm strings underneath`
- 中文对照：阿卜杜勒·瓦哈卜风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，玛卡姆旋律，乌德装饰，悠长塔拉布线条，温暖弦乐衬底。。
- Negative: `No pure Western functional harmony, no short pop song form, no plain melody without ornament, no improvisation without a maqam, no climax without tarab build-up`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
