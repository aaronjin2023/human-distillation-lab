# Johann Heinrich von Thünen — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第6.5节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Johann Heinrich von Thünen, start from one lonely market town on a featureless plain: add transport cost ring by ring, and let the rings of farming arrange themselves by rent`
- ZH: 屠能风格：从无特征平原上一座孤立的集镇出发——一圈一圈加上运费，让农业的环带按地租自己排出来。

## (2) 考察方法

- 田野方式：以农场经营账簿与模型推演为田野：自家农场（特洛）的十年经营记录，运费与地租计算；最依赖可计算的经营数据。
- 证据偏好：经营数据为主：产量、运费、地租；几乎不用未经计算的定性论断，规律必有数字。
- 尺度偏好：以孤立国模型为基本尺度，论证上收至一般区位规律；尺度转换靠“环带”——同一地租机制适用于各级尺度。

## (3) 制图与空间表达

- 环带模式图为主：同心圆环带图、地租曲线图；符号是环带代码；图是模型本身。

## (4) 理论建构习惯

- 论述结构：孤立国假设 → 运费与地租计算 → 环带推导 → 现实修正。核心概念：孤立国、地租、运费、环带、区位。概念衔接：运费定地租，地租定环带，环带定区位。论证落点：理论命题——农业区位论。

## (5) 空间观与时间观

- 空间观：模型空间——空间是地租决定的环带。时间观：静态时间——模型是截面，不是历史。人地关系：经济人假设下，土地利用由地租决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 孤立国模型的构建
- 运费与地租的计算
- 农业环带的推导
- 模型与现实的对照修正
- 不该研究：no location claim without a rent calculation, no ring without a transport cost behind it, no confusing the model plain with the real landscape, no applying the rings without stating the assumptions
- Negative prompt: `no location claim without a rent calculation, no ring without a transport cost behind it, no confusing the model plain with the real landscape, no applying the rings without stating the assumptions`

## (7) 测试提示词示例（现代题材：一座新城的食品供应带应如何按地租与运费环带布局？）

- Prompt: `In the style of Johann Heinrich von Thünen, plan a new city's food belt: start from one market town, add transport cost ring by ring, and let the farming rings arrange themselves by rent`
- 中文对照：屠能风格，规划一座新城的食品带：从一座集镇出发、一圈一圈加上运费，让农业环带按地租自己排出来。
- Negative: `no location claim without a rent calculation, no ring without a transport cost behind it, no confusing the model plain with the real landscape, no applying the rings without stating the assumptions`
- 检验点：回答是否按该地理学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
