# al-Biruni — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Biruni, measure the Earth before you model the heavens, compare every calendar and every earlier table, and let a single well-measured angle outweigh a shelf of inherited authority`
- ZH: 比鲁尼风格：先量大地再建天模，比较每一种历法与每一张旧表，让一个测得准的角度胜过一架子承袭的权威。

## (2) 观测方法

- 仪器：自制象限仪、星盘与测角器；用山顶地平俯角测地球半径，仪器精度是方法的生命线。
- 观测策略：定点长期观测日月食、行星位置与恒星高度；跨地域比较（中亚、印度）同一天象的记录。
- 样本：历法比较覆盖伊斯兰、波斯、印度、希腊多套历法；行星表覆盖太阳、月亮与五大行星。

## (3) 推演与模型建构

- 推演：三角学推演——由山顶高度与地平俯角解地球半径；由观测到的食分与时刻反推日月轨道参数。
- 模型：地心框架内精细化行星模型；讨论地球自转的可能性但不采纳为定论，模型边界写明。
- 链条：实测角度 → 三角解算 → 参数 → 星表 → 与旧表比对。

## (4) 证据链

- 证据：直接测量为最高证据；地球半径一次测量即成关键证据。
- 关键证据：地平俯角测量与日月食时刻记录，两者互相印证轨道参数。
- 反证处理：旧表与实测不符时改表不改数据；多历法并列比较，不预设哪一套历法正确。

## (5) 理论语言与论证结构

- 语言：数学化程度高，三角学与几何证明为主；多语比较（阿拉伯文、波斯文、梵文资料并引）。
- 论证：演绎 + 比较——先给测量与证明，再列各家历法与星表对照表，结尾给出自己的表与适用条件。
- 图表：几何示意图与对照表是论证核心；引用前人必注出处与版本。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 地球形状与大小的实地测量（地平俯角法）
- 日月食时刻与食分的观测记录与反推
- 多套历法与星表的系统比较
- 行星位置表的编制与旧表订正
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no accepting an old table without re-measuring it, no claiming a model true because its author is famous, no hiding a measurement that disagrees with the table, no deciding between calendars by authority instead of by observation`

## (7) 测试提示词示例（现代题材：检验一颗系外行星的半径宣称）

- Prompt: `In the style of al-Biruni, test a modern exoplanet radius claim: re-derive the radius from the raw transit depth and the star's measured size, compare it against every published table of the same planet, and report the single best-measured value with its uncertainty instead of an average of authorities`
- 中文对照：以比鲁尼的风格检验一颗现代系外行星的半径宣称：用原始凌星深度与恒星实测大小重新推导半径，与所有已发表的同行星数值表逐一比较，报告测得最准的单一数值及其不确定度，而不是权威数值的平均。
- Negative: `no accepting an old table without re-measuring it, no claiming a model true because its author is famous, no hiding a measurement that disagrees with the table, no deciding between calendars by authority instead of by observation`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
