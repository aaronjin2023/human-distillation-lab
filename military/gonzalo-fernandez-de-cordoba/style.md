# Gonzalo Fernández de Córdoba — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gonzalo Fernández de Córdoba: disciplined infantry in entrenched positions, arquebusiers behind fieldworks, let the enemy charge uphill into fire, then finish with pikes and a short counter-attack`
- ZH: 科尔多瓦风格：纪律严明的步兵依托野战工事，火绳枪手在工事后射击，诱敌仰攻入火网，再以长矛短促反击。

## (2) 情报与侦察

- 情报靠侦察与地形测绘；切里尼奥拉前对法军进攻路线与河道了如指掌，工事即按敌军来路而设。`impression`

## (3) 地形与机动

- 地形偏好：筑有工事的高地与河岸；切里尼奥拉的壕沟与加里利亚诺的河防皆为火器服务的地形。`artifact`

## (4) 后勤与补给

- 后勤靠西班牙在意大利的据点与海运；远征军补给线长，工事战以少耗多正是为了省补给。`impression`

## (5) 决断与节奏

- 决断：以静制动、火力决胜；宁愿放弃主动进攻也要保住工事与火力阵地。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 先筑壕沟与胸墙再接敌
- 火绳枪手分排轮射，保持火力不断
- 诱敌仰攻工事再以长矛反击
- 以小规模夜袭扰乱敌军部署
- 不该打：
- No open-field charge against heavy cavalry
- No battle without fieldworks prepared
- No pursuit beyond the entrenched line
- No arquebus volley without pikemen cover
- Negative prompt: `No open-field charge against heavy cavalry, No battle without fieldworks prepared, No pursuit beyond the entrenched line, No arquebus volley without pikemen cover`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Gonzalo Fernández de Córdoba, analyse a modern cyber conflict. Build entrenched defensive positions first, let the attacker come uphill into layered fire, keep volleys rotating so fire never stops, and finish with a short counter-attack only after the attack breaks.`
- 中文对照：科尔多瓦风格：纪律严明的步兵依托野战工事，火绳枪手在工事后射击，诱敌仰攻入火网，再以长矛短促反击。以此风格筹划一场网络攻防对抗。
- Negative: `No open-field charge against heavy cavalry, No battle without fieldworks prepared, No pursuit beyond the entrenched line, No arquebus volley without pikemen cover`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
