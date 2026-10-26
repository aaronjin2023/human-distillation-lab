# Carlos Chávez — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carlos Chávez, Mexican nationalist composition, pre-Columbian percussion and melody, clear polyphonic texture, lean orchestration, folk material developed with modernist harmony`
- ZH: 卡洛斯·查韦斯风格，墨西哥民族乐派作曲，前哥伦布打击乐与旋律，清晰复调织体，精简配器，民间材料以现代主义和声发展。

## (2) 音高与和声方向

- 以墨西哥民间调式与五声音阶为主，和声简洁、少装饰；调性清晰，不协和音用作节奏重音。`impression`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律短小、重复音型多、带民间歌舞的切分；线条简洁，不尚抒情长线。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 管弦乐 + 墨西哥打击乐（前哥伦布乐器）；配器精简，声部清晰，不堆叠。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 交响曲与组曲为主；民间主题作对位与变奏发展，结构简洁。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：民间节奏型、前哥伦布打击乐、清晰复调、精简配器、主题变奏。`artifact`
- 不该写：华丽配器、抒情长线堆砌、脱离民间材料的抽象和声。
- Negative prompt: `lush orchestration, piled-up lyric lines, folk-free abstract harmony, sentimental swell`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，午后晚些时候）

- Prompt: `In the style of Carlos Chávez, a 30-second piece for a cup of coffee left on a windowsill in the late afternoon, Mexican nationalist composition, pre-Columbian percussion and melody, clear polyphonic texture, lean orchestration, folk material developed with modernist harmony`
- 中文对照：卡洛斯·查韦斯风格，为一杯放在窗台上的咖啡，午后晚些时候写一段 30 秒配乐，墨西哥民族乐派作曲，前哥伦布打击乐与旋律，清晰复调织体，精简配器，民间材料以现代主义和声发展。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
