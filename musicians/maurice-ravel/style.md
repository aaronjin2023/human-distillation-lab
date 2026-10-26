# Maurice Ravel — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Precision and polish, orchestration as jewel-cutting, Basque and Spanish colour, jazz glint, classical forms in modern dress`
- ZH: 精确与打磨，配器如宝石切割，巴斯克与西班牙色彩，爵士闪光，古典曲式穿现代外衣

## (2) 音高与和声方向

- 主：功能和声 + 调式、半音、爵士和声作色彩，调性清晰；禁：模糊的印象主义漫游、无结构的色彩堆砌。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性 + 装饰精致，乐句均衡；节奏：波莱罗固定节奏、西班牙舞曲节奏、爵士切分；织体：主调，配器分层极精，独奏乐器轮流歌唱。`artifact`

## (4) 配器与音色

- 配器：管弦乐教科书级精确，每件乐器只说一句、说得恰到好处；音色明亮、精致；钢琴织体如管弦乐缩影。`artifact`

## (5) 曲式与结构

- 曲式：奏鸣曲式、组曲式、舞剧，严守古典骨架；《波莱罗》以固定节奏上的配器渐变构成全曲；结尾常辉煌收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：精确配器、西班牙色彩、固定节奏渐变、古典曲式
- 不该写：模糊漫游、无结构色彩堆砌、厚重配器
- Negative prompt: `vague wandering, unstructured colour, heavy orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Maurice Ravel, a 30-second miniature for a small Yorkshire terrier sitting on a subway seat, a precise singing melody, Bolero-like steady rhythm with orchestration that slowly brightens, Spanish colour, jewel-like polish`
- 中文对照：拉威尔风格，为地铁座位上的约克夏犬写 30 秒微型曲，精确歌唱旋律，波莱罗式稳定节奏配器渐亮，西班牙色彩，宝石般打磨
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
