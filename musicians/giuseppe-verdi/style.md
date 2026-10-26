# Giuseppe Verdi — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Bel canto vocal line made dramatic, clear orchestration serving the voice, chorus as people, melody that anyone can sing and no one can forget`
- ZH: 美声唱法线条戏剧化，清晰配器服务于人声，合唱即人民，旋律人人能唱、无人能忘

## (2) 音高与和声方向

- 主：功能和声，清晰、直接，调性服务于戏剧（每幕定调）；禁：半音迷雾、为和声而和声。`artifact`

## (3) 旋律与节奏

- 旋律：声乐化长线，音域宽、呼吸长，咏叹调旋律一听即记；节奏：歌剧节奏随戏剧，合唱节奏有力；织体：声乐主导、管弦乐伴奏，合唱织体厚实。`artifact`

## (4) 配器与音色

- 配器：管弦乐清晰、克制，铜管在高潮处才全出；音色明亮、直接；《阿依达》加异域色彩但不掩人声。`artifact`

## (5) 曲式与结构

- 曲式：分曲歌剧（咏叹调—重唱—合唱—终曲），晚期更连续；《安魂曲》七乐章，末日经高潮与极弱收束并置。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：咏叹调式旋律、重唱、合唱、戏剧性调性布局
- 不该写：半音迷雾、管弦乐压倒人声、为复杂而复杂
- Negative prompt: `chromatic fog, orchestra drowning the voice, complexity for its own sake`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Giuseppe Verdi, a 30-second aria-like miniature for a small Yorkshire terrier sitting on a subway seat, a singable soaring melody, clear warm orchestration, dramatic swell then tender close, as if the dog were singing its own Traviata`
- 中文对照：威尔第风格，为地铁座位上的约克夏犬写 30 秒咏叹调式微型曲，可唱的翱翔旋律，清晰温暖配器，戏剧性涌起后温柔收束，仿佛狗在唱自己的《茶花女》
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
