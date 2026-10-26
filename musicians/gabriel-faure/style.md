# Gabriel Fauré — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Modal subtlety, quiet harmony, restrained lyricism, late style austere and luminous, French understatement`
- ZH: 调式微妙，静谧和声，克制抒情，晚期风格简省 而明亮，法国式含蓄

## (2) 音高与和声方向

- 主：调式和声（多利亚、利底亚）、功能和声弱化，半音作微妙色彩；禁：瓦格纳式半音迷雾、煽情高潮。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性长线，音域窄、起伏小，呼吸长；节奏：平稳、少切分，流动如散文；织体：主调 + 轻复调，织体薄、透明。`artifact`

## (4) 配器与音色

- 配器：管弦乐轻、透明，弦乐柔和，木管歌唱；《安魂曲》不用小号与定音鼓的末日轰鸣（与威尔第对比）；音色柔、暖、静。`artifact`

## (5) 曲式与结构

- 曲式：安魂曲七乐章（无末日经全奏）、组曲式、歌曲集；结尾多极弱、宁静收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：调式歌唱旋律、静谧和声、克制抒情、宁静收束
- 不该写：半音迷雾、煽情高潮、厚重配器
- Negative prompt: `chromatic fog, sentimental climax, heavy orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Gabriel Faure, a 30-second piece for a small Yorkshire terrier sitting on a subway seat at night, a quiet modal melody, subtle harmony, restrained lyricism, transparent strings, ending in a soft luminous close`
- 中文对照：福雷风格，为夜里坐在地铁座位上的约克夏犬写 30 秒小品，静谧调式旋律，微妙和声，克制抒情，透明弦乐，以柔和明亮收束
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
