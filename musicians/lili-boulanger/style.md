# Lili Boulanger — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Lili Boulanger style, French modal harmony, luminous orchestration, intense lyricism, psalm setting, short life mature voice, impressionist colour with dramatic contrast`
- ZH: 莉莉·布朗热风格，法国调式和声，明亮配器，强烈的抒情，诗篇配曲，短暂一生中的成熟声音，印象主义色彩配戏剧对比。

## (2) 音高与和声方向

- 主：调式和声、半音化抒情、印象主义平行和弦；调性游移但有中心；禁：德国式动机发展的沉重与功能和声的强解决。`artifact`

## (3) 旋律与节奏

- 旋律：人声旋律歌唱性强、线条长、呼吸感强；器乐旋律带德彪西式片段感；节奏：自由、跟随歌词重音。`artifact`

## (4) 配器与音色

- 管弦乐与人声：弦乐明亮、木管清澈、铜管克制、竖琴与管风琴点缀（《耶稣羔羊》配高声部、弦乐四重奏、竖琴、管风琴）；音色透明。`artifact`

## (5) 曲式与结构

- 曲式：康塔塔、诗篇配曲、管弦乐双联画（《春晨》与《悲伤的黄昏》）；结构：段落对比鲜明，高潮短促有力，结尾常归于宁静。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：调式抒情、诗篇配曲、明亮配器、人声长线条、短促戏剧对比。
- 不该写：见 Negative prompt。
- Negative prompt: `heavy Germanic development, mechanical functional cadence, dense orchestration, sentimental swell, formless wandering`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Lili Boulanger, a 30-second piece for a cup of coffee left on a windowsill in the morning light, Lili Boulanger style, French modal harmony, luminous orchestration, intense lyricism, psalm setting, short life mature voice, impressionist colour with dramatic contrast`
- 中文对照：莉莉·布朗热风格，为一杯放在窗台上的咖啡写一段 30 秒配乐，莉莉·布朗热风格，法国调式和声，明亮配器，强烈的抒情，诗篇配曲，短暂一生中的成熟声音，印象主义色彩配戏剧对比。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
