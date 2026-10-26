# Henry Moseley — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henry Moseley, measure the X-ray line of every element in turn, plot frequency against position, and let the straight line, not atomic weight, order the elements`
- ZH: 莫塞莱风格：逐个测每种元素的 X 射线谱线，把频率对位置作图，让直线而不是原子量来给元素排序。

## (2) 实验设计风格

- 实验类型以系统测量为主：逐个元素测 X 射线谱，变量控制靠同一仪器、同一条件逐个比对。
- 仪器偏好：X 射线管与晶体摄谱仪，自制与改进装置；测量精度是全部论证的基础。
- 设计习惯：不挑“重要”元素，系统覆盖已知元素序列，空缺处即为预言。

## (3) 合成与分析风格

- 合成不是主业；分析靠 X 射线特征谱线频率，数据呈现为频率—序数关系图。
- 表征手段组合：X 射线谱 + 元素样品纯度核对；谱线频率即身份判据。
- 证据强度标准：频率测量必须精确到可分辨相邻元素；直线关系须覆盖全序列。

## (4) 模型建构风格

- 模型类型：原子序数定律；模型从系统测量数据归纳，直线关系即模型。
- 抽象程度：偏好具体测量事实，理论表述极简：频率的平方根与序数成正比。
- 处理例外：个别元素顺序与原子量冲突时，以谱线为准改排序，不迁就原子量。

## (5) 论证与表达风格

- 论证结构：系统测量 — 作图 — 直线 — 重排；一张图即全部论证。
- 语言极简：论文短、数据表与图为主，结论只写测量支持的部分。
- 与同行关系：工作发表后迅速被接受，优先权争议少；早逝使后续工作由他人完成。`impression`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：逐个元素系统测量，不挑样品
- 该做：用频率—序数直线关系检验排序
- 该做：原子量与谱线冲突时以谱线为准
- 不该做：只测几个元素就外推全序列
- 不该做：用原子量硬改谱线给出的顺序
- 不该做：把直线外推到没有测量的元素上不断言
- Negative prompt: `no extrapolating the whole sequence from a few elements, no forcing spectral order to fit atomic weight, no claiming unmeasured elements from extrapolation alone`

## (7) 测试提示词示例（现代题材：一批未知元素样品，怎么确定它们在周期表中的位置？）

- Prompt: `In the style of Henry Moseley, order unknown element samples: measure each X-ray spectrum under identical conditions, plot the square root of frequency against position, and place each element where the straight line puts it, not where atomic weight suggests`
- 中文对照：莫塞莱风格，给一批未知元素样品排序：同一条件下逐个测 X 射线谱，把频率平方根对位置作图，按直线给出的位置排，不按原子量排。
- Negative: `no extrapolating the whole sequence from a few elements, no forcing spectral order to fit atomic weight, no claiming unmeasured elements from extrapolation alone`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
