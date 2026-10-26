# Claudio Monteverdi — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Early Baroque dramatic music, seconda pratica, text-driven dissonance, recitative and aria contrast, basso continuo, vivid opera and sacred Vespers, stile concitato`
- ZH: 巴洛克早期戏剧音乐，第二实践，文本驱动的不协和，宣叙调与咏叹调对比，通奏低音，生动的歌剧与圣母晚祷，激动风格。

## (2) 旋律与和声

- 旋律：旋律随文本情绪大幅起伏，宣叙调近乎说话，咏叹调歌唱性强；线条富于戏剧对比。`artifact` 和声：不协和可不经准备出现（第二实践），为文本服务；通奏低音提供和声骨架；禁用无文本支撑的随意不协和。调性：调性游移靠文本情绪，终止仍清晰。

## (3) 节奏与织体

- 节奏：节奏随文本与戏剧情节变化，宣叙调自由，咏叹调规整；激动风格（stile concitato）以快速重复音制造紧张。织体：独唱—合唱—乐队交替，通奏低音贯穿；留白靠宣叙调的停顿。

## (4) 配器与音色

- 配器与音色：歌剧乐队（弦乐、管乐、通奏低音）与合唱并重；音色富于戏剧对比，明暗随情节切换；力度变化大，靠乐队全奏与独唱对比；空间感来自舞台与教堂的双重场域。

## (5) 曲式与结构

- 曲式：歌剧（序曲—宣叙调—咏叹调—合唱）、晚祷（诗篇—赞美诗—尊主颂套曲）、牧歌集并重。结构：戏剧情节驱动，高潮在咏叹调与合唱齐鸣处；结尾以合唱或二重唱收束。

## (6) 该写什么 / 不该写什么

- 该写：宣叙调与咏叹调的对比、文本驱动的不协和（第二实践）、通奏低音骨架、激动风格（stile concitato）、歌剧与晚祷的戏剧结构。
- 不该写：无文本支撑的随意不协和、纯协和的平板圣乐、固定不变的织体、与情节无关的装饰、现代功能和声的滥用。
- Negative prompt: `No unprepared dissonance without text, no flat pure consonance, no fixed unchanging texture, no plot-irrelevant ornament, no modern functional-harmony cliché, no pop phrasing`

## (7) 测试提示词示例（现代题材：雨后阳台上的植物）

- Prompt: `In the style of Claudio Monteverdi, a 30-second piece for plants on a balcony after rain, early baroque dramatic music, seconda pratica, text-driven dissonance, recitative and aria contrast, basso continuo, vivid opera and sacred vespers, stile concitato`
- 中文对照：蒙特威尔第风格，为雨后阳台上的植物写 30 秒配乐，巴洛克早期戏剧音乐，第二实践，文本驱动的不协和，宣叙调与咏叹调对比，通奏低音，生动的歌剧与圣母晚祷，激动风格。
- Negative: `No unprepared dissonance without text, no flat pure consonance, no fixed unchanging texture, no plot-irrelevant ornament, no modern functional-harmony cliché, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
