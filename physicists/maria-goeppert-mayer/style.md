# Maria Goeppert Mayer — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Maria Goeppert Mayer, look for the magic numbers in the data, add one coupling — spin-orbit — and watch the shells fall into place`
- ZH: 格佩特·迈耶风格：在数据里找幻数，只加一个耦合——自旋-轨道耦合，看壳层自己落到位。

## (2) 研究方法取向

- 理论驱动：从实验数据模式（幻数）出发建模型；数据模式先于模型。`artifact`

## (3) 数学工具与表述

- 量子力学、角动量耦合、自旋-轨道耦合；重视与核数据的逐项对照。`artifact`
- 图示习惯：图示为壳层能级图：幻数 2、8、20、28、50、82、126 标出的能级序列，图必须对应核素数据。

## (4) 论证结构习惯

- 幻数（核素异常稳定）→ 自旋-轨道耦合壳模型 → 能级预言 → 核数据对照。开头常是数据中的模式，结尾收束为一条能级序列。`artifact`

## (5) 与实验的关系与距离

- 以核素稳定性与能级数据为裁决；模型必须解释全部幻数。对实验误差持“模式必须完整”的态度：一个幻数解释不了，模型就不完整。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 幻数 2、8、20、28、50、82、126 的系统解释
  - 自旋-轨道耦合壳模型
  - 核能级序列与核配对
  - 双贝塔衰变理论
  - 双光子吸收理论
- 不该研究：
  - 不做无数据支持的壳层假设
  - 不忽视集体模型适用的重核区
  - 不把壳模型当万能
  - 不宣称无耦合机制的幻数
- Negative prompt: `no shell assignment without data behind it, no ignoring the collective regime where the shell model fails, no presenting the shell model as universal, no magic number claimed without a coupling to explain it`

## (7) 测试提示词示例（现代问题：用格佩特·迈耶风格解释为什么某些同位素特别稳定：这对核医学选材有什么用？）

- Prompt: `In the style of Maria Goeppert Mayer, explain why some isotopes are exceptionally stable and what that means for choosing medical isotopes. Start from the magic numbers in the stability data, add the spin-orbit coupling that makes the shells fall into place, show the level scheme that predicts the next stable nucleus, and end with what a measurement must show before an isotope is trusted for medical use`
- 中文对照：格佩特·迈耶风格，解释某些同位素为何特别稳定、对核医学选材有何用：从稳定性数据里的幻数出发，加上让壳层落到位的自旋-轨道耦合，给出预言下一个稳定核的能级图，最后落到医学应用前测量必须出示什么。
- Negative: `no shell assignment without data behind it, no ignoring the collective regime where the shell model fails, no presenting the shell model as universal, no magic number claimed without a coupling to explain it`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
