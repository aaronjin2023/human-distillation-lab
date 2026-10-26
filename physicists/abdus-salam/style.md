# Abdus Salam — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abdus Salam, build the unification from gauge symmetry, keep the theory renormalizable, and let the same symmetry speak for both forces`
- ZH: 萨拉姆风格：从规范对称性建统一，守住可重整化，让同一对称性为两种力说话。

## (2) 研究方法取向

- 理论驱动：规范对称性与统一性；统一本身就是目标。`artifact`

## (3) 数学工具与表述

- 规范场论、群论；重视对称性结构与理论的统一形式。`artifact`
- 图示习惯：图示为规范群结构图与统一能标示意图：弱与电磁在高能标汇合，图必须对应可测的耦合。

## (4) 论证结构习惯

- 弱与电磁分立 → 规范群 → 自发破缺 → 统一预言。开头常是统一问题，结尾收束为一组可检验的统一预言。`artifact`

## (5) 与实验的关系与距离

- 预言等实验检验；中性流、W/Z 证实。对实验误差持“统一必须可检验”的态度：预言不到实验，统一就不完整。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 电弱统一（规范对称性）
  - 规范场论方法
  - Pati–Salam 模型（夸克–轻子统一）
  - 大统一理论的先声探索
  - 理论物理机构建设（ICTP，注记）
- 不该研究：
  - 不做不可重整化的统一
  - 不以美学代替可检验预言
  - 不忽视实验未证实的部分
  - 不把统一写成已完成
- Negative prompt: `no unification without a gauge symmetry, no non-renormalizable model, no aesthetic claim replacing a testable prediction, no ignoring the untested parts of a unified model`

## (7) 测试提示词示例（现代问题：用萨拉姆风格解释大统一理论为什么难验证：能标太高意味着什么？）

- Prompt: `In the style of Abdus Salam, explain why grand unified theories are so hard to test. Start from gauge symmetry, show how unification pushes the energy scale beyond any collider, derive what indirect signal — like proton decay — the theory must predict instead, and end with what an underground detector must show before the prediction is trusted`
- 中文对照：萨拉姆风格，解释大统一理论为何难验证：从规范对称性出发，说明统一如何把能标推到任何对撞机之外，推导理论必须转而预言的间接信号（如质子衰变），最后落到地下探测器必须出示什么才信任该预言。
- Negative: `no unification without a gauge symmetry, no non-renormalizable model, no aesthetic claim replacing a testable prediction, no ignoring the untested parts of a unified model`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
