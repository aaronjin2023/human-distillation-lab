# Irving Berlin — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Simple unforgettable song, diatonic melody, ragtime rhythm, direct emotion, show-tune craft, melody first`
- ZH: 简单难忘歌曲，全音阶旋律，拉格泰姆节奏，直接情感，音乐剧歌曲工艺，旋律第一。

## (2) 旋律与和声

- 旋律：全音阶级进，简单、易记；主题短小、歌唱性强。`artifact`
- 和声：功能和声，简单明确；转调温和，解决明确。`artifact`

## (3) 节奏与织体

- 节奏：拉格泰姆切分，动感；织体：主调为主，钢琴与乐队轻盈。

## (4) 配器与音色

- 配器：音乐剧乐队，钢琴突出；音色明亮、直接。

## (5) 曲式与结构

- 曲式：歌曲（AABA）、音乐剧；结构简洁，高潮克制，结尾明亮收束。

## (6) 该写什么 / 不该写什么

- 该写：简单全音阶旋律、拉格泰姆切分、功能和声、AABA 歌曲曲式、直接情感。
- 不该写：chromatic wandering、no dense counterpoint、no atonal harmony、no heavy orchestration、no ironic distance、no free improvisation without a written song。
- Negative prompt: `No chromatic wandering, no dense counterpoint, no atonal harmony, no heavy orchestration, no ironic distance, no free improvisation without a written song`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Irving Berlin, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, simple diatonic melody, ragtime syncopation, bright show-tune warmth, clear cadence`
- 中文对照：欧文·柏林风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，简单全音阶旋律，拉格泰姆切分，明亮音乐剧温暖感，清晰收束。
- Negative: `No chromatic wandering, no dense counterpoint, no atonal harmony, no heavy orchestration, no ironic distance, no free improvisation without a written song`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
