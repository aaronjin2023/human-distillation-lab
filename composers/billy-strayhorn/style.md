# Billy Strayhorn — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Lush chromatic harmony, lyrical melody, sophisticated big-band writing, Ellington colour with more harmonic daring, ballad intimacy`
- ZH: 丰满半音和声，抒情旋律，精致大乐队写法，艾灵顿音色而和声更大胆，叙事曲亲密感。

## (2) 旋律与和声

- 旋律：抒情长线，级进与半音交替；《Lush Life》旋律复杂而歌唱。`artifact`
- 和声：半音化丰富，扩展和弦；调性游移，解决温和而出人意料。`artifact`

## (3) 节奏与织体

- 节奏：摇摆与叙事曲自由节奏并存；织体：大乐队透明，独奏突出。

## (4) 配器与音色

- 配器：大乐队，弱音铜管与萨克斯；叙事曲中钢琴与独奏突出。

## (5) 曲式与结构

- 曲式：歌曲、叙事曲；结构简洁，高潮克制，结尾常渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：丰满半音和声、抒情长线旋律、大乐队透明配器、叙事曲亲密感、摇摆节奏。
- 不该写：simple diatonic pop harmony、no atonal wandering、no loud big-band blast as the main colour、no sentimental swell、no free improvisation without a written theme。
- Negative prompt: `No simple diatonic pop harmony, no atonal wandering, no loud big-band blast as the main colour, no sentimental swell, no free improvisation without a written theme`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Billy Strayhorn, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, lush chromatic harmony, lyrical long line, muted brass, intimate ballad warmth`
- 中文对照：斯特雷霍恩风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，丰满半音和声，抒情长线，弱音铜管，叙事曲亲密温暖感。
- Negative: `No simple diatonic pop harmony, no atonal wandering, no loud big-band blast as the main colour, no sentimental swell, no free improvisation without a written theme`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
