# Qigang Chen — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Qigang Chen, Chinese contemporary composition, refined orchestral colour, pentatonic fragments over French spectral harmony, lyrical line inside modernist texture, East-West balance without exoticism`
- ZH: 陈其钢风格，中国当代作曲，精致的管弦乐色彩，五声音阶碎片配法国频谱和声，现代主义织体里的抒情线条，东西平衡而不猎奇。

## (2) 音高与和声方向

- 以五声音阶碎片与频谱和声混合为主；和声由泛音列组织，调性游移，色彩细腻。`impression`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律抒情、线条长、带五声的滑音；动机短小，在频谱和声中缓慢展开。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 管弦乐为主，音色精致、层次清；力度以中弱为主，强音克制。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 变奏与并置为主：五声主题作变奏，段落靠和声色彩衔接；结尾常以音色渐弱收束。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：五声碎片、频谱和声、抒情长线、精致配器、主题变奏。`artifact`
- 不该写：功能和声进行、密集配器、响亮高潮、猎奇式东方色彩。
- Negative prompt: `functional harmony, dense orchestration, loud climax, exotic orientalism, sentimental swell`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，午后晚些时候）

- Prompt: `In the style of Qigang Chen, a 30-second piece for a cup of coffee left on a windowsill in the late afternoon, Chinese contemporary composition, refined orchestral colour, pentatonic fragments over French spectral harmony, lyrical line inside modernist texture, East-West balance without exoticism`
- 中文对照：陈其钢风格，为一杯放在窗台上的咖啡，午后晚些时候写一段 30 秒配乐，中国当代作曲，精致的管弦乐色彩，五声音阶碎片配法国频谱和声，现代主义织体里的抒情线条，东西平衡而不猎奇。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
