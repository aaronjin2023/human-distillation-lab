# Sergei Prokofiev — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音上实测的精确数值；频率等如需给，必须标注“近似参考，非实测”。

## (1) 一句话风格（prompt-ready）

- EN: `Prokofiev style, sharp motor rhythm, biting dissonance on diatonic base, lyrical melody with ironic twist, bright orchestration, classical form with modern harmony`
- ZH: 普罗科菲耶夫风格，锋利的动力节奏，调性基础上的尖锐不协和，带讽刺转折的抒情旋律，明亮配器，古典曲式配现代和声。

## (2) 音高与和声方向

- 主：调性基础 + 半音摩擦、附加音与错位和弦；不协和来自调性内的碰撞而非无调性；禁：无调性序列与功能和声的平庸进行。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性强、线条清晰、常带突然的半音转折与讽刺收尾；节奏：动力性、切分、机械重复；钢琴写作打击性强。`artifact`

## (4) 配器与音色

- 管弦乐明亮：木管尖锐、铜管短促、弦乐清晰；打击乐节奏化；钢琴协奏曲中钢琴如打击乐器使用。`artifact`

## (5) 曲式与结构

- 曲式：古典奏鸣曲式、组曲、芭蕾多乐章；结构：主题—发展—再现清晰，高潮靠节奏加速与音量，结尾明确。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：动力节奏、讽刺抒情、调性摩擦、明亮配器、古典曲式、儿童音乐的清晰叙事。
- 不该写：见 Negative prompt。
- Negative prompt: `atonal wandering, vague impressionism, sentimental swell, formless improvisation, muddy orchestration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Sergei Prokofiev, a 30-second piece for a late-night ramen shop with steam rising, Prokofiev style, sharp motor rhythm, biting dissonance on diatonic base, lyrical melody with ironic twist, bright orchestration, classical form with modern harmony`
- 中文对照：普罗科菲耶夫风格，为深夜拉面店升起的热气写一段 30 秒配乐，普罗科菲耶夫风格，锋利的动力节奏，调性基础上的尖锐不协和，带讽刺转折的抒情旋律，明亮配器，古典曲式配现代和声。
- Negative: 见第 (6) 节。
- 检验点：风格标志（见第 2–5 节）是否可辨，而不是写成一般性的同体裁音乐；现代题材是否被风格转化，而不是只换了标题。
