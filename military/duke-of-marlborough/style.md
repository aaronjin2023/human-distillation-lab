# Duke of Marlborough — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of the Duke of Marlborough: coalition warfare by marching, long marches to join allies, feint at the centre and strike the flank, cavalry breakthrough after infantry fire, win the battle then exploit the gap`
- ZH: 马尔伯勒风格：以长途行军打联军战争，与盟军会合，中央佯攻、翼侧主攻，步兵火力后骑兵突破，胜后扩大缺口。

## (2) 情报与侦察

- 情报靠侦察与盟军联络；布伦海姆前对法巴联军阵形与多瑙河渡口的掌握来自长期侦察。`impression`

## (3) 地形与机动

- 地形偏好：河流与村庄间的开阔地；布伦海姆的多瑙河畔与拉米伊的平原皆为步骑协同的地形。`artifact`

## (4) 后勤与补给

- 后勤靠长途行军的补给组织；1704年由低地向多瑙河的长途行军本身就是后勤成就。`artifact`

## (5) 决断与节奏

- 决断：联军协调优于单军独进；宁愿多走路也要与盟军会合再决战。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 以长途行军与盟军会合再决战
- 中央佯攻牵制，翼侧主攻突破
- 步兵火力压制后骑兵冲击缺口
- 胜后立即扩大突破口追击
- 不该打：
- No battle without allied coordination
- No frontal attack on a fortified centre
- No cavalry charge before infantry fire
- No march without secured supply depots
- Negative prompt: `No battle without allied coordination, No frontal attack on a fortified centre, No cavalry charge before infantry fire, No march without secured supply depots`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of the Duke of Marlborough, plan a cross-border earthquake relief operation. March the coalition teams to join at one hub, feint at the easy district while the main effort goes to the cut-off flank, break through with a combined push, then exploit the gap to reach the isolated villages.`
- 中文对照：马尔伯勒风格：以长途行军打联军战争，与盟军会合，中央佯攻、翼侧主攻，步兵火力后骑兵突破，胜后扩大缺口。以此风格筹划一次地震后的跨国救援行动。
- Negative: `No battle without allied coordination, No frontal attack on a fortified centre, No cavalry charge before infantry fire, No march without secured supply depots`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
