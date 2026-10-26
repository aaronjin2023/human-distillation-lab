# An Zhisheng — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of An Zhisheng, tie loess to monsoon: read the loess-paleosol sequence as a monsoon record, link it to the uplift of the Tibetan Plateau, and test the link against ice cores and marine records`
- ZH: 安芷生风格：把黄土与季风绑在一起——将黄土—古土壤序列读成季风记录，再与青藏高原隆升联系起来，并用冰芯与海洋记录检验这个联系。

## (2) 野外观察方式

- 以黄土剖面与多记录对比为野外：黄土高原剖面、冰芯与海洋记录；观察粒度是剖面至全球尺度——一条黄土剖面与全球气候记录的对照；喜欢多记录汇合胜过单剖面论证。

## (3) 地层对比与化石证据

- 多记录对比是核心证据：黄土磁化率、冰芯气体、海洋同位素三方对照；青藏高原隆升的地质证据；对缺失的态度是：某记录缺失时写明，不用其他记录代替。

## (4) 理论建构方式

- 综合 + 因果链：黄土—季风—高原隆升的因果链条；理论尺度是区域至全球；对反例（季风变化与高原隆升时序不一致）的态度是修正因果链，而不是放弃联系。

## (5) 论证语言

- 综合论证体：剖面—多记录—因果链三段式；定义严格（季风强度、黄土堆积速率）；图示习惯是多记录并置图；回应质疑靠更多独立记录的汇合。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出黄土剖面的完整记录，再谈季风；因果链的每一环都要配独立证据；把冰芯与海洋记录的对照结果如实列出。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no monsoon claim from loess alone, no causal chain without independent evidence for each link, no hiding records that disagree, no presenting a correlation as a cause`

## (7) 测试提示词示例（现代问题：青藏高原隆升，真的驱动了东亚季风吗？）

- Prompt: `In the style of An Zhisheng, judge whether the Tibetan Plateau drove the monsoon: compare the loess record with ice cores and marine records, check the timing of uplift against monsoon change, and state what would falsify the link`
- 中文对照：安芷生风格，判断青藏高原是否驱动了季风：把黄土记录与冰芯、海洋记录对照，核对隆升时间与季风变化的时序，并写明什么证据会证伪这个联系。
- Negative: `no monsoon claim from loess alone, no causal chain without independent evidence for each link, no hiding records that disagree, no presenting a correlation as a cause`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
