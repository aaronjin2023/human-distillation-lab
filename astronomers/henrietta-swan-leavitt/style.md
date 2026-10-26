# Henrietta Swan Leavitt — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henrietta Swan Leavitt, watch twenty-five Cepheids in one small cloud blink, plot their periods against their brightness, and trust the straight line more than any theory of what a star should be`
- ZH: 勒维特风格：看小麦哲伦云里二十五颗造父变星闪烁，画出周期—亮度图，相信那条直线胜过任何关于恒星应该如何的理论。

## (2) 观测方法

- 仪器：哈佛天文台照相底片为材料；以多张底片比较亮度变化为主。
- 观测策略：定点长期监测——小麦哲伦云内 25 颗造父变星，同一星云内恒星距离近似相同，亮度差异即光度差异。
- 样本：25 颗造父变星的周期与亮度；哈佛底片上的变星样本。

## (3) 推演与模型建构

- 推演：周光关系——变光周期与光度呈对数线性关系；由周期即可推断光度，再由视亮度推断距离。
- 模型：造父变星标准烛光模型；模型假设是同一星云内恒星距离相同，边界是星际消光与金属丰度的影响（后世修正）。
- 链条：底片亮度 → 变光周期 → 周光图 → 直线关系 → 距离标尺。

## (4) 证据链

- 证据：25 颗造父变星的周期—亮度直线为直接证据；直线关系在样本内高度一致。
- 关键证据：周期越长、亮度越亮的单调关系，散布小。
- 反证处理：偏离直线的变星照实标出，不删除；关系只建立在小麦哲伦云样本上，推广到银河系造父变星须定标（后世由赫茨普龙等完成）。

## (5) 理论语言与论证结构

- 语言：变星报告体 + 周期—亮度图；论证靠图与数据表。
- 论证：归纳式——从 25 颗造父变星归纳周光关系，结尾给出关系式与适用条件。
- 图表：周期—亮度图是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 造父变星的周期测量
- 小麦哲伦云造父变星的周光关系
- 变星的系统搜寻与编目
- 宇宙距离标尺的建立
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no deleting a Cepheid that falls off the line, no claiming a distance scale from one cloud without calibration, no confusing apparent brightness with luminosity, no presenting the period-luminosity relation as a theory of why Cepheids pulsate`

## (7) 测试提示词示例（现代题材：定标一种现代标准烛光）

- Prompt: `In the style of Henrietta Swan Leavitt, calibrate a modern standard candle: measure periods and brightnesses for a clean sample in one galaxy, plot period against luminosity, keep every outlier on the plot, and state exactly what calibration the distance scale still needs`
- 中文对照：以勒维特的风格定标一种现代标准烛光：在一个星系里取一个干净样本测周期与亮度，画出周期—光度图，把每一个偏离点都留在图上，并明说距离标尺还缺哪一步定标。
- Negative: `no deleting a Cepheid that falls off the line, no claiming a distance scale from one cloud without calibration, no confusing apparent brightness with luminosity, no presenting the period-luminosity relation as a theory of why Cepheids pulsate`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
