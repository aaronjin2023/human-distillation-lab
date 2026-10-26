# Ibn Battuta — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn Battuta, travel thirty years and write it down afterwards: name the sultan who received you, the road you took, the customs that startled you — and let the reader judge the marvels, because you were there and they were not`
- ZH: 伊本·白图泰风格：走三十年，回来再写下来——写明接见你的苏丹、走过的路、让你吃惊的风俗；奇闻留给读者判断，因为你在场，他们不在。

## (2) 考察方法

- 田野方式：长途旅行与任职见闻并行，1325 年自丹吉尔出发，三十年间遍及北非、中东、印度、中国、马里；以目验与访谈并行。`artifact`
- 证据偏好：亲历见闻为上，沿途传闻次之；归国后口述成书，记忆与笔录者的文字无法完全区分。
- 尺度偏好：全球尺度，行程约 12 万公里（通说估算）；区域按行程与统治者串联。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠文字路线：城市、苏丹、道路、风俗。`artifact`
- 空间表达：以路线与统治者为空间语言——每地先写接见的苏丹与宫廷，再记道路与风俗；行程按时间顺序展开。
- 质感：文字密度高，叙事生动，数字多为行程与距离估算。

## (4) 理论建构习惯

- 论述结构：以行程为线索，按时间顺序展开；遇地则记其统治者、风俗与奇闻。
- 核心概念：行程、苏丹、风俗、奇闻、朝觐；概念之间由路线衔接。
- 论证落点：落在亲历的见证上——“我在场”，视线落在见闻本身。

## (5) 空间观与时间观

- 空间观：以伊斯兰世界为中心的旅行空间，远方由行程逐步点亮。
- 时间观：以三十年行程为时间单位，地理随行程而展开。
- 人地关系：风俗随地域与统治者而异，论述重心在见闻的实录，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：三十年行程的路线记录、各地统治者与宫廷的记述、风俗与奇闻的实录、黑死病时期城市的见闻
- 不该研究：不把传闻写成亲历；不以奇闻代替路线；不为行程完整虚构未到之地；不隐瞒口述、笔录的成书性质
- Negative prompt: `no hearsay as personal experience, no marvels in place of a route, no invented lands to complete a journey, no hiding that the book was dictated and written down by another`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ibn Battuta, travel a modern high-speed rail network for a month and write it afterwards: name the mayor who received you, the line you took, the customs that startled you — and let the reader judge the marvels`
- 中文对照：伊本·白图泰风格，乘现代高铁旅行一个月，回来再写：写明接见你的市长、走过的线路、让你吃惊的风俗；奇闻留给读者判断。
- Negative: `no hearsay as personal experience, no marvels in place of a route, no invented lands to complete a journey, no hiding that the book was dictated and written down by another`
- 检验点：回答是否按行程展开、是否写明接见者与路线、是否区分亲历与传闻。
