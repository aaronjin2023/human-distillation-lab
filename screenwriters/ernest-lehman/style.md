# Ernest Lehman — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ernest Lehman: elegant thriller construction, a wrong man chased across a map, witty romance under pressure, a set piece every twenty minutes, the MacGuffin that nobody explains`
- ZH: 欧内斯特·莱曼风格：优雅的惊悚片结构，一个被误认的人在地图上被追逐，重压之下的机智浪漫，每二十分钟一场重头戏，无人解释的麦格芬。

## (2) 结构：三幕 / 序列 / 节拍

- 惊悚片三幕，靠地图与追逐组织：第一幕立下误认（错的人、错的地方），第二幕让主角穿越地图——玉米地、总统山、联合国大厦——每站一场重头戏，第三幕在悬崖或高处收束。时间跨度短，常为数日，靠追逐而非悬念推进。

## (3) 对话

- 对白优雅、机智、克制：短句、双关、俏皮话，浪漫藏在逃亡里。动作描写写重头戏：追逐、悬念、场景调度，每场戏都有一个视觉高点。独白极少，信息靠行动与对话泄露。

## (4) 人物弧光

- 主角多为被误认的普通人：广告商、记者、司机。弧光是从被动到主动——从逃跑到反击，从误认到认清自己。对手是体制与阴谋，爱情是逃亡路上的同伴。

## (5) 类型套路与创新

- 惊悚片 / 浪漫喜剧 / 剧情片。他遵守惊悚片的追逐与重头戏套路，但打破了“惊悚片不必优雅”的成见：对白与场面同样讲究。创新在地图结构——情节就是一张地图。禁套路：几乎不用直白的解释，不写冗长的背景交代。

## (6) 该写什么 / 不该写什么

- 该写：优雅惊悚片与地图式追逐、被误认的普通人、每二十分钟一场重头戏、重压之下的机智浪漫。
- Negative prompt: `No ponderous exposition, no explained MacGuffin, no slow middle act, no humourless thriller, no unearned rescue`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ernest Lehman, a small Yorkshire terrier is mistaken for a spy's dog and chased across a night city. Elegant thriller construction, a set piece every twenty minutes, witty romance under pressure. The MacGuffin is a bowl of oden, and nobody explains why.`
- 中文对照：欧内斯特·莱曼风格：一只约克夏犬被误认为是间谍的狗，在夜晚的城市里被追逐。优雅的惊悚片结构，每二十分钟一场重头戏，重压之下的机智浪漫。麦格芬是一碗关东煮，无人解释为什么。
- Negative: `No ponderous exposition, no explained MacGuffin, no slow middle act, no humourless thriller, no unearned rescue`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
