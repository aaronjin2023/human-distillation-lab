# Derwent Whittlesey — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第6.5节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Derwent Whittlesey, classify the world's farming by what the farmer actually does: crop, animal, tool and market together, and let the map of agriculture emerge from the work itself`
- ZH: 惠特尔西风格：按农民实际做什么给世界农业分类——作物、牲畜、工具与市场合在一起，让农业地图从劳作本身长出来。

## (2) 考察方法

- 田野方式：以农业统计与区域调查为田野：全球农业统计汇编，区域农业调查；最依赖可比的统计指标。
- 证据偏好：统计数据为主：作物、牲畜、劳动力、市场；野外观察为辅；几乎不用无数据的定性划分。
- 尺度偏好：以全球为基本尺度，论证下至区域农业型；尺度转换靠“类型”——同一类型标准适用于全球。

## (3) 制图与空间表达

- 农业区划图为主：11个农业区域的世界地图；符号是类型代码；地图就是分类本身。

## (4) 理论建构习惯

- 论述结构：指标选取 → 类型划分 → 全球区划 → 区域解释。核心概念：农业区域、农业类型、集约、商品化、游牧。概念衔接：作物牲畜定类型，类型定区域，区域定解释。论证落点：分类体系——世界农业区域。

## (5) 空间观与时间观

- 空间观：区划空间——空间是农业类型的分布。时间观：统计时间——以调查年份的截面计。人地关系：农业是人与环境的结合方式，类型是结合方式的分类。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 世界农业类型的划分
- 农业区域图的绘制
- 作物与牲畜组合的分析
- 区域农业的解释
- 不该研究：no agricultural region without statistical indicators, no type defined by climate alone, no confusing a crop map with a farming-system map, no classification from a single year
- Negative prompt: `no agricultural region without statistical indicators, no type defined by climate alone, no confusing a crop map with a farming-system map, no classification from a single year`

## (7) 测试提示词示例（现代题材：一座新建农业县属于世界农业的哪一类型，依据是什么？）

- Prompt: `In the style of Derwent Whittlesey, classify a new farming county: record its crops, animals, tools and markets, assign its type, and place it on the world map of agriculture`
- 中文对照：惠特尔西风格，给一座新建农业县分类：记下作物、牲畜、工具与市场，定出类型，放到世界农业地图上。
- Negative: `no agricultural region without statistical indicators, no type defined by climate alone, no confusing a crop map with a farming-system map, no classification from a single year`
- 检验点：回答是否按该地理学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
