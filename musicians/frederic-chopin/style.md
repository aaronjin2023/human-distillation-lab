# Frédéric Chopin — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Piano alone, bel canto melody over chromatic harmony, rubato breathing, Polish dance rhythms, intimate and heroic by turns`
- ZH: 只写钢琴，声乐化旋律覆于半音和声之上，自由速度的呼吸，波兰舞曲节奏，亲密与英雄交替

## (2) 音高与和声方向

- 主：功能和声 + 大量半音、借调、那不勒斯和弦，调性游移但总有归宿；禁：无调性、机械的和声循环。`artifact`

## (3) 旋律与节奏

- 旋律：声乐化长线，装饰音是旋律本身（颤音、回音、倚音）；节奏：rubato——右手自由、左手稳住拍子，玛祖卡与波兰舞曲节奏是民族标记；织体：主调，左手和声—低音、右手歌唱。`artifact`

## (4) 配器与音色

- 配器：只用钢琴；音色靠触键与踏板分层（弱音的透明、强音的饱满），不用管弦乐思维写钢琴。`artifact`

## (5) 曲式与结构

- 曲式：叙事曲自由曲式（奏鸣曲骨架 + 幻想曲自由）；夜曲三段式；波兰舞曲舞曲曲式；玛祖卡组曲式；结尾常由抒情突转为辉煌或黯然收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：夜曲式歌唱旋律、叙事曲、玛祖卡与波兰舞曲节奏、装饰音
- 不该写：管弦乐式厚重、机械节拍、无装饰的直白旋律
- Negative prompt: `orchestral thickness, metronomic rigidity, plain undecorated melody, pop chord loop`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Frederic Chopin, a 30-second piano nocturne for a small Yorkshire terrier sitting on a subway seat at night, bel canto melody, chromatic harmony, rubato breathing, delicate ornamentation, intimate and tender`
- 中文对照：肖邦风格，为夜里坐在地铁座位上的约克夏犬写 30 秒钢琴夜曲，声乐化旋律，半音和声，自由速度呼吸，精致装饰音，亲密温柔
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
