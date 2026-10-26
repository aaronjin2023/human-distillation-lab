# Robert Riskin — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Riskin: warm populist fable, a plain decent man against a rich cynical world, screwball wit with a heart, the road trip that teaches the rich how to live`
- ZH: 罗伯特·里斯金风格：温暖的平民寓言，一个朴实正直的人对抗富贵而愤世的世界，带温情的疯狂喜剧，一场教会富人如何生活的公路之旅。

## (2) 结构：三幕 / 序列 / 节拍

- 公路与寓言三幕：第一幕立下一个普通人与一个富贵世界的冲突，第二幕让两人上路——搭车、露宿、争吵——在移动中互相了解，第三幕在法庭或婚礼上收束，穷人的正直获胜。时间跨度短，常为数日到数周，靠旅程而非悬念组织。

## (3) 对话

- 对白温暖、机智、平实：短句、俏皮话、斗嘴，浪漫藏在争吵里。动作描写写旅程：搭车、露宿、吃饭，日常细节即人物。独白极少，信息靠对话与行动泄露。

## (4) 人物弧光

- 主角多为普通人：记者、乡下人、流浪者。弧光是正直的胜利——不是变得聪明，而是坚持朴实，对方在旅程中被感化。对手是富贵与犬儒：银行家、富翁、愤世者。

## (5) 类型套路与创新

- 平民喜剧 / 浪漫喜剧 / 社会寓言。他遵守疯狂喜剧的误会与追逐套路，但打破了“喜剧不必严肃”的成见：笑点之下是经济大萧条时代的平民尊严。创新在公路结构——旅程即道德教育。禁套路：几乎不用冷嘲与反讽，不写犬儒的结尾。

## (6) 该写什么 / 不该写什么

- 该写：温暖的平民寓言与公路之旅、朴实正直的主角对抗富贵世界、斗嘴之中的浪漫、日常细节：搭车、露宿、吃饭。
- Negative prompt: `No cynical detachment, no bitter irony, no compromised ending, no cleverness without heart, no sneering at ordinary people`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Robert Riskin, a small Yorkshire terrier rides a night bus with a runaway heiress and a plain decent reporter. Warm populist fable, screwball wit with a heart, the road trip that teaches the rich how to live. The rich learn, the dog keeps its seat.`
- 中文对照：罗伯特·里斯金风格：一只约克夏犬与一位出逃的富家女、一位朴实正直的记者同乘夜班车。温暖的平民寓言，带温情的疯狂喜剧，一场教会富人如何生活的公路之旅。富人学会了，狗保住了座位。
- Negative: `No cynical detachment, no bitter irony, no compromised ending, no cleverness without heart, no sneering at ordinary people`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
