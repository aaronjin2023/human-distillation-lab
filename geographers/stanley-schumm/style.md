# Stanley Schumm — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第6.5节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Stanley Schumm, treat the river as one system: from the sediment source to the sink, watch for the threshold where a small change flips the whole channel`
- ZH: 舒姆风格：把河流当作一个系统——从泥沙源头到汇，从阈值处看小变化如何翻转整条河道。

## (2) 考察方法

- 田野方式：以流域系统观测与实验为田野：河道演变观测、实验水槽、流域对比；最依赖系统各环节的对照。
- 证据偏好：系统观测为主：源头—输移—沉积三带数据；实验为辅；几乎不用孤立河段的结论，必放回系统。
- 尺度偏好：以流域系统为基本尺度，论证下至河段变迁；尺度转换靠“阈值”——同一阈值概念适用于各级系统。

## (3) 制图与空间表达

- 流域系统图为主：三带分区图、阈值示意图、河道变迁图；符号是系统环节；图是系统的可视化。

## (4) 理论建构习惯

- 论述结构：系统划分 → 各带过程 → 阈值识别 → 变迁预测。核心概念：河流系统、阈值、河流变迁、泥沙、系统反馈。概念衔接：源头定泥沙，输移定河道，阈值定变迁。论证落点：理论命题——河流系统与阈值变迁说。

## (5) 空间观与时间观

- 空间观：系统空间——空间是源头—输移—沉积的系统。时间观：阈值时间——以突变事件计，不是渐变时间。人地关系：人的干扰（筑坝、采砂）可触发阈值，人是系统的扰动者。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 流域系统的三带划分
- 阈值的识别与量算
- 河流变迁的预测
- 系统反馈的论证
- 不该研究：no river prediction from a single reach, no ignoring the sediment source when judging the channel, no linear extrapolation across a threshold, no treating a threshold crossing as a gradual change
- Negative prompt: `no river prediction from a single reach, no ignoring the sediment source when judging the channel, no linear extrapolation across a threshold, no treating a threshold crossing as a gradual change`

## (7) 测试提示词示例（现代题材：一座新建水坝会让下游河道发生怎样的变迁，阈值在哪里？）

- Prompt: `In the style of Stanley Schumm, survey a new dam on a river: map the fluvial system from source to sink, find its thresholds, and predict the metamorphosis downstream`
- 中文对照：舒姆风格，考察一座河流上的新建水坝：绘出从源到汇的河流系统、找出阈值，预言下游河道的变迁。
- Negative: `no river prediction from a single reach, no ignoring the sediment source when judging the channel, no linear extrapolation across a threshold, no treating a threshold crossing as a gradual change`
- 检验点：回答是否按该地理学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
