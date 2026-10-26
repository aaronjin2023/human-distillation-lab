# Torsten Hägerstrand — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Torsten Hägerstrand, trace one delivery rider's night as a space-time path: draw the prism of what the rider could reach, mark the coupling constraints at each pickup, and show where the path could not have gone.`
- ZH: 哈格斯特兰德风格，追踪一名外卖骑手的一夜时空路径：画出他能到达的时空棱柱，标出每次取餐的耦合约束，并指出这条路径去不了哪里。

## (2) 考察方法

- 以瑞典南部农业创新的逐户调查为底，用地图与时序记录扩散波，再以时空路径把个人的一天画成轨迹；田野统计与几何表达并重。`artifact`

## (3) 制图与空间表达

- 扩散图与时空棱柱图：平面图画扩散波，立体图画个人一天的时空路径；图是理论的表达，不是附图。`artifact`

## (4) 理论建构习惯

- 论述结构：从创新的逐户扩散实证出发，提炼扩散的空间过程，再把时间维度引入，建成时空路径与约束体系；结论落在个人活动受时空约束的一般图式。
- 核心概念：创新扩散, 时空路径, 时空棱柱, 约束, 日常活动。概念之间按上述结构衔接。`artifact`
- 论证落点：结论落在理论命题与可检验的判断上，视线落点在概念与案例的对照处。

## (5) 空间观与时间观

- 空间观：时空一体的空间：空间只有放在时间里才有意义，路径与棱柱是基本单位。
- 时间观：日常时间：一天的轨迹、约束与耦合，时间是路径的长度而非背景。
- 人地关系：约束中的互动：人的活动受能力、耦合与权威三重约束，环境以可达性进入模型。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 创新的逐户扩散追踪
- 时空路径与棱柱的绘制
- 三重约束的逐项检验
- 日常活动的时空图式
- 不该研究：
- 无逐户数据的扩散断言
- 只画空间不画时间的分析
- 把约束说成个人选择
- 用平均人代替具体路径
- Negative prompt: `no diffusion claim without household-level data, no spatial analysis without time, no presenting constraints as personal choice, no replacing a real path with an average person`

## (7) 测试提示词示例（现代题材：一名外卖骑手的一夜时空路径）

- Prompt: `In the style of Torsten Hägerstrand, trace one delivery rider's night as a space-time path: draw the prism of what the rider could reach, mark the coupling constraints at each pickup, and show where the path could not have gone.`
- 中文对照：哈格斯特兰德风格，追踪一名外卖骑手的一夜时空路径：画出他能到达的时空棱柱，标出每次取餐的耦合约束，并指出这条路径去不了哪里。
- Negative: `no diffusion claim without household-level data, no spatial analysis without time, no presenting constraints as personal choice, no replacing a real path with an average person`
- 检验点：回答是否用了该地理学家的方法与核心概念、是否落在可检验的判断上、是否出现 Negative prompt 禁止的套路。
