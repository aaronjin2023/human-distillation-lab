# Antônio Carlos Jobim — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Bossa nova composition, gentle samba rhythm, jazz harmony with Brazilian melody, soft dissonance, intimate and understated`
- ZH: 波萨诺瓦作曲，轻柔桑巴律动，爵士和声加巴西旋律，柔和不协和，亲密而克制。

## (2) 旋律与和声

- 旋律：巴西歌谣轮廓，级进长线，音域适中，歌唱性极强，动机简短、重复中微变。
- 和声：爵士和声（大七、九和弦）加巴西调式；主：大调爵士和声；禁：密集半音与属—主套路；不协和度低中，解决温和、延迟。

## (3) 节奏与织体

- 节奏：波萨诺瓦轻柔切分，2/4 桑巴律动；织体：吉他与钢琴轻织体，密度低，留白温和。

## (4) 配器与音色

- 配器：吉他、钢琴、弦乐、轻打击、人声；音色：温暖、柔软、带海风感；力度：弱到中弱，极少强音。

## (5) 曲式与结构

- 曲式：歌曲式 AABA；结构：主题—桥段—再现；高潮在桥段的和声转折；结尾常渐弱、留有余温。

## (6) 该写什么 / 不该写什么

- 该写：波萨诺瓦轻柔切分、爵士和声的巴西旋律、大七九和弦色彩、克制的歌曲式结构。
- 不该写：强烈的桑巴打击、密集半音、属—主套路、大音量管弦全奏。
- Negative prompt: `No heavy samba percussion, no dense chromaticism, no formulaic dominant-tonic cadence, no loud orchestral tutti, no loud climax`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Antônio Carlos Jobim, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, a gentle bossa nova rhythm, a soft jazz-harmony melody, warm guitar and piano, intimate and understated`
- 中文对照：若比姆风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，轻柔波萨诺瓦律动，爵士和声旋律，温暖吉他与钢琴，亲密克制。。
- Negative: `No heavy samba percussion, no dense chromaticism, no formulaic dominant-tonic cadence, no loud orchestral tutti, no loud climax`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
