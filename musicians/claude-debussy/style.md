# Claude Debussy — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Whole-tone and pentatonic colour, parallel chords, sound as light and water, suggestion before statement, orchestration like mist`
- ZH: 全音阶与五声色彩，平行和弦，声音如光与水，暗示先于陈述，配器如雾

## (2) 音高与和声方向

- 主：全音阶 + 五声音阶 + 平行和弦，高色彩、低功能性，调性游移；禁：属—主强解决的大面积使用、德国式动机发展。`artifact`

## (3) 旋律与节奏

- 旋律：短小、碎片化，级进 + 五声跳进，呼吸如水波；节奏：自由、流动，少强拍重音；织体：主调 + 平行和弦，织体薄、透明，留白是结构。`artifact`

## (4) 配器与音色

- 配器：管弦乐透明，木管与竖琴色彩鲜明，弦乐分部细；音色柔、亮、如雾；力度多弱奏。`artifact`

## (5) 曲式与结构

- 曲式：自由曲式、组曲式，乐章如海浪起伏；《大海》三乐章如光的变化；结尾多渐弱、悬置。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：全音阶与五声、平行和弦、雾状配器、暗示性旋律
- 不该写：属—主强解决、德国式动机发展、厚重配器
- Negative prompt: `strong dominant-tonic cadence, Germanic motivic development, heavy orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Claude Debussy, a 30-second piece for a small Yorkshire terrier sitting on a subway seat at night, whole-tone shimmer, pentatonic fragments, parallel chords, sparse notes and long silences, dreamlike mist, like moonlight on water`
- 中文对照：德彪西风格，为夜里坐在地铁座位上的约克夏犬写 30 秒小品，全音阶闪烁，五声碎片，平行和弦，稀疏音符与长休止，梦幻雾气，如月光照水
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
