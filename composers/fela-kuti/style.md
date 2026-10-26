# Fela Kuti — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Afrobeat composition, long hypnotic grooves, call-and-response horns, Yoruba rhythm, political chant over relentless percussion`
- ZH: Afrobeat 作曲，悠长催眠律动，呼应式铜管，约鲁巴律动，政治 chant 衬以不懈打击。

## (2) 旋律与和声

- 旋律：呼应式短句，级进与重复，歌唱性让位于口号感，动机循环中微变。
- 和声：调式与单和弦循环，功能和声极简；主：小调调式循环；禁：复杂和声进行；不协和度低，解决靠律动而非和声。

## (3) 节奏与织体

- 节奏：Afrobeat 复节奏，打击层叠加，悠长、催眠；织体：打击与铜管层叠，密度高，留白靠律动呼吸。

## (4) 配器与音色

- 配器：打击、贝斯、吉他、铜管、键盘、人声；音色：粗粝、热烈、带街头感；力度：中强持续，极少弱音。

## (5) 曲式与结构

- 曲式：长律动循环，呼应段落拼贴；结构：律动建立—铜管呼应—人声 chant—再现；高潮在层叠最密处；结尾常以律动渐弱。

## (6) 该写什么 / 不该写什么

- 该写：悠长 Afrobeat 律动、呼应式铜管、单和弦调式循环、口号式人声 chant。
- 不该写：复杂和声进行、短曲式流行歌、无律动的抒情、西方管弦铺陈。
- Negative prompt: `No complex harmonic progression, no short pop song form, no lyricism without groove, no Western orchestral padding, no climax without a groove build-up`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Fela Kuti, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a long Afrobeat groove, call-and-response horns, a modal chant, relentless percussion`
- 中文对照：费拉·库蒂风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，悠长 Afrobeat 律动，呼应式铜管，调式 chant，不懈打击。。
- Negative: `No complex harmonic progression, no short pop song form, no lyricism without groove, no Western orchestral padding, no climax without a groove build-up`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
