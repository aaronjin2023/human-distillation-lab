# Gustav Mahler — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Huge symphony as world, folk song and sublime in one span, irony and transcendence, orchestration from whisper to cataclysm`
- ZH: 交响曲即世界，民间歌曲与崇高同框，反讽与超越，配器从耳语到天崩地裂

## (2) 音高与和声方向

- 主：功能和声 + 大胆半音、借调、调性长期游移后解决；禁：四平八稳的古典和声、无张力的解决。`artifact`

## (3) 旋律与节奏

- 旋律：民间歌唱线 + 崇高长线并置，动机短、可变形；节奏：进行曲、兰德勒舞曲、葬礼节奏交替；织体：管弦乐织体极厚与独奏耳语交替，声部密度变化极大。`artifact`

## (4) 配器与音色

- 配器：超大管弦乐，乐器极多，音色从极弱独奏到全奏天崩；人声（独唱、合唱）是交响曲的一部分。`artifact`

## (5) 曲式与结构

- 曲式：交响曲四至六乐章，时长常超一小时；动机在各乐章间互引；高潮迟来、收束或升华或渐弱。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：民间歌曲、崇高长线、超大配器、交响曲即世界
- 不该写：四平八稳、无张力的解决、轻薄配器
- Negative prompt: `square phrasing, tensionless cadence, thin orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Gustav Mahler, a 30-second symphonic miniature for a small Yorkshire terrier sitting on a subway seat, a folk-like singing theme, huge warm orchestration that swells from a whisper, irony and tenderness in one breath, ending in a luminous hush`
- 中文对照：马勒风格，为地铁座位上的约克夏犬写 30 秒交响微型曲，民间式歌唱主题，庞大温暖配器从耳语涌起，反讽与温柔同呼吸，以明亮寂静收束
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
