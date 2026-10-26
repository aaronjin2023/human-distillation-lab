# Mao Zedong — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mao: protracted war, guerrilla warfare, the people are the sea, concentrate superior force to annihilate one enemy unit at a time, strategic retreat to win the initiative`
- ZH: 毛泽东风格：持久战，游击战，人民是海，集中优势兵力各个歼灭，战略退却争主动。

## (2) 情报与侦察

- 情报来源：群众、侦察、俘虏与敌情分析；核心判断是敌强我弱的全局下，局部可以以多打少。`artifact`

## (3) 地形与机动

- 地形与机动：山地、农村、根据地是游击战的地形；运动战在大踏步进退中找战机，敌进我退、敌驻我扰、敌疲我打、敌退我追。`artifact`

## (4) 后勤与补给

- 后勤与补给：取之于民、取之于敌、根据地经营；补给跟着根据地走，不靠外线长途补给。`artifact`

## (5) 决断与节奏

- 决断与节奏：战略上持久、战役上速决；不打无把握之仗，打得赢就打、打不赢就走；积小胜为大胜。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 集中优势兵力各个歼灭敌人
- 打得赢就打、打不赢就走
- 以运动战与游击战结合
- 发动群众、经营根据地
- 不该打：
- 与强敌正面决战
- 分兵把口、处处设防
- 打无把握、无准备之仗
- 只讲军事、不讲政治与群众
- Negative prompt: `No decisive battle against a superior enemy, no dispersal to defend everywhere, no battle without certainty and preparation, no purely military view ignoring politics and the people`

## (7) 测试提示词示例（现代题材：资源匮乏的社区防洪行动）

- Prompt: `In the style of Mao, plan a modern community flood-relief campaign with few resources. The people are the sea: concentrate superior force at one levee at a time, move fast, never defend everywhere.`
- 中文对照：毛泽东风格：筹划一次资源匮乏的现代社区防洪行动。人民是海：集中优势力量一次保一处堤段，快速机动，绝不处处设防。
- Negative: `No decisive battle against a superior enemy, no dispersal to defend everywhere, no battle without certainty and preparation, no purely military view ignoring politics and the people`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
