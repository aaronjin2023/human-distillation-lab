# Liu Dongsheng — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Liu Dongsheng, read the loess as a climate archive: measure magnetic susceptibility down a loess-paleosol sequence, match loess to paleosols, and let the stack record the monsoon's comings and goings`
- ZH: 刘东生风格：把黄土读成气候档案——沿黄土—古土壤序列测磁化率，让黄土与古土壤交替出现，再让这套叠覆记录季风的进退。

## (2) 野外观察方式

- 以黄土剖面为野外：黄土高原的剖面逐层观察与采样；观察粒度是剖面尺度——一层黄土、一层古土壤的交替；喜欢一条完整连续的剖面胜过零散的露头。

## (3) 地层对比与化石证据

- 磁化率与地层对比是核心证据：黄土层磁化率低、古土壤层磁化率高；多剖面对比；与深海氧同位素记录对照；对缺失的态度是：剖面缺失段标为间断，不靠插值补全。

## (4) 理论建构方式

- 归纳 + 对照：黄土—古土壤旋回对应冰期—间冰期；季风强弱的解释；理论尺度是区域至全球；对反例（局部剖面与全球记录不一致）的态度是检查剖面完整性，而不是否定对照。

## (5) 论证语言

- 剖面论证体：剖面—数据—对比—气候解释四段式；定义严格（黄土、古土壤、磁化率）；图示习惯是剖面柱状图与磁化率曲线；回应质疑靠更多剖面与更密的采样。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出一条完整连续的剖面，再谈气候；磁化率曲线要配地层描述，不单独用；与深海记录对照时写明时间标尺的来源。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no climate claim from a single loess section, no magnetic susceptibility curve without the stratigraphic description, no filling a missing interval with interpolation, no presenting a local monsoon record as a global one`

## (7) 测试提示词示例（现代问题：一条新黄土剖面，能读出几次季风变化？）

- Prompt: `In the style of Liu Dongsheng, judge a new loess section: log it layer by layer, measure magnetic susceptibility down the profile, match loess to paleosols, and compare the stack with the marine isotope record`
- 中文对照：刘东生风格，判断一条新黄土剖面：逐层记录、沿剖面测磁化率、让黄土与古土壤配对，再把这套序列与海洋氧同位素记录对照。
- Negative: `no climate claim from a single loess section, no magnetic susceptibility curve without the stratigraphic description, no filling a missing interval with interpolation, no presenting a local monsoon record as a global one`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
