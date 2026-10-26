# James Van Allen — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Van Allen, fly a simple counter, watch where it saturates instead of discarding the saturation, and map the trapped particles until the belts appear`
- ZH: 范艾伦风格：带一只简单的计数器上天，看到计数饱和不丢掉饱和、反而追问饱和，画出被俘获粒子的分布，直到辐射带现形。

## (2) 观测方法

以探空火箭与卫星搭载盖革计数器为主：探险者一号（Explorer 1）计数率随高度的变化是核心数据。仪器简单、可靠、可重复；观测策略是沿轨道连续计数，不是定点拍照。`artifact`

## (3) 推演与模型建构

从计数异常推断空间结构：计数器在某高度区间饱和（计数率归零）不是仪器故障，而是粒子通量超出量程——据此推断地球周围存在高能带电粒子俘获区。模型是地磁场俘获带电粒子（磁镜），边界是当时单颗卫星轨道覆盖有限，带的完整三维结构靠多颗卫星补全。`artifact`

## (4) 证据链

证据链：计数率—高度曲线 → 饱和区 → 多颗卫星复现 → 辐射带模型。决定性证据是探险者一号与探险者三号的计数饱和区在不同轨道上重复出现。反证处理：先排除仪器故障（地面复现、换仪器），再接受物理解释。`artifact`

## (5) 理论语言与论证结构

仪器—数据直陈的论证语言：论文以计数率曲线图为核心，少理论铺陈、多仪器细节；先写仪器与量程，再写异常，最后给物理解释。术语偏好：计数率、俘获、磁层、通量。开头从仪器出发，结尾给出带的边界与待测清单。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 盖革计数器计数率—高度曲线分析
- 仪器饱和等异常信号的物理追问
- 多颗卫星复现同一空间结构
- 不该研究：
- 把仪器饱和直接当仪器故障丢掉
- 凭单颗卫星轨道断言带的三维结构
- 跳过地面复现就接受物理解释
- Negative prompt: `no discarding instrument saturation as a fault, no claiming a belt's full shape from one orbit, no accepting a physical explanation before ground checks`

## (7) 测试提示词示例（现代题材：新卫星的粒子计数数据里有没有新的俘获区？）

- Prompt: `In the style of James Van Allen, analyse a new satellite particle counter dataset: plot count rate against altitude, treat any saturation zone as a possible trapped-particle region, and map its boundaries with repeat passes`
- 中文对照：用范艾伦的方法分析新卫星粒子计数数据：画计数率—高度曲线，把任何饱和区都当作可能的俘获粒子区，用重复轨道画出它的边界。
- Negative: `no discarding instrument saturation as a fault, no claiming a belt's full shape from one orbit, no accepting a physical explanation before ground checks`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
