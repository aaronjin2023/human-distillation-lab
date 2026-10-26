# Philip II of Macedon — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Philip II of Macedon: reform first, fight later; long sarissa phalanx holds the centre, cavalry decides on the wing, diplomacy and bribery open the road before the battle`
- 中文：腓力二世风格：先改革、后打仗；长矛方阵稳住中央，骑兵在侧翼决胜，外交与贿赂先于决战开路。

## （2）情报与侦察

情报来自使节、外交网络与雇佣兵；先摸清希腊诸城邦的联盟与内斗，再决定打谁、拉谁。情报用来分化：贿赂与结盟先行，决战殿后。`artifact`

## （3）地形与机动

偏好开阔平原的方阵决战；机动方式是方阵正面牵制、骑兵侧翼突击，辅以攻城器械对付设防城市。`artifact`

## （4）后勤与补给

补给靠改革后的常备军与王室财政支撑，行军辎重精简；长期围城（如拜占庭）受后勤与季节约束，围而不克即转外交。`impression`

## （5）决断与节奏

决断风格：耐心与速决并用——能等则等（外交、贿赂、围困），该打则以方阵与骑兵合力一击致命；不打无把握的消耗战。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 长矛方阵正面牵制敌军
- 骑兵从侧翼或敌阵薄弱处突击决胜
- 战前以外交、结盟与贿赂分化敌方
- 改革兵制、常备军与攻城器械先行
- 打赢后以同盟与驻军巩固，不赶尽杀绝

**不该打（风格上的禁区）：**

- 方阵脱离骑兵掩护孤军深入
- 不打没有外交准备的硬仗
- 骑兵过早投入正面消耗
- 围城硬耗而无后勤保障
- 胜后滥杀、毁掉希腊同盟基础

**Negative prompt（可直接给文本模型）：**

`no phalanx advancing without cavalry cover, no battle without diplomatic preparation, no cavalry wasted in frontal attrition, no siege without logistics, no massacre after victory`

## （7）测试提示词示例（现代题材：一次现代企业的组织改革与市场决战）

- Prompt: `In the style of Philip II of Macedon, plan a company's reorganisation before a market showdown. Reform the core team first, hold the centre with a disciplined product line, let a fast mobile unit strike the competitor's weak flank, and use partnerships to split the rival alliance before the launch.`
- 中文对照：以腓力二世的风格，筹划一家企业的组织改革与市场决战：先改革核心团队，以严整的产品线稳住中央，让快速机动单元打击对手侧翼弱点，决战前用合作分化对手联盟。
- Negative: `no charge without reform, no flank attack without a solid centre, no frontal price war, no battle without allies`
