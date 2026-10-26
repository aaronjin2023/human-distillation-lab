# Joan Sutherland — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Coloratura soprano in the style of Joan Sutherland: pure silvery soprano, effortless coloratura, floating high notes, bel canto line, cool elegance`
- ZH: 萨瑟兰风格：纯净银亮的花腔女高音，花腔毫不费力，高音轻盈漂浮，美声线条，冷静优雅。

## (2) 音色与音域

- 花腔女高音，音色银亮纯净，高音轻盈漂浮；主音色为银亮的花腔女高音，辅音色为弱音的轻盈，禁音色为戏剧性的胸声吼叫。`artifact`

## (3) 唱腔与发声技法

- 发声：气息轻盈，起音干净，收尾多渐弱漂浮；唱腔：花腔跑动均匀清晰，颤音细腻，连音线条长，弱音控制极佳。`artifact`

## (4) 咬字与语言

- 意大利语花腔咬字轻，元音统一，辅音不抢；换气点藏在花腔间隙。`artifact`

## (5) 节奏与即兴

- 速度均匀，装饰音精确落在拍点；乐句流畅，节奏稳健。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：贝里尼与多尼采蒂花腔女主角（露琪亚、《梦游女》阿米娜）、威尔第抒情女主角（薇奥莱塔）、亨德尔与莫扎特花腔曲目、长线条美声咏叹调、疯狂场面的花腔段落。
- 不该唱：`No dramatic chest voice, no rough chesty belt, no heavy vibrato, no spoken declamation, no jazz phrasing`
- Negative prompt: `No dramatic chest voice, no rough chesty belt, no heavy vibrato, no spoken declamation, no jazz phrasing`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `Sing in the style of Joan Sutherland, a song about a cup of coffee cooling on a windowsill in the morning. Pure silvery soprano, effortless coloratura, floating high notes, bel canto line, cool elegance, light orchestra.`
- 中文对照：萨瑟兰风格：唱一首关于清晨一杯咖啡放在窗台上变凉的歌。纯净银亮的花腔女高音，花腔毫不费力，高音轻盈漂浮，美声线条，冷静优雅，轻型管弦乐伴奏。
- Negative: `No dramatic chest voice, no rough chesty belt, no heavy vibrato, no spoken declamation, no jazz phrasing`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
