# Preston Sturges — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Preston Sturges: screwball farce at full sprint, verbal wit piled on slapstick, class satire with a heart, a con that turns into love and a love that turns into a con`
- ZH: 普雷斯顿·斯特奇斯风格：全速冲刺的疯狂喜剧，语言机智叠加闹剧动作，带温情的阶级讽刺，骗局变成爱情、爱情变成骗局。

## (2) 结构：三幕 / 序列 / 节拍

- 疯狂喜剧三幕，速度即一切：第一幕以骗局或误会开场，第二幕让身份错位与追逐连环升级，第三幕在当场揭穿后以一句俏皮话或一个拥抱收束。场次短、切换快，常在火车、游艇、豪宅之间跳跃，时间跨度压缩在数日之内。

## (3) 对话

- 对白是全片的燃料：快、密、机智，双关与反语不断，人物一边斗嘴一边行动。动作描写写闹剧：跌倒、追逐、撞门，与台词同步进行。浪漫台词藏在骗局里，越是动情越要拿话顶回去。

## (4) 人物弧光

- 主角多为骗子、富翁或流浪导演：聪明、自负、爱演，弧光是骗局反噬——骗人者被自己的骗局困住，在揭穿的一刻才说出真话。对手是阶级与金钱，爱情是唯一的破局。

## (5) 类型套路与创新

- 疯狂喜剧 / 讽刺喜剧。他遵守疯狂喜剧的误会与追逐套路，但打破了“喜剧不必有主题”的成见：在《苏利文的旅行》中让喜剧导演去体验穷人的生活，喜剧本身成了主题。创新在速度与密度的结合——台词与动作同时满负荷。禁套路：几乎不用缓慢的抒情，不写道德说教。

## (6) 该写什么 / 不该写什么

- 该写：全速疯狂喜剧与身份错位、机智对白叠加闹剧动作、阶级讽刺之下的温情、骗局反噬：骗人者被自己的骗局困住。
- Negative prompt: `No slow lyricism, no moral lecture, no earnest confession, no ponderous realism, no humourless satire`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Preston Sturges, a con artist and a rich heiress argue over the last oden at a convenience store late at night. Screwball dialogue at full sprint, slapstick, class satire with a heart. The con turns into love, the love turns into a con, and the last line is a joke.`
- 中文对照：普雷斯顿·斯特奇斯风格：一个骗子与一位富家女深夜在便利店为最后一块关东煮争吵。疯狂喜剧对白全速冲刺，闹剧动作不断，阶级讽刺带着温情。骗局变成爱情，爱情变成骗局，最后一句是个玩笑。
- Negative: `No slow lyricism, no moral lecture, no earnest confession, no ponderous realism, no humourless satire`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
