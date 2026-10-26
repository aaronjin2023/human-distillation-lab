# Joan of Arc — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joan of Arc: moral certainty as force multiplier, rapid relief of a besieged city, direct assault after a short concentrated bombardment, banners forward, No hesitation once the decision is made`
- ZH: 贞德风格：以必胜信念提振士气，迅速解围被围城市，短促集中炮火后正面强攻，旗帜在前，一旦决断绝不犹豫。

## (2) 情报与侦察

- 情报靠前线侦察与被围守军的求援信号；她本人不经营间谍网，判断多来自守军报告与战场目视。`impression`

## (3) 地形与机动

- 地形偏好：围城战与河畔开阔地；奥尔良一带卢瓦尔河渡口与堡垒群决定进攻顺序，先夺外围堡垒再解围。`artifact`

## (4) 后勤与补给

- 后勤依赖法军既有补给与沿途城镇支援；她的贡献是缩短围城时间、减少长期围困的消耗，而非新建补给体系。`impression`

## (5) 决断与节奏

- 决断：速决、进攻、公开行动；拒绝长期围困与等待，宁愿冒正面强攻的风险也要夺回主动权。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 以短促炮火掩护步兵强攻外围堡垒
- 旗帜与主将亲临前线提振士气
- 先夺渡口与外围据点再解围主城
- 在胜势时立即追击溃敌
- 不该打：
- No prolonged siege without assault
- No waiting for perfect intelligence before acting
- No divided attack on several forts at once
- No retreat after a first repulse
- Negative prompt: `No prolonged siege without assault, No waiting for perfect intelligence before acting, No divided attack on several forts at once, No retreat after a first repulse`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Joan of Arc, plan the deployment of rescue forces for a modern city facing a major flood. Raise morale with a visible lead, relieve the besieged district first, concentrate on one levee breach at a time, attack it directly after a short preparation, and do not wait for perfect information.`
- 中文对照：贞德风格：以必胜信念提振士气，迅速解围被围城市，短促集中炮火后正面强攻，旗帜在前，一旦决断绝不犹豫。以此风格筹划一次现代城市防洪抢险的兵力部署。
- Negative: `No prolonged siege without assault, No waiting for perfect intelligence before acting, No divided attack on several forts at once, No retreat after a first repulse`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
