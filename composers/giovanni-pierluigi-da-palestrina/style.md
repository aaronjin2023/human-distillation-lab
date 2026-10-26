# Giovanni Pierluigi da Palestrina — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Roman school polyphony, smooth stepwise lines, pure consonance, restrained dissonance, clear text declamation, serene sacred counterpoint, model of Palestrina style`
- ZH: 罗马乐派复调，平滑级进线条，纯净协和，克制的不协和，清晰的文本宣叙，宁静的圣乐对位，帕莱斯特里纳风格的范式。

## (2) 旋律与和声

- 旋律：级进为主，跳进后立即弥补，线条平滑如波浪；各声部皆可唱。`artifact` 和声：以协和三度、六度为骨架，不协和只出现在弱拍经过音并立即解决；禁用大跳后的不协和滞留。调性：调式稳定，终止清晰而克制。

## (3) 节奏与织体

- 节奏：节奏平稳，跟随拉丁文音节；声部进入以模仿为主但不抢文本。织体：四—六声部复调，密度均匀；文本可懂度优先，声部不遮盖歌词。

## (4) 配器与音色

- 配器与音色：无伴奏人声（合唱）为本体；音色纯净、宁静；力度变化极小，靠声部增减；空间感来自教堂共鸣。

## (5) 曲式与结构

- 曲式：弥撒曲与经文歌并重；结构靠文本段落组织，乐章间以同一动机统一。高潮在文本最重处（如 Credo 的高潮句）；结尾以平静终止收束。

## (6) 该写什么 / 不该写什么

- 该写：平滑级进旋律、纯净协和与弱拍不协和解决、清晰的文本宣叙、弥撒曲的庄重结构、经文歌的段落对比。
- 不该写：大跳后的不协和滞留、半音化与功能和声、节奏切分与世俗舞曲、管弦乐式配器、夸张的表情对比。
- Negative prompt: `No unresolved dissonance, no chromaticism, no functional harmony, no dance rhythms, no orchestral scoring, no exaggerated expression`

## (7) 测试提示词示例（现代题材：清晨苏醒的菜市场）

- Prompt: `In the style of Giovanni Pierluigi da Palestrina, a 30-second piece for a morning vegetable market waking up, roman school polyphony, smooth stepwise lines, pure consonance, restrained dissonance, clear text declamation, serene sacred counterpoint, model of palestrina style`
- 中文对照：帕莱斯特里纳风格，为清晨苏醒的菜市场写 30 秒配乐，罗马乐派复调，平滑级进线条，纯净协和，克制的不协和，清晰的文本宣叙，宁静的圣乐对位，帕莱斯特里纳风格的范式。
- Negative: `No unresolved dissonance, no chromaticism, no functional harmony, no dance rhythms, no orchestral scoring, no exaggerated expression`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
