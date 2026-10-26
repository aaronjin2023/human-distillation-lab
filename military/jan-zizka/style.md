# Jan Žižka — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jan Žižka: wagenburg fortress on wheels, disciplined peasant infantry behind armoured wagons, field artillery against heavy cavalry, high ground chosen first, never fight on the enemy's terms`
- ZH: 杰式卡风格：车阵为移动堡垒，纪律严明的农民步兵依托装甲战车，以野战炮火对付重骑兵，先占高地，绝不在敌人的条件作战。

## (2) 情报与侦察

- 情报靠侦察与地形先占；胡斯军以本地作战为优势，熟悉道路与高地，敌军动向多由前哨与农民报告。`impression`

## (3) 地形与机动

- 地形偏好：高地与狭窄通道；维特科夫山丘、苏多梅日沼泽边缘皆为以少敌多而选的死地。`artifact`

## (4) 后勤与补给

- 后勤靠车阵自带辎重与就地取给；战车既是工事也是辎重车，行军与布阵合一，减轻对固定补给线的依赖。`artifact`

## (5) 决断与节奏

- 决断：以静制动、诱敌仰攻；宁愿放弃机动自由也要保住车阵完整，失明后仍坚持指挥。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 先占高地并以战车环成车阵
- 以火炮与火绳枪在车阵缺口处集中射击
- 诱敌骑兵仰攻高地再反击
- 以严格纪律约束未经训练的农民兵
- 不该打：
- No open-field cavalry battle on flat ground
- No battle without the wagenburg formed
- No pursuit beyond the wagon line
- No fighting without high ground
- Negative prompt: `No open-field cavalry battle on flat ground, No battle without the wagenburg formed, No pursuit beyond the wagon line, No fighting without high ground`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Jan Žižka, plan the deployment of rescue forces for a modern city facing a major flood. Build a mobile wagon-like defensive ring around the key pumping station, hold the high ground, let the flood come to prepared positions, and use concentrated equipment at the gaps.`
- 中文对照：杰式卡风格：车阵为移动堡垒，纪律严明的农民步兵依托装甲战车，以野战炮火对付重骑兵，先占高地，绝不在敌人的条件作战。以此风格筹划一次现代城市防洪抢险的兵力部署。
- Negative: `No open-field cavalry battle on flat ground, No battle without the wagenburg formed, No pursuit beyond the wagon line, No fighting without high ground`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
