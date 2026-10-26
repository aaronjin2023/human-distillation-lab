# Heitor Villa-Lobos — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Brazilian composition, Bach counterpoint fused with folk melody, guitar and street song, dense polyphony, national colour without folklore quotation alone`
- ZH: 巴西作曲，巴赫对位融合民间旋律，吉他与街头歌谣，密集复调，民族色彩而不止于民歌引用。

## (2) 旋律与和声

- 旋律：巴西民间歌谣轮廓，级进与跳进并存，歌唱性强，动机带舞蹈感。
- 和声：功能和声加民间调式色彩；主：大调—小调、民间调式；禁：无调性；不协和度中，解决靠对位声部。

## (3) 节奏与织体

- 节奏：巴西舞蹈律动，切分与复节奏；织体：复调为主，声部密度高，吉他织体穿插。

## (4) 配器与音色

- 配器：管弦乐、吉他、合唱、打击；音色：明亮、热烈、带街头感；力度：动态宽，舞蹈段落突强。

## (5) 曲式与结构

- 曲式：组曲与巴赫式曲式并置；结构：民间主题—对位发展—再现；高潮在复调最密处；结尾常以舞蹈节奏收束。

## (6) 该写什么 / 不该写什么

- 该写：巴西民间旋律与巴赫对位、吉他织体、舞蹈律动组曲、合唱与管弦的民间色彩。
- 不该写：纯欧洲学院对位、无民间根源的抽象现代主义、单声部民歌照搬、无律动的抒情堆砌。
- Negative prompt: `No pure European academic counterpoint, no rootless abstract modernism, no bare folk-song quotation, no lyricism without dance rhythm, no atonal wandering`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Heitor Villa-Lobos, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Brazilian folk melody, Bach-like counterpoint, guitar colour, dance rhythm, warm orchestral colour`
- 中文对照：维拉-洛博斯风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，巴西民间旋律，巴赫式对位，吉他色彩，舞蹈律动，温暖管弦。。
- Negative: `No pure European academic counterpoint, no rootless abstract modernism, no bare folk-song quotation, no lyricism without dance rhythm, no atonal wandering`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
