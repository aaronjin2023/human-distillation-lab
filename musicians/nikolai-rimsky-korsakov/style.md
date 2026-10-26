# Nikolai Rimsky-Korsakov — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Orchestration as art itself, oriental colour, octatonic shimmer, fairy-tale clarity in dazzling instrumental dress`
- ZH: 配器本身就是艺术，东方色彩，八声音阶闪烁，童话般清晰覆于耀眼器乐华服之下

## (2) 音高与和声方向

- 主：功能和声 + 八声音阶、全音阶、调式色彩，调性清晰但色彩游移；禁：德国式厚重半音、无色彩的功能和声。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性 + 东方装饰，独奏乐器（小提琴、大管、长笛）轮流歌唱；节奏：舞曲节奏、东方节奏型；织体：管弦乐分层精细，独奏与全奏交替。`artifact`

## (4) 配器与音色

- 配器：管弦乐教科书级——乐器组合精细、音色分层清晰，独奏段落是结构；音色明亮、闪烁、异域。`artifact`

## (5) 曲式与结构

- 曲式：组曲式（《天方夜谭》四乐章）、歌剧分幕、随想曲自由曲式；独奏主题变形即结构。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：精细配器、东方色彩、八声音阶、独奏歌唱段落
- 不该写：厚重半音、无色彩的功能和声、模糊配器
- Negative prompt: `heavy chromaticism, colourless functional harmony, muddy orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Nikolai Rimsky-Korsakov, a 30-second orchestral miniature for a small Yorkshire terrier sitting on a subway seat, a solo violin Scheherazade-like theme, octatonic shimmer, dazzling transparent orchestration, fairy-tale clarity`
- 中文对照：里姆斯基-科萨科夫风格，为地铁座位上的约克夏犬写 30 秒管弦乐微型曲，独奏小提琴如天方夜谭主题，八声音阶闪烁，耀眼透明配器，童话般清晰
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
