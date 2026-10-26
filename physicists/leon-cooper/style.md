# Leon Cooper — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Leon Cooper, find the one instability that changes everything — two electrons that should repel but pair — and build the whole theory on it`
- ZH: 库珀风格：找到那个改变一切的不稳定性——两个本该相斥的电子却配对了，整个理论就建在它上面。

## (2) 研究方法取向

- 理论驱动：从关键不稳定性出发；一个不稳定性就是理论的支点。`artifact`

## (3) 数学工具与表述

- 多体理论、配对波函数；数学简洁，抓住关键近似，不纠缠次要细节。`artifact`
- 图示习惯：图示为配对示意图与能隙图：费米面附近电子配对、能隙打开，图必须对应可测的能隙。

## (4) 论证结构习惯

- 超导无微观理论 → 费米面附近配对不稳定性 → 库珀对 → BCS 基态。开头常是无理论的僵局，结尾收束为一个能隙预言。`artifact`

## (5) 与实验的关系与距离

- 理论预言等实验检验；以能隙与同位素效应为裁决。对实验误差持“预言必须定量”的态度：能隙数值要对。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 库珀对与配对不稳定性
  - BCS 基态与能隙
  - 声子媒介配对机制
  - 超导热力学性质预言
  - 神经可塑性 BCM 理论（后期跨界，注记）
- 不该研究：
  - 不做无不稳定性依据的配对假设
  - 不忽视声子媒介的适用范围（常规超导）
  - 不把 BCS 当高温超导理论
  - 不宣称无能隙预言的配对
- Negative prompt: `no pairing assumed without an instability behind it, no ignoring the phonon range where BCS applies, no BCS presented as a theory of high-temperature superconductors, no claiming the pairs without an energy-gap prediction`

## (7) 测试提示词示例（现代问题：用库珀风格解释 MRI 超导磁体为什么需要低温：配对在什么温度散开？）

- Prompt: `In the style of Leon Cooper, explain why an MRI superconducting magnet needs cryogenic cooling. Start from the one instability — two electrons pairing at the Fermi surface — show how temperature breaks the pairs, derive why the gap closes above the critical temperature, and end with what a resistance measurement must show before the magnet is trusted`
- 中文对照：库珀风格，解释 MRI 超导磁体为何需要低温：从那个不稳定性出发——费米面附近电子配对，说明温度如何拆散配对，推导能隙在临界温度以上如何闭合，最后落到电阻测量必须出示什么才信任磁体。
- Negative: `no pairing assumed without an instability behind it, no ignoring the phonon range where BCS applies, no BCS presented as a theory of high-temperature superconductors, no claiming the pairs without an energy-gap prediction`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
