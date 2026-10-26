# Alberto Ginastera — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alberto Ginastera, Argentine nationalist to modernist composition, folk dance rhythm and malambo pulse, bitonal harmony, percussive piano and orchestral writing, folk motif developed with twelve-tone technique in late works`
- ZH: 阿尔韦托·希纳斯特拉风格，阿根廷民族乐派到现代主义作曲，民间舞曲节奏与马兰博脉动，双调性和声，打击性钢琴与管弦乐写作，晚期以十二音技法发展民间动机。

## (2) 音高与和声方向

- 早期以民间调式与功能和声为主；中期双调性与多调性；晚期十二音序列，但民间动机仍可辨。`impression`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律短小、带民间舞曲的切分与重复音型；动机以节奏型为核心，音高其次。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 管弦乐 + 打击乐组突出，钢琴作打击乐器用；音色硬朗、节奏驱动。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 舞曲组曲与协奏曲式为主；民间主题作变奏与对位发展，晚期以序列结构组织。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：民间舞曲节奏、马兰博脉动、打击性配器、民间动机变奏、双调性。`artifact`
- 不该写：脱离节奏的抒情旋律、光滑的功能和声、配器盖住打击乐脉动。
- Negative prompt: `lyricism without rhythm, smooth functional harmony, orchestration burying percussion pulse, folk-free abstraction`

## (7) 测试提示词示例（现代题材：一只小约克夏犬坐在地铁座位上）

- Prompt: `In the style of Alberto Ginastera, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Argentine nationalist to modernist composition, folk dance rhythm and malambo pulse, bitonal harmony, percussive piano and orchestral writing, folk motif developed with twelve-tone technique in late works`
- 中文对照：阿尔韦托·希纳斯特拉风格，为一只小约克夏犬坐在地铁座位上写一段 30 秒配乐，阿根廷民族乐派到现代主义作曲，民间舞曲节奏与马兰博脉动，双调性和声，打击性钢琴与管弦乐写作，晚期以十二音技法发展民间动机。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
