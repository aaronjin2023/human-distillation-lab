# Robert Schumann — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Literary piano cycles and songs, fragmentary character pieces, Florestan fire and Eusebius dream in one frame, intimate confession in miniature forms`
- ZH: 文学性钢琴套曲与艺术歌曲，片段式性格小品，弗洛雷斯坦的火与欧塞比乌斯的梦同框，微型体裁里的亲密告白

## (2) 音高与和声方向

- 主：功能和声 + 频繁半音、借调与意外转调，调性常在乐句中途游移；禁：学院式四平八稳的和声进行。`artifact`

## (3) 旋律与节奏

- 旋律：短小动机、碎片化乐句，歌唱性与朗诵性交替；节奏：切分、交叉节奏、突然的速度与力度对比；织体：钢琴主调 + 复调穿插，声乐与钢琴对话平等。`artifact`

## (4) 配器与音色

- 配器：钢琴独奏与艺术歌曲（钢琴伴奏是第二主角）、室内乐与交响曲；音色温暖、内向，管弦乐也求亲密而非辉煌。`artifact`

## (5) 曲式与结构

- 曲式：套曲式（《狂欢节》《诗人之恋》由性格小品连缀）；奏鸣曲式常被片段打断；交响曲四乐章但乐章内多性格对比。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：性格小品套曲、艺术歌曲、短动机碎片、文学性标题
- 不该写：四平八稳的学院曲式、空洞的辉煌、直白无对比的抒情
- Negative prompt: `academic square phrasing, empty grandeur, unrelieved sentimental lyricism`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Robert Schumann, a 30-second piano character piece for a small Yorkshire terrier sitting on a subway seat, fragmentary singing phrases, sudden tender-to-fiery contrasts, warm chromatic harmony, like a page from Carnaval`
- 中文对照：舒曼风格，为地铁座位上的约克夏犬写 30 秒钢琴性格小品，片段化歌唱乐句，温柔与炽热突然对比，温暖半音和声，如《狂欢节》中的一页
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
