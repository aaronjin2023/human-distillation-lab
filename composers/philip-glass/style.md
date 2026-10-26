# Philip Glass — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Additive rhythm, arpeggiated cycles, pulsing harmony, clear pulse, lyrical melody over repetition, opera and film scoring`
- ZH: 加法节奏，琶音循环，脉动和声，清晰脉冲，重复之上的抒情旋律，歌剧与电影配乐。

## (2) 旋律与和声

- 旋律：琶音循环中的抒情线条，级进为主；音型重复中渐变。`artifact`
- 和声：和弦循环，调性清晰；和声变化缓慢，靠音型叠加。`artifact`

## (3) 节奏与织体

- 节奏：加法节奏——音型逐音增加；固定脉冲；织体：多层琶音叠加，密度渐变。

## (4) 配器与音色

- 配器：键盘、木管、弦乐、人声；歌剧编制大，电影配乐以钢琴与弦乐为主。

## (5) 曲式与结构

- 曲式：循环与加法结构、歌剧多场；高潮靠密度积累，结尾渐弱或循环收束。

## (6) 该写什么 / 不该写什么

- 该写：加法节奏、琶音循环、脉动和声、重复之上的抒情旋律、清晰脉冲、歌剧与电影配乐。
- 不该写：sudden contrast without process、no functional cadence as climax、no dense counterpoint、no rubato blurring the pulse、no sentimental swell without repetition、no random improvisation。
- Negative prompt: `No sudden contrast without process, no functional cadence as climax, no dense counterpoint, no rubato blurring the pulse, no sentimental swell without repetition, no random improvisation`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Philip Glass, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, additive arpeggiated cycles, pulsing harmony, lyrical line over repetition, clear pulse`
- 中文对照：格拉斯风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，加法琶音循环，脉动和声，重复之上的抒情线条，清晰脉冲。
- Negative: `No sudden contrast without process, no functional cadence as climax, no dense counterpoint, no rubato blurring the pulse, no sentimental swell without repetition, no random improvisation`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
