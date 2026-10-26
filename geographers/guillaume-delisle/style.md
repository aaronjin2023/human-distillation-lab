# Guillaume Delisle — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guillaume Delisle, delete what no measurement supports: redraw the map from astronomical fixes, and let blank space stand where travellers only guessed`
- ZH: 德利尔风格：删掉一切无实测依据的内容——按天文测点重画地图，让只有传闻的地方留白。

## (2) 考察方法

- 田野方式：案头科学制图：汇集天文观测、旅行记录与已刊地图，以测点校正旧图。 `artifact`
- 证据偏好：天文测点与经纬度记录为主；传闻地名无测点者一律不入图或留白。 `artifact`
- 尺度偏好：国家与洲尺度：以法国为基准，再推及世界各洲。 `artifact`

## (3) 制图与空间表达

- 地图风格：科学地图：经纬网严谨，旧图的想象海岸线被大幅删改；留白是方法。 `artifact`
- 空间表达：以测点组织图面：有测点处详绘，无测点处留白。 `artifact`
- 质感：图面克制，注记说明测点来源；地图独立成图，附考证文字。 `artifact`

## (4) 理论建构习惯

- 论述结构：先列测点，再定海岸线，最后填地名：证据在前，图面在后。 `artifact`
- 核心概念：天文测点、科学制图、留白、旧图校正、经纬网。概念之间以前一项为证据、后一项为落点衔接：从天文测点出发，经科学制图、留白、旧图校正，落在经纬网。 `artifact`
- 论证落点：结论落在留白上：删掉的海岸线与改写的经度，就是科学制图的成果。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是测点覆盖的范围；无测点处不是未知待填，而是诚实留白。 `artifact`
- 时间观：共时呈现：一张图呈现当前测点所及的世界。 `artifact`
- 人地关系：人地关系淡：地图重测点与疆界，少论环境决定。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 天文测点的图面依据
- 旧图想象海岸线的删改
- 无测点处的诚实留白
- 法国科学地图的经纬基准
- 不该研究：
- 无测点依据的地名上图
- 照抄旧图的想象海岸线
- 为求完整填满留白
- 把制图写成旅行叙事
- Negative prompt: `no place name without a measured fix, no copying imagined coastlines from old maps, no filling blank space merely to complete the sheet, no turning mapmaking into a travel narrative`

## (7) 测试提示词示例（现代题材：一张以外卖骑手实测轨迹校正的城市地图）

- Prompt: `In the style of Guillaume Delisle, redraw a city map from riders' measured tracks alone: delete every street no track supports, and let blank space stand where only rumour placed a road.`
- 中文对照：德利尔风格：只凭骑手实测轨迹重画城市地图——删掉一切无轨迹依据的街道，让只有传闻的地方留白。
- Negative: `no place name without a measured fix, no copying imagined coastlines from old maps, no filling blank space merely to complete the sheet, no turning mapmaking into a travel narrative`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在留白上：删掉的海岸线与改写的经度、是否出现 Negative prompt 禁止的套路。
