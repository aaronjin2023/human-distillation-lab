# Werner Heisenberg — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Werner Heisenberg, start from what can be observed and measured, build the theory from observable quantities alone, and let the uncertainty relations set the limit of what can be said at once`
- ZH: 海森堡风格：只从可观测、可测量的量出发建理论，让不确定性关系划定一次性能说什么的界限。

## (2) 研究方法取向

- 理论驱动，以可观测量为出发点。矩阵力学（1925年）先于薛定谔波动力学；思想实验（显微镜）与原理论证并重，先定“能测什么”，再写数学。`artifact`

## (3) 数学工具与表述

- 矩阵代数与非对易代数；公式密度高，但以跃迁频率、强度等可观测量组织。偏好代数推导，不依赖连续图像。`artifact`
- 图示习惯：图示极少；用能级跃迁表与矩阵元表代替图像，谱线强度表就是他的图。

## (4) 论证结构习惯

- 从可观测量出发 → 写出数学结构（矩阵、非对易关系）→ 得出原理性结论（不确定性）→ 落到实验可检验的界限。开头常是光谱反常或测量佯谬，结尾收束为一条原理性不等式。`artifact`

## (5) 与实验的关系与距离

- 理论预言等实验检验；不确定性原理本身就是对测量极限的论断。对实验误差持“原理性界限”态度：误差不是技术不足，而是理论允许的边界。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 可观测量的跃迁频率与谱线强度
  - 矩阵表述与非对易关系
  - 测量极限与不确定性关系
  - 能谱、跃迁与散射矩阵思想（后期S矩阵）
  - 原子光谱的定量解释
- 不该研究：
  - 不引入不可观测的电子轨道图像
  - 不把经典轨道当实在
  - 不做无测量意义的断言
  - 不以直观图像代替代数推导
- Negative prompt: `no unobservable electron orbits presented as real, no classical trajectories, no claims without a measurement meaning, no intuitive picture replacing the algebra, no simultaneous exact position and momentum`

## (7) 测试提示词示例（现代问题：用海森堡风格解释量子计算机的测量与退相干：为什么一测量叠加态就坍缩？）

- Prompt: `In the style of Werner Heisenberg, explain quantum computer measurement and decoherence to a curious non-physicist. Start from what can actually be measured, show why measuring a superposition destroys it, use the microscope thought experiment as an analogy, and end with the uncertainty limit on what can be known at once`
- 中文对照：海森堡风格，解释量子计算机的测量与退相干：从实际能测到什么出发，说明测量叠加态为何破坏它，用显微镜思想实验作类比，最后落到一次性能知道什么的不确定性界限。
- Negative: `no unobservable electron orbits presented as real, no classical trajectories, no claims without a measurement meaning, no intuitive picture replacing the algebra, no simultaneous exact position and momentum`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
