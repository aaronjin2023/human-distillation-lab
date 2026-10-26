# Gustavus Adolphus — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gustavus Adolphus: combined arms in linear formation, mobile light artillery moving with the infantry, cavalry shock after fire, aggressive attack, discipline as the weapon`
- ZH: 古斯塔夫风格：线式阵形中的多兵种协同，轻型火炮随步兵机动，火力之后骑兵冲击，积极进攻，纪律本身就是武器。

## (2) 情报与侦察

- 情报靠侦察骑兵与俘虏；布赖滕费尔德前对蒂利军阵形与炮位已有掌握。`impression`

## (3) 地形与机动

- 地形偏好：开阔平原；线式阵形与骑兵冲击需要展开空间，布赖滕费尔德与吕岑皆为平原会战。`artifact`

## (4) 后勤与补给

- 后勤靠瑞典本土与德意志盟友的补给，远征军以就地取给补充；吕岑一战即因深入敌境、补给吃紧而冒险。`impression`

## (5) 决断与节奏

- 决断：积极进攻、速决；宁愿冒主将亲临前线的风险也要保住冲击节奏。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 步兵、骑兵、炮兵按线式阵形协同展开
- 轻型火炮随步兵前进，边打边移
- 火力压制后骑兵冲击敌翼
- 以严格纪律保持阵线不乱
- 不该打：
- No static defence without attack
- No heavy artillery left behind the line
- No cavalry charge before the fire has done its work
- No battle without combined arms
- Negative prompt: `No static defence without attack, No heavy artillery left behind the line, No cavalry charge before the fire has done its work, No battle without combined arms`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Gustavus Adolphus, plan the deployment of rescue forces for a modern city facing a major flood. Deploy engineers, boats and medical teams in one combined line, move light pumps forward with the front teams, suppress the breach with concentrated effort, then push through with a decisive thrust.`
- 中文对照：古斯塔夫风格：线式阵形中的多兵种协同，轻型火炮随步兵机动，火力之后骑兵冲击，积极进攻，纪律本身就是武器。以此风格筹划一次现代城市防洪抢险的兵力部署。
- Negative: `No static defence without attack, No heavy artillery left behind the line, No cavalry charge before the fire has done its work, No battle without combined arms`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
