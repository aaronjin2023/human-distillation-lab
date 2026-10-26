# Johannes Brahms — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Developing variation, classical forms filled with Romantic warmth, autumnal melody, cross-rhythm and hemiola, orchestration dark and warm`
- ZH: 发展变奏，古典曲式填满浪漫暖意，秋日旋律，交叉节奏与赫米奥拉，配器暗而暖

## (2) 音高与和声方向

- 主：功能和声，半音丰富但调性稳固，借调与意外转调服务于动机；禁：无调性、为新奇而新奇的和声。`artifact`

## (3) 旋律与节奏

- 旋律：长线歌唱，三度、六度音程常见，动机短而可发展；节奏：交叉节奏、赫米奥拉、切分是标记；织体：复调密度高，弦乐织体厚而暖。`artifact`

## (4) 配器与音色

- 配器：管弦乐暗暖，弦乐主导，木管歌唱，铜管克制；室内乐（弦乐四重奏、钢琴三重奏）与交响曲同等重要。`artifact`

## (5) 曲式与结构

- 曲式：奏鸣曲式、变奏曲式（第四交响曲末乐章帕萨卡利亚）、回旋曲式严守古典骨架；结尾常由变奏推向庄严收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：发展变奏、帕萨卡利亚、交叉节奏、秋日歌唱旋律
- 不该写：无调性漫游、为新奇而新奇、轻薄配器
- Negative prompt: `atonal wandering, novelty harmony, thin orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Johannes Brahms, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, warm autumnal melody, developing variation, cross-rhythms, dark warm strings, classical balance, tender and serious`
- 中文对照：勃拉姆斯风格，为地铁座位上的约克夏犬写 30 秒小品，温暖秋日旋律，发展变奏，交叉节奏，暗暖弦乐，古典均衡，温柔而严肃
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
