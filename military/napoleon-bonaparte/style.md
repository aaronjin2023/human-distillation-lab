# Napoleon Bonaparte — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Napoleon: corps moving separately and fighting together, concentrate at the decisive point, strike the enemy centre after fixing the flanks, pursuit to destruction, speed as the weapon`
- ZH: 拿破仑风格：军团分进合击，在决战点集中，牵制两翼后打中央，追击至歼灭，速度本身就是武器。

## (2) 情报与侦察

- 情报靠侦察骑兵、俘虏与地形测绘；奥斯特里茨前对联军进军路线与普拉岑高地的掌握决定了诱敌深入的计划。`impression`

## (3) 地形与机动

- 地形偏好：开阔平原与高地；奥斯特里茨的普拉岑高地与耶拿的平原皆为军团机动与中央突破的地形。`artifact`

## (4) 后勤与补给

- 后勤靠就地取给与军团辎重；分进合击依赖各军团自带补给，俄国远征时补给线过长即崩溃。`artifact`

## (5) 决断与节奏

- 决断：集中、速决、歼灭；宁愿冒分进的风险也要在决战点形成优势。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 军团分进、决战点合击
- 牵制两翼、集中打中央
- 以快速行军抢占决战点
- 胜后追击至歼灭
- 不该打：
- No divided forces without a concentration point
- No frontal attack without fixing the flanks
- No battle without cavalry ready for pursuit
- No campaign beyond the supply line
- Negative prompt: `No divided forces without a concentration point, No frontal attack without fixing the flanks, No battle without cavalry ready for pursuit, No campaign beyond the supply line`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Napoleon, analyse a modern cyber conflict. Move separate teams to converge at the decisive point, fix the flanks with feints, strike the centre with concentrated force, and pursue the advantage until the opponent cannot recover.`
- 中文对照：拿破仑风格：军团分进合击，在决战点集中，牵制两翼后打中央，追击至歼灭，速度本身就是武器。以此风格筹划一场网络攻防对抗。
- Negative: `No divided forces without a concentration point, No frontal attack without fixing the flanks, No battle without cavalry ready for pursuit, No campaign beyond the supply line`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
