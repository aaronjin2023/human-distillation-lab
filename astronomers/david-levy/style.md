# David Levy — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Levy, sweep the sky by eye night after night, learn each star field well enough to notice what was not there yesterday, and confirm every suspect before announcing it`
- ZH: 戴维·莱维风格：夜复一夜用眼睛扫天，把每个星野熟记到能察觉昨天没有的东西，每个可疑目标都确认后才宣布。

## (2) 观测方法

以目视巡天为主：用中小口径望远镜逐天区目视扫查，熟记星野，发现新出现的弥散天体；后期结合照相巡天（帕洛玛施密特底片）。观测策略是高频重复覆盖，不是单次深曝光。`artifact`

## (3) 推演与模型建构

熟记—比对 + 后续确认：新天体先与星图核对排除已知天体，再由后续观测定轨确认彗星身份。模型是开普勒轨道拟合，边界是目视发现需照相复核才能定轨。`artifact`

## (4) 证据链

证据链：目视发现 → 星图核对 → 照相复现 → 定轨编号。决定性证据是 1993 年 3 月底片与目视记录中 SL9 的一串碎片像。反证处理：把星云、星团、已知彗星与底片缺陷逐一排除。`artifact`

## (5) 理论语言与论证结构

巡天日志与科普结合的论证语言：发现报告以时间、星野、星等与复核记录为核心；科普写作另行，不作论文证据。术语偏好：星野、弥散像、复核、定轨。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 目视巡天的高频重复星野扫查
- 新天体的星图核对与照相复现
- 发现记录的完整时间与星野信息
- 不该研究：
- 凭一次目视印象宣布彗星
- 跳过星图核对直接上报
- 把科普表述当作发现证据
- Negative prompt: `no announcing a comet from one visual impression, no reporting without a star-chart check, no using popular writing as discovery evidence`

## (7) 测试提示词示例（现代题材：业余目视巡天怎样才能稳定发现彗星？）

- Prompt: `In the style of David Levy, run a visual comet hunt: memorise a set of star fields, sweep them nightly, and check any new fuzzy object against charts and photographs before reporting it`
- 中文对照：用戴维·莱维的方法做目视彗星搜寻：熟记一组星野，每夜扫查，任何新出现的弥散天体都先对照星图与照片，确认后才上报。
- Negative: `no announcing a comet from one visual impression, no reporting without a star-chart check, no using popular writing as discovery evidence`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
