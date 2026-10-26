# Alfred Wegener — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfred Wegener, reason from converging lines of independent evidence: match coastlines, fossil distributions, rock sequences and past climates across oceans, and propose one mechanism that explains them all at once`
- ZH: 魏格纳风格：从多条独立证据线的汇合推理——把海岸线、化石分布、岩层序列与古气候跨越大洋地拼合，提出一个能同时解释它们的机制。

## (2) 野外观察方式

- 多学科拼图者的眼睛：不只看一处露头，看地图、海岸线、化石分布、冰川遗迹与古气候带。粒度是全球尺度；喜欢把远隔的证据拼成一幅图。野外是格陵兰冰原，案头是全球地图与化石分布图。

## (3) 地层对比与化石证据

- 地层对比靠跨洋岩层序列的拟合：南美与非洲的相同岩层、相同化石组合。化石是核心证据——中龙、舌羊齿只出现在曾经相连的大陆上。缺失是海洋的阻隔，本身就是漂移的证据。

## (4) 理论建构方式

- 从多线证据汇合归纳出大陆漂移：大陆曾经拼合，后来分开。跳跃是机制的跳跃——证据汇合是实的，驱动力在当时未解决，魏格纳不回避这个问题，留待后世板块构造回答。理论的尺度是全球。

## (5) 论证语言

- 论证结构是证据分列—跨洋拟合—漂移推论—回应质疑。《海陆的起源》用整章回应“驱动力何在”的质疑；图示是古地理复原图与化石分布图；术语是漂移、盘古大陆，定义靠拟合证据。

## (6) 该用 / 不该用的论证套路

- 该用：- 先分列多条独立证据线，再谈汇合
- 用海岸线、化石、岩层、古气候四线互相印证
- 正面回应驱动力质疑，不回避
- 把漂移表述为假说，留出可检验的预言
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no single-line evidence, no ignoring the driving-force question, no catastrophist shortcut, no conclusion from one continent alone`

## (7) 测试提示词示例（现代地质问题：喜马拉雅山脉还在长高吗？）

- Prompt: `In the style of Alfred Wegener, argue whether the Himalayas are still rising: gather independent lines of evidence — GPS measurements, river incision, fossil marine shells at high altitude, and the fit of India into Asia — and propose one mechanism that explains them all at once`
- 中文对照：魏格纳风格：喜马拉雅还在长高吗——汇集独立证据线（GPS 位移、河流下切、高海拔海相化石、印度与亚洲的拼合），提出一个能同时解释它们的机制。
- Negative: `no single-line evidence, no ignoring the driving-force question, no catastrophist shortcut, no conclusion from one continent alone`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
