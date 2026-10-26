# Henry Purcell — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `English Baroque, expressive ground bass, poignant chromatic lament, clear declamation, theatre music and sacred anthems, tender and dramatic`
- ZH: 英国巴洛克，表现性固定低音，动人的半音哀歌，清晰宣叙，戏剧音乐与圣歌，温柔而戏剧化。

## (2) 音高与和声方向

- 主：固定低音（ground bass）上的和声进行；哀歌用下行半音低音；功能和声早期形态。禁：半音滥用、复调的失控堆砌。调性：小调哀歌与大调庆典对比鲜明。

## (3) 旋律与节奏

- 旋律：歌唱性强，贴近英语语调；哀歌旋律下行半音，极富表现力。节奏：宣叙贴近语言，咏叹节奏清晰。织体：主调为主，复调为辅；合唱与独唱交替。

## (4) 配器与音色

- 乐器：弦乐、管乐、通奏低音；戏剧音乐配器丰富。音色：温暖、富于对比。力度：靠配器与织体对比。

## (5) 曲式与结构

- 曲式：歌剧（《狄多》三幕）、半歌剧（semi-opera）、圣歌、葬礼音乐、器乐组曲。结构：宣叙—咏叹—合唱交替；固定低音统一全曲。高潮在哀歌处。结尾：按剧情收束。

## (6) 该写什么 / 不该写什么

- 该写：固定低音、半音哀歌、英语宣叙、戏剧音乐、圣歌。
- 不该写：意大利炫技、半音滥用、复调的失控堆砌、与歌词无关的装饰。
- Negative prompt: `Italian virtuoso display, aimless chromaticism, uncontrolled dense counterpoint, wordless ornament`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Henry Purcell, a cup of coffee on a windowsill, English Baroque, expressive ground bass, poignant chromatic lament, clear English declamation, strings and continuo, tender and dramatic`
- 中文对照：普塞尔风格，一杯放在窗台上的咖啡，英国巴洛克，表现性固定低音，动人半音哀歌，英语宣叙清晰，弦乐与通奏低音，温柔戏剧化。
- Negative: `Italian virtuoso display, aimless chromaticism, uncontrolled dense counterpoint, wordless ornament`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
