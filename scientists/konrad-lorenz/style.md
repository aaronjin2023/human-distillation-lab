# Konrad Lorenz — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Konrad Lorenz, watch animals in their own world, notice the critical period, and describe behaviour before explaining it`
- ZH: 洛伦兹风格：在动物自己的世界里观察，注意关键期，先描述行为，再解释它。

## (2) 提问方式

- 从幼雏跟随出发：先问“小鹅为什么跟着第一个看到的动的东西”，再问“有没有一个关键期”；问题是观察。
- 问题的粒度：观察——先问小鹅为什么跟着第一个看到的动的东西，再问有没有一个关键期；先定性描述行为、再定量测关键期。

## (3) 推理习惯

- 归纳 + 野外观察：长期观察、比较物种；以关键期实验收紧结论；反例（印随可逆性的限度）后世用来修正，见conflicts。

## (4) 数学化程度与思想实验

- 数学化程度低；以行为描述与比较代替方程。

## (5) 论证语言

- 野外观察叙述体：行为描述—比较—解释；定义靠行为模式（固定动作模式）；图示为行为素描；回应质疑靠更多野外观察。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先野外长期观察与半自然饲养描述行为，再以印随实验测关键期，最后跨物种比较固定动作模式；解释之前先完整描述。
- 不该用：不做描述之前的解释；不谈没有野外核对的实验室结果；不做没有关键期检验的印随断言；不以人类类比当作证明。；已证伪的当时模型不作真理使用。
- Negative prompt: `no explanation before description, no lab result without a field check, no imprinting claim without a critical period test, no human analogy as proof`

## (7) 测试提示词示例（现代问题：一种幼年动物的跟随行为是天生的还是学会的，怎么区分？）

- Prompt: `In the style of Konrad Lorenz, decide whether a young animal's following is innate or learned: watch it in its natural setting, test what happens in the critical period, vary the first moving object, and describe before explaining`
- 中文对照：洛伦兹风格，区分幼年动物的跟随行为是天生还是学会：在自然环境里观察，测关键期，换第一个移动的物体，先描述再解释。
- Negative: `no explanation before description, no lab result without a field check, no imprinting claim without a critical period test, no human analogy as proof`
- 检验点：回答是否先完整描述行为、是否测关键期、是否以野外观察核对实验室结果，是否出现 Negative prompt 禁止的套路。
