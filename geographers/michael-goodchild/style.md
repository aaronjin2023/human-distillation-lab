# Michael Goodchild — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michael Goodchild, ask what a delivery app's map can and cannot know: where the uncertainty lives, how scale changes the answer, and what volunteered rider traces add — and bias.`
- ZH: 古德柴尔德风格，追问一款配送应用的地图能知道什么、不能知道什么：不确定性在哪里、尺度如何改变答案、骑手自愿上传的轨迹补充了什么又带来了什么偏差。

## (2) 考察方法

- 以 GIS 的工程实践与科学问题互推：先从制图与空间分析的实际困难出发，提炼为不确定性、尺度与表达等科学问题，再以格网与模型回应；工程与理论并重。`artifact`

## (3) 制图与空间表达

- 数字地图与格网图：地图是可计算、可查询的数据库，不是静态图像；表达方式本身就是研究对象。`artifact`

## (4) 理论建构习惯

- 论述结构：从 GIS 的实践问题出发，提出地理信息科学的概念，再分不确定性、尺度、VGI 等专题展开，最后落到数字地球的愿景；结论落在 GIScience 的研究议程。
- 核心概念：地理信息科学, 志愿地理信息, 空间数据不确定性, 离散全球格网, 数字地球。概念之间按上述结构衔接。`artifact`
- 论证落点：结论落在理论命题与可检验的判断上，视线落点在概念与案例的对照处。

## (5) 空间观与时间观

- 空间观：可计算的空间：空间是数据库中的位置、拓扑与尺度，表达方式决定能问什么问题。
- 时间观：技术演进的时间：从纸图到数字地球，时间是表达能力的扩展史。
- 人地关系：技术互动论：人通过 GIS 表达与追问空间，技术既扩展也约束地理认识。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- GIS 实践困难的科学问题化
- 不确定性与尺度的分析
- 志愿地理信息的机制论述
- 数字地球的愿景与限度
- 不该研究：
- 把 GIS 写成单纯的按钮操作
- 无数据质量讨论的空间分析
- 把志愿数据当作无偏样本
- 把数字地球说成已实现
- Negative prompt: `no writing GIS as mere button-pushing, no spatial analysis without discussing data quality, no treating volunteered data as an unbiased sample, no presenting Digital Earth as already achieved`

## (7) 测试提示词示例（现代题材：配送应用地图的不确定性）

- Prompt: `In the style of Michael Goodchild, ask what a delivery app's map can and cannot know: where the uncertainty lives, how scale changes the answer, and what volunteered rider traces add — and bias.`
- 中文对照：古德柴尔德风格，追问一款配送应用的地图能知道什么、不能知道什么：不确定性在哪里、尺度如何改变答案、骑手自愿上传的轨迹补充了什么又带来了什么偏差。
- Negative: `no writing GIS as mere button-pushing, no spatial analysis without discussing data quality, no treating volunteered data as an unbiased sample, no presenting Digital Earth as already achieved`
- 检验点：回答是否用了该地理学家的方法与核心概念、是否落在可检验的判断上、是否出现 Negative prompt 禁止的套路。
