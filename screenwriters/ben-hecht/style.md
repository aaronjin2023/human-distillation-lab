# Ben Hecht — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ben Hecht: hard-boiled newspaper speed, overlapping rapid-fire dialogue, cynical romance, crime and the press as one machine, sentiment smuggled in under wisecracks`
- ZH: 本·赫克特风格：硬汉报人式的速度，重叠的快语对白，愤世嫉俗的浪漫，犯罪与报界同一台机器，俏皮话之下偷渡的温情。

## (2) 结构：三幕 / 序列 / 节拍

- 高速三幕式，靠新闻时效驱动：第一幕以突发事件开场，第二幕多线并行、消息与谣言满天飞，第三幕在截稿时间或枪战中收束。场次极短、切换极快，时间跨度常压缩在数日之内。喜剧与犯罪片共用同一套速度逻辑。

## (3) 对话

- 对白是全片的引擎：短句、抢白、重叠、打断，语速极快；俏皮话与黑话密集，人物一边说话一边行动。浪漫台词藏在斗嘴里——越是动情越要拿话顶回去。动作描写只写必要的走位与枪。

## (4) 人物弧光

- 主角多为记者、骗子、黑帮分子或间谍：聪明、愤世嫉俗、嘴上不饶人，弧光是硬壳裂开一道缝——在截稿或枪口之下露出一瞬温情，旋即又合上。对手是体制（报社、黑帮、情报机关），也是主角自己的犬儒。

## (5) 类型套路与创新

- 黑帮片 / 报界喜剧 / 间谍片。他遵守类型片的速度与桥段，但打破了“硬汉没有感情”的写法：温情只在俏皮话的缝隙里出现一次。创新在重叠对白与新闻节奏——剧本读起来像报纸排字间。禁套路：几乎不用缓慢的抒情场面，不写直白的爱情告白。

## (6) 该写什么 / 不该写什么

- 该写：重叠快语对白与抢白、报界与黑帮的硬汉世界、俏皮话之下的一瞬温情、截稿时间驱动的高速三幕。
- Negative prompt: `No slow lyrical scenes, no direct love confession, no earnest moral lecture, no ponderous exposition, no soft sentimental ending`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ben Hecht, a crime reporter buys oden at a convenience store late at night while a gangster waits outside. Overlapping rapid-fire dialogue, wisecracks, a deadline ticking. One line of tenderness slips through the jokes, then the hard shell closes again.`
- 中文对照：本·赫克特风格：一位犯罪记者深夜在便利店买关东煮，黑帮分子在门外等着。对白重叠快语、俏皮话不断，截稿时间滴答作响。一句温情从玩笑的缝隙里溜出来，随即硬壳又合上了。
- Negative: `No slow lyrical scenes, no direct love confession, no earnest moral lecture, no ponderous exposition, no soft sentimental ending`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
