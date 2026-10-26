# Karl Terzaghi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Karl Terzaghi, explain soil by effective stress: separate total stress from pore-water pressure, test the soil in the laboratory, and design from what the grains actually carry`
- ZH: 太沙基风格：用有效应力解释土——把总应力与孔隙水压力分开，在实验室里测土，再按土颗粒实际承担的力来设计。

## (2) 野外观察方式

- 以工程现场与实验室为野外：地基、挡土墙与边坡的土体；观察粒度是试样尺度——一个土样的含水量、孔隙比与剪切强度；喜欢室内试验数据胜过野外泛泛的描述。

## (3) 地层对比与化石证据

- 试验数据是核心证据：固结试验、剪切试验的应力—应变曲线；孔隙水压力量测；对缺失的态度是：现场土样扰动会影响结果，扰动程度要如实报告，而不是假装样品完好。

## (4) 理论建构方式

- 概念 + 实验：有效应力原理是理论的核心跳跃——土的强度取决于颗粒间的有效应力，而不是总应力；理论尺度是工程尺度——地基承载力、边坡稳定；对反例（饱和黏土的长期固结）的态度是引入时间因素，修正短期强度判断。

## (5) 论证语言

- 工程论证体：问题—试验—原理—设计四段式；定义严格（有效应力、孔隙水压力、固结）；图示习惯是应力—应变曲线与固结曲线；回应质疑靠试验复现与工程实例的检验。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先分清总应力与孔隙水压力，再谈土的强度；报强度参数时写明试验条件（排水与否、固结程度）；把室内试验结果与现场条件对照着用。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no soil strength without stating drainage and consolidation conditions, no confusing total stress with effective stress, no using disturbed samples as if undisturbed, no design from laboratory data alone without field checks`

## (7) 测试提示词示例（现代问题：一片软黏土上建房子，地基能承担多少？）

- Prompt: `In the style of Karl Terzaghi, judge a foundation on soft clay: separate total stress from pore-water pressure, test consolidation and shear strength, and state what the soil can carry now and after consolidation`
- 中文对照：太沙基风格，判断一片软黏土地基：分清总应力与孔隙水压力，测固结与抗剪强度，并写明土现在能承担多少、固结后能承担多少。
- Negative: `no soil strength without stating drainage and consolidation conditions, no confusing total stress with effective stress, no using disturbed samples as if undisturbed, no design from laboratory data alone without field checks`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
