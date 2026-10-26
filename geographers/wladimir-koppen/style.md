# Wladimir Köppen — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第6.5节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wladimir Köppen, let vegetation draw the map: take temperature and rainfall, find the thresholds where one plant world gives way to another, and classify the whole earth by those lines`
- ZH: 柯本风格：让植被来画地图——取气温与降水，找出一种植物世界让位于另一种的阈值，用这些界线给整个地球分类。

## (2) 考察方法

- 田野方式：以气象站数据汇编与植被分布对照为田野：全球气象记录收集，植被带比对；最依赖长期观测数据的统计汇总。
- 证据偏好：统计数据为主：气温、降水、植被分布；几乎不用野外考察，分类必有数据阈值。
- 尺度偏好：以全球为基本尺度，论证下至地方气候型；尺度转换靠“阈值”——同一阈值适用于全球。

## (3) 制图与空间表达

- 气候区划图为主：字母代码分区、等值线、植被带；符号是字母代码系统；地图就是分类本身。

## (4) 理论建构习惯

- 论述结构：数据汇编 → 阈值确定 → 分区编码 → 全球区划图。核心概念：气候型、阈值、植被带、字母代码、干湿季。概念衔接：气温降水定阈值，阈值定植被界线，界线定气候型。论证落点：分类体系——柯本气候分类。

## (5) 空间观与时间观

- 空间观：区划空间——空间是气候型的分布。时间观：统计时间——以多年平均值计，略去单年波动。人地关系：气候设限，植被是气候的指示器，人是分类的使用者。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 气温与降水阈值的确定
- 植被带与气候型的对照
- 全球气候区划图的绘制
- 字母代码分类体系
- 不该研究：no climate type without a numeric threshold, no boundary drawn without vegetation evidence, no classification from a single year's data, no confusing weather with climate
- Negative prompt: `no climate type without a numeric threshold, no boundary drawn without vegetation evidence, no classification from a single year's data, no confusing weather with climate`

## (7) 测试提示词示例（现代题材：一座新城的气候属于柯本分类的哪一型，依据是什么？）

- Prompt: `In the style of Wladimir Köppen, classify a new city's climate: take its temperature and rainfall, find the thresholds, and assign its letter code`
- 中文对照：柯本风格，给一座新城的气候分类：取气温与降水、找出阈值，定出它的字母代码。
- Negative: `no climate type without a numeric threshold, no boundary drawn without vegetation evidence, no classification from a single year's data, no confusing weather with climate`
- 检验点：回答是否按该地理学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
