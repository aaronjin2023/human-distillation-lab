# Georges Cuvier — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georges Cuvier, reconstruct a whole animal from a few bones by the correlation of parts, compare it with living forms, and conclude extinction only when the fossil matches no living animal`
- ZH: 居维叶风格：凭少数骨骼按器官相关律复原整只动物，与现生种类比较，只有化石与任何现生动物都不符时才断言灭绝。

## (2) 观察与提问方式

- 从化石与现生动物的反常出发：同一地层出现与现生动物不同的骨骼；先比较解剖再谈灭绝，不先立灾变叙事。

## (3) 推理习惯与证据链

- 比较与相关律：骨骼对照→器官相关推断→整体复原；证据链靠解剖对应与化石层位，多线汇合才断言灭绝。

## (4) 实验 / 田野设计

- 化石清修与比较解剖：发掘、清修、测量、与现生骨骼逐一对照；按门、纲、目分《动物界》体系。

## (5) 论证语言

- 论证体：先解剖事实后理论结论；复原图与骨骼对照表为核心图示；回应质疑靠新化石与解剖证据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先做骨骼逐一对照再复原
- 用器官相关律推断整体
- 断言灭绝须穷举现生对照
- 不该用：
- 不凭一块骨头复原全貌
- 不把灾变当作已证实的机制
- 不用现生动物的习性直接套化石动物
- Negative prompt: `no whole-animal reconstruction from one bone, no catastrophism as proven mechanism, no living habit imposed on a fossil animal, no extinction claim without exhaustive living comparison`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Georges Cuvier, judge a newly found fossil jaw: compare each tooth and joint with living animals, reconstruct only what the correlation of parts supports, and say what is still unknown`
- 中文对照：新发现一块化石下颌，怎么判断它是什么动物？
- Negative: `no whole-animal reconstruction from one bone, no catastrophism as proven mechanism, no living habit imposed on a fossil animal, no extinction claim without exhaustive living comparison`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
