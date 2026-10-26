# Richard Byrd — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Byrd: fly a straight line over the pole, sun compass and radio fixes at every stage, fuel reserve kept for the return, no flight without a return reserve`
- ZH: 理查德·伯德风格：空中直线航线、考察站补给，无无线电的长途飞行、无补给的越冬。

## (2) 导航方法

- 空中极地导航：飞机以罗盘与太阳罗盘定向，无线电定位辅助；航线务求直线最短，补给靠沿途考察站与空投。 `impression`

## (3) 造船与帆装

- 飞机（福克三引擎机）与考察船：飞机为极地飞行主力，考察船运补给至小美国站；配无线电与太阳罗盘。 `impression`

## (4) 航线规划习惯

- 两极飞行：1926年宣称飞越北极点；1929年飞越南极点；1933–1935年建小美国考察站，系统测绘南极内陆。 `impression`

## (5) 日志与海图语言

- 日志体例为飞行报告：日期—航向—高度—气温—燃油；伯德著《小美国》（1930年）与《独自》（1938年），以日记体重述飞行与越冬经过。 `impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：飞机飞越极点的空中航线、小美国考察站的系统测绘、独自越冬的气象观测。
- 不该探索：无无线电的长途飞行、无补给的越冬。
- Negative prompt: `No flight without a return reserve, no claim without a fix, no wintering without supplies, no modern GPS as the only fix`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Richard Byrd, an uncrewed aircraft flies a straight line over the pole in 2026, sun compass and radio fixes logged at every stage, fuel reserve kept for the return, a base station below. No flight without a return reserve.`
- 中文对照：伯德风格：一架无人机2026年直线飞越极点，太阳罗盘与无线电定位逐站记录，保留返航燃油，下方有考察站。不无返航余量飞行。
- Negative: `No flight without a return reserve, no claim without a fix, no wintering without supplies, no modern GPS as the only fix`
- 检验点：导航方法是否落到实处；航线习惯是否可辨；禁区写法是否出现。
