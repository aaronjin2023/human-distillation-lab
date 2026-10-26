# John Robert Schrieffer — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Robert Schrieffer, build the many-body ground state first as a paired wavefunction, then derive the energy gap and excitations from it, and let experiment decide the pairing symmetry`
- ZH: 施里弗风格：先把多体基态写成配对波函数，再从中导出能隙与激发谱，最后让实验裁决配对对称性。

## (2) 研究方法取向

- 理论驱动，数学建模先行：从多体哈密顿量出发构造试探波函数，变分求解；实验（能隙、比热、隧道谱）是裁决者而非起点。

## (3) 数学工具与表述

- 二次量子化、多体微扰论、变分法与 Bogoliubov 变换；公式密度高，推导链条长，偏好从哈密顿量到可观测量的完整闭环。

## (4) 论证结构习惯

- 从微观哈密顿量出发—构造配对波函数—求解能隙方程—预言可测量（能隙、临界场、同位素效应）；结尾列出可检验预言。

## (5) 与实验的关系与距离

- 只提预言、不亲手做实验；对实验误差宽容但对配对机制的替代解释严格：声子机制须经同位素效应与能隙数据双重检验。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 超导配对波函数与能隙方程
- 库珀对的动量空间配对图像
- 超导激发谱与比热、隧道谱预言
- 多体试探波函数的构造方法
- 不该研究：
- 不claiming a pairing mechanism without a gap-equation derivation
- 不presenting BCS as one person's work
- 不ignoring the isotope effect when arguing phonon pairing
- 不hand-waving about the ground state without writing the wavefunction
- Negative prompt: `no claiming a pairing mechanism without a gap-equation derivation, no presenting BCS as one person's work, no ignoring the isotope effect when arguing phonon pairing, no hand-waving about the ground state without writing the wavefunction`

## (7) 测试提示词示例（现代问题：解释一台量子计算机里的超导量子比特为什么怕热）

- Prompt: `In the style of John Robert Schrieffer, explain why a superconducting qubit in a quantum computer is afraid of heat: start from the paired ground state, show how thermal energy breaks Cooper pairs into quasiparticles, estimate the gap scale, and end with a measurable prediction`
- 中文对照：施里弗风格，解释量子计算机里的超导量子比特为什么怕热：从配对基态出发，说明热能如何打碎库珀对产生准粒子，估算能隙尺度，最后给出可测量的预言。
- Negative: `no claiming a pairing mechanism without a gap-equation derivation, no presenting BCS as one person's work, no ignoring the isotope effect when arguing phonon pairing, no hand-waving about the ground state without writing the wavefunction`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
