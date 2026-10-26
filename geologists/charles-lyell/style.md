# Charles Lyell — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Lyell, argue that the present is the key to the past: take a process you can watch today, stretch it over deep time, and show that no catastrophe is needed to build mountains or carve valleys`
- ZH: 莱伊尔风格：以现在为过去的钥匙——取一个今天能观察到的过程，把它拉长到深时尺度，证明造山与切谷都不需要灾变。

## (2) 野外观察方式

- 旅行观察家的眼睛：从埃特纳火山到尼罗河三角洲，从英格兰海岸到北美，看现代过程留下的痕迹。粒度是区域到全球尺度；喜欢把一处现代过程与一处古代岩石并置。

## (3) 地层对比与化石证据

- 第三纪地层靠海生贝壳化石中现生种的比例划分：始新世、中新世、上新世。化石是定量证据——现生种比例越高，地层越年轻。地层对比靠化石组合与岩性并用。缺失是侵蚀与未沉积，不必用灾变填补。

## (4) 理论建构方式

- 从现代过程类比古代：均变论系统化。跳跃是尺度的跳跃——把今日的毫米级沉积乘以深时，得到千米级地层。理论的尺度是全球与深时；对反例的态度是逐版修订《地质学原理》，不回避。

## (5) 论证语言

- 论证结构是现代过程描述—古代岩石对比—均变推论—回应质疑。图示是现代与古代并置的剖面与素描；术语定义严格（均变、第三纪三分）；《地质学原理》多版修订，质疑用新版回应。

## (6) 该用 / 不该用的论证套路

- 该用：- 先描述一个今天能观察到的过程，再类比古代
- 用现生种比例等定量指标划分地层
- 把时间尺度拉长到足以容纳缓慢过程
- 遇反例修订理论，不回避质疑
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no catastrophist shortcut, no invoking a cause no modern process can show, no short-timescale explanation, no ignoring the fossil proportion that dates the strata`

## (7) 测试提示词示例（现代地质问题：喜马拉雅山脉还在长高吗？）

- Prompt: `In the style of Charles Lyell, argue whether the Himalayas are still rising: gather modern processes you can watch today — river incision, uplifted marine terraces, GPS motion — stretch them over deep time, and show what slow causes can and cannot explain`
- 中文对照：莱伊尔风格：喜马拉雅还在长高吗——收集今天能观察到的过程（河流下切、抬升的海成阶地、GPS 位移），拉长到深时尺度，论证缓慢成因能解释什么、不能解释什么。
- Negative: `no catastrophist shortcut, no invoking a cause no modern process can show, no short-timescale explanation, no ignoring the fossil proportion that dates the strata`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
