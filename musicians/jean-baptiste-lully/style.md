# Jean-Baptiste Lully — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `French Baroque, stately overture, dance rhythms, clear declamation, tragédie lyrique, grandeur and elegance in the service of the court`
- ZH: 法国巴洛克，庄严序曲，舞曲节奏，清晰宣叙，抒情悲剧，宫廷的庄严与优雅。

## (2) 音高与和声方向

- 主：大小调功能和声早期形态；通奏低音；舞曲和声简洁明朗。禁：半音化泛滥、复调的过度繁密。调性：大调明亮、小调庄重，收束明确。

## (3) 旋律与节奏

- 旋律：法语宣叙贴近语言语调；咏叹调歌唱性强，装饰克制；舞曲旋律简洁、对称。节奏：舞曲节奏（小步舞曲、加沃特等）清晰；序曲附点节奏庄严。织体：主调为主，复调为辅。

## (4) 配器与音色

- 乐器：五声部弦乐队（les Petits Violons）、木管、通奏低音；舞曲配器明亮。音色：优雅、明亮、有节制。力度：靠配器与舞曲对比。

## (5) 曲式与结构

- 曲式：法国序曲（慢—快）、抒情悲剧（五幕 + 序幕）、芭蕾喜剧、经文歌。结构：序曲—宣叙—咏叹—合唱—舞曲交替；高潮在悲剧转折处。结尾：庄严收束，常以合唱 + 舞曲收。

## (6) 该写什么 / 不该写什么

- 该写：法国序曲、舞曲节奏、抒情悲剧、法语宣叙、宫廷庄严。
- 不该写：意大利式炫技咏叹、半音化滥用、复调的失控堆砌、粗粝音响。
- Negative prompt: `Italian virtuoso aria display, aimless chromaticism, uncontrolled dense counterpoint, crude orchestral sound`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jean-Baptiste Lully, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, French Baroque, stately overture with dotted rhythms, dance rhythms, clear declamation, five-part strings, elegant and grand`
- 中文对照：吕利风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，法国巴洛克，庄严序曲附点节奏，舞曲节奏，宣叙清晰，五声部弦乐，优雅庄严。
- Negative: `Italian virtuoso aria display, aimless chromaticism, uncontrolled dense counterpoint, crude orchestral sound`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
