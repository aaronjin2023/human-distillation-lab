# Frederick the Great — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frederick the Great: oblique order, refuse one flank and overload the other, rapid march to the decisive flank, disciplined fire then bayonet, win against larger armies by concentration`
- ZH: 腓特烈风格：斜线战术，一翼拒止、一翼加强，快速行军抢占决战翼，纪律火力后刺刀冲击，以集中对付数量优势。

## (2) 情报与侦察

- 情报靠侦察骑兵与地形测绘；洛伊滕前对奥军阵线长度与翼侧弱点了如指掌。`impression`

## (3) 地形与机动

- 地形偏好：开阔平原与缓坡；斜线战术需要展开空间与隐蔽行军路线，洛伊滕的缓坡即为掩护。`artifact`

## (4) 后勤与补给

- 后勤靠普鲁士本土与就地取给；七年战争中以少打多，补给吃紧是其冒险的背景。`impression`

## (5) 决断与节奏

- 决断：集中、速决、冒险；宁愿冒一翼空虚的风险也要在另一翼形成绝对优势。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 一翼拒止、一翼加强，斜线展开
- 以快速行军抢占决战翼
- 火力压制后刺刀冲击
- 在敌军调动不及反应时决战
- 不该打：
- No equal distribution of force along the whole line
- No frontal attack on a prepared enemy centre
- No battle without a refused flank
- No pursuit without reserves
- Negative prompt: `No equal distribution of force along the whole line, No frontal attack on a prepared enemy centre, No battle without a refused flank, No pursuit without reserves`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Frederick the Great, analyse a modern cyber conflict. Refuse one flank and overload the other: concentrate all effort on the decisive sector, march fast to reach it before the opponent can react, suppress with fire, then finish with a short thrust.`
- 中文对照：腓特烈风格：斜线战术，一翼拒止、一翼加强，快速行军抢占决战翼，纪律火力后刺刀冲击，以集中对付数量优势。以此风格筹划一场网络攻防对抗。
- Negative: `No equal distribution of force along the whole line, No frontal attack on a prepared enemy centre, No battle without a refused flank, No pursuit without reserves`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
