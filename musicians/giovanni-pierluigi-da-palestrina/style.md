# Giovanni Pierluigi da Palestrina — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Roman Renaissance polyphony, smooth stepwise lines, restrained dissonance, serene clarity, perfect text intelligibility, sacred counterpoint at its purest`
- ZH: 罗马文艺复兴复调，平滑级进线条，克制的非协和，宁静清晰，歌词极清晰，最纯粹的圣咏对位。

## (2) 音高与和声方向

- 主：调式对位，级进声部进行；不协和只出现在弱拍、经经过音或延留音后解决。禁：跳进过多、半音化泛滥、功能和声。调性：调式中心稳定，收束庄重；和声是声部进行的副产品，不是驱动力。

## (3) 旋律与节奏

- 旋律：级进为主，跳进后必反向级进弥补；音域窄（一般在八度内）；线条平滑、无棱角。节奏：从容、流动，无强烈重音。织体：四—六声部，模仿与自由对位交替，声部进入错落有致。

## (4) 配器与音色

- 人声：四—六声部无伴奏合唱。音色：纯净、宁静、均衡。力度：弱—中，靠织体疏密起伏。

## (5) 曲式与结构

- 曲式：弥撒套曲、经文歌、牧歌（世俗）。结构：模仿点层层推进，织体由疏到密再到疏；高潮温和、在中段。结尾：平静收束，常以同节奏齐唱收尾。

## (6) 该写什么 / 不该写什么

- 该写：平滑级进对位、弥撒套曲、经文歌、歌词清晰的圣咏复调。
- 不该写：大跳、半音化泛滥、强烈节奏、功能和声、乐队化。
- Negative prompt: `large leaps, rampant chromaticism, strong accents, functional harmony, orchestral texture, dramatic climax`

## (7) 测试提示词示例（现代题材：现代城市街角便利店夜景）

- Prompt: `In the style of Palestrina, a quiet night scene at a small convenience store in a modern city, Roman Renaissance polyphony, smooth stepwise lines, restrained dissonance, serene clarity, five voices, unaccompanied, peaceful`
- 中文对照：帕莱斯特里纳风格，现代城市小便利店夜景，罗马文艺复兴复调，平滑级进，克制非协和，宁静清晰，五声部无伴奏，平和。
- Negative: `large leaps, rampant chromaticism, strong accents, functional harmony, orchestral texture, dramatic climax`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
