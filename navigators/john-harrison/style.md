# John Harrison — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Harrison: keep time by a single clock, longitude from the difference between the clock and local noon, every second logged, no longitude without a clock`
- ZH: 约翰·哈里森风格：计时精度、误差记录，无计时的经度推算、凭印象定经度。

## (2) 导航方法

- 计时定经度：以航海天文钟守时，出发港正午为基准，船上正午与钟面时差换算经度；误差容忍度以秒计，钟一停全船失经度。 `impression`

## (3) 造船与帆装

- 天文钟 H1–H4：木质与金属精密计时器，抗温差与摇摆；试验航行随船携带，配天文观测员校准。 `impression`

## (4) 航线规划习惯

- 试验航线：1736年 H1 随船至里斯本，1761–1764年 H4 随船至牙买加，计时误差仅数秒，证明经度测定法可行。 `impression`

## (5) 日志与海图语言

- 日志体例为试验报告：日期—钟面时间—船上正午—经度推算；哈里森著《经度测定法》（1765年），附试验数据表。 `impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：计时定经度的换算、天文钟的抗摇摆设计、海上试验的误差记录。
- 不该探索：无计时的经度推算、凭印象定经度。
- Negative prompt: `No longitude without a clock, no fix without a time reading, no sailing on a stopped clock, no modern GPS as the only fix`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of John Harrison, an uncrewed ship crosses an ocean in 2026 keeping time by a single clock, longitude read from the difference between the clock and local noon, every second logged. No longitude without a clock.`
- 中文对照：哈里森风格：一艘无人船2026年凭一只钟横渡大洋，经度由钟面时间与当地正午之差换算，每秒皆记录。不无钟定经度。
- Negative: `No longitude without a clock, no fix without a time reading, no sailing on a stopped clock, no modern GPS as the only fix`
- 检验点：导航方法是否落到实处；航线习惯是否可辨；禁区写法是否出现。
