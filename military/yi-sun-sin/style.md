# Yi Sun-sin — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yi Sun-sin: thirteen ships against three hundred; use the current, not the cannon; hold the strait, never fight in open water you do not own`
- ZH: 李舜臣风格：十三艘对三百艘；用水流、不用大炮；守住海峡，绝不在不属于自己的开阔水域作战。

## (2) 情报与侦察

- 情报来自渔民与斥候船：日军水军动向、鸣梁海峡潮流与漩涡；战前先测潮流时辰。`artifact`（《乱中日记》）

## (3) 地形与机动

- 海峡与潮流地形：鸣梁海峡狭窄急流，日军大船队入峡即乱；闲山岛以鹤翼阵诱敌入湾。`artifact`

## (4) 后勤与补给

- 朝鲜水军造船与粮草：龟船与板屋船自造自修，战前囤积于闲山岛基地。`impression`

## (5) 决断与节奏

- 决断是守峡与潮流：鸣梁以十三艘守海峡，借急流破三百艘；“尚有十二艘”而不退。`artifact`（《乱中日记》有“今臣战船尚有十二”之语，译文不作 verbatim）

## (6) 该打什么 / 不该打什么

- 该打：守海峡、借潮流破敌；鹤翼阵诱敌入湾；龟船当先、火炮齐射；战后修船、再战。
- 不该打：no battle in open water against superior numbers；no fighting without knowing the tide；no retreat while ships remain；no victory without repairing the fleet after。
- Negative prompt: `no battle in open water against superior numbers, no fighting without knowing the tide, no retreat while ships remain, no victory without repairing the fleet after`

## (7) 测试提示词示例（现代题材：一次现代港口拥堵的疏通行动）

- Prompt: `In the style of Yi Sun-sin, plan the unblocking of a congested modern port. Thirteen tugs against three hundred ships: hold the strait, use the current not brute force, never fight in open water you do not own, repair the fleet after every battle.`
- 中文对照：李舜臣风格：十三艘对三百艘；用水流、不用大炮；守住海峡，绝不在不属于自己的开阔水域作战。以此风格筹划一次现代港口拥堵的疏通行动：先侦察、再定计，不打无准备之仗。
- Negative: `no battle in open water against superior numbers, no fighting without knowing the tide, no retreat while ships remain, no victory without repairing the fleet after`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
