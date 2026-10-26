# Edvard Grieg — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Norwegian folk melody, Hardanger fiddle colour, short lyric pieces, mountain air in miniature forms`
- ZH: 挪威民间旋律，哈丹格小提琴色彩，短小抒情小品，微型体裁里的山间空气

## (2) 音高与和声方向

- 主：功能和声 + 挪威民间调式（利底亚、混合利底亚）、五声片段；禁：德国式厚重半音、为宏大而宏大的和声。`artifact`

## (3) 旋律与节奏

- 旋律：民间歌唱线，短小、级进，装饰如民间小提琴；节奏：哈林舞曲（halling）跳跃节奏、民歌三拍子；织体：主调，钢琴小品织体清，管弦乐轻盈。`artifact`

## (4) 配器与音色

- 配器：钢琴小品为主，管弦乐轻盈（《培尔·金特》组曲），民间乐器色彩以管弦乐模拟；音色清、亮、冷中带暖。`artifact`

## (5) 曲式与结构

- 曲式：抒情小品组曲式、钢琴协奏曲三乐章、戏剧配乐组曲；每首短小，一个性格；结尾多温柔收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：挪威民间旋律、抒情小品、哈林舞曲节奏、山间音色
- 不该写：德国式厚重、为宏大而宏大、无民间色彩的直白抒情
- Negative prompt: `German heaviness, bombast, plain lyricism without folk colour`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Edvard Grieg, a 30-second lyric piece for a small Yorkshire terrier sitting on a subway seat, a short Norwegian folk-like melody, clear piano texture, mountain air, tender and fresh, like a Lyric Piece`
- 中文对照：格里格风格，为地铁座位上的约克夏犬写 30 秒抒情小品，短小挪威民间式旋律，清晰钢琴织体，山间空气，温柔清新，如一首《抒情小品》
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
