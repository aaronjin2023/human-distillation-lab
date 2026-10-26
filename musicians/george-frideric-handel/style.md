# George Frideric Handel — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Baroque grandeur, majestic choruses, graceful Italianate melody, clear tonal harmony, dramatic opera and oratorio, public and ceremonial`
- ZH: 巴洛克庄严，雄伟合唱，优雅意大利式旋律，清晰调性和声，戏剧歌剧与清唱剧，公开而仪式化。

## (2) 音高与和声方向

- 主：功能和声清晰；合唱和声丰满；属—主收束明确。禁：半音化滥用、复调的失控堆砌。调性：调性稳定，大调庆典、小调庄重。

## (3) 旋律与节奏

- 旋律：意大利式歌唱线条，级进为主，装饰优雅；合唱旋律简洁有力。节奏：庄严附点节奏与舞曲节奏交替。织体：主调为主，合唱复调为辅。

## (4) 配器与音色

- 乐器：管弦乐队、合唱、独唱；《水上音乐》用管乐与弦乐。音色：辉煌、庄严。力度：靠合唱与乐队对比。

## (5) 曲式与结构

- 曲式：清唱剧、歌剧、协奏曲、组曲、圣歌。结构：宣叙—咏叹—合唱交替；合唱为高潮。结尾：庄严收束，常以合唱齐唱收尾。

## (6) 该写什么 / 不该写什么

- 该写：清唱剧、歌剧、雄伟合唱、意大利式旋律、仪式音乐。
- 不该写：半音化滥用、复调的失控堆砌、模糊调性、私密小品。
- Negative prompt: `aimless chromaticism, uncontrolled dense counterpoint, vague tonality, intimate miniature, sentimental swell`

## (7) 测试提示词示例（现代题材：现代城市街角便利店夜景）

- Prompt: `In the style of George Frideric Handel, a quiet night scene at a small convenience store in a modern city, Baroque grandeur, majestic choruses, graceful Italianate melody, clear tonal harmony, orchestra and chorus, public and ceremonial`
- 中文对照：亨德尔风格，现代城市小便利店夜景，巴洛克庄严，雄伟合唱，优雅意大利式旋律，清晰调性，管弦乐与合唱，公开仪式化。
- Negative: `aimless chromaticism, uncontrolled dense counterpoint, vague tonality, intimate miniature, sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
