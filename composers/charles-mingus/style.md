# Charles Mingus — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz composition, hard bop and gospel roots, collective improvisation, shout chorus, blues form stretched to suite scale, bass-led counterpoint`
- ZH: 爵士作曲，硬波普与福音根源，集体即兴，呼喊式合唱，布鲁斯曲式拉伸为组曲规模，低音主导的对位。

## (2) 旋律与和声

- 旋律：布鲁斯音阶与福音式呼喊轮廓，大跳与滑音并存，主题短小、口号感强，器乐化人声线条。
- 和声：布鲁斯进行为骨架，叠加半音经过与多调性摩擦；主：小调布鲁斯、属七堆叠；禁：学院式功能和声的平滑解决；不协和度中高，靠集体声部张力解决。

## (3) 节奏与织体

- 节奏：摇摆律动为底，复节奏与突然停顿、 tempo 伸缩；织体：多声部集体即兴，声部密度高，留白靠突然的齐奏收束。

## (4) 配器与音色

- 配器：中型爵士乐队（萨克斯、铜管、钢琴、低音、鼓），低音提琴既是节奏引擎又是旋律声部；音色粗粝、带人声喊叫感；力度对比极端。

## (5) 曲式与结构

- 曲式：布鲁斯与 AABA 拉伸为多乐章组曲；结构：主题—集体即兴—呼喊合唱—再现；高潮在集体即兴最密处；结尾常以齐奏重音收束。

## (6) 该写什么 / 不该写什么

- 该写：布鲁斯主题与福音呼喊、集体即兴段落、多乐章爵士组曲、低音主导的对位线条。
- 不该写：规整的 AABA 流行歌、平滑的学院和声解决、单声部独奏加伴奏、无张力的背景爵士。
- Negative prompt: `No smooth academic harmony, no tidy pop AABA form, no solo-with-backing texture, no polite background jazz, no swing without tension`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Charles Mingus, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, blues shout chorus, collective improvisation, bass-led counterpoint, sudden stops, gospel-tinged brass`
- 中文对照：明格斯风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，布鲁斯呼喊合唱，集体即兴，低音主导对位，突然停顿，福音味铜管。。
- Negative: `No smooth academic harmony, no tidy pop AABA form, no solo-with-backing texture, no polite background jazz, no swing without tension`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
