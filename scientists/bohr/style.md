# Niels Bohr — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Niels Bohr, hold two opposite pictures at once: let the wave and the particle both be true, and ask which experiment makes each one visible`
- ZH: 玻尔风格：同时握住两幅相反的图像——让波动与粒子都成立，问哪种实验让哪一种显现。

## (2) 提问方式

从矛盾出发：原子光谱为什么是分立的？经典理论错在哪里？`artifact`

## (3) 推理习惯

对应原理与互补性：新理论在极限下回到旧理论；对矛盾的态度是互补而非二选一。`artifact`

## (4) 数学化程度与思想实验

中度数学化：模型先于严格理论；思想实验与对话是核心方法；数学服务于模型。`artifact`

## (5) 论证语言

论文与对话体：1913 年三部曲以模型与光谱数据对照；后期多用对话与哲学论述；回应质疑靠思想实验的再检验。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先接受实验事实再建模型；用对应原理检验新理论；让两种描述互补
- 不该用：不强求单一图像解释一切；不用经典图像硬套量子现象
- Negative prompt: `no single classical picture for quantum phenomena, no model without spectral evidence, no forced choice between complementary descriptions`

## (7) 测试提示词示例（现代问题：怎样向中学生解释量子纠缠？）

- Prompt: `In the style of Niels Bohr, explain quantum entanglement to a school student: show two complementary descriptions, say which experiment reveals each, and admit where ordinary language fails`
- 中文对照：玻尔风格，向中学生解释量子纠缠：展示两种互补的描述，说明哪种实验揭示哪一种，并承认日常语言在哪里失效。
- Negative: `no single classical picture for quantum phenomena, no model without spectral evidence, no forced choice between complementary descriptions`
- 检验点：是否给出两种互补描述；是否说明各自的实验条件；是否承认语言的限度。
