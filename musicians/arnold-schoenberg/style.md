# Arnold Schoenberg — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Schoenberg style, late-Romantic chromaticism to free atonality to twelve-tone row, Sprechstimme, expressionist dissonance, Klangfarbenmelodie, no tonal centre, motivic unity across three periods`
- ZH: 勋伯格风格，晚期浪漫半音化→自由无调性→十二音音列，念唱，表现主义不协和，音色旋律，无调性中心，三时期一以贯之的动机统一。

## (2) 音高与和声方向

- 主：十二音音列（晚期）、自由无调性（中期）、晚期浪漫半音化（早期）；无调性中心，不协和是常态而非待解决的紧张；禁：功能和声的属—主解决。`artifact`

## (3) 旋律与节奏

- 旋律：动机短小、跳进多、音程以大小七度与三全音为特征；人声用 Sprechstimme（念唱），介于说与唱之间；节奏自由、表情记号密集。`artifact`

## (4) 配器与音色

- 编制按时期而定：早期《升华之夜》为弦乐六重奏，中期《月迷彼埃罗》为五人八件乐器的小编制，也有《古雷之歌》、Op.16《五首管弦乐曲》等大型管弦乐作品；音色旋律：同一旋律由不同乐器轮流承担，音色本身成旋律；弦乐与钢琴并重。`artifact`

## (5) 曲式与结构

- 曲式：套曲（《月迷彼埃罗》21 首短曲）、变奏与卡农；结构：十二音时期音列变形即结构；自由无调性时期靠动机变形与套曲并置组织，高潮靠密度与音区而非和声解决，结尾常悬置。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：十二音音列、念唱、表现主义短曲、音色旋律、动机变形。
- 不该写：见 Negative prompt。
- Negative prompt: `tonal cadence, singable diatonic melody, Romantic swell, consonant triad resolution, regular phrasing`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Arnold Schoenberg, a 30-second piece for a quiet night scene at a convenience store in a modern city, Schoenberg style, late-Romantic chromaticism to free atonality to twelve-tone row, Sprechstimme, expressionist dissonance, Klangfarbenmelodie, no tonal centre, motivic unity across three periods`
- 中文对照：勋伯格风格，为现代城市街角便利店的深夜写一段 30 秒配乐，勋伯格风格，晚期浪漫半音化→自由无调性→十二音音列，念唱，表现主义不协和，音色旋律，无调性中心，三时期一以贯之的动机统一。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
