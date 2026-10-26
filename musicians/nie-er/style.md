# Nie Er — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nie Er, Chinese modern song composition, pentatonic melody with march rhythm, short singable refrain, folk dance pulse, theme written to be sung by a crowd at once`
- ZH: 聂耳风格，中国近现代歌曲作曲，五声音阶旋律配进行曲节奏，短小可唱的副歌，民间舞曲脉动，主题写来就能让群众立刻齐唱。

## (2) 音高与和声方向

- 以五声音阶与大调功能和声为主；调性清晰，和声极简，半音极少。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律短小、可唱、级进中夹跳进，节奏铿锵；副歌一句可记，是其最稳定的写法。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 人声 + 简洁伴奏（钢琴 / 小乐队 / 民间打击乐）；配器极简，不抢旋律。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 歌曲主歌—副歌为主，段落短；进行曲式结尾以副歌重复收束。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：五声短旋律、进行曲节奏、可唱副歌、民间舞曲脉动、简洁伴奏。`artifact`
- 不该写：复杂和声、长抒情线、密集配器、个人化装饰音。
- Negative prompt: `complex harmony, long lyrical line, dense orchestration, private ornament, sentimental swell`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，午后晚些时候）

- Prompt: `In the style of Nie Er, a 30-second piece for a cup of coffee left on a windowsill in the late afternoon, Chinese modern song composition, pentatonic melody with march rhythm, short singable refrain, folk dance pulse, theme written to be sung by a crowd at once`
- 中文对照：聂耳风格，为一杯放在窗台上的咖啡，午后晚些时候写一段 30 秒配乐，中国近现代歌曲作曲，五声音阶旋律配进行曲节奏，短小可唱的副歌，民间舞曲脉动，主题写来就能让群众立刻齐唱。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
