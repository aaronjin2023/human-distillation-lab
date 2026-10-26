# Wolfgang Amadeus Mozart — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Classical perfection, balanced phrases, graceful melody, clear tonal harmony, operatic drama and instrumental elegance in perfect proportion`
- ZH: 古典完美，均衡乐句，优雅旋律，清晰调性和声，歌剧戏剧与器乐优雅的完美比例。

## (2) 音高与和声方向

- 主：功能和声清晰；奏鸣曲式调性布局；半音为转调与表情服务。禁：无调性、半音滥用。调性：调性稳定，转调优雅。（半音化与复调是莫扎特晚期风格的组成部分，如《朱庇特》终乐章的赋格式对位、《唐·乔瓦尼》《安魂曲》的半音化；禁的是滥用，不是半音化本身。）

## (3) 旋律与节奏

- 旋律：歌唱性强，级进为主，均衡乐句；主题短小、富于发展。节奏：清晰，舞曲与歌剧节奏交替。织体：主调为主，复调为辅；歌剧中声部对话。

## (4) 配器与音色

- 乐器：管弦乐队、钢琴、弦乐四重奏、歌剧人声。音色：明亮、透明、均衡。力度：靠配器与织体对比。

## (5) 曲式与结构

- 曲式：奏鸣曲式、歌剧（正歌剧、喜歌剧）、协奏曲、交响曲、弥撒。结构：呈示—展开—再现；歌剧以剧情结构定音乐结构。高潮在展开部与剧情转折处。结尾：明确收束。

## (6) 该写什么 / 不该写什么

- 该写：奏鸣曲式、歌剧、钢琴协奏曲、交响曲、均衡乐句、优雅旋律。
- 不该写：半音化滥用、无调性、复调的失控堆砌、炫技泛滥。
- Negative prompt: `aimless chromaticism, atonality, uncontrolled dense counterpoint, empty virtuosity, sentimental swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Wolfgang Amadeus Mozart, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Classical perfection, balanced phrases, graceful melody, clear tonal harmony, piano and strings, elegant and luminous`
- 中文对照：莫扎特风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，古典完美，均衡乐句，优雅旋律，清晰调性，钢琴与弦乐，优雅明亮。
- Negative: `aimless chromaticism, atonality, uncontrolled dense counterpoint, empty virtuosity, sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
