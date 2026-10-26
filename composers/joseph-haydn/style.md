# Joseph Haydn — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Classical symphony and string quartet, witty surprises, balanced sonata form, folk-like themes, clear tonal harmony, elegant humour, father of the symphony`
- ZH: 古典交响曲与弦乐四重奏，机智的惊喜，均衡的奏鸣曲式，民歌式主题，清晰调性和声，优雅的幽默，交响曲之父。

## (2) 旋律与和声

- 旋律：旋律民歌式，级进为主，乐句均衡；主题短小、富于发展。`artifact` 和声：功能和声明确，属—主收束清晰；突然转调与停顿作幽默；禁用随意半音。调性：调性稳定，转调靠模进与表情。

## (3) 节奏与织体

- 节奏：节奏清晰，小步舞曲与谐谑曲是骨架；突然停顿与强弱对比作幽默。织体：主调为主，四声部弦乐四重奏各声部平等；留白靠突然停顿。

## (4) 配器与音色

- 配器与音色：弦乐四重奏与管弦乐队并重；音色优雅、明亮；力度靠突然强弱对比；空间感来自埃斯特哈齐宫廷与伦敦公众音乐会。

## (5) 曲式与结构

- 曲式：交响曲（四乐章）、弦乐四重奏、清唱剧（《创世纪》）并重；奏鸣曲式是骨架。结构：呈示—展开—再现，高潮在展开部最密处；结尾以清晰终止收束。

## (6) 该写什么 / 不该写什么

- 该写：奏鸣曲式、弦乐四重奏四声部平等、机智的突然停顿与转调、民歌式主题、伦敦交响曲的公众气度。
- 不该写：无发展的主题堆砌、随意半音与无调性、管弦乐盖过主题、与结构无关的装饰、感伤的滥情。
- Negative prompt: `No undeveloped theme piling, no random chromaticism, no orchestra covering themes, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`

## (7) 测试提示词示例（现代题材：清晨窗台上的一杯咖啡）

- Prompt: `In the style of Joseph Haydn, a 30-second piece for a cup of coffee on a windowsill in the morning light, classical symphony and string quartet, witty surprises, balanced sonata form, folk-like themes, clear tonal harmony, elegant humour, father of the symphony`
- 中文对照：海顿风格，为清晨窗台上的一杯咖啡写 30 秒配乐，古典交响曲与弦乐四重奏，机智的惊喜，均衡的奏鸣曲式，民歌式主题，清晰调性和声，优雅的幽默，交响曲之父。
- Negative: `No undeveloped theme piling, no random chromaticism, no orchestra covering themes, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
