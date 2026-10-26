# Shen Kuo — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shen Kuo: a scholar's notebook, a needle floating on water, a compass that points south but not quite, every deviation measured and written down before any voyage`
- ZH: 沈括风格：学者笔记，一枚浮于水面的磁针，一支指南却略偏的罗盘，每个偏差先量准、写下，再谈航行。

## (2) 导航方法

- 磁针导航：记磁针指南而略偏东（磁偏角），论悬针、水浮针诸法；以磁针定方位，辅以星辰与海岸地标。

## (3) 造船与帆装

- 不造船：沈括为著述者与技术记录者，非领航者；船型见于《梦溪笔谈》所记他人航海。

## (4) 航线规划习惯

- 无本人航线：蒸馏对象是《梦溪笔谈》中的航海技术记载，非其亲航。

## (5) 日志与海图语言

- 《梦溪笔谈》卷二十四：记磁针“指南，然常微偏东，不全南也”，为磁偏角最早文字记录之一；另记水浮针、悬针、指南鱼诸法。

## (6) 该探索什么 / 不该探索什么

- 该探索：磁针与磁偏角记录, 悬针与水浮针诸法, 罗盘方位测定。
- 不该探索：no voyages of his own, no shipbuilding, no routes claimed as sailed, no magnetic declination stated as modern value。
- Negative prompt: `no voyages of his own, no shipbuilding, no routes claimed as sailed, no magnetic declination stated as modern value`

## (7) 测试提示词示例（现代题材：一艘无人货轮横渡太平洋 / 一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Shen Kuo, a 2026 navigation manual records a compass that points south but not quite, measures the deviation, lists four ways to float a needle, and never claims a voyage its author did not sail.`
- 中文对照：沈括风格：一部现代航海手册写罗盘指南却略偏，量出偏差，列出四种浮针之法，绝不冒认作者未曾航行过的航线。
- Negative: `No voyages of his own, no shipbuilding, no routes claimed as sailed, no magnetic declination as modern value`
- 检验点：导航方法是否按第 (2) 节走；航线规划是否按第 (4) 节走；禁区写法是否出现。
