# Zheng He — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zheng He: an imperial treasure fleet, two hundred ships moving as one city, monsoon legs from Malacca to Calicut to Hormuz, tribute routes kept, every port visited in order, nothing left to a single ship`
- ZH: 郑和风格：帝国宝船队，两百艘船如一座移动的城，乘季风自马六甲至古里至忽鲁谟斯，朝贡航线一丝不乱，港口按序访问，绝不托付单船。

## (2) 导航方法

- 季风分段航行与针路：以牵星术测纬、指南针定向，按季风分段：夏乘西南季风西行，冬乘东北季风返航；针路与更数成册。

## (3) 造船与帆装

- 宝船队：大船载宝、马船载马、粮船载粮、战船护航，分工编组；船队规模与宝船尺寸诸说不一，蒸馏只用航线与随行记录。

## (4) 航线规划习惯

- 七次下西洋：南京—马六甲—古里—忽鲁谟斯，远及东非木骨都束；航线固定，港口按序，不冒险改道。

## (5) 日志与海图语言

- 无郑和本人日志传世：航线靠马欢《瀛涯胜览》、费信《星槎胜览》、巩珍《西洋番国志》与《郑和航海图》重建。

## (6) 该探索什么 / 不该探索什么

- 该探索：七下西洋固定航线, 季风分段航行, 朝贡港口按序访问, 牵星与针路导航。
- 不该探索：no single-ship voyages, no trade outside the tribute system, no exaggerated ship sizes, no routes beyond the escort records。
- Negative prompt: `no single-ship voyages, no trade outside the tribute system, no exaggerated ship sizes, no routes beyond the escort records`

## (7) 测试提示词示例（现代题材：一艘无人货轮横渡太平洋 / 一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Zheng He, a 2026 fleet of uncrewed cargo ships sails in formation from Malacca to Calicut to Hormuz, keeping the monsoon legs and the port order, a moving city that never trusts a single ship.`
- 中文对照：郑和风格：一支 2026 年无人货运船队编队自马六甲航向古里、忽鲁谟斯，守住季风航段与港口次序，如一座移动的城，绝不托付单船。
- Negative: `No single-ship voyages, no trade outside the tribute system, no exaggerated ship sizes, no routes beyond the escort records`
- 检验点：导航方法是否按第 (2) 节走；航线规划是否按第 (4) 节走；禁区写法是否出现。
