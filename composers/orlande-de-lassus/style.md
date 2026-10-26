# Orlande de Lassus — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Late Renaissance polyphony, expressive chromaticism, vivid text painting, flexible imitation, sacred motets and secular chansons, master of musical rhetoric`
- ZH: 晚期文艺复兴复调，富于表情的半音化，生动的文本描绘，灵活的模仿，宗教经文歌与世俗香颂并重，音乐修辞大师。

## (2) 旋律与和声

- 旋律：线条富于表情，随文本意义起伏；半音化用于描绘痛苦、眼泪、预言等情绪。`artifact` 和声：调式为基底，半音进行作表情手段（《先知预言》以大胆半音著称）；不协和仍按规则解决，但表情优先。调性：调式游移靠半音，仍有明确终止。

## (3) 节奏与织体

- 节奏：节奏灵活，随文本重音变化；声部进入以模仿为主，偶有同节奏齐唱强调关键词。织体：四—八声部复调，密度随文本情绪变化；留白靠声部骤减。

## (4) 配器与音色

- 配器与音色：无伴奏人声为本体，偶有乐器；音色富于变化，靠半音与声部密度制造明暗；力度随文本情绪起伏，动态范围较帕莱斯特里纳更宽。

## (5) 曲式与结构

- 曲式：经文歌、弥撒曲、香颂、牧歌并重；《圣彼得的眼泪》以 21 首牧歌加尾声作套曲结构。结构：文本段落驱动，高潮在文本最痛处；结尾常以静默收束。

## (6) 该写什么 / 不该写什么

- 该写：文本描绘（word painting）、表情性半音化、灵活的声部模仿、经文歌的修辞结构、套曲式的情感推进。
- 不该写：无表情的纯协和堆砌、现代功能和声、管弦乐式配器、固定不变的织体、与文本无关的装饰。
- Negative prompt: `No expressionless consonance, no modern functional harmony, no orchestral scoring, no fixed unchanging texture, no text-irrelevant ornament, no pop phrasing`

## (7) 测试提示词示例（现代题材：黄昏时分的高铁车窗外）

- Prompt: `In the style of Orlande de Lassus, a 30-second piece for a high-speed train window at dusk, late renaissance polyphony, expressive chromaticism, vivid text painting, flexible imitation, sacred motets and secular chansons, master of musical rhetoric`
- 中文对照：拉索风格，为黄昏时分的高铁车窗外写 30 秒配乐，晚期文艺复兴复调，富于表情的半音化，生动的文本描绘，灵活的模仿，宗教经文歌与世俗香颂并重，音乐修辞大师。
- Negative: `No expressionless consonance, no modern functional harmony, no orchestral scoring, no fixed unchanging texture, no text-irrelevant ornament, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
