# Heinrich Schütz — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `German early Baroque, sacred polyphony with Italian monody, vivid text painting, restrained grandeur, psalms and passions in clear declamation`
- ZH: 德国巴洛克早期，圣咏复调融意大利单声部歌曲，生动绘词，克制的庄严，诗篇与受难曲的清晰宣叙。

## (2) 音高与和声方向

- 主：调式向大小调过渡的和声；通奏低音为骨架；绘词性半音。禁：世俗歌剧式的炫技、功能和声的机械进行。调性：调式中心稳定，收束庄重。

## (3) 旋律与节奏

- 旋律：贴近德语歌词语调，级进为主，关键处跳进；宣叙性强。节奏：歌词重音主导。织体：复调与单声交替，合唱与独唱对比。

## (4) 配器与音色

- 人声：合唱与独唱；乐器：通奏低音、弦乐、管乐（按场合增减）。音色：素净、庄严。力度：靠织体对比。

## (5) 曲式与结构

- 曲式：诗篇经文歌、受难曲（福音史家宣叙 + 群众合唱）、合唱音乐集。结构：以经文结构定音乐结构；受难曲以宣叙推进、合唱定格。高潮在受难叙事的关键句。结尾：平静收束。

## (6) 该写什么 / 不该写什么

- 该写：德语圣咏复调、绘词、受难曲、诗篇经文歌、通奏低音。
- 不该写：歌剧炫技、与歌词无关的装饰、功能和声机械进行。
- Negative prompt: `operatic virtuosity, wordless ornament, mechanical functional harmony, orchestral bombast`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Heinrich Schütz, a cup of coffee on a windowsill, German early Baroque sacred polyphony, vivid text painting, restrained grandeur, voices with basso continuo, solemn and clear`
- 中文对照：许茨风格，一杯放在窗台上的咖啡，德国巴洛克早期圣咏复调，生动绘词，克制庄严，人声与通奏低音，肃穆清晰。
- Negative: `operatic virtuosity, wordless ornament, mechanical functional harmony, orchestral bombast`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
