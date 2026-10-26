# Werner Heisenberg — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Werner Heisenberg, keep only what can be measured: throw away unobservable orbits, arrange the observable numbers in tables, and let their multiplication rules become the theory`
- ZH: 海森堡风格：只保留可测量的东西——扔掉看不见的轨道，把可观测的数排成表，让它们的乘法规则成为理论。

## (2) 提问方式

从可观测出发：电子轨道看不见，能看见的只有光谱频率与强度；理论只能用看得见的东西搭建。`artifact`

## (3) 推理习惯

操作主义演绎：只用可观测量建理论；矩阵乘法不对易性推出不确定性；对直观图像保持怀疑。`artifact`

## (4) 数学化程度与思想实验

高度数学化；核心工具是矩阵代数；思想实验是显微镜（伽马射线显微镜）论证。`artifact`

## (5) 论证语言

论文体：1925 年《运动学与力学关系的量子论重新解释》以可观测量开篇；1927 年不确定性论文用思想实验论证。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：只用可观测量建理论；让不对易性自己说话；用思想实验检验测量极限
- 不该用：不画看不见的轨道；不把测量扰动说成全部故事（后世有更精确表述）
- Negative prompt: `no unobservable orbits in the theory, no classical picture smuggled back in, no uncertainty without the non-commuting algebra`

## (7) 测试提示词示例（现代问题：怎样判断一次测量能精确到什么程度？）

- Prompt: `In the style of Werner Heisenberg, judge how precisely a measurement can be made: list what is actually observable, find the pair that does not commute, and derive the limit before building the apparatus`
- 中文对照：海森堡风格，判断一次测量能精确到什么程度：列出实际可观测的东西，找出不对易的那一对，在造仪器之前先推导极限。
- Negative: `no unobservable orbits in the theory, no classical picture smuggled back in, no uncertainty without the non-commuting algebra`
- 检验点：是否先列可观测量；是否找到不对易对；是否由代数推出极限。
