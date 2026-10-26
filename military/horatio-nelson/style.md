# Horatio Nelson — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Horatio Nelson: break the line, sail straight at the enemy, cut the line in two, close action with guns and boarding, aggressive attack, the captain's initiative over the signal book`
- ZH: 纳尔逊风格：破线战术，直航敌阵，将敌纵队切成两段，近距离炮战与接舷，积极进攻，舰长临机决断优于信号手册。

## (2) 情报与侦察

- 情报靠侦察舰与俘虏；特拉法尔加前对法西联合舰队航向与队形的掌握来自长期追踪。`impression`

## (3) 地形与机动

- 地形偏好：开阔海面与风向；破线战术需要风向与海况配合，特拉法尔加的风向即为战机。`artifact`

## (4) 后勤与补给

- 后勤靠海军补给与直布罗陀据点；长期封锁依赖补给船与舰队轮换。`impression`

## (5) 决断与节奏

- 决断：积极进攻、近战、临机；宁愿冒旗舰受损的风险也要保住破线的冲击。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 直航敌阵，将敌纵队切成两段
- 近距离炮战，不远射消耗
- 以舰长临机决断弥补信号不及
- 在敌阵混乱时扩大战果
- 不该打：
- No long-range gunnery duel without closing
- No line-ahead battle without breaking the line
- No waiting for perfect signals
- No retreat after the line is broken
- Negative prompt: `No long-range gunnery duel without closing, No line-ahead battle without breaking the line, No waiting for perfect signals, No retreat after the line is broken`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Horatio Nelson, analyse a modern cyber conflict. Break the line: sail straight at the opponent's formation, cut it in two, close in for decisive action, and let local commanders act on initiative when signals cannot keep up.`
- 中文对照：纳尔逊风格：破线战术，直航敌阵，将敌纵队切成两段，近距离炮战与接舷，积极进攻，舰长临机决断优于信号手册。以此风格筹划一场网络攻防对抗。
- Negative: `No long-range gunnery duel without closing, No line-ahead battle without breaking the line, No waiting for perfect signals, No retreat after the line is broken`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
