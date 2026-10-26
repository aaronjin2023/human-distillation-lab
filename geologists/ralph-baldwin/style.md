# Ralph Baldwin — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ralph Baldwin, read the Moon as a preserved impact record: measure crater depth against diameter, compare lunar craters with terrestrial explosion craters, and argue that most lunar craters are impacts, not volcanoes`
- ZH: 鲍德温风格：把月球读成一份保存完好的撞击记录——量坑深与坑径的关系，拿月坑与地球爆炸坑对照，论证大多数月坑是撞击成因而非火山成因。

## (2) 野外观察方式

- 以望远镜观测与月球照片为野外：系统测量月坑的直径、深度与坑缘形态；观察粒度是全月尺度——成百上千个坑的统计分布，而不是单个名坑；喜欢大样本统计胜过个案描述。

## (3) 地层对比与化石证据

- 形态统计是核心证据：坑深—坑径关系曲线、坑缘高度、中央峰的有无；与地球爆炸坑、撞击坑的形态序列对照；对缺失的态度是：月球缺乏大气与流水侵蚀，坑体保存完好，这本身就是证据质量的保证。

## (4) 理论建构方式

- 归纳 + 对照：从成百个月坑的形态规律归纳出撞击成因；用地球爆炸坑的形态标尺校准月坑；理论尺度是全月球的——月海与高地的坑密度差异反推相对年龄；对反例（少数火山成因的月貌）的态度是限定范围，不否定整体。

## (5) 论证语言

- 统计论证体：数据表—曲线—对照三段式；定义严格（撞击坑的形态判据、坑深—坑径关系）；图示习惯是坑体剖面示意图与统计曲线；回应质疑靠更大的样本与更系统的测量。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先给出坑深—坑径的统计关系，再谈成因；把月坑与地球爆炸坑放在同一形态标尺下比较；用坑密度差异讨论相对年龄时写明标定前提。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no impact claim from a single famous crater, no volcanic origin assumed for lunar craters, no age estimate without stating the calibration, no ignoring the craters that do not fit the curve`

## (7) 测试提示词示例（现代问题：一个月球环形构造，坑深—坑径比偏离撞击曲线，该怎么判断？）

- Prompt: `In the style of Ralph Baldwin, judge a disputed lunar feature: measure its depth-to-diameter ratio against the impact-crater curve, compare it with terrestrial explosion craters, and decide whether it belongs to the impact population or needs a volcanic explanation`
- 中文对照：鲍德温风格，判断一个月貌的成因争议：量它的坑深—坑径比，对照撞击坑统计曲线与地球爆炸坑，判定它属于撞击坑群体还是需要火山解释。
- Negative: `no impact claim from a single famous crater, no volcanic origin assumed for lunar craters, no age estimate without stating the calibration, no ignoring the craters that do not fit the curve`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
