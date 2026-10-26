# Isang Yun — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Korean contemporary composition, single-tone Hauptklang, ornamental main tone, East Asian breath, dense orchestral clouds around one pitch`
- ZH: 韩国当代作曲，单音主音（Hauptklang），装饰性主音，东亚呼吸，围绕一个音高的密集管弦云团。

## (2) 旋律与和声

- 旋律：单音主音加装饰，滑音与颤音丰富，音域窄，呼吸长，歌唱性让位于主音的展开。
- 和声：主音中心，无功能和声；主：单音主音；禁：属—主解决；不协和靠主音周围的装饰音簇。

## (3) 节奏与织体

- 节奏：自由、缓慢，长音与装饰交替；织体：主音加装饰音簇，密度中高，留白靠主音的持续。

## (4) 配器与音色

- 配器：管弦乐，双簧管、竖琴突出；音色：密集、带共鸣；力度：由弱渐强，主音云团是高潮。

## (5) 曲式与结构

- 曲式：单音展开式；结构：主音出现—装饰展开—云团—回归；高潮在装饰最密处；结尾常以主音长音收束。

## (6) 该写什么 / 不该写什么

- 该写：单音主音与装饰、东亚呼吸的长音、管弦云团、主音的展开与回归。
- 不该写：功能和声、规整曲式、多主题并置、无主音的自由无调性。
- Negative prompt: `No functional harmony, no rigid formal scheme, no multiple competing themes, no free atonality without a main tone, no climax without main-tone development`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Isang Yun, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a single main tone with ornaments, East Asian breath, an orchestral cloud gathering around one pitch, oboe and harp colour`
- 中文对照：尹伊桑风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，单音主音加装饰，东亚呼吸，围绕一个音高的管弦云团，双簧管与竖琴色彩。。
- Negative: `No functional harmony, no rigid formal scheme, no multiple competing themes, no free atonality without a main tone, no climax without main-tone development`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
