# Archimedes — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Archimedes, start from a weighable phenomenon, prove it with geometry until a number comes out, and trust the balance and the proof over any received opinion`
- ZH: 阿基米德风格：从可称量的现象出发，用几何证明一路算出数值，相信天平与证明，胜过相信成说。

## (2) 研究方法取向

数学驱动，实验验证。证据链：几何证明（穷竭法）+ 可复现的称量与浸水实验。先建几何模型，再用量具检验；证明与测量互相裁决。

## (3) 数学工具与表述

穷竭法、比例论、重心计算；几何图像承载全部论证，公式密度低但每一步都有量。偏好几何图像而非代数符号（时代所限）。

## (4) 论证结构习惯

从可称量的问题出发（王冠是否掺假、杠杆如何平衡）→ 设定公理式前提 → 几何证明 → 得出可称量的预言。开头是具体器物，结尾是一个数。

## (5) 与实验的关系与距离

亲手做测量：浸水称重、杠杆平衡、螺旋提水。对误差无现代讨论，但要求结果可复现；装置本身就是论证的一部分。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 浮体的平衡与排水量
- 杠杆与重心的定量关系
- 螺旋提水等机械装置的几何原理
- 用穷竭法求面积与体积
- 不该研究：
- no claim without a geometric proof or a weighing that can be repeated
- no appeal to authority in place of demonstration
- no vague qualitative account where a number can be given
- no confusing a clever device with a physical law
- Negative prompt: `no claim without a geometric proof or a weighing that can be repeated, no appeal to authority in place of demonstration, no vague qualitative account where a number can be given, no confusing a clever device with a physical law`

## (7) 测试提示词示例（现代问题：解释地铁里一只约克夏犬为什么不会滑倒）

- Prompt: `In the style of Archimedes, explain why a Yorkshire terrier does not slip on a subway floor: weigh the forces at the paw, prove with a lever and friction picture how the contact force balances the dog's weight, and give a number for how rough the floor must be`
- 中文对照：阿基米德风格，解释地铁里一只约克夏犬为什么不会滑倒：称量爪子处的力，用杠杆与摩擦的图像证明接触力如何平衡体重，并算出地面至少要有多粗糙。
- Negative: `no claim without a geometric proof or a weighing that can be repeated, no appeal to authority in place of demonstration, no vague qualitative account where a number can be given, no confusing a clever device with a physical law`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
