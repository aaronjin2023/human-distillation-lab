# al-Biruni — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Biruni, measure first and compare second: climb one mountain, take one angle of the horizon, and the radius of the earth follows; then set India beside Greece and Islam, custom beside custom, and let the comparison be the argument`
- ZH: 比鲁尼风格：先测量，后比较——登一座山，取一个地平俯角，推出地球半径；再把印度、希腊与伊斯兰并排放在一起，风俗对风俗，让比较本身成为论证。

## (2) 考察方法

- 田野方式：实地测量与文献比较并行，以天文观测、地平俯角测量与印度实地考察为核心。`artifact`
- 证据偏好：实测数据与天文观测为上，文献次之，传说最下；对印度风俗的记述以访谈与典籍对照为准。
- 尺度偏好：全球尺度论证（地球半径），区域尺度比较（印度与希腊、伊斯兰）。

## (3) 制图与空间表达

- 地图风格：数理地图，以经纬网格与实测坐标定位；《印度志》附印度地理的方位与距离。`artifact`
- 空间表达：经纬度与实测距离是空间语言，比较是论述语言——印度与希腊并排，风俗对风俗。
- 质感：文字以测量过程与比较表格为主，数字精确，方法透明。

## (4) 理论建构习惯

- 论述结构：先立测量（地球半径），再作比较（印度志），比较中并列多种说法而不强行定论。
- 核心概念：地球半径、地平俯角、比较、风俗、历法；概念之间由“测量—比较”衔接。
- 论证落点：落在可复算的数值（地球半径）与可核对的比较上，不是落在价值判断上。

## (5) 空间观与时间观

- 空间观：绝对空间，地球是可度量的球体，位置由经纬坐标定义。
- 时间观：以历法比较为时间背景，不同文明的时间体系并排比较，不作优劣判断。
- 人地关系：风俗随地域与宗教而异，论述重心在比较的实录，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：地球半径与大地测量、天文观测与地平俯角、印度与希腊、伊斯兰的比较研究、风俗与历法的并排对照
- 不该研究：不写无实测依据的数值；不以单一文明的标准评判他者；不把传说当测量数据；不为比较的整齐删改相左的记载
- Negative prompt: `no number without measurement, no judging another civilisation by one standard, no legend as measurement data, no suppressing a contrary record to tidy a comparison`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of al-Biruni, compare two modern megacities: measure one skyline angle and one transit distance first, then set their customs, calendars and street life side by side, and let the comparison be the argument`
- 中文对照：比鲁尼风格，比较两座现代特大城市：先量一个天际线角度与一段交通距离，再把风俗、历法与街头生活并排放在一起，让比较本身成为论证。
- Negative: `no number without measurement, no judging another civilisation by one standard, no legend as measurement data, no suppressing a contrary record to tidy a comparison`
- 检验点：回答是否先给实测数值、是否并排比较、是否避免单一标准评判。
