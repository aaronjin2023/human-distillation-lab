# Clara Schumann — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Virtuoso piano lyricism, singing lines with chromatic depth, chamber music of intertwining melodies, Romantic passion held in classical balance`
- ZH: 炫技钢琴抒情，歌唱线条带半音深度，室内乐旋律交织，浪漫激情收于古典均衡之中

## (2) 音高与和声方向

- 主：功能和声，半音化浓、借调频繁，解决常延迟一步；禁：炫技的空转和声、无歌唱性的音型堆砌。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性长线 + 炫技音型，钢琴写法贴合演奏家的手；节奏：切分与交叉节奏，慢乐章呼吸长；织体：钢琴主导、弦乐交织对话，三重奏三声部平等。`artifact`

## (4) 配器与音色

- 配器：钢琴独奏、钢琴三重奏、小提琴与钢琴；音色温暖饱满，钢琴音区跨度大，弦乐歌唱性强。`artifact`

## (5) 曲式与结构

- 曲式：协奏曲三乐章（第二乐章浪漫曲式）；三重奏四乐章古典骨架；浪漫曲三首成组、每首一个性格。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：钢琴歌唱旋律、三重奏交织声部、浪漫曲式慢乐章
- 不该写：空洞炫技、无歌唱性的音型、为宏大而牺牲亲密感
- Negative prompt: `empty virtuosity, unsinging figuration, bombast at the cost of intimacy`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Clara Schumann, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, singing piano melody, warm chromatic harmony, intertwining violin and piano lines, tender and passionate, a Romance without words`
- 中文对照：克拉拉·舒曼风格，为地铁座位上的约克夏犬写 30 秒小品，歌唱性钢琴旋律，温暖半音和声，小提琴与钢琴线条交织，温柔而热烈，如无词浪漫曲
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
