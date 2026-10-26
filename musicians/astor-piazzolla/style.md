# Astor Piazzolla — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Astor Piazzolla, Nuevo tango, bandoneón-led melody over sharp tango rhythm, jazz harmony and classical counterpoint, sudden dynamic contrasts, melancholy lyricism inside dance pulse`
- ZH: 阿斯托尔·皮亚佐拉风格，探戈新风，班多钮手风琴主导旋律配锐利探戈节奏，爵士和声与古典对位，突然的力度对比，舞曲脉动里的忧郁抒情。

## (2) 音高与和声方向

- 以小调与探戈调式为主，和声带爵士的半音与扩展和弦；调性清晰，紧张来自半音经过与突然转调。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律由班多钮呈示，线条长、带哭腔的滑音与装饰音；动机短小，反复中加装饰变形。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 班多钮 + 小提琴、钢琴、吉他、低音提琴的五重奏为核心；音色对比强烈——班多钮的呼吸对弦乐的歌唱。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 探戈舞曲曲式 + 变奏：主题—变奏—再现，段落间以突然的力度与速度对比衔接。`artifact`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：班多钮旋律、探戈切分节奏、爵士和声、突然力度对比、主题变奏。`artifact`
- 不该写：传统探戈的刻板伴奏、光滑的流行和声、独奏堆砌、情绪单一的舞曲。
- Negative prompt: `formula tango accompaniment, smooth pop harmony, solo showcase, single-mood dance music, no dynamic contrast`

## (7) 测试提示词示例（现代题材：现代城市街角便利店的夜景）

- Prompt: `In the style of Astor Piazzolla, a 30-second piece for a quiet night scene at a small convenience store in a modern city, Nuevo tango, bandoneón-led melody over sharp tango rhythm, jazz harmony and classical counterpoint, sudden dynamic contrasts, melancholy lyricism inside dance pulse`
- 中文对照：阿斯托尔·皮亚佐拉风格，为现代城市街角便利店的夜景写一段 30 秒配乐，探戈新风，班多钮手风琴主导旋律配锐利探戈节奏，爵士和声与古典对位，突然的力度对比，舞曲脉动里的忧郁抒情。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
