# Jean-Philippe Rameau — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `French Baroque, harmonic theory in practice, rich chromatic harmony, vivid orchestral colour, dance and opera, bold and sensual`
- ZH: 法国巴洛克，和声理论的实践，丰富的半音和声，生动的管弦色彩，舞曲与歌剧，大胆而感性。

## (2) 音高与和声方向

- 主：功能和声理论（《和声学》1722 年）的实践；根音进行、七和弦、半音转调。禁：无调性、半音滥用。调性：调性清晰，但半音转调大胆；不协和为色彩。

## (3) 旋律与节奏

- 旋律：歌唱性强，装饰丰富；舞曲旋律简洁。节奏：舞曲节奏清晰；歌剧节奏富于对比。织体：主调为主，复调为辅；管弦织体丰富。

## (4) 配器与音色

- 乐器：羽管键琴、弦乐、管乐、打击乐；歌剧配器色彩丰富。音色：明亮、感性、富于对比。力度：靠配器对比。

## (5) 曲式与结构

- 曲式：歌剧（抒情悲剧、歌剧芭蕾）、羽管键琴组曲、康塔塔。结构：序曲—宣叙—咏叹—合唱—舞曲交替；高潮在戏剧转折处。结尾：庄严收束。

## (6) 该写什么 / 不该写什么

- 该写：功能和声、半音转调、歌剧芭蕾、羽管键琴组曲、管弦色彩。
- 不该写：无调性、半音滥用、复调的失控堆砌、沉闷慢速。
- Negative prompt: `atonality, aimless chromaticism, uncontrolled dense counterpoint, sluggish tempo, dull orchestration`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Jean-Philippe Rameau, a cup of coffee on a windowsill, French Baroque, rich chromatic harmony, vivid orchestral colour, harpsichord and strings, dance rhythms, bold and sensual`
- 中文对照：拉莫风格，一杯放在窗台上的咖啡，法国巴洛克，丰富半音和声，生动管弦色彩，羽管键琴与弦乐，舞曲节奏，大胆感性。
- Negative: `atonality, aimless chromaticism, uncontrolled dense counterpoint, sluggish tempo, dull orchestration`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
