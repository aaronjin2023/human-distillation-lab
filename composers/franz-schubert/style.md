# Franz Schubert — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Early Romantic song and symphony, endless singing melody, sudden harmonic shifts, major-minor ambiguity, wandering and homecoming, Lieder and chamber music`
- ZH: 浪漫主义早期艺术歌曲与交响曲，无尽的歌唱旋律，突然的和声转折，大小调暧昧，流浪与归家，艺术歌曲与室内乐。

## (2) 旋律与和声

- 旋律：旋律无尽歌唱，级进为主，乐句绵长；艺术歌曲旋律贴合德文诗歌。`artifact` 和声：功能和声为基底，突然转调（三度关系）与大小调暧昧是标志；禁用无诗歌支撑的随意半音。调性：调性游移靠突然转调，终止仍清晰。

## (3) 节奏与织体

- 节奏：节奏随诗歌与旋律流动；钢琴伴奏音型（如《冬之旅》的脚步声）是节奏骨架。织体：主调为主，声乐加钢琴；室内乐四—五声部对话；留白靠乐句呼吸。

## (4) 配器与音色

- 配器与音色：声乐与钢琴为本体，管弦乐队与室内乐并重；音色温暖、抒情；力度靠旋律与和声对比；空间感来自维也纳沙龙与音乐会的 intimate。

## (5) 曲式与结构

- 曲式：艺术歌曲（六百余首）、套曲（《冬之旅》）、交响曲、室内乐并重。结构：诗歌段落驱动，高潮在和声转折处；交响曲以奏鸣曲式组织；结尾常以静默或渐弱收束。

## (6) 该写什么 / 不该写什么

- 该写：艺术歌曲与套曲、无尽歌唱旋律、突然三度转调、大小调暧昧、钢琴伴奏音型描绘。
- 不该写：无歌唱性的机械音型、无诗歌支撑的随意半音、管弦乐盖过声乐、与结构无关的装饰、感伤的滥情。
- Negative prompt: `No unlyrical mechanical figuration, no poetry-free chromaticism, no orchestra covering voices, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`

## (7) 测试提示词示例（现代题材：深夜只亮着一盏台灯的空办公室）

- Prompt: `In the style of Franz Schubert, a 30-second piece for an empty office late at night with one desk lamp on, early romantic song and symphony, endless singing melody, sudden harmonic shifts, major-minor ambiguity, wandering and homecoming, lieder and chamber music`
- 中文对照：舒伯特风格，为深夜只亮着一盏台灯的空办公室写 30 秒配乐，浪漫主义早期艺术歌曲与交响曲，无尽的歌唱旋律，突然的和声转折，大小调暧昧，流浪与归家，艺术歌曲与室内乐。
- Negative: `No unlyrical mechanical figuration, no poetry-free chromaticism, no orchestra covering voices, no structure-irrelevant ornament, no sentimental excess, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
