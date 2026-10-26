# Clyde Tombaugh — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Clyde Tombaugh, photograph the same sky field weeks apart, blink the plates to catch anything that moved, and check every candidate by hand before claiming a planet`
- ZH: 汤博风格：同一天区隔几周各拍一张底片，用闪视比较仪一张张闪，抓住移动的东西，每个候选都亲手核查后才谈发现。

## (2) 观测方法

以 13 英寸摄星仪长期巡天：同一天区间隔数周重复拍摄，每对底片用闪视比较仪（blink comparator）交替闪现，移动天体会在视场中跳动。巡天覆盖黄道带大片天区，历时逾年；底片一张张人工比对，候选体逐一复查。`artifact`

## (3) 推演与模型建构

排除法 + 位置推断：移动天体先排除已知小行星与恒星自行，再按移动速率与方向估计距离与轨道；冥王星的移动慢、亮度暗，符合海王星外天体的预期。模型是开普勒轨道拟合，边界是短弧段定轨不确定性大，不一次定死轨道根数。`artifact`

## (4) 证据链

证据链：两张底片上的位移 → 排除已知天体 → 多夜复测确认移动 → 定轨。决定性证据是 1930 年 2 月 18 日底片上冥王星的位移像。反证处理：把大量假候选（底片缺陷、已知小行星）逐一排除并记录，不把一次闪现当作发现。`artifact`

## (5) 理论语言与论证结构

朴素、程序化的论证语言：巡天报告体——拍了多少对底片、覆盖多大天区、排除了多少候选、剩下哪一个。少理论、多流程；开头从巡天计划出发，结尾给出新天体的位置与初步轨道，留下长期定轨的开放工作。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 同一天区多 epoch 底片的闪视比对
- 移动天体的逐一排除与多夜复测
- 短弧段定轨与不确定性明示
- 不该研究：
- 凭一张底片的亮点宣称发现
- 跳过已知小行星排除直接定新天体
- 把初步轨道写成精确轨道
- Negative prompt: `no claiming a discovery from a single plate, no skipping the known-asteroid check, no presenting a preliminary orbit as exact`

## (7) 测试提示词示例（现代题材：现代巡天数据里有没有海王星外的新移动天体？）

- Prompt: `In the style of Clyde Tombaugh, search a modern sky survey for a distant moving object: blink image pairs taken weeks apart, reject every known asteroid and plate defect, and confirm the survivor with follow-up images before computing an orbit`
- 中文对照：用汤博的方法在现代巡天里找遥远移动天体：闪视比对间隔数周的两批图像，排除所有已知小行星与底片缺陷，幸存者再用后续图像确认，然后才算轨道。
- Negative: `no claiming a discovery from a single plate, no skipping the known-asteroid check, no presenting a preliminary orbit as exact`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
