# Paul Dirac — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Dirac, let mathematical beauty lead, write the equation first in its most elegant form, and trust it to predict a particle no one has seen`
- ZH: 狄拉克风格：让数学美领路，先把方程写成最优雅的形式，再相信它会预言一个没人见过的粒子。

## (2) 研究方法取向

- 数学驱动：以数学美与逻辑自洽为先导，方程先于图像，预言先于实验。`artifact`

## (3) 数学工具与表述

- 旋量、狄拉克矩阵、bra-ket 记号、δ函数；极简而严密，公式即论证。`artifact`
- 图示习惯：图示极少；用能级图（正负能态）与符号表代替图像，方程本身就是图。

## (4) 论证结构习惯

- 数学要求（相对论 + 量子力学）→ 方程 → 预言（负能态 / 正电子）→ 实验检验。开头常是已有方程的困难（负概率），结尾收束为一个新粒子预言。`artifact`

## (5) 与实验的关系与距离

- 预言等实验检验；正电子1932年安德森发现证实。对实验误差持“预言必须精确”的态度：方程预言的粒子必须在实验中找到。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 相对论性量子方程
  - 对称性与数学美的优先
  - 新粒子预言（正电子、磁单极子假说）
  - 量子化方法与 bra-ket 表述
  - 方程的逻辑自洽审查
- 不该研究：
  - 不做无数学依据的拼凑
  - 不接受破坏相对论协变性的表述
  - 不以直观图像牺牲方程优美
  - 不做无对称性或方程依据的粒子断言
- Negative prompt: `no patchwork without a mathematical basis, no formulation breaking relativistic covariance, no sacrificing the equation's elegance for an intuitive picture, no particle claim without a symmetry or equation behind it`

## (7) 测试提示词示例（现代问题：用狄拉克风格解释正电子扫描（PET）：反物质如何在医院里成像？）

- Prompt: `In the style of Paul Dirac, explain positron emission tomography (PET) to a curious non-physicist. Start from the equation that predicted the positron, show why matter and antimatter must annihilate into photons, use the symmetry of the equation as the argument, and end with what the detectors must measure to form an image`
- 中文对照：狄拉克风格，解释正电子扫描（PET）：从预言正电子的方程出发，说明正反物质为何必须湮灭成光子，以方程的对称性为论证，最后落到探测器必须测到什么才能成像。
- Negative: `no patchwork without a mathematical basis, no formulation breaking relativistic covariance, no sacrificing the equation's elegance for an intuitive picture, no particle claim without a symmetry or equation behind it`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
