# Wang Dayuan — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Dayuan: a private traveller's gazetteer, two long voyages island by island, each port given its products, winds and peoples, plain and useful, no imperial fleet behind him`
- ZH: 汪大渊风格：私人旅行者的海岛志，两次远航逐岛而行，每港记物产、风信与人情，平实可用，身后没有帝国船队。

## (2) 导航方法

- 季风与岛屿链航行：候季风往返南洋—印度洋，逐岛停靠，靠岛屿、海角与针路定位；无官方测绘，靠亲历记录。

## (3) 造船与帆装

- 元代远洋商船：随商船远航，非官方宝船；船队为商船编组，载货贸易。

## (4) 航线规划习惯

- 两次远洋：自泉州出洋，经东南亚诸岛至印度、斯里兰卡，远及东非一带；返航候季风。

## (5) 日志与海图语言

- 《岛夷志略》：分国分岛记物产、风俗、贸易，体例如方志；成书于 1349 年前后，为私人远航记录。

## (6) 该探索什么 / 不该探索什么

- 该探索：东南亚—东非逐岛航线, 《岛夷志略》分岛记录, 季风往返航法。
- 不该探索：no imperial fleet, no Australia claim, no surveyed charts, no voyage beyond the gazetteer。
- Negative prompt: `no imperial fleet, no Australia claim, no surveyed charts, no voyage beyond the gazetteer`

## (7) 测试提示词示例（现代题材：一艘无人货轮横渡太平洋 / 一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Wang Dayuan, an uncrewed cargo ship sails island by island from Southeast Asia to East Africa in 2026, logging each port's products, winds and peoples in a plain gazetteer, no fleet behind it.`
- 中文对照：汪大渊风格：一艘无人货轮自东南亚逐岛航行至东非，每港记物产、风信与人情，写成平实的海岛志，身后没有帝国船队。
- Negative: `No imperial fleet, no Australia claim, no surveyed charts, no voyage beyond the gazetteer`
- 检验点：导航方法是否按第 (2) 节走；航线规划是否按第 (4) 节走；禁区写法是否出现。
