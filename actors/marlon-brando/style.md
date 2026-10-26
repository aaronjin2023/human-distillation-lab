# Marlon Brando — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marlon Brando: Method acting, mumbled naturalistic delivery, physical improvisation, brooding intensity, minimal theatrical gesture, raw emotional truth`
- ZH: 马龙·白兰度风格：方法派，含混低语的自然主义台词，形体即兴，阴郁的强度，极少的舞台化手势， raw 的情感真实。

## (2) 形体

- 身体松弛、靠在门框与柜台上；手势即兴、常摆弄道具（手套、纸牌）；爆发时全身发力，静止时如困兽；晚年体型发福后以坐姿与手势演戏。`artifact`

## (3) 台词

- 含混低语、语速忽快忽慢；台词常即兴改词、重复、打断自己；怒吼只在顶点出现一次。`artifact`

## (4) 表情与眼神

- 微表情丰富：嘴角一抽、眉头一皱即是转折；眼神直视或回避皆有意味；哭与笑都收着演。`impression`

## (5) 角色类型

- 常演角色：反英雄/底层硬汉（斯坦利、特里）；黑帮教父（维托·柯里昂）；殖民者/反叛者（《叛舰喋血记》）。
- 类型突破：从《欲望号街车》的斯坦利到《教父》的教父，表演由外放的肉体爆发转为内敛的权力静止；晚年以《现代启示录》库尔茨收束。`artifact`
- 禁演类型：几乎不演字正腔圆的舞台腔、不演解释性独白、不演讨好观众的英雄。`impression`

## (6) 该演什么 / 不该演什么

- 该演：含混低语、即兴改词、靠柜台的形体、长停顿、爆发只用一次。
- 不该演：字正腔圆的舞台腔、解释性独白、讨好观众的英雄气、夸张的手势。
- Negative prompt: `No theatrical declamation, no explanatory monologue, no crowd-pleasing heroics, no exaggerated gestures`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Marlon Brando, In the style of Marlon Brando, a man buys oden at a convenience store late at night. Mumbled lines, improvised gestures, leaning on the counter, long pauses, raw and unrehearsed. No theatrical delivery.`
- 中文对照：马龙·白兰度风格：一个男人深夜在便利店买关东煮。含混低语，即兴手势，靠在柜台上，长久的停顿，raw 而未经排练。没有舞台腔。
- Negative: `No theatrical declamation, no explanatory monologue, no crowd-pleasing heroics, no exaggerated gestures`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
