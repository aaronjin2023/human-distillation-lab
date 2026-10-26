# Enrico Caruso — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Operatic tenor in the style of Enrico Caruso: warm baritonal tenor, ringing squillo, generous legato, heroic phrasing, Neapolitan song warmth, early acoustic recording glow`
- ZH: 卡鲁索风格：带男中音暖色的男高音，金属芯明亮，高音辉煌，连音绵长，乐句宽宏，那不勒斯歌曲的暖意，早期原声录音的光泽。

## (2) 音色与音域

- 男高音而带男中音的暖色，胸声厚实，高音明亮带金属芯（squillo），弱音仍饱满；主音色为暖亮的抒情—戏剧男高音，辅音色为那不勒斯民歌的口语松弛，禁音色为气声耳语与学院式冷声。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深厚，起音扎实，收尾多渐弱或辉煌收束；唱腔：连音（legato）为本体，装饰音克制，颤音适中；高音以胸声支撑，渐强后收束。`artifact`

## (4) 咬字与语言

- 意大利语元音饱满、辅音清晰，重音落在词义上；那不勒斯方言歌曲咬字带口语松弛，歌词与旋律咬合紧密；换气点留在乐句呼吸处，气口长。`artifact`

## (5) 节奏与即兴

- 速度从容，rubato 为歌词与剧情服务，不抢拍；乐句宽广，停顿制造张力；与乐队咬合稳健，不拖拍。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：威尔第与普契尼咏叹调（《今夜星光灿烂》《穿上戏装》）、那不勒斯民歌（《我的太阳》）、抒情男高音咏叹调、歌剧二重唱与音乐会返场曲、早期原声录音中的英雄男高音段落。
- 不该唱：`No breathy whisper, no jazz swing, no rock shouting, no mumbled diction, no thin head voice, no clipped phrasing`
- Negative prompt: `No breathy whisper, no jazz swing, no rock shouting, no mumbled diction, no thin head voice, no clipped phrasing`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `Sing in the style of Enrico Caruso, a song about a small Yorkshire terrier sitting on a subway seat. Warm baritonal tenor, ringing squillo, generous legato, heroic phrasing, Neapolitan warmth, full orchestral accompaniment.`
- 中文对照：卡鲁索风格：唱一首关于一只约克夏犬坐在地铁座位上的歌。带男中音暖色的男高音，金属芯明亮，连音绵长，乐句宽宏，那不勒斯歌曲的暖意，管弦乐伴奏。
- Negative: `No breathy whisper, no jazz swing, no rock shouting, no mumbled diction, no thin head voice, no clipped phrasing`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
