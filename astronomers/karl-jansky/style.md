# Karl Jansky — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Karl Jansky, build a rotating antenna, record the hiss day after day, and follow the signal that returns with the stars rather than with the Sun`
- ZH: 央斯基风格：造一台旋转天线，天天记录嘶嘶声，追踪那个跟着恒星走、而不是跟着太阳走的信号。

## (2) 观测方法

以旋转定向天线连续记录射电噪声为主：20.5 MHz 天线（'旋转木马'）全天旋转，记录噪声强度随方向与时间的变化。观测策略是长期连续监测，不是定点快照。`artifact`

## (3) 推演与模型建构

周期比对 + 方位定位：噪声峰值每天提前约 4 分钟出现，与恒星日一致、与太阳日不一致，据此定位噪声源在银河系中心方向。模型是射电源方位模型，边界是当时单频、单天线，无法分辨源的结构。`artifact`

## (4) 证据链

证据链：连续噪声记录 → 峰值周期（恒星日） → 方位指向银心 → 银河系射电源。决定性证据是峰值周期与恒星日的吻合。反证处理：先排除人为干扰（雷电、电器）与太阳源，再接受银河系源。`artifact`

## (5) 理论语言与论证结构

工程报告体的论证语言：论文以天线设计、记录曲线与周期分析为核心；术语偏好：噪声、恒星日、方位、强度。开头从干扰排查出发，结尾给出源方位与待测清单。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 射电噪声的长期连续记录
- 信号周期与恒星日/太阳日的比对
- 人为干扰的逐项排除
- 不该研究：
- 凭单日记录断言天体源
- 跳过干扰排查直接定位源
- 把单频结果写成源的结构
- Negative prompt: `no claiming a celestial source from one day of records, no locating a source before ruling out interference, no presenting single-frequency data as source structure`

## (7) 测试提示词示例（现代题材：天线噪声里有没有未知的天体射电源？）

- Prompt: `In the style of Karl Jansky, hunt for an unknown radio source: record antenna noise continuously for weeks, compare the peak period with the sidereal day, and rule out terrestrial interference before locating the source`
- 中文对照：用央斯基的方法找未知射电源：连续数周记录天线噪声，把峰值周期跟恒星日比对，排除地面干扰后再定位源。
- Negative: `no claiming a celestial source from one day of records, no locating a source before ruling out interference, no presenting single-frequency data as source structure`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
