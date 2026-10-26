# Bob Dylan — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bob Dylan, Folk-rock songwriting, plainspoken vocal melody over simple diatonic harmony, long narrative verses, harmonica interjections, talking-blues phrasing, words carried by the tune rather than decorated by it`
- ZH: 鲍勃·迪伦风格，民谣摇滚歌曲写作，质朴人声旋律配简单自然音阶和声，长叙事诗句，口琴间奏，说唱蓝调式句法，词由旋律承载而非装饰。

## (2) 音高与和声方向

- 以大调—小调自然音阶为主，和声进行简单（I–IV–V 及其变体），调性稳定；半音化极少，张力来自歌词与句法而非和声。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律音域窄、级进为主、近乎说话的起伏；长句 + 短促口琴乐句交替，呼吸感来自词的断句而非乐句对称。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 木吉他 / 电吉他 + 口琴 + 贝斯 + 鼓的简洁组合；后期加管风琴与钢琴，但始终以人声为中心，配器不抢词。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 主歌—副歌 / 叙事连缀为主，多段主歌不重复旋律细节；结尾常以副歌重复或口琴收束，不追求器乐高潮。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：叙事长句、口琴间奏、简单和声上的旋律起伏、主歌连缀结构。`artifact`
- 不该写：华丽和声进行、炫技器乐独奏、工整对称的流行副歌、过度编曲盖住人声。
- Negative prompt: `lush harmony, virtuoso instrumental solos, polished symmetrical pop chorus, overproduced arrangement burying the vocal, sentimental swell`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，午后晚些时候）

- Prompt: `In the style of Bob Dylan, a 30-second piece for a cup of coffee left on a windowsill in the late afternoon, Folk-rock songwriting, plainspoken vocal melody over simple diatonic harmony, long narrative verses, harmonica interjections, talking-blues phrasing, words carried by the tune rather than decorated by it`
- 中文对照：鲍勃·迪伦风格，为一杯放在窗台上的咖啡，午后晚些时候写一段 30 秒配乐，民谣摇滚歌曲写作，质朴人声旋律配简单自然音阶和声，长叙事诗句，口琴间奏，说唱蓝调式句法，词由旋律承载而非装饰。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
