# Christoph Willibald Gluck — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Classical opera reform, noble simplicity, music serving drama, restrained ornament, clear Italianate melody, expressive chorus, truth over virtuosity`
- ZH: 古典歌剧改革，高贵的单纯，音乐服务于戏剧，克制的装饰，清晰的意大利式旋律，富于表情的合唱，真实高于炫技。

## (2) 旋律与和声

- 旋律：旋律清晰歌唱，装饰克制；咏叹调短小，服务于剧情。`artifact` 和声：功能和声明确，属—主收束清晰；半音仅作表情；禁用无剧情支撑的炫技装饰。调性：调性稳定，转调靠剧情情绪。

## (3) 节奏与织体

- 节奏：节奏随剧情变化，合唱与舞曲段落规整；宣叙调贴合文本。织体：独唱—合唱—乐队交替；留白靠宣叙停顿。

## (4) 配器与音色

- 配器与音色：弦乐、管乐与合唱并重；音色高贵、克制；力度靠合唱与乐队对比；空间感来自维也纳与巴黎歌剧院。

## (5) 曲式与结构

- 曲式：歌剧改革三部曲（《奥菲欧》《阿尔切斯特》《伊菲格涅亚》）为核心；结构靠剧情驱动，高潮在合唱与咏叹调处；结尾以合唱收束。

## (6) 该写什么 / 不该写什么

- 该写：歌剧改革（音乐服务戏剧）、高贵的单纯、克制的咏叹调、表情合唱、剧情驱动的结构。
- 不该写：无剧情支撑的炫技装饰、da capo 咏叹调的冗长重复、管弦乐盖过独唱、与剧情无关的芭蕾、感伤的滥情。
- Negative prompt: `No plot-free virtuoso ornament, no long da capo repetition, no orchestra covering voices, no plot-irrelevant ballet, no sentimental excess, no pop phrasing`

## (7) 测试提示词示例（现代题材：现代城市深夜的一家便利店）

- Prompt: `In the style of Christoph Willibald Gluck, a 30-second piece for a quiet convenience store at night in a modern city, classical opera reform, noble simplicity, music serving drama, restrained ornament, clear italianate melody, expressive chorus, truth over virtuosity`
- 中文对照：格鲁克风格，为现代城市深夜的一家便利店写 30 秒配乐，古典歌剧改革，高贵的单纯，音乐服务于戏剧，克制的装饰，清晰的意大利式旋律，富于表情的合唱，真实高于炫技。
- Negative: `No plot-free virtuoso ornament, no long da capo repetition, no orchestra covering voices, no plot-irrelevant ballet, no sentimental excess, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
