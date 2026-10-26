# Ma Sicong — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ma Sicong, Chinese modern composition, pentatonic folk melody over Western violin and orchestral forms, lyrical pastoral line, folk dance rhythm, theme that sings like a folk song`
- ZH: 马思聪风格，中国近现代作曲，五声音阶民间旋律配西方小提琴与管弦乐曲式，抒情田园线条，民间舞曲节奏，主题像民歌一样歌唱。

## (2) 音高与和声方向

- 以五声音阶与大调—小调功能和声混合为主；调性清晰，和声温和，半音少。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律抒情、歌唱性强、级进为主，民间歌腔的滑音；小提琴线条长而连贯。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 小提琴 + 管弦乐为主，间加民间打击乐；音色温暖、透明，独奏占前景。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 组曲与音诗为主：多段民间主题连缀，靠调性与节奏对比衔接；结尾常以抒情主题再现收束。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：五声民间旋律、抒情小提琴线、民间舞曲节奏、组曲结构、田园音色。`artifact`
- 不该写：复杂和声、半音化旋律、密集配器盖住独奏、个人化炫技。
- Negative prompt: `complex harmony, chromatic melody, dense orchestration burying the soloist, virtuoso display, sentimental swell`

## (7) 测试提示词示例（现代题材：现代城市街角便利店的夜景）

- Prompt: `In the style of Ma Sicong, a 30-second piece for a quiet night scene at a small convenience store in a modern city, Chinese modern composition, pentatonic folk melody over Western violin and orchestral forms, lyrical pastoral line, folk dance rhythm, theme that sings like a folk song`
- 中文对照：马思聪风格，为现代城市街角便利店的夜景写一段 30 秒配乐，中国近现代作曲，五声音阶民间旋律配西方小提琴与管弦乐曲式，抒情田园线条，民间舞曲节奏，主题像民歌一样歌唱。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
