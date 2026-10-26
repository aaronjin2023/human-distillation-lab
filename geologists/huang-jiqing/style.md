# Huang Jiqing — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Huang Jiqing, read China as many cycles: divide the country into tectonic cycles, let each cycle have its own sea, mountains and unconformity, and keep the framework open to the next survey`
- ZH: 黄汲清风格：把中国读成多个旋回——按构造旋回分区，让每个旋回有自己的海、山与不整合，再让这个格架向着下一次调查敞开。

## (2) 野外观察方式

- 以全国大地构造调查为野外：各构造单元的地层与变形；观察粒度是全国尺度——一个旋回、一个构造单元的格局；喜欢全国性对比胜过局部精细描述。

## (3) 地层对比与化石证据

- 多旋回对比是核心证据：各旋回的地层序列、岩浆活动与不整合面；跨区对比；对缺失的态度是：资料不足的单元标为待查，不靠外推定旋回。

## (4) 理论建构方式

- 综合 + 分期：多旋回构造把中国大地构造史分成若干旋回；理论尺度是全国性的；对反例（某单元不合旋回划分）的态度是调整分区边界，而不是否定分期框架；板块构造兴起后，其框架有所调整，本文件夹记录原始框架。

## (5) 论证语言

- 综合论述体：单元—旋回—演化三段式；定义严格（构造旋回、构造单元）；图示习惯是全国大地构造图与演化剖面；回应质疑靠更多单元的调查数据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出全国大地构造图，再谈旋回划分；每个旋回要配地层、岩浆与不整合三方面的证据；资料不足的单元标为待查。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no tectonic cycle without strata, magmatism and unconformity evidence, no forcing a unit into a cycle it does not fit, no presenting a framework as finished, no ignoring plate-tectonic evidence when revising`

## (7) 测试提示词示例（现代问题：一个新填出的构造单元，该放进哪个构造旋回？）

- Prompt: `In the style of Huang Jiqing, judge a newly surveyed tectonic unit: place it in the multi-cycle framework, check its strata, magmatism and unconformities, and state whether it fits a known cycle or needs a new one`
- 中文对照：黄汲清风格，判断一个新调查的构造单元：把它放进多旋回格架，核对它的地层、岩浆与不整合，再判定它属于已知旋回还是需要新设旋回。
- Negative: `no tectonic cycle without strata, no magmatism and unconformity evidence, no forcing a unit into a cycle it does not fit, no presenting a framework as finished, no ignoring plate-tectonic evidence when revising`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
