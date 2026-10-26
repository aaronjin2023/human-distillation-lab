# Josquin des Prez — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `High Renaissance polyphony, imitative counterpoint, paired imitation, clear text declamation, expressive chromatic touches, perfect balance of voices`
- ZH: 盛期文艺复兴复调，模仿对位，成对模仿，清晰的歌词宣叙，表现性半音，声部完美均衡。

## (2) 音高与和声方向

- 主：模仿对位中的调式和声；三度、六度协和；偶有表现性半音（如《千声悔恨》的下行半音）。禁：功能和声、持续半音化。调性：调式中心清晰，收束庄重；不协和按规则经过、延留后解决。

## (3) 旋律与节奏

- 旋律：主题短小、歌唱性强，级进为主；模仿进入时主题在各声部依次出现。节奏：从容、均衡，歌词重音决定节奏。织体：四—六声部，模仿与自由对位交替，偶有同节奏齐唱（homophony）强调歌词。

## (4) 配器与音色

- 人声：四—六声部无伴奏合唱。音色：纯净、均衡、透明。力度：靠声部进入与织体疏密。

## (5) 曲式与结构

- 曲式：定旋律弥撒、释义弥撒（paraphrase mass）、经文歌、尚松。结构：模仿点（point of imitation）为基本单位，层层推进；高潮在织体最密、音区最高处。结尾：庄重收束，常以同节奏齐唱收尾。

## (6) 该写什么 / 不该写什么

- 该写：模仿对位、定旋律与释义弥撒、经文歌、歌词清晰的复调。
- 不该写：功能和声、主调伴奏、半音化泛滥、乐队化。
- Negative prompt: `functional harmony, melody with accompaniment, rampant chromaticism, orchestral texture`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Josquin des Prez, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, High Renaissance polyphony, imitative counterpoint, paired imitation, clear text declamation, four equal voices, balanced and luminous`
- 中文对照：若斯坎风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，盛期文艺复兴复调，模仿对位，成对模仿，歌词清晰，四声部均衡，明亮。
- Negative: `functional harmony, melody with accompaniment, rampant chromaticism, orchestral texture`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
