# Carlos Chávez — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Mexican composition, pre-Columbian percussion and modes, lean neoclassical counterpoint, folk melody without Romantic excess`
- ZH: 墨西哥作曲，前哥伦布打击乐与调式，精简新古典对位，民间旋律而无浪漫滥情。

## (2) 旋律与和声

- 旋律：墨西哥民间与印第安调式轮廓，级进为主，动机短小、克制。
- 和声：调式与功能和声混合，精简；主：民间调式；禁：浪漫式半音堆砌；不协和度中低，解决靠对位。

## (3) 节奏与织体

- 节奏：印第安打击律动，复节奏与不规则重音；织体：复调与打击层，密度中等，留白清晰。

## (4) 配器与音色

- 配器：管弦乐加印第安打击乐；音色：干、冷、带石质感；力度：动态中等，重音清晰。

## (5) 曲式与结构

- 曲式：交响曲、组曲；结构：民间主题—对位发展—再现；高潮在打击与对位叠加处；结尾常以重音收束。

## (6) 该写什么 / 不该写什么

- 该写：印第安调式旋律、前哥伦布打击乐、精简对位、克制的民间色彩。
- 不该写：浪漫式半音堆砌、华丽管弦铺陈、无民间根源的抽象、单声部民歌照搬。
- Negative prompt: `No Romantic chromatic excess, no lavish orchestral padding, no rootless abstraction, no bare folk-song quotation, no sentimental swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Carlos Chávez, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a pre-Columbian percussion pattern, a lean folk-mode melody, neoclassical counterpoint, dry and clear texture`
- 中文对照：查韦斯风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，前哥伦布打击律动，精简民间调式旋律，新古典对位，干爽清晰织体。。
- Negative: `No Romantic chromatic excess, no lavish orchestral padding, no rootless abstraction, no bare folk-song quotation, no sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
