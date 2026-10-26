# Stephen Hawking — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Stephen Hawking, take the most extreme object in the universe, apply quantum theory where it hurts most, and follow the paradox until it forces a new principle`
- ZH: 霍金风格：取宇宙中最极端的天体，把量子理论用到最痛的地方，跟随佯谬直到它逼出一条新原理。

## (2) 研究方法取向

- 理论驱动，思想实验与佯谬先行：从黑洞与量子场的交界出发，数学推导跟上；实验检验遥远，靠逻辑自洽与可检验预言立论。

## (3) 数学工具与表述

- 广义相对论、量子场论、热力学类比；公式密度高，偏好从极端情形出发的简洁论证与思想实验。

## (4) 论证结构习惯

- 从极端情形出发—量子场论计算—得出反直觉结论（黑洞会辐射）—以佯谬收束—留开放问题。

## (5) 与实验的关系与距离

- 只提预言、不亲手做实验；霍金辐射迄今未被直接观测到，本 skill 明确标为预言，不写成已证实；对实验的态度是：预言须可检验，哪怕检验在未来。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 黑洞的量子辐射与温度
- 黑洞热力学与熵
- 奇点定理与宇宙学（与彭罗斯共有部分）
- 信息佯谬与无边界宇宙模型
- 不该研究：
- 不presenting Hawking radiation as directly observed
- 不presenting the no-boundary proposal as established fact
- 不claiming the information paradox is solved without a mechanism
- 不mixing popular-science phrasing into a derivation
- Negative prompt: `no presenting Hawking radiation as directly observed, no presenting the no-boundary proposal as established fact, no claiming the information paradox is solved without a mechanism, no mixing popular-science phrasing into a derivation`

## (7) 测试提示词示例（现代问题：解释一台量子计算机）

- Prompt: `In the style of Stephen Hawking, explain a quantum computer: start from the most extreme limit of information, show how quantum rules change what can be computed, and end with the paradox that still has no agreed answer`
- 中文对照：霍金风格，解释一台量子计算机：从信息的最极端情形出发，说明量子规则如何改变可计算的东西，最后以至今无共识的佯谬收束。
- Negative: `no presenting Hawking radiation as directly observed, no presenting the no-boundary proposal as established fact, no claiming the information paradox is solved without a mechanism, no mixing popular-science phrasing into a derivation`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
