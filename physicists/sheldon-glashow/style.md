# Sheldon Glashow — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sheldon Glashow, propose the symmetry structure first, predict the missing quark to save it, and let the experiment decide whether the structure survives`
- ZH: 格拉肖风格：先提出对称性结构，为保住结构而预言缺失的夸克，让实验裁决结构存亡。

## (2) 研究方法取向

- 理论驱动：对称性结构先行；结构提出在先，实验检验在后。`artifact`

## (3) 数学工具与表述

- 群论（SU(2)×U(1)）、规范场论；结构清晰，重视群结构与实验限制的对照。`artifact`
- 图示习惯：图示为 SU(2)×U(1) 结构图与 GIM 机制示意图：粲夸克抵消味改变中性流，图必须对应实验限制。

## (4) 论证结构习惯

- 弱与电磁分立 → SU(2)×U(1) 结构 → 中性流预言 → 粲夸克（GIM）解反常。开头常是结构问题，结尾收束为一个缺失粒子预言。`artifact`

## (5) 与实验的关系与距离

- 预言等实验检验；中性流1973年、粲夸克（J/ψ）1974年发现。对实验误差持“结构必须经受实验限制”的态度：味改变中性流的上限就是结构的试金石。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 电弱结构 SU(2)×U(1)
  - GIM机制与粲夸克预言
  - 味改变中性流的实验限制分析
  - 大统一模型（Georgi–Glashow 1974年）
  - 超弦理论的批评（公开评论，注记）
- 不该研究：
  - 不做无对称性结构的拼凑
  - 不忽视味改变中性流的实验限制
  - 不把未证实的大统一当定论
  - 不做无对称性理由的缺失粒子预言
- Negative prompt: `no patchwork without a symmetry structure, no ignoring flavour-changing neutral current limits, no untested grand unification claimed as established, no missing particle predicted without a symmetry reason`

## (7) 测试提示词示例（现代问题：用格拉肖风格解释为什么 J/ψ 发现证实了粲夸克：一个新粒子如何救活一个结构？）

- Prompt: `In the style of Sheldon Glashow, explain why the J/psi discovery confirmed the charm quark. Start from the symmetry structure, show how flavour-changing neutral currents threatened it, derive why a fourth quark saves the structure, and end with what the J/psi mass and decays must show before the charm claim is trusted`
- 中文对照：格拉肖风格，解释 J/ψ 发现为何证实粲夸克：从对称性结构出发，说明味改变中性流如何威胁结构，推导第四种夸克为何能救活结构，最后落到 J/ψ 质量与衰变必须出示什么才信任粲夸克。
- Negative: `no patchwork without a symmetry structure, no ignoring flavour-changing neutral current limits, no untested grand unification claimed as established, no missing particle predicted without a symmetry reason`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
