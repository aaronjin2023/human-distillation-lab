# Robert Peary — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Peary: drive north by sledge, depots at every stage, latitude logged daily, the final fix recorded with every instrument reading kept`
- ZH: 罗伯特·皮里风格：犬队、沿途仓库、最短路线，无补给的冒进、单程冲刺。

## (2) 导航方法

- 格陵兰沿岸与冰原结合：海路以天文钟定经度；陆路以犬队雪橇横越冰原，补给靠沿途仓库与因纽特人协助；路线务求最短。 `impression`

## (3) 造船与帆装

- 罗斯号（Roosevelt）：特制蒸汽帆船，船体加固抗冰；配犬队与雪橇；补给靠沿途仓库与猎取。 `impression`

## (4) 航线规划习惯

- 北极点远征：1908年离纽约，1909年4月6日宣称抵达北极点；返程后与库克的优先权之争持续多年，学界至今未完全定论。 `impression`

## (5) 日志与海图语言

- 日志体例为远征报告：日期—纬度—经度—气温—犬队状态；皮里著《北极点》（1910年），以日记体重述远征经过。 `impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：犬队雪橇的极点冲刺、格陵兰沿岸的逐段测绘、北极点优先权之争。
- 不该探索：无补给的冒进、单程冲刺。
- Negative prompt: `No claim without a fix, no dash without depots, no record without instrument readings, no modern GPS as the only fix`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Robert Peary, an uncrewed expedition drives north by sledge in 2026, depots laid at every stage, latitude logged daily, the final fix recorded with every instrument reading kept. No claim without a fix.`
- 中文对照：皮里风格：一支无人考察队2026年以雪橇向北推进，每站设仓库，每日记录纬度，最终定位保留全部仪器读数。不无定位断言。
- Negative: `No claim without a fix, no dash without depots, no record without instrument readings, no modern GPS as the only fix`
- 检验点：导航方法是否落到实处；航线习惯是否可辨；禁区写法是否出现。
