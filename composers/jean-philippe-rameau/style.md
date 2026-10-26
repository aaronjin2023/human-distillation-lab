# Jean-Philippe Rameau — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `French Baroque opera and harpsichord music, harmony theorist, rich orchestral colour, dance suites, expressive chromaticism within French elegance, tragédie lyrique`
- ZH: 法国巴洛克歌剧与羽管键琴音乐，和声理论家，丰富的管弦乐色彩，舞曲组曲，法国优雅内的表情性半音，抒情悲剧。

## (2) 旋律与和声

- 旋律：旋律贴合法语，咏叹调优雅；羽管键琴曲以装饰音与音型见长。`artifact` 和声：和声理论（《和声学》）的实践者，功能和声意识明确，半音作表情；禁用无理论支撑的随意半音。调性：调性稳定，转调靠和声逻辑。

## (3) 节奏与织体

- 节奏：舞曲节奏是骨架（小步舞曲、加沃特、里戈东）；歌剧宣叙调贴合法语。织体：独唱—合唱—乐队交替，羽管键琴曲为单人多声部；留白靠宣叙停顿。

## (4) 配器与音色

- 配器与音色：管弦乐色彩丰富（木管、铜管、弦乐），羽管键琴音色清脆；力度靠乐队全奏与独奏对比；空间感来自巴黎歌剧院的华丽。

## (5) 曲式与结构

- 曲式：抒情悲剧、歌剧—芭蕾（《殷勤的印第安人》四幕异国风情）、羽管键琴组曲并重。结构：剧情驱动，高潮在咏叹与合唱处；舞曲套曲作间奏；结尾以合唱或舞曲收束。

## (6) 该写什么 / 不该写什么

- 该写：法国抒情悲剧、歌剧—芭蕾结构、羽管键琴组曲、丰富的管弦乐色彩、和声理论指导的转调。
- 不该写：无和声逻辑的半音、与法语脱节的旋律、无舞曲的纯宣叙堆砌、管弦乐盖过独唱、意大利式炫技的滥用。
- Negative prompt: `No unprincipled chromaticism, no melody detached from French speech, no recitative without dance, no orchestra covering voices, no Italianate virtuosity excess, no pop phrasing`

## (7) 测试提示词示例（现代题材：黄昏时分的高铁车窗外）

- Prompt: `In the style of Jean-Philippe Rameau, a 30-second piece for a high-speed train window at dusk, french baroque opera and harpsichord music, harmony theorist, rich orchestral colour, dance suites, expressive chromaticism within french elegance, tragédie lyrique`
- 中文对照：拉莫风格，为黄昏时分的高铁车窗外写 30 秒配乐，法国巴洛克歌剧与羽管键琴音乐，和声理论家，丰富的管弦乐色彩，舞曲组曲，法国优雅内的表情性半音，抒情悲剧。
- Negative: `No unprincipled chromaticism, no melody detached from French speech, no recitative without dance, no orchestra covering voices, no Italianate virtuosity excess, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
