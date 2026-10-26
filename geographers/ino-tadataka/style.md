# Inō Tadataka — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Inō Tadataka, walk every coast with a measuring chain: latitude by the stars, distance by steps, and let the surveyed line replace every copied coastline`
- ZH: 伊能忠敬风格：以测绳走遍每一段海岸——纬度凭星测，距离凭步量，让实测线取代一切抄来的海岸线。

## (2) 考察方法

- 田野方式：徒步沿海实测：以步测与天文观测逐段测绘日本海岸，历时多年。 `artifact`
- 证据偏好：实测步数与天文纬度为主；几乎不用未经实测的旧图海岸线。 `artifact`
- 尺度偏好：国家尺度：以海岸线为单元，逐段拼成日本全国图。 `artifact`

## (3) 制图与空间表达

- 地图风格：实测地形图：海岸线精确，内陆地名据实测点填充；比例尺统一。 `artifact`
- 空间表达：以海岸线组织图面：沿海逐段推进，内陆据测点补绘。 `artifact`
- 质感：图面精确，注记为测点与地名；地图独立成图，附测绘记录。 `artifact`

## (4) 理论建构习惯

- 论述结构：先测一段海岸，再拼下一段，最后合成为全国图：实测在前，成图在后。 `artifact`
- 核心概念：沿海实测、步测、天文纬度、全国地形图、逐段拼接。概念之间以前一项为证据、后一项为落点衔接：从沿海实测出发，经步测、天文纬度、全国地形图，落在逐段拼接。 `artifact`
- 论证落点：结论落在全图上：日本全国海岸线第一次由实测拼成。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是步测覆盖的距离；海岸线是实测的线，不是抄来的线。 `artifact`
- 时间观：线性累积时间：多年逐段实测，图随测绘生长。 `artifact`
- 人地关系：人地关系淡：地图重海岸与地形，少论环境决定。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 沿海实测的海岸线
- 步测与天文纬度的测点
- 全国图的逐段拼接
- 统一比例尺的图面
- 不该研究：
- 未经实测的旧图海岸线
- 无测点依据的内陆地名
- 为求快照抄旧图
- 把测绘写成游记
- Negative prompt: `no coastline copied from old maps, no inland name without a measured point, no copying old maps merely to finish faster, no turning the survey into a travelogue`

## (7) 测试提示词示例（现代题材：一张以骑手步测轨迹拼成的城市地图）

- Prompt: `In the style of Inō Tadataka, walk every street of a city with a measuring chain: fix each corner by observation, and let the surveyed line replace every copied street map.`
- 中文对照：伊能忠敬风格：以测绳走遍城市的每条街道——每个路口凭观测定位，让实测线取代一切抄来的街道图。
- Negative: `no coastline copied from old maps, no inland name without a measured point, no copying old maps merely to finish faster, no turning the survey into a travelogue`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在全图上：日本全国海岸线第一次由实、是否出现 Negative prompt 禁止的套路。
