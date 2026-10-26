# Ryuichi Sakamoto — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ryuichi Sakamoto, Japanese contemporary and electronic composition, piano melody over electronic texture, sparse notes and silence, pentatonic fragments, ambient sound as music, theme that dissolves into texture`
- ZH: 坂本龙一风格，日本当代—电子作曲，钢琴旋律配电子织体，稀疏音符与静默，五声音阶碎片，环境声即音乐，主题溶入织体。

## (2) 音高与和声方向

- 以五声音阶与大调—小调混合为主，和声稀疏、少功能进行；电子织体作和声背景，调性游移。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律以钢琴短句为主，音符稀疏、长静默间隔；动机短小，在电子织体中浮现又消失。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 钢琴 + 合成器、电子织体、环境录音；音色冷而透明，力度轻。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 主题—织体式：主题呈示后溶入电子织体，段落靠音色变化衔接；结尾常以静默收束。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：钢琴短句、电子织体、稀疏音符、长静默、五声碎片。`artifact`
- 不该写：密集配器、功能和声进行、动机发展式结构、响亮高潮。
- Negative prompt: `dense orchestration, functional harmony, developmental structure, loud climax, sentimental melody`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，午后晚些时候）

- Prompt: `In the style of Ryuichi Sakamoto, a 30-second piece for a cup of coffee left on a windowsill in the late afternoon, Japanese contemporary and electronic composition, piano melody over electronic texture, sparse notes and silence, pentatonic fragments, ambient sound as music, theme that dissolves into texture`
- 中文对照：坂本龙一风格，为一杯放在窗台上的咖啡，午后晚些时候写一段 30 秒配乐，日本当代—电子作曲，钢琴旋律配电子织体，稀疏音符与静默，五声音阶碎片，环境声即音乐，主题溶入织体。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
