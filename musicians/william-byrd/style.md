# William Byrd — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `English Renaissance polyphony, restrained expressive counterpoint, clear text, keyboard fantasias and consort music, sacred Latin and English anthems in one hand`
- ZH: 英国文艺复兴复调，克制而富表现力的对位，歌词清晰，键盘幻想曲与合奏曲，拉丁弥撒与英文圣歌同源。

## (2) 音高与和声方向

- 主：调式对位，级进为主；偶有表现性半音与交叉关系（false relation，英国特色）。禁：功能和声、持续半音化。调性：调式中心稳定，收束庄重；交叉关系是色彩，不是体系。

## (3) 旋律与节奏

- 旋律：级进、歌唱性强；键盘作品以模仿点与音型交织。节奏：从容，歌词重音主导；键盘作品节奏更自由。织体：三—六声部人声；键盘为复调织体；维奥尔合奏为声部等重。

## (4) 配器与音色

- 人声：三—六声部无伴奏合唱；键盘（维吉纳琴、羽管键琴）；维奥尔合奏。音色：素净、均衡、内敛。力度：靠织体疏密。

## (5) 曲式与结构

- 曲式：弥撒、经文歌、圣歌（anthem）、键盘幻想曲、舞曲、变奏曲。结构：模仿点层层推进；键盘幻想曲以模仿点串联。结尾：平静收束。

## (6) 该写什么 / 不该写什么

- 该写：英国复调、弥撒与圣歌、键盘幻想曲、维奥尔合奏、克制表现。
- 不该写：功能和声、炫技、半音滥用、乐队化。
- Negative prompt: `functional harmony, virtuoso display, aimless chromaticism, orchestral texture, dramatic climax`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of William Byrd, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, English Renaissance polyphony, restrained expressive counterpoint, clear text, virginals and voices, serene and inward`
- 中文对照：伯德风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，英国文艺复兴复调，克制表现对位，歌词清晰，维吉纳琴与人声，宁静内敛。
- Negative: `functional harmony, virtuoso display, aimless chromaticism, orchestral texture, dramatic climax`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
