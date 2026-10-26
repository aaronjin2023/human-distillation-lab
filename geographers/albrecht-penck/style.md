# Albrecht Penck — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第6.5节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Albrecht Penck, map the ice before the land: trace moraines and terraces, order the glaciations, and let the surface explain the climate that made it`
- ZH: 彭克风格：先绘冰、再读地——追踪冰碛与阶地，排出冰期序列，让地表自己说出造就它的气候。

## (2) 考察方法

- 田野方式：以阿尔卑斯野外调查与冰川地貌测绘为田野：冰碛、阶地、冰蚀谷实地观测；最依赖地貌标志的系统编目。
- 证据偏好：地貌标志观测为主：冰碛垄、阶地、磨光面；量算为辅；几乎不用纯理论推演，冰期序列必有野外标志。
- 尺度偏好：以阿尔卑斯山系为基本尺度，论证上收至第四纪全球冰期；尺度转换靠“冰期序列”——地方阶地叠加即全球气候史。

## (3) 制图与空间表达

- 冰川地貌图为主：冰碛分布、阶地序列、冰川范围；符号精确，比例尺明确；地图是冰期论证的证据。

## (4) 理论建构习惯

- 论述结构：地貌标志编目 → 阶地对比 → 冰期序列 → 气候推论。核心概念：冰期、间冰期、冰碛、阶地、地表形态学。概念衔接：冰碛定冰川范围，阶地定冰期次序，次序定气候变化。论证落点：理论命题——阿尔卑斯四次冰期序列。

## (5) 空间观与时间观

- 空间观：冰川空间——空间是冰进冰退留下的痕迹场。时间观：第四纪时间——以冰期—间冰期计。人地关系：不直接论人地，只论冰川与地表。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 冰碛与阶地的系统编目
- 冰期序列的对比与排序
- 冰川地貌图的绘制
- 地表形态的分类
- 不该研究：no ice-age sequence without field markers, no terrace correlation without a mapped section, no climate claim from a single moraine, no landform described without its glacial origin
- Negative prompt: `no ice-age sequence without field markers, no terrace correlation without a mapped section, no climate claim from a single moraine, no landform described without its glacial origin`

## (7) 测试提示词示例（现代题材：一座山区的河谷，冰碛与阶地能告诉我们怎样的冰期与气候史？）

- Prompt: `In the style of Albrecht Penck, survey a new mountain valley: map its moraines and terraces, order the glaciations, and read the climate history from the surface`
- 中文对照：彭克风格，考察一座新建山区的河谷：绘出冰碛与阶地、排出冰期序列，从地表读出气候史。
- Negative: `no ice-age sequence without field markers, no terrace correlation without a mapped section, no climate claim from a single moraine, no landform described without its glacial origin`
- 检验点：回答是否按该地理学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
