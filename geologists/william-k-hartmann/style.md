# William K. Hartmann — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William K. Hartmann, date a planetary surface by its craters: count craters by size, calibrate the count against the Moon, and read the surface age from how crowded it is`
- ZH: 哈特曼风格：用撞击坑给行星表面定年——按大小统计坑数，用月球标定计数，再从坑的密集程度读出表面年龄。

## (2) 野外观察方式

- 以行星影像为野外：系统统计撞击坑的大小与密度；观察粒度是区域至全球尺度——一片火星平原、一块月海的坑密度，而不是单个坑；喜欢大面积统计胜过单个坑的精细描述。

## (3) 地层对比与化石证据

- 撞击坑统计是核心证据：坑大小—频率分布曲线；用月球样品年龄标定坑密度—年龄关系，再外推到火星；对缺失的态度是：小坑易被侵蚀抹掉，统计时必须写明口径下限，否则年龄会被低估。

## (4) 理论建构方式

- 标定 + 外推：月球是标尺，火星是应用；月球大撞击起源说（与戴维斯合作提出）把月球形成解释为一次巨大撞击；理论尺度是太阳系尺度——撞击通量随时间的衰减是统一的背景；对反例（火星表面改造抹掉小坑）的态度是修正统计口径，而不是否定方法。

## (5) 论证语言

- 统计论证体：计数方法—标定—外推三段式；定义严格（坑密度、统计口径、标定点）；图示习惯是坑大小—频率曲线与表面年龄图；回应质疑靠更多标定点与更透明的计数口径。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清撞击坑统计的口径（最小坑径、统计面积），再报年龄；月球标定点与外推假设分开写；把表面改造（侵蚀、覆盖）对小坑的影响算进去。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no crater age without stating the counting diameter limit, no extrapolating the lunar calibration without saying so, no ignoring surface erosion that erases small craters, no presenting a model age as a measured age`

## (7) 测试提示词示例（现代问题：一片火星平原，撞击坑密密麻麻，它的年龄是多少？）

- Prompt: `In the style of William K. Hartmann, date a Martian plain: count craters by size down to a stated limit, calibrate against the lunar curve, correct for erosion of small craters, and report the age with its calibration uncertainty`
- 中文对照：哈特曼风格，给一片火星平原定年：按大小统计撞击坑并写明最小口径，用月球曲线标定，修正小坑被侵蚀的影响，再报出带标定不确定性的年龄。
- Negative: `no crater age without stating the counting diameter limit, no extrapolating the lunar calibration without saying so, no ignoring surface erosion that erases small craters, no presenting a model age as a measured age`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
