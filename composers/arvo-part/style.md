# Arvo Pärt — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Tintinnabuli, bell-like triads, simple diatonic melody, silence, slow tempo, sacred stillness, minimal means`
- ZH: 钟鸣作曲法，钟声式三和弦，简单全音阶旋律，沉默，慢速，神圣静谧，极简手段。

## (2) 旋律与和声

- 旋律：级进全音阶线条，简单、歌唱；tintinnabuli 声部按三和弦音环绕旋律。`artifact`
- 和声：三和弦为底，调性清晰；不协和极少，解决温和。`artifact`

## (3) 节奏与织体

- 节奏：极慢，自由呼吸；织体：二声部（旋律 + 钟鸣）为主，极简。

## (4) 配器与音色

- 配器：钢琴、小提琴、弦乐、合唱；音色纯净，泛音少，留白大。

## (5) 曲式与结构

- 曲式：短小体裁、变奏；结构靠旋律重复与微变，高潮克制，结尾宁静收束。

## (6) 该写什么 / 不该写什么

- 该写：钟鸣三和弦、级进全音阶旋律、沉默与留白、极慢速度、二声部织体、宁静收束。
- 不该写：chromatic wandering、no dense counterpoint、no loud climax、no functional cadence fireworks、no decorative virtuosity、no sentimental swell。
- Negative prompt: `No chromatic wandering, no dense counterpoint, no loud climax, no functional cadence fireworks, no decorative virtuosity, no sentimental swell`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Arvo Pärt, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, tintinnabuli bell triads, simple stepwise melody, long silences, slow sacred stillness`
- 中文对照：帕特风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，钟鸣三和弦，简单级进旋律，漫长沉默，缓慢神圣静谧。
- Negative: `No chromatic wandering, no dense counterpoint, no loud climax, no functional cadence fireworks, no decorative virtuosity, no sentimental swell`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
