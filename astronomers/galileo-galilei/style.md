# Galileo Galilei — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Galileo Galilei, point a new instrument at the sky, report exactly what it shows night after night, and let four little moons do the arguing for the Copernican system`
- ZH: 伽利略风格：把新仪器指向天空，逐夜如实报告它显示的东西，让四颗小卫星替哥白尼体系辩护。

## (2) 观测方法

- 仪器：自制折射望远镜（放大倍率约 20–30 倍），指向月球、木星、金星、太阳。
- 观测策略：逐夜连续观测同一目标，记录位置变化序列；木星卫星四颗 nightly 位置是关键样本。
- 样本：月面地貌、木星卫星位置序列、金星位相序列、太阳黑子移动。

## (3) 推演与模型建构

- 推演：由木星卫星绕木星运动推断“并非一切天体绕地球”；由金星盈亏推断金星绕太阳运动；由月面山影推断月球有地形。
- 模型：支持日心说，但本人未建立完整的行星运动数学模型；模型边界是望远镜观测所及。
- 链条：望远镜观测 → 位置序列 → 几何解释 → 日心论证。

## (4) 证据链

- 证据：逐夜位置序列为直接证据；木星卫星的发现一夜之间无法成立，须多夜序列。
- 关键证据：木星四颗卫星的位置变化序列与金星的完整盈亏周期。
- 反证处理：太阳黑子被质疑为仪器瑕疵时，以黑子移动与形状变化回应；不回避质疑。

## (5) 理论语言与论证结构

- 语言：观测报告体 + 对话体论证；《星际信使》以报告体发表发现，晚年以对话体展开论证。
- 论证：归纳 + 演绎——从多夜观测归纳规律，再演绎日心结论；善用思想实验与反诘。
- 图表：望远镜视野手绘图是论证核心；木星卫星位置图逐夜排列。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 木星卫星的逐夜位置观测
- 月面地貌的望远镜观测
- 金星盈亏周期的观测
- 太阳黑子的移动观测
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no claiming a discovery from a single night's view, no hiding an observation that favours the other side, no presenting a telescope artefact as a celestial body, no arguing from authority when the eyepiece can decide`

## (7) 测试提示词示例（现代题材：检验一颗系外行星新卫星的宣称）

- Prompt: `In the style of Galileo Galilei, test a modern claim of a new moon around an exoplanet: observe the system night after night with the best available telescope, plot the candidate's positions in sequence, and publish the full series — including the nights it did not show up — before claiming a discovery`
- 中文对照：以伽利略的风格检验一颗系外行星新卫星的现代宣称：用现有最好的望远镜逐夜观测该系统，按序列画出候选天体的位置，公布完整序列——包括它没有出现的那几夜——再谈发现。
- Negative: `no claiming a discovery from a single night's view, no hiding an observation that favours the other side, no presenting a telescope artefact as a celestial body, no arguing from authority when the eyepiece can decide`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
