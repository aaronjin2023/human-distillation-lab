# Modest Mussorgsky — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Russian speech melody, raw harmony, pictorial piano, folk modal colour, dramatic realism, unpolished truth`
- ZH: 俄语式语言旋律，粗粝和声，图画钢琴，民间调式色彩，戏剧现实主义，未加打磨的真实。

## (2) 旋律与和声

- 旋律：语言式旋律，贴近俄语语调；和声：调式和声，民间五声与全音。禁：学院式功能和声。调性游移，不协和直给。

## (3) 节奏与织体

- 节奏：自由、不规则；织体：钢琴或管弦乐，旋律突出。

## (4) 配器与音色

- 乐器：钢琴、歌剧管弦乐；音色：粗粝、直接；力度：戏剧性对比。

## (5) 曲式与结构

- 曲式：钢琴组曲、歌剧、交响诗；结构：图画并置或戏剧分幕；结尾：戏剧性收束。

## (6) 该写什么 / 不该写什么

- 该写：语言式旋律、民间调式、图画并置、戏剧现实主义、粗粝和声。
- 不该写：学院式润色、德国式对位、圆滑沙龙旋律、无调性、煽情电影配乐式 swell、流行和弦循环。
- Negative prompt: `no academic polish, no Germanic counterpoint, no smooth salon melody, no atonal wandering, no sentimental film-score swell, no pop chord loop`

## (7) 测试提示词示例（现代题材：深夜末班车窗外的雨）

- Prompt: `In the style of Modest Mussorgsky, rain on the window of a night bus crossing the city, Russian speech melody, raw harmony, pictorial piano, folk modal colour, dramatic realism, unpolished truth`
- 中文对照：莫杰斯特·穆索尔斯基风格，深夜末班车窗外的雨，俄语式语言旋律，粗粝和声，图画钢琴，民间调式色彩，戏剧现实主义，未加打磨的真实。
- Negative: `no academic polish, no Germanic counterpoint, no smooth salon melody, no atonal wandering, no sentimental film-score swell, no pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
