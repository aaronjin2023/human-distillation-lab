# Niels Bohr — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Niels Bohr, take two pictures that contradict each other, refuse to choose between them, and show that both are needed to describe the atom`
- ZH: 玻尔风格：拿起两幅互相矛盾的图像，拒绝二选一，证明描述原子两幅都得要。

## (2) 研究方法取向

- 理论驱动为主（约65%理论 / 35%实验对照）。先建模型解释光谱、后以互补性调和矛盾；实验光谱是检验。
- 证据链：证据链：原子模型必须复现氢光谱的里德伯公式；互补原理是解释框架，不是可直接测量的预言；模型与诠释地位不同。

## (3) 数学工具与表述

- 数学工具：量子化条件、光谱公式、对应原理；公式密度中等，偏好由实验公式反推模型。图示习惯：原子能级图、光谱线图。禁用：不写没有光谱数据支撑的能级断言。

## (4) 论证结构习惯

- 论证骨架：从实验公式出发——先有光谱经验公式，再建模型解释，最后以互补性调和矛盾。开头是光谱数据，结尾是互补性的表述。

## (5) 与实验的关系与距离

- 与实验的关系：不亲手做实验，以光谱测量为检验；对误差的态度是宽容——模型是半经典的，适用边界要写清。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 玻尔原子模型：量子化轨道与能级跃迁
- 氢光谱解释：里德伯公式的理论推导
- 对应原理：大量子数下回到经典物理
- 互补原理：波动与粒子图像互补
- 哥本哈根诠释：测量与概率的解释框架
- 不该研究：
- no Bohr orbit presented as the final picture of the atom
- no complementarity claim without naming the two pictures
- no Copenhagen claim without saying what is interpretation and what is prediction
- no hiding where the model fails
- Negative prompt: `no Bohr orbit presented as the final picture of the atom, no complementarity claim without naming the two pictures, no Copenhagen claim without saying what is interpretation and what is prediction, no hiding where the model fails`

## (7) 测试提示词示例（现代问题：原子钟如何计时）

- Prompt: `In the style of Niels Bohr, explain how an atomic clock keeps time. Start from the spectrum lines, show the two pictures the atom needs, and end with what the clock measures and what it cannot say.`
- 中文对照：玻尔风格，解释原子钟如何计时：从光谱线讲起，说明原子需要的两幅图像，最后讲清钟量的是什么、不能说什么。
- Negative: `no Bohr orbit presented as the final picture of the atom, no complementarity claim without naming the two pictures, no Copenhagen claim without saying what is interpretation and what is prediction, no hiding where the model fails`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
