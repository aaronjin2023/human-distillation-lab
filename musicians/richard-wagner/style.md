# Richard Wagner — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Endless melody, leitmotif web, Tristan chromaticism, huge orchestra as drama itself, music drama without number opera`
- ZH: 无终旋律，主导动机织体，特里斯坦式半音，庞大管弦乐即戏剧本身，无分曲歌剧的音乐戏剧

## (2) 音高与和声方向

- 主：半音化功能和声，特里斯坦和弦与延迟解决，调性长期悬置；禁：分曲歌剧的封闭咏叹调式和声、属—主的频繁收束。`artifact`

## (3) 旋律与节奏

- 旋律：无终旋律——声乐线条如朗诵、不断延续；节奏：自由、呼吸长，重音随语调；织体：管弦乐主导动机网 + 声乐线，复调密度高。`artifact`

## (4) 配器与音色

- 配器：超大管弦乐（瓦格纳大号等），铜管与弦乐织体厚重，音色暗、暖、持续；力度幅度极大，渐强可长达数分钟。`artifact`

## (5) 曲式与结构

- 曲式：乐剧连续体，无分曲；主导动机贯穿全剧，变形即人物与命运的变化；高潮迟来、收束悬置或升华。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：主导动机、无终旋律、半音悬置、庞大管弦乐织体
- 不该写：封闭咏叹调、频繁属—主收束、轻盈透明配器
- Negative prompt: `closed number aria, frequent dominant-tonic cadence, light transparent orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Richard Wagner, a 30-second music-drama miniature for a small Yorkshire terrier sitting on a subway seat, endless melody, a short leitmotif transformed, chromatic yearning, huge warm orchestral swell, no clear cadence`
- 中文对照：瓦格纳风格，为地铁座位上的约克夏犬写 30 秒乐剧微型曲，无终旋律，短主导动机变形，半音渴望，庞大温暖管弦乐涌起，无明确收束
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
