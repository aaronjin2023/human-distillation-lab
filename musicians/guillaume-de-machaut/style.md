# Guillaume de Machaut — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Ars Nova polyphony, isorhythm, intricate rhythmic notation, sweet thirds and sixths, modal, courtly chanson and sacred mass, elegant and cerebral`
- ZH: 新艺术复调，等节奏，复杂节奏记谱，甜美的三六度，调式，宫廷尚松与弥撒，优雅而精密。

## (2) 音高与和声方向

- 主：调式对位，三度、六度为协和音程；等节奏（isorhythm）的 talea 与 color 循环。禁：功能和声、属—主解决、大小调二元。调性：调式中心 + 临时升降（musica ficta）收束；不协和短暂出现、迅速解决。

## (3) 旋律与节奏

- 旋律：长音 cantus firmus 在低声部，上下声部以短小动机交织；级进为主，跳进克制。节奏：等节奏重复、切分、复节奏，是风格本体。织体：三—四声部复调，声部等重。

## (4) 配器与音色

- 人声：三—四声部无伴奏合唱；世俗尚松偶配乐器（记谱未明，见 conflicts）。音色：清澈、均衡、无乐队。力度：靠声部进入与密度，不靠力度标记。

## (5) 曲式与结构

- 曲式：弥撒套曲（史上首部署名作曲家的完整弥撒套曲，见 conflicts）、回旋曲（rondeau）、叙事歌（ballade）、维勒莱（virelai）。结构：等节奏循环统一全曲；高潮在声部最密处。结尾：调式收束，常以空五度—八度收。

## (6) 该写什么 / 不该写什么

- 该写：等节奏循环、尚松与弥撒套曲、三度六度协和复调、宫廷抒情题材。
- 不该写：功能和声、奏鸣曲式、大乐队、半音化泛滥、通俗旋律。
- Negative prompt: `functional harmony, sonata form, large orchestra, rampant chromaticism, catchy pop melody, sentimental swell`

## (7) 测试提示词示例（现代题材：现代城市街角便利店夜景）

- Prompt: `In the style of Guillaume de Machaut, a quiet night scene at a small convenience store in a modern city, Ars Nova polyphony, isorhythm, sweet thirds and sixths, modal, three equal voices, elegant and cerebral, no instruments`
- 中文对照：马肖风格，现代城市小便利店夜景，新艺术复调，等节奏，甜美三六度，调式，三声部等重，优雅精密，无乐器。
- Negative: `functional harmony, sonata form, large orchestra, chromaticism, catchy pop melody`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
