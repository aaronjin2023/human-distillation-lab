# Henry Purcell — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `English Baroque dramatic music, ground bass, expressive word painting, Italianate melody with French dance grace, opera and semi-opera, anthems and funeral music`
- ZH: 英国巴洛克戏剧音乐，固定低音，富于表情的文本描绘，意大利式旋律兼法国舞曲优雅，歌剧与半歌剧，圣歌与葬礼音乐。

## (2) 旋律与和声

- 旋律：旋律富于表情，半音用于描绘悲伤（如狄多的 lament）；线条歌唱性强。`artifact` 和声：功能和声成型，固定低音（ground bass）提供骨架；半音作表情手段；禁用无文本支撑的半音。调性：调性稳定，固定低音上的半音下行是标志。

## (3) 节奏与织体

- 节奏：节奏随文本与戏剧情节变化；舞曲段落规整；固定低音的循环提供稳定脉动。织体：独唱—合唱—乐队交替；留白靠宣叙调停顿。

## (4) 配器与音色

- 配器与音色：弦乐、管乐、通奏低音与合唱并重；音色富于戏剧对比；力度靠全奏与独唱对比；空间感来自剧场与教堂。

## (5) 曲式与结构

- 曲式：歌剧（《狄多》三幕）、半歌剧（《仙后》戏剧加音乐插段）、圣歌、葬礼音乐并重。结构：剧情驱动，高潮在 lament 与合唱处；固定低音段落作情感核心；结尾以合唱收束。

## (6) 该写什么 / 不该写什么

- 该写：固定低音（ground bass）、半音 lament、文本描绘、半歌剧结构、圣歌与葬礼音乐的庄重。
- 不该写：无文本支撑的半音、固定低音的机械重复、管弦乐盖过独唱、与剧情无关的装饰、现代功能和声的滥用。
- Negative prompt: `No text-free chromaticism, no mechanical ground-bass repetition, no orchestra covering voices, no plot-irrelevant ornament, no modern functional-harmony cliché, no pop phrasing`

## (7) 测试提示词示例（现代题材：深夜雨中行驶的一辆出租车）

- Prompt: `In the style of Henry Purcell, a 30-second piece for a taxi driving through rain late at night, english baroque dramatic music, ground bass, expressive word painting, italianate melody with french dance grace, opera and semi-opera, anthems and funeral music`
- 中文对照：普塞尔风格，为深夜雨中行驶的一辆出租车写 30 秒配乐，英国巴洛克戏剧音乐，固定低音，富于表情的文本描绘，意大利式旋律兼法国舞曲优雅，歌剧与半歌剧，圣歌与葬礼音乐。
- Negative: `No text-free chromaticism, no mechanical ground-bass repetition, no orchestra covering voices, no plot-irrelevant ornament, no modern functional-harmony cliché, no pop phrasing`
- 检验点：风格是否可辨（旋律、和声、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
