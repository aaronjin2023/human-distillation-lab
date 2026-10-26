# Franz Schubert — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Early Romantic lyricism, endless song-like melody, wandering harmony, intimate and expansive at once, the song as the centre of all forms`
- ZH: 浪漫主义早期抒情，无尽的歌唱性旋律，游移和声，亲切与辽阔并存，艺术歌曲为一切体裁的中心。

## (2) 音高与和声方向

- 主：功能和声 + 游移转调（三度关系转调）；半音为色彩与游移服务。禁：无调性、半音滥用。调性：调性常游移，大调与小调并置；不协和温和解决。

## (3) 旋律与节奏

- 旋律：歌唱性强，级进为主，乐句绵长；艺术歌曲旋律贴近德语诗歌。节奏：流动，钢琴伴奏音型驱动。织体：主调为主，人声 + 钢琴；室内乐声部对话。

## (4) 配器与音色

- 乐器：人声 + 钢琴、弦乐四重奏 / 五重奏、管弦乐队。音色：温暖、亲切、富于歌唱性。力度：弱—中，靠旋律起伏。

## (5) 曲式与结构

- 曲式：艺术歌曲、套曲（《冬之旅》24 首）、交响曲、室内乐、奏鸣曲。结构：歌曲以诗歌结构定音乐结构；交响曲以奏鸣曲式但旋律主导。高潮在旋律最高点。结尾：按诗歌情绪收束，或平静或悬置。

## (6) 该写什么 / 不该写什么

- 该写：艺术歌曲、套曲、游移和声、歌唱旋律、室内乐。
- 不该写：无调性、半音滥用、炫技、情感浮夸。
- Negative prompt: `atonality, aimless chromaticism, virtuoso display, sentimental bombast, pop chord loop`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡）

- Prompt: `In the style of Franz Schubert, a cup of coffee on a windowsill, early Romantic lyricism, endless song-like melody, wandering harmony, voice and piano, intimate and expansive, tender and drifting`
- 中文对照：舒伯特风格，一杯放在窗台上的咖啡，浪漫主义早期抒情，无尽歌唱旋律，游移和声，人声与钢琴，亲切而辽阔，温柔漂泊。
- Negative: `atonality, aimless chromaticism, virtuoso display, sentimental bombast, pop chord loop`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
