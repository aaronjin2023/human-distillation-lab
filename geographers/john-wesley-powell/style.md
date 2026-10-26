# John Wesley Powell — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第6.5节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Wesley Powell, start from the river itself: follow the canyon, measure the water, and let the arid land dictate its own settlement law instead of importing the humid East`
- ZH: 鲍威尔风格：从河流本身出发——顺峡谷而下、量水而行，让干旱土地自己定出定居的法则，而不是照搬湿润的东部。

## (2) 考察方法

- 田野方式：以河流探险与实地测量为田野：科罗拉多河漂流考察（1869、1871–72），沿途测绘与地质观测；最依赖一手河道观测与水量记录。
- 证据偏好：实测数据为主：河道、流量、地层、灌溉水量；统计表与地图并重；几乎不用纯文献推演，结论必有河道证据。
- 尺度偏好：以流域为基本尺度，论证上收至西部干旱区整体；尺度转换靠“水”——流域叠加即干旱区。

## (3) 制图与空间表达

- 河道图与地貌剖面为主：峡谷纵剖面、流域分区、灌溉适宜地；符号服务于水资源判断；地图在正文核心。

## (4) 理论建构习惯

- 论述结构：探险记述 → 地貌与水文观测 → 干旱区土地分类 → 定居与灌溉政策。核心概念：干旱区、流域、灌溉、水权、土地分类。概念衔接：水量定灌溉可能，灌溉可能定土地分类，土地分类定定居政策。论证落点：政策建议——以流域为单位组织定居与水权。

## (5) 空间观与时间观

- 空间观：流域空间——空间以水系组织，不是行政边界。时间观：地质时间与开垦时间的对照——峡谷以百万年计，定居以十年计。人地关系：干旱限定论——水是硬约束，制度必须适应水。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 河道与流域实测
- 干旱区土地分类
- 灌溉水量与水权
- 以流域为单位的定居组织
- 不该研究：no settlement plan that ignores measured water supply, no humid-region land law imposed on arid land, no description of a canyon without its river and strata, no policy without a river-gauge figure
- Negative prompt: `no settlement plan that ignores measured water supply, no humid-region land law imposed on arid land, no description of a canyon without its river and strata, no policy without a river-gauge figure`

## (7) 测试提示词示例（现代题材：一座向干旱盆地扩张的新城，水能允许什么样的定居规模？）

- Prompt: `In the style of John Wesley Powell, survey a new city expanding into a dry basin: follow its rivers, measure the water, classify the land by irrigation, and say what settlement the water will allow`
- 中文对照：鲍威尔风格，考察一座向干旱盆地扩张的新城：顺河量水、按灌溉给土地分类，说清水能允许什么样的定居。
- Negative: `no settlement plan that ignores measured water supply, no humid-region land law imposed on arid land, no description of a canyon without its river and strata, no policy without a river-gauge figure`
- 检验点：回答是否按该地理学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
