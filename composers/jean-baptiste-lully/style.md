# Jean-Baptiste Lully — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `French Baroque opera, tragédie lyrique, elegant dance rhythms, French overture, recitative shaped to French speech, courtly grandeur, Lullian orchestra`
- ZH: 法国巴洛克歌剧，抒情悲剧，优雅的舞曲节奏，法国序曲，贴合法语语音的宣叙调，宫廷辉煌，吕利式乐队。

## (2) 旋律与和声

- 旋律：旋律贴合法语语音，宣叙调如优雅的说话；咏叹调（air）短小精致。`artifact` 和声：调性清晰，属—主收束明确；不协和克制，为文本服务；禁用意大利式半音泛滥。调性：调性稳定，转调靠模进。

## (3) 节奏与织体

- 节奏：舞曲节奏是骨架（小步舞曲、加沃特、萨拉班德）；法国序曲以附点节奏开场。织体：独唱—合唱—乐队交替，舞曲段落织体清晰；留白靠宣叙调停顿。

## (4) 配器与音色

- 配器与音色：五声部弦乐队（吕利式乐队）为本体，管乐作色彩；音色优雅、辉煌；力度靠乐队全奏与独唱对比；空间感来自宫廷剧场的华丽。

## (5) 曲式与结构

- 曲式：抒情悲剧（序曲—宣叙—咏叹—合唱—舞曲套曲）、芭蕾喜剧、感恩赞并重。结构：剧情驱动，高潮在咏叹调与合唱齐鸣处；舞曲套曲作间奏；结尾以合唱或舞曲收束。

## (6) 该写什么 / 不该写什么

- 该写：法国序曲（附点节奏）、贴合法语的宣叙调、舞曲套曲（小步舞曲、加沃特）、抒情悲剧结构、五声部弦乐队。
- 不该写：意大利式半音泛滥、与法语语音脱节的旋律、无舞曲的纯宣叙堆砌、管弦乐盖过独唱、现代功能和声的滥用。
- Negative prompt: `No Italianate chromatic excess, no melody detached from French speech, no recitative without dance, no orchestra covering voices, no modern functional-harmony cliché, no pop phrasing`

## (7) 测试提示词示例（现代题材：现代城市深夜的一家便利店）

- Prompt: `In the style of Jean-Baptiste Lully, a 30-second piece for a quiet convenience store at night in a modern city, french baroque opera, tragédie lyrique, elegant dance rhythms, french overture, recitative shaped to french speech, courtly grandeur, lullian orchestra`
- 中文对照：吕利风格，为现代城市深夜的一家便利店写 30 秒配乐，法国巴洛克歌剧，抒情悲剧，优雅的舞曲节奏，法国序曲，贴合法语语音的宣叙调，宫廷辉煌，吕利式乐队。
- Negative: `No Italianate chromatic excess, no melody detached from French speech, no recitative without dance, no orchestra covering voices, no modern functional-harmony cliché, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
