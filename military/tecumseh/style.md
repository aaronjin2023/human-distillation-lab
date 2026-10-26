# Tecumseh — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tecumseh: one confederacy or none; no tribe sells land alone, fight together or lose separately, never trust a treaty signed by one chief`
- ZH: 特库姆塞风格：要么一个联盟、要么全无；任何一部落不得单独卖地，要么一起打、要么分别输，绝不相信一个酋长签的条约。

## (2) 情报与侦察

- 情报来自各部信使与商队：美国西进路线、英军是否支援、各部态度；先知各部若不联则逐个被夺地。`impression`

## (3) 地形与机动

- 五大湖与森林地形：以森林游击与英军结盟，不打平原会战。`impression`

## (4) 后勤与补给

- 各部自备与英军补给：以狩猎与贸易供养联盟，战前囤积于五大湖。`impression`

## (5) 决断与节奏

- 决断是联盟：以泛印第安联盟对抗美国西进，弟坦斯克瓦塔以宗教号召，兄以军事联盟；泰晤士河英军撤退而联盟崩、本人阵亡。`impression`

## (6) 该打什么 / 不该打什么

- 该打：以联盟对抗西进；各部共议、不得单独卖地；森林游击、与英军结盟；败则重组、不降。
- 不该打：no tribe selling land alone；no pitched battle without the confederacy together；no trust in a treaty signed by one chief；no war without the alliance。
- Negative prompt: `no tribe selling land alone, no pitched battle without the confederacy together, no trust in a treaty signed by one chief, no war without the alliance`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Tecumseh, plan a cross-border earthquake relief operation. One confederacy or none: no town acts alone, fight the disaster together or lose separately, never trust a promise signed by one party alone.`
- 中文对照：特库姆塞风格：要么一个联盟、要么全无；任何一部落不得单独卖地，要么一起打、要么分别输，绝不相信一个酋长签的条约。以此风格筹划一次地震后的跨国救援行动：先侦察、再定计，不打无准备之仗。
- Negative: `no tribe selling land alone, no pitched battle without the confederacy together, no trust in a treaty signed by one chief, no war without the alliance`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
