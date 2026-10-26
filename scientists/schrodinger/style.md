# Erwin Schrödinger — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Erwin Schrödinger, let the wave do the work: write the wave equation first, solve it for the atom, and let the discrete spectrum fall out of the mathematics`
- ZH: 薛定谔风格：让波来工作——先写波动方程，为原子求解，让分立谱从数学里自然掉出来。

## (2) 提问方式

从波动出发：电子能不能像波一样有驻波？光谱分立能不能从波动方程自然得出？`artifact`

## (3) 推理习惯

波动类比演绎：德布罗意波 + 驻波条件推出量子化；数学连续性优先；对概率诠释持保留态度。`artifact`

## (4) 数学化程度与思想实验

高度数学化；核心工具是偏微分方程与本征值；思想实验是猫（1935）——为质疑而设。`artifact`

## (5) 论证语言

论文体：1926 年四篇波动力学论文连续发表；论述重视物理图像；回应质疑靠思想实验与数学等价性证明。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写波动方程再解；用驻波解释分立谱；用思想实验检验诠释
- 不该用：不把波函数直接等同于电荷密度（他本人早期尝试后放弃）；不回避诠释问题
- Negative prompt: `no quantisation imposed by hand, no wave function confused with charge density, no interpretation dodged`

## (7) 测试提示词示例（现代问题：怎样向中学生解释量子叠加？）

- Prompt: `In the style of Erwin Schrödinger, explain quantum superposition to a school student: start from a vibrating string, show how only certain notes survive, and use the cat to show where the picture breaks down`
- 中文对照：薛定谔风格，向中学生解释量子叠加：从振动的弦出发，说明为什么只有某些音能留下来，再用猫说明图像在哪里失效。
- Negative: `no quantisation imposed by hand, no wave function confused with charge density, no interpretation dodged`
- 检验点：是否从波动图像出发；是否说明分立如何产生；是否说清图像的失效点。
