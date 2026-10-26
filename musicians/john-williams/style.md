# John Williams — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率如需给，必须标注“近似参考，非实测”——本文件不给频率值。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Williams, Film scoring in the late-Romantic orchestral tradition, leitmotif system, brass fanfare and string lyricism, clear tonal harmony, themes that identify characters and return transformed`
- ZH: 约翰·威廉姆斯风格，晚期浪漫主义管弦乐传统的电影配乐，主导动机体系，铜管号角与弦乐抒情，清晰调性和声，主题标识人物并变形再现。

## (2) 音高与和声方向

- 以功能和声与调式混合为主，调性清晰；半音化用于紧张与神秘，不破坏调性中心；不协和音短暂出现即解决。`artifact`
- 主调式 / 主和声：见上；禁用进行：他几乎不用的和声见第 (6) 节 Negative prompt；调性倾向与不协和度范围见上。
- 不编造实测频率值；以上均为通用术语描述。`impression`

## (3) 旋律与节奏

- 旋律：旋律轮廓鲜明、音程跳进大、节奏铿锵（号角式）或歌唱性长线（弦乐式），两路并存；动机短小，可变形、可倒置。`artifact`
- 节奏与织体：见上；留白（休止 / 静默）的作用：休止不是空白，是句法的一部分，见 language.md。

## (4) 配器与音色

- 大型管弦乐队全编制：铜管组号角、弦乐组歌唱线、木管色彩、打击乐节奏驱动；配器层次清晰，声部不糊。`artifact`
- 力度与空间：动态范围按作品段落定，焦点段落的力度见 process.md；声场布局以主奏 / 主题声部居前、伴奏居后为常态。

## (5) 曲式与结构

- 主导动机 + 组曲式：主题随人物与场景变形再现，全片音乐有交响曲式的布局与高潮。`impression`
- 高潮位置：多在中后段；结尾方式：见上，不追求单一固定的终止式。

## (6) 该写什么 / 不该写什么

- 该写：主导动机、铜管号角主题、弦乐抒情线、主题变形再现、清晰高潮布局。`artifact`
- 不该写：无主题的氛围铺垫、和声游移不定、配器浑浊、主题一次性出现即丢。
- Negative prompt: `theme-less ambient padding, wandering harmony, muddy orchestration, throwaway motifs, no climax architecture`

## (7) 测试提示词示例（现代题材：一只小约克夏犬坐在地铁座位上）

- Prompt: `In the style of John Williams, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, Film scoring in the late-Romantic orchestral tradition, leitmotif system, brass fanfare and string lyricism, clear tonal harmony, themes that identify characters and return transformed`
- 中文对照：约翰·威廉姆斯风格，为一只小约克夏犬坐在地铁座位上写一段 30 秒配乐，晚期浪漫主义管弦乐传统的电影配乐，主导动机体系，铜管号角与弦乐抒情，清晰调性和声，主题标识人物并变形再现。
- Negative: 见第 (6) 节。
- 检验点：主题是否一听可认、而不是风格标签的堆砌；配器是否按第 (4) 节的组合走、而不是通用管弦乐；结构是否按第 (5) 节走、而不是流行歌曲的套路。
