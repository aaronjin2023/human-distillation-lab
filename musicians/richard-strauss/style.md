# Richard Strauss — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Tone poem and opera of orchestral virtuosity, late Romantic opulence, waltz elegance and autumnal song in one frame`
- ZH: 交响诗与歌剧的管弦乐炫技，晚期浪漫主义的华美，圆舞曲优雅与秋日歌曲同框

## (2) 音高与和声方向

- 主：功能和声 + 大胆半音、借调，调性清晰但色彩浓烈；禁：无调性、为新奇而新奇的和声。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性长线，音域宽，装饰华美；节奏：圆舞曲、交响诗自由节奏；织体：管弦乐织体厚而透明，独奏乐器轮流歌唱。`artifact`

## (4) 配器与音色

- 配器：超大管弦乐，音色华美、分层清晰，铜管与弦乐推高潮；歌剧配器服务人声。`artifact`

## (5) 曲式与结构

- 曲式：交响诗单乐章、歌剧三幕、歌曲集；《查拉图斯特拉如是说》以自然音程开场；晚期歌曲极简、极美。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：交响诗、圆舞曲、华美配器、秋日歌曲
- 不该写：无调性漫游、轻薄配器、为新奇而新奇
- Negative prompt: `atonal wandering, thin orchestration, novelty for its own sake`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Richard Strauss, a 30-second tone-poem miniature for a small Yorkshire terrier sitting on a subway seat, a soaring singing theme, opulent warm orchestration, waltz elegance, ending in a luminous autumnal close`
- 中文对照：理查·施特劳斯风格，为地铁座位上的约克夏犬写 30 秒交响诗微型曲，翱翔歌唱主题，华美温暖配器，圆舞曲优雅，以明亮秋日收束
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
