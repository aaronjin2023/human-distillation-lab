# Joe Hisaishi — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joe Hisaishi, Japanese film scoring, simple singable melody over gentle harmony, piano-led lyricism, orchestral warmth, theme that returns in varied instrumentation, minimalism without coldness`
- ZH: 久石让风格，日本电影配乐，简单可唱的旋律配温和和声，钢琴主导的抒情，管弦乐温暖，主题以不同配器再现，极简而不冷。

## (2) 音高与和声方向

- 以大调—小调功能和声为主，间有五声音阶色彩；调性清晰，和声温和，半音少。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律简单、可唱、级进为主，钢琴呈示；动机短小，副歌一句可记。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 钢琴 + 弦乐为主，间加木管与轻打击乐；音色温暖、透明，配器不厚。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 主题—变奏为主，主题在片中多次再现，每次换配器；结尾常以主题的钢琴独奏收束。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：简单可唱旋律、钢琴抒情线、温和和声、主题配器变奏、透明配器。`artifact`
- 不该写：复杂和声、密集配器、响亮高潮、主题一次性出现即丢。
- Negative prompt: `complex harmony, dense orchestration, loud climax, throwaway theme, sentimental swell`

## (7) 测试提示词示例（现代题材：一只小约克夏犬坐在地铁座位上）

- Prompt: `In the style of Joe Hisaishi, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Japanese film scoring, simple singable melody over gentle harmony, piano-led lyricism, orchestral warmth, theme that returns in varied instrumentation, minimalism without coldness`
- 中文对照：久石让风格，为一只小约克夏犬坐在地铁座位上写一段 30 秒配乐，日本电影配乐，简单可唱的旋律配温和和声，钢琴主导的抒情，管弦乐温暖，主题以不同配器再现，极简而不冷。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
