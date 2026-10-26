# A. R. Rahman — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of A. R. Rahman, Indian film music composition, Carnatic and Hindustani melody over Western harmony and electronics, catchy refrain over layered rhythm, orchestral warmth with synthesized texture, theme that survives remixing`
- ZH: A. R. 拉赫曼风格，印度电影音乐作曲，卡纳蒂克与北印度旋律配西方和声与电子音色，朗朗上口的副歌配层叠节奏，管弦乐温暖加合成器织体，主题经得起混音。

## (2) 音高与和声方向

- 以印度拉格调式与大调—小调功能和声混合为主；和声色彩丰富，调性清晰，半音用作装饰。`impression`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律歌唱性强、带印度装饰音的滑音，副歌一句可记；动机短小，反复中加和声变奏。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 管弦乐 + 合成器、印度打击乐、合唱；音色层叠，电子与原声并置。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 电影歌曲主歌—副歌为主，主题在片中多次再现；配乐以主题变奏组织全片。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：印度旋律装饰音、朗朗上口的副歌、层叠节奏、电子与管弦并置、主题再现。`artifact`
- 不该写：无旋律的氛围铺垫、和声游移不定、配器盖住人声、主题一次性出现即丢。
- Negative prompt: `melody-free ambient padding, wandering harmony, orchestration burying the vocal, throwaway theme, sentimental swell`

## (7) 测试提示词示例（现代题材：现代城市街角便利店的夜景）

- Prompt: `In the style of A. R. Rahman, a 30-second piece for a quiet night scene at a small convenience store in a modern city, Indian film music composition, Carnatic and Hindustani melody over Western harmony and electronics, catchy refrain over layered rhythm, orchestral warmth with synthesized texture, theme that survives remixing`
- 中文对照：A. R. 拉赫曼风格，为现代城市街角便利店的夜景写一段 30 秒配乐，印度电影音乐作曲，卡纳蒂克与北印度旋律配西方和声与电子音色，朗朗上口的副歌配层叠节奏，管弦乐温暖加合成器织体，主题经得起混音。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
