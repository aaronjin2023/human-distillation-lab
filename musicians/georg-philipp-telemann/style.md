# Georg Philipp Telemann — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `German Baroque, galant ease, dance suites and concertos, fluent melody, cosmopolitan mix of French, Italian and Polish styles`
- ZH: 德国巴洛克，华丽风格的流畅，舞曲组曲与协奏曲，流畅旋律，法国、意大利、波兰风格的融合。

## (2) 音高与和声方向

- 主：功能和声清晰；法国舞曲和声 + 意大利协奏曲和声 + 波兰民间色彩。禁：半音化滥用、复调的失控堆砌。调性：调性稳定，转调温和。

## (3) 旋律与节奏

- 旋律：流畅、歌唱性强，装饰优雅；波兰风格用民间舞曲节奏。节奏：舞曲节奏清晰，节奏感明快。织体：主调为主，复调为辅。

## (4) 配器与音色

- 乐器：长笛、小提琴、弦乐、管乐、通奏低音；编制灵活。音色：明亮、流畅。力度：靠配器与舞曲对比。

## (5) 曲式与结构

- 曲式：组曲、协奏曲、清唱剧、幻想曲。结构：舞曲组曲按舞曲顺序；协奏曲为利都奈罗。结尾：明确收束。

## (6) 该写什么 / 不该写什么

- 该写：舞曲组曲、协奏曲、长笛幻想曲、华丽风格、波兰民间色彩。
- 不该写：半音化滥用、复调的失控堆砌、沉重慢速、模糊调性。
- Negative prompt: `aimless chromaticism, uncontrolled dense counterpoint, vague tonality, sluggish tempo, heavy orchestration`

## (7) 测试提示词示例（现代题材：现代城市街角便利店夜景）

- Prompt: `In the style of Georg Philipp Telemann, a quiet night scene at a small convenience store in a modern city, German Baroque galant ease, fluent melody, dance suites, flute and strings, cosmopolitan French-Italian-Polish mix, light and graceful`
- 中文对照：泰勒曼风格，现代城市小便利店夜景，德国巴洛克华丽风格，流畅旋律，舞曲组曲，长笛与弦乐，法意波兰融合，轻盈优雅。
- Negative: `aimless chromaticism, uncontrolled dense counterpoint, vague tonality, sluggish tempo, heavy orchestration`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
