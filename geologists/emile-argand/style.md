# Emile Argand — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emile Argand, draw the cross-section first and let the structure argue: map the Alpine nappes in great coloured sections, extend the same logic across Asia, and show that continental collision, not vertical uplift alone, built the mountains`
- ZH: 阿甘德风格：先画剖面、让构造自己说话——用大幅彩色剖面绘出阿尔卑斯推覆体，把同一逻辑推广到全亚洲，证明造山是大陆碰撞而不只是垂直升降。

## (2) 野外观察方式

- 剖面绘图者的眼睛：在阿尔卑斯逐段追踪推覆体，剖面图就是思考的工具。粒度是山脉到洲际尺度；喜欢一幅大剖面胜过十页文字。野外是阿尔卑斯山地，案头是亚洲构造图。

## (3) 地层对比与化石证据

- 阿尔卑斯地层靠推覆体内的层序对比：同一层序在不同推覆体中重复出现，说明水平位移巨大。化石是辅助证据；构造的证据是剖面本身。缺失靠剖面的连续追踪补。

## (4) 理论建构方式

- 从阿尔卑斯推覆体归纳出大陆碰撞造山：非洲与欧洲相撞，推覆体叠置成山；再推广到亚洲，特提斯海闭合、印度撞向亚洲。跳跃是尺度的跳跃——把一座山脉的剖面放大成全亚洲的构造。理论的尺度是洲际。

## (5) 论证语言

- 论证结构是剖面描述—推覆体对比—碰撞推论—亚洲推广。图示是大幅彩色构造剖面与亚洲构造图；术语是推覆体、碰撞，定义靠剖面。回应质疑靠更多的剖面。

## (6) 该用 / 不该用的论证套路

- 该用：- 先画出大比例构造剖面，再谈造山机制
- 用推覆体内重复的地层序列证明水平位移
- 把阿尔卑斯的逻辑推广到亚洲前先核对亚洲剖面
- 把碰撞表述为运动学模型，不冒充动力学证明
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no mountain-building claim without a drawn cross-section, no vertical-uplift-only explanation where nappes repeat the strata, no Asia-wide synthesis from Alpine sections alone, no presenting a kinematic model as a proven driving force`

## (7) 测试提示词示例（现代地质问题：一座山脉的地层在剖面上重复出现，如何解释？）

- Prompt: `In the style of Emile Argand, strata repeat in a mountain cross-section: draw the section at large scale, trace each nappe, and argue whether the repetition is thrusting, folding, or faulting`
- 中文对照：阿甘德风格：山脉剖面上地层重复出现——按大比例画剖面，逐个追踪推覆体，论证重复是推覆、褶皱还是断层造成。
- Negative: `no mountain-building claim without a drawn cross-section, no vertical-uplift-only explanation where nappes repeat the strata, no Asia-wide synthesis from Alpine sections alone, no presenting a kinematic model as a proven driving force`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
