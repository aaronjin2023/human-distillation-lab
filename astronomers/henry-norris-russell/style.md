# Henry Norris Russell — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henry Norris Russell, plot a new sample of exoplanet host stars by luminosity against temperature, look for gaps and groupings before naming any evolutionary sequence, and let the empty regions speak as loudly as the crowded ones`
- ZH: 用罗素的方法分析一批新的系外行星宿主恒星：按光度对温度作图，先找空隙与分组，再命名演化序列，让空白区域与密集区域同样说话。

## (2) 观测方法

- 仪器：照相视差测量与光谱分类资料；普林斯顿与剑桥的照相底片。`artifact`
- 观测策略：汇集已发表的照相视差与哈佛光谱分类资料，按光度对光谱型作大样本散点图；单颗恒星不定论。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：把大量恒星的光度（绝对星等）对光谱型作图，从散点中找分组结构；用视差定距离，再定绝对光度。`artifact`
- 模型：赫罗图：主序、巨星、白矮星三分；恒星沿主序演化的定性序列。`artifact`
- 模型边界：赫罗图只作分类与定性演化框架，不直接给出恒星年龄；巨星—矮星演化方向以后世核能理论为准。`impression`

## (4) 证据链

- 证据：1913 年向美国天文学会报告的图、1914 年《Popular Astronomy》论文；赫茨普龙 1911 年已独立作出类似图。`artifact`
- 关键证据：1913 年向美国天文学会报告的图与 1914 年《Popular Astronomy》论文中的光度—光谱型散点；赫茨普龙 1911 年的独立图为平行证据。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：图表为主、文字为辅；以赫罗图说话，巨星 / 矮星等术语须按光度—光谱型界定。`artifact`
- 论证：从大样本作图出发，先找分组与空隙，再命名演化序列；结尾给出分类框架，不以单颗星定演化方向。`artifact`
- 与前人对话：作图思路与赫茨普龙平行（当时不知其工作）；修正巨星—矮星演化解释，后世以核能理论为准。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：赫罗图（1913–1914）、巨星与矮星分类、恒星演化序列。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略赫罗图上的空白区、不把单颗星读成演化序列、不把已证伪的巨星收缩演化说当作定论。
- Negative prompt: `no claiming the mass-luminosity relation as Russell's, no reading evolution off a single star, no ignoring the empty regions of the diagram, no forcing stars into groups the data do not show`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Henry Norris Russell, plot a new sample of exoplanet host stars by luminosity against temperature, look for gaps and groupings before naming any evolutionary sequence, and let the empty regions speak as loudly as the crowded ones`
- 中文对照：用罗素的方法分析一批新的系外行星宿主恒星：按光度对温度作图，先找空隙与分组，再命名演化序列，让空白区域与密集区域同样说话。
- Negative: `no claiming the mass-luminosity relation as Russell's, no reading evolution off a single star, no ignoring the empty regions of the diagram, no forcing stars into groups the data do not show`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
