# Florence Price — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Romantic symphonic form fused with spirituals and Juba dance, pentatonic melody, warm orchestration, Dvorak-influenced structure with Black folk idiom`
- ZH: 浪漫交响曲式融合灵歌与朱巴舞，五声音阶旋律，温暖配器，德沃夏克式结构中的黑人民间语汇。

## (2) 旋律与和声

- 旋律：五声音阶与灵歌式级进线条，歌唱性强；主题原创，不直接引用民间曲调。`artifact`
- 和声：浪漫主义功能和声为底，蓝调音与五声色彩点缀；转调温和，解决明确。`artifact`

## (3) 节奏与织体

- 节奏：朱巴舞的切分与跺脚节奏替代传统谐谑曲；灵歌节奏自由而富于呼吸；织体：主调为主，复调点缀。

## (4) 配器与音色

- 配器：浪漫派大编制，弦乐温暖，木管歌唱，打击乐点出舞曲节奏；钢琴协奏曲独奏与乐队对答抒情。

## (5) 曲式与结构

- 曲式：四乐章交响曲，第三乐章以朱巴舞代谐谑曲；组曲式结构；高潮在乐章后段，结尾温暖收束。

## (6) 该写什么 / 不该写什么

- 该写：灵歌式五声旋律、朱巴舞节奏、浪漫交响曲式、温暖弦乐配器、钢琴协奏曲抒情对答。
- 不该写：direct folk-song quotation presented as composition、no atonal wandering、no ironic march、no thin chamber texture as the main sound、no unresolved dissonance as climax。
- Negative prompt: `No direct folk-song quotation presented as composition, no atonal wandering, no ironic march, no thin chamber texture as the main sound, no unresolved dissonance as climax`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Florence Price, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, pentatonic spiritual-like melody, warm strings, gentle Juba dance rhythm`
- 中文对照：普赖斯风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，五声灵歌式旋律，温暖弦乐，轻柔朱巴舞节奏。
- Negative: `No direct folk-song quotation presented as composition, no atonal wandering, no ironic march, no thin chamber texture as the main sound, no unresolved dissonance as climax`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
