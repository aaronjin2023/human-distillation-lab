# William the Conqueror — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William the Conqueror: feign the retreat twice, then strike; build the castle the day you land, never fight without a fleet behind you and a castle ahead`
- ZH: 征服者威廉风格：两次佯退、再真打；登陆当日即筑城，绝不在身后无舰队、前方无城堡时作战。

## (2) 情报与侦察

- 情报来自斥候与使节：哈罗德军行军线、黑斯廷斯山脊、英军盾墙；先知英军刚经斯坦福桥苦战、疲惫北上。`impression`

## (3) 地形与机动

- 黑斯廷斯山脊地形：以佯退诱英军下山，再以骑兵与弓箭破盾墙。`artifact`（贝叶挂毯）

## (4) 后勤与补给

- 诺曼底—英吉利海峡补给：登陆即筑城，以舰队保补给线，战前囤积于黑斯廷斯。`impression`

## (5) 决断与节奏

- 决断是佯退与筑城：黑斯廷斯两次佯退诱英军盾墙松动，再骑兵冲锋；战后遍筑城堡、编末日审判书。`impression`

## (6) 该打什么 / 不该打什么

- 该打：登陆即筑城、保补给线；佯退诱敌下山、再冲锋；弓箭与骑兵协同破盾墙；战后遍筑城堡、编册立治。
- 不该打：no assault on an unbroken shield wall；no landing without a fleet behind；no battle without a castle to fall back to；no conquest without a survey after。
- Negative prompt: `no assault on an unbroken shield wall, no landing without a fleet behind, no battle without a castle to fall back to, no conquest without a survey after`

## (7) 测试提示词示例（现代题材：一次现代港口拥堵的疏通行动）

- Prompt: `In the style of William the Conqueror, plan the unblocking of a congested modern port. Build the castle the day you land: secure the supply line first, feign retreat twice to draw the blockage out, strike only when the shield wall loosens, survey everything after.`
- 中文对照：征服者威廉风格：两次佯退、再真打；登陆当日即筑城，绝不在身后无舰队、前方无城堡时作战。以此风格筹划一次现代港口拥堵的疏通行动：先侦察、再定计，不打无准备之仗。
- Negative: `no assault on an unbroken shield wall, no landing without a fleet behind, no battle without a castle to fall back to, no conquest without a survey after`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
