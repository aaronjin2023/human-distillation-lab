# Tan Dun — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tan Dun, Chinese contemporary composition, water and paper and stone as instruments, pentatonic melody over orchestral colour, ritual theatre, East-West timbre, theme carried by sound itself`
- ZH: 谭盾风格，中国当代作曲，水、纸、石即乐器，五声音阶旋律配管弦乐色彩，仪式剧场，东西音色交融，主题由声音本身承载。

## (2) 音高与和声方向

- 以五声音阶与调式为主，和声色彩化、少功能进行；水声、纸声作音高之外的声音材料。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律以五声碎片为主，线条简洁、带民间歌腔的滑音；动机短小，在仪式结构中反复。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 管弦乐 + 水、纸、石、陶等非常规乐器；音色对比强烈——水的流动对管弦乐的厚重。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 仪式剧场式：段落按仪式流程排列，靠声音事件（水声、纸声）衔接；结尾常以静默收束。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：五声碎片、水纸石音色、仪式结构、东西音色并置、声音事件。`artifact`
- 不该写：功能和声进行、动机发展式结构、密集配器盖住非常规音色、响亮高潮。
- Negative prompt: `functional harmony, developmental structure, dense orchestration burying found sounds, loud climax, sentimental melody`

## (7) 测试提示词示例（现代题材：现代城市街角便利店的夜景）

- Prompt: `In the style of Tan Dun, a 30-second piece for a quiet night scene at a small convenience store in a modern city, Chinese contemporary composition, water and paper and stone as instruments, pentatonic melody over orchestral colour, ritual theatre, East-West timbre, theme carried by sound itself`
- 中文对照：谭盾风格，为现代城市街角便利店的夜景写一段 30 秒配乐，中国当代作曲，水、纸、石即乐器，五声音阶旋律配管弦乐色彩，仪式剧场，东西音色交融，主题由声音本身承载。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
