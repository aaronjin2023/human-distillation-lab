# Fridtjof Nansen — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fridtjof Nansen: freeze into the ice and drift with the current, log latitude, ice state and soundings daily, leave on skis for the final push`
- ZH: 弗里乔夫·南森风格：随冰漂流、以冰为路，硬闯浮冰带、蒸汽破冰。

## (2) 导航方法

- 冰上漂流导航：弗拉姆号随海冰漂流，以星辰与罗盘定位，测深辨海底地形；滑雪横越格陵兰，以罗盘与太阳定方向，补给靠雪橇拖运。 `impression`

## (3) 造船与帆装

- 弗拉姆号：特制圆底船体，冰压下会上浮而非被挤碎；配滑雪板、雪橇与犬队；补给靠船载口粮与猎取海豹。 `impression`

## (4) 航线规划习惯

- 漂流航线：1893年离挪威，北上至新西伯利亚群岛，弗拉姆号冻入海冰、随洋流漂向北极点方向；1895年南森与约翰森离船滑雪北上，次年返航。 `impression`

## (5) 日志与海图语言

- 日志体例为科学远征报告：日期—纬度—经度—冰况—测深—气温；南森著《极北之地》（1897年），以日记体重述漂流经过。 `impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：随冰漂流的被动航行、滑雪横越格陵兰、离船北上的雪橇冲刺。
- 不该探索：硬闯浮冰带、蒸汽破冰。
- Negative prompt: `No forcing through pack ice, no dash to the pole without return supplies, no sailing without soundings, no modern GPS as the only fix`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Fridtjof Nansen, an uncrewed vessel freezes into the ice in 2026 and drifts with the current toward the pole, logging latitude, ice state and soundings daily, the crew leaving on skis for the final push. No forcing through pack ice.`
- 中文对照：南森风格：一艘无人船2026年冻入海冰、随洋流漂向极点，每日记录纬度、冰况与测深，队员最后滑雪冲刺。不硬闯浮冰带。
- Negative: `No forcing through pack ice, no dash to the pole without return supplies, no sailing without soundings, no modern GPS as the only fix`
- 检验点：导航方法是否落到实处；航线习惯是否可辨；禁区写法是否出现。
