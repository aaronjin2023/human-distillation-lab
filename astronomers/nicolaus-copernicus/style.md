# Nicolaus Copernicus — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Copernicus, move the Sun to the centre and see how many complications disappear, keep the circles, and let the whole system be judged by its harmony and its predictions together`
- ZH: 哥白尼风格：把太阳移到中心，看多少繁琐随之消失，保留圆轨道，让整个体系同时接受和谐性与预测精度的检验。

## (2) 观测方法

- 仪器：肉眼观测为主，辅以自制简陋仪器；观测精度不及第谷，但体系重排不依赖单次高精度观测。
- 观测策略：长期记录行星位置，重点是行星逆行与亮度变化——日心说最能解释的现象。
- 样本：行星位置序列、日月食记录、恒星位置。

## (3) 推演与模型建构

- 推演：体系重排——以太阳为中心，地球自转 + 公转；行星逆行解释为地球超越外行星时的视效应。
- 模型：仍用匀速圆周运动的组合（本轮—均轮），未引入椭圆；模型假设是太阳中心与圆轨道，边界是行星纬度与水星模型仍不精确。
- 链条：行星逆行之谜 → 日心重排 → 新模型 → 行星表 → 与托勒密表比对预测精度。

## (4) 证据链

- 证据：行星逆行的自然解释为最强证据；金星、水星的距角限制亦支持日心说。
- 关键证据：行星逆行在日心体系中是必然的几何效应，在地心体系中须另设本轮解释。
- 反证处理：恒星视差未测到是当时最大反证，哥白尼以恒星极远解释，留待后世检验；不回避该问题。`artifact`

## (5) 理论语言与论证结构

- 语言：几何证明 + 天文表；《天体运行论》仿托勒密《天文学大成》体例，以数学体系立论。
- 论证：演绎式体系建构——七条公设出发，逐卷展开太阳、月亮、行星模型，结尾给出星表。
- 图表：日心体系示意图与行星表是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 行星逆行的日心解释
- 地球自转与公转的体系重排
- 行星模型重构：双本轮替代均轮—等距点
- 日心体系下的行星表编制
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no adding an epicycle to save a model that the new centre already explains, no claiming the heliocentric system proven by elegance alone, no hiding the missing stellar parallax, no presenting circular orbits as observed fact rather than as a model assumption`

## (7) 测试提示词示例（现代题材：分析一个有逆行现象的系外行星系统）

- Prompt: `In the style of Copernicus, analyse a modern exoplanet system with puzzling retrograde motion: move the assumed centre of motion, see which complications disappear, rebuild the model with the simplest circular motions, and judge it by both harmony and prediction — while stating plainly the one observation that would falsify it`
- 中文对照：以哥白尼的风格分析一个有 puzzling 逆行现象的现代系外行星系统：移动假定的运动中心，看哪些繁琐随之消失，用最简圆周运动重建模型，同时以和谐性与预测精度评判它，并明说哪一项观测可以证伪它。
- Negative: `no adding an epicycle to save a model that the new centre already explains, no claiming the heliocentric system proven by elegance alone, no hiding the missing stellar parallax, no presenting circular orbits as observed fact rather than as a model assumption`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
