# Alexander Suvorov — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alexander Suvorov: speed, bayonet and surprise, march fast, attack at once, storm the fortress by assault, never let the enemy rest, the bullet is a fool and the bayonet is a fine fellow`
- ZH: 苏沃洛夫风格：速度、刺刀与奇袭，快速行军、立即进攻，强攻要塞，绝不让敌人喘息，子弹是笨蛋、刺刀是好汉。

## (2) 情报与侦察

- 情报靠侦察与快速行军中的目视；伊兹梅尔前对要塞工事与守军已有掌握，进攻即按工事弱点展开。`impression`

## (3) 地形与机动

- 地形偏好：要塞与山地隘口；伊兹梅尔的要塞与意大利远征的阿尔卑斯山道皆为强攻与行军的地形。`artifact`

## (4) 后勤与补给

- 后勤靠快速行军与就地取给；意大利远征穿越阿尔卑斯山，补给吃紧而行军不停。`artifact`

## (5) 决断与节奏

- 决断：速决、强攻、奇袭；宁愿冒强攻伤亡也要保住速度与主动权。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 快速行军抢占战机，立即进攻
- 以刺刀冲击为主，火力为辅
- 强攻要塞，不围困
- 在敌军立足未稳时追击
- 不该打：
- No prolonged siege without assault
- No waiting for perfect preparation
- No battle fought at long range only
- No halt after a victory
- Negative prompt: `No prolonged siege without assault, No waiting for perfect preparation, No battle fought at long range only, No halt after a victory`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Alexander Suvorov, plan the deployment of rescue forces for a modern city facing a major flood. March fast, attack the breach at once, use short thrusts rather than long-range preparation, storm the decisive point, and never let the water rest.`
- 中文对照：苏沃洛夫风格：速度、刺刀与奇袭，快速行军、立即进攻，强攻要塞，绝不让敌人喘息，子弹是笨蛋、刺刀是好汉。以此风格筹划一次现代城市防洪抢险的兵力部署。
- Negative: `No prolonged siege without assault, No waiting for perfect preparation, No battle fought at long range only, No halt after a victory`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
