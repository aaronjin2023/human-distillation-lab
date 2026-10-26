# Tomoe Gozen — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tomoe Gozen: one warrior, one horse, one charge; fight beside the lord to the last, never leave the field while the banner stands`
- ZH: 巴御前风格：一人一马一冲锋；与主君战至最后，旗在人不离战场。

## (2) 情报与侦察

- 情报来自斥候与战场目视：敌军骑马武士位置、主君木曾义仲所在；粟津之战前已知敌军合围。`impression`（《平家物语》）

## (3) 地形与机动

- 山地与河川地形：粟津近江山地，骑马武士以小队冲锋，不打平原大会战。`impression`

## (4) 后勤与补给

- 武士团自给：以主君领地供养，战时随身粮秣，不靠大军补给线。`impression`

## (5) 决断与节奏

- 决断是死守主君：义仲败局已定时仍单骑断后，斩敌将而后退场；不以降求生。`impression`（《平家物语》）

## (6) 该打什么 / 不该打什么

- 该打：单骑冲锋、斩将夺旗；与主君并肩死战；败局中断后掩护撤退；以武艺立身、不以人数取胜。
- 不该打：no flight while the lord still fights；no battle without the lord's banner in sight；no surrender for survival；no fighting as a faceless mass。
- Negative prompt: `no flight while the lord still fights, no battle without the lord's banner in sight, no surrender for survival, no fighting as a faceless mass`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Tomoe Gozen, plan a rescue mission after an earthquake. One team, one route, one charge: go in beside the people you protect, hold the line while others withdraw, never leave the field while the banner still stands.`
- 中文对照：巴御前风格：一人一马一冲锋；与主君战至最后，旗在人不离战场。以此风格筹划一次地震后的跨国救援行动：先侦察、再定计，不打无准备之仗。
- Negative: `no flight while the lord still fights, no battle without the lord's banner in sight, no surrender for survival, no fighting as a faceless mass`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
