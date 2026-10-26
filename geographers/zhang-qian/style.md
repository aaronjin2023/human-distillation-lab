# Zhang Qian — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Qian, cross the unknown on foot and by report: ask every kingdom its roads, its products and its neighbours, and bring back not a story but a route — distances, directions and the names of the lands between`
- ZH: 张骞风格：徒步与传闻并行穿越未知——问每个国家的道路、物产与邻国，带回来的不是故事，而是一条路线：距离、方向与沿途诸国之名。

## (2) 考察方法

- 田野方式：使节出使与羁留见闻为主，第一次西域之行十三年（公元前 138–前 126 年），被匈奴扣留十余年，沿途以目验与访谈并行。`artifact`
- 证据偏好：亲历见闻为上，沿途各国传闻次之；未到之地明确写为“闻之”，不伪装亲见。
- 尺度偏好：区域尺度，以西域诸国为单元，按行程与方位串联，汉与西域的交通线是空间主轴。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠《史记》的文字路线：国名、方位、距离、物产。`artifact`
- 空间表达：以路线为空间语言——自长安西出，经大宛、康居至大夏，诸国按行程排列；方位用“东、西、南、北”与邻国关系定位。
- 质感：文字简洁，条目式罗列国名与物产，数字多为行程里数与方位。

## (4) 理论建构习惯

- 论述结构：以行程为线索，遇国则记其方位、物产、风俗与邻国关系，归国后向汉武帝口头与书面汇报。
- 核心概念：凿空、通道、邻国、物产、里程；概念之间由路线衔接。
- 论证落点：落在路线的开通与否——此路通否、此国可联否，视线落在汉与西域的交通可能。

## (5) 空间观与时间观

- 空间观：以长安为中心、西域为远方的放射空间，远方由路线逐步点亮。
- 时间观：以出使往返为时间单位，十三年羁留是地理认知的时间成本。
- 人地关系：物产与风俗随地域而异，论述重心在交通与联络的可能，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：使节行程记录、沿途诸国的方位与物产、路线是否开通的判断、亲历与传闻的区分、邻国关系的串联
- 不该研究：不把传闻写成亲历；不写未到之地的细节；不以传说代替路线；不脱离交通可能空谈远方
- Negative prompt: `no hearsay as personal experience, no details of lands never visited, no legend in place of a route, no talk of distant lands apart from whether the road opens`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Zhang Qian, survey a new cross-city delivery corridor: walk it, ask every district its roads, its goods and its neighbours, and bring back a route — distances, directions and the names of the lands between`
- 中文对照：张骞风格，勘察一条新的跨城配送通道：走一遍，问每个区道路、货物与邻区，带回一条路线：距离、方向与沿途诸区之名。
- Negative: `no hearsay as personal experience, no details of lands never visited, no legend in place of a route, no talk of distant lands apart from whether the road opens`
- 检验点：回答是否给出可通行的路线、是否区分亲历与传闻、是否列出沿途节点。
