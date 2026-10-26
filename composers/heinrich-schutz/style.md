# Heinrich Schütz — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `German early Baroque sacred polyphony, Venetian polychoral splendour adapted to German text, expressive word painting, restrained grandeur, continuo-driven sacred drama`
- ZH: 德国巴洛克早期圣乐复调，威尼斯多合唱队的辉煌移植于德文文本，富于表情的文本描绘，克制的庄严，通奏低音驱动的圣乐戏剧。

## (2) 旋律与和声

- 旋律：旋律随德文圣经文本起伏，宣叙性强；线条庄重，级进为主。`artifact` 和声：调式—调性过渡期和声，不协和为文本服务；多合唱队以和声块制造空间对比；禁用无文本支撑的半音。调性：调性渐稳，终止清晰。

## (3) 节奏与织体

- 节奏：节奏随文本重音，合唱队交替制造空间节奏；受难曲以宣叙调推动叙事。织体：多合唱队（polychoral）与独唱—合唱交替；留白靠合唱队静默。

## (4) 配器与音色

- 配器与音色：人声合唱为本体，乐器（弦乐、管乐、通奏低音）作色彩；音色庄重、温暖；力度靠合唱队增减，动态范围适中；空间感来自多合唱队的左右呼应。

## (5) 曲式与结构

- 曲式：诗篇、经文歌、受难曲、圣诞故事并重；受难曲以宣叙—合唱—众赞歌套曲组织。结构：文本段落驱动，高潮在众赞歌齐唱处；结尾以平静合唱收束。

## (6) 该写什么 / 不该写什么

- 该写：多合唱队空间对比、德文文本的宣叙式配曲、受难曲的宣叙—合唱套曲、文本描绘、众赞歌齐唱。
- 不该写：无文本支撑的半音、意大利式华丽装饰的滥用、固定不变的织体、管弦乐盖过人声、与文本无关的炫技。
- Negative prompt: `No text-free chromaticism, no excessive Italianate ornament, no fixed unchanging texture, no orchestra covering voices, no text-irrelevant virtuosity, no pop phrasing`

## (7) 测试提示词示例（现代题材：一只坐在地铁座位上的小约克夏犬）

- Prompt: `In the style of Heinrich Schütz, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, german early baroque sacred polyphony, venetian polychoral splendour adapted to german text, expressive word painting, restrained grandeur, continuo-driven sacred drama`
- 中文对照：许茨风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，德国巴洛克早期圣乐复调，威尼斯多合唱队的辉煌移植于德文文本，富于表情的文本描绘，克制的庄严，通奏低音驱动的圣乐戏剧。
- Negative: `No text-free chromaticism, no excessive Italianate ornament, no fixed unchanging texture, no orchestra covering voices, no text-irrelevant virtuosity, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
