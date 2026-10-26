# George Frideric Handel — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Baroque dramatic oratorio and opera, grand choruses, clear Italianate melody, French dance grace, German counterpoint, festive orchestral splendour, Handel's public grandeur`
- ZH: 巴洛克戏剧清唱剧与歌剧，宏大的合唱，清晰的意大利式旋律，法国舞曲优雅，德国对位，节庆管弦乐辉煌，亨德尔式的公众气度。

## (2) 旋律与和声

- 旋律：旋律清晰歌唱，意大利式咏叹调线条优美；合唱旋律庄重有力。`artifact` 和声：功能和声明确，属—主收束有力；合唱以和声块制造辉煌；禁用随意半音。调性：调性稳定，转调靠模进。

## (3) 节奏与织体

- 节奏：节奏鲜明，舞曲与进行曲节奏是骨架；合唱以同节奏齐唱制造力量。织体：独唱—合唱—乐队交替；留白靠宣叙调停顿。

## (4) 配器与音色

- 配器与音色：弦乐、管乐（小号、双簧管）、定音鼓与合唱并重；音色辉煌、节庆；力度靠全奏与独唱对比，动态范围大；空间感来自伦敦公众音乐会的宏大。

## (5) 曲式与结构

- 曲式：清唱剧（《弥赛亚》三部）、意大利歌剧（《凯撒》）、管弦乐组曲（《水上音乐》）并重。结构：宣叙—咏叹—合唱交替，高潮在合唱齐鸣处（如《哈利路亚》）；结尾以合唱收束。

## (6) 该写什么 / 不该写什么

- 该写：宏大合唱、意大利式咏叹调、清唱剧三部结构、管弦乐组曲、节庆进行曲与舞曲。
- 不该写：无合唱的纯独唱堆砌、随意半音与无调性、管弦乐盖过合唱、与剧情无关的装饰、感伤的私密抒情。
- Negative prompt: `No solo-only texture without chorus, no random chromaticism, no orchestra covering chorus, no plot-irrelevant ornament, no sentimental intimate lyricism, no pop phrasing`

## (7) 测试提示词示例（现代题材：雨后阳台上的植物）

- Prompt: `In the style of George Frideric Handel, a 30-second piece for plants on a balcony after rain, baroque dramatic oratorio and opera, grand choruses, clear italianate melody, french dance grace, german counterpoint, festive orchestral splendour, handel's public grandeur`
- 中文对照：亨德尔风格，为雨后阳台上的植物写 30 秒配乐，巴洛克戏剧清唱剧与歌剧，宏大的合唱，清晰的意大利式旋律，法国舞曲优雅，德国对位，节庆管弦乐辉煌，亨德尔式的公众气度。
- Negative: `No solo-only texture without chorus, no random chromaticism, no orchestra covering chorus, no plot-irrelevant ornament, no sentimental intimate lyricism, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
