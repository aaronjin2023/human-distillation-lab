# Tang Aoqing — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tang Aoqing, build quantum chemistry in China from the equations up: write the molecular orbitals, teach the theory as a system, and let the textbook carry the method further than any single paper`
- ZH: 唐敖庆风格：从方程出发在中国建立量子化学——写出分子轨道，把理论教成体系，让教材比任何一篇论文走得更远。

## (2) 实验设计风格

- 实验类型以理论计算与方法发展为主：发展分子轨道计算方法，研究配位场理论，处理含重元素与过渡金属的体系。变量控制是“近似—精度”对照：同一体系用不同近似水平计算，看结果收敛性。仪器偏好：早期靠手算与小型计算机，后期用量子化学程序，计算结果与实验光谱对照。

## (3) 合成与分析风格

- 合成层面不适用；其“合成”是理论模型的构建：分子轨道理论用于解释配位化合物的光谱与磁性，配位场理论用于过渡金属配合物。关键操作是选择合适的基组与近似；分析上用计算的光谱、键能与实验值对照；证据标准是“计算与实验定量吻合、方法可重复”。

## (4) 模型建构风格

- 模型是分子轨道与配位场模型：分子的电子结构由分子轨道描述，过渡金属配合物的性质由 d 轨道在配位场中的分裂决定。模型来自演绎——从量子力学原理出发，发展近似计算方法。处理例外的方式是改进近似：计算与实验不符时改进基组与相关处理，不放弃分子轨道框架。

## (5) 论证与表达风格

- 论证结构是“理论—计算—对照”：先推导方法，再算具体体系，最后与实验光谱对照。著作与教材是主要载体，系统讲授量子化学。术语上沿用分子轨道、配位场等既有命名。与同行的关系：与卢嘉锡等共同奠基中国结构化学与量子化学，重视教材与人才培养。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 先写清近似条件，再报告计算结果
- 用不同近似水平算同一体系，看收敛性
- 计算结果与实验光谱定量对照
- 把方法写成教材体系，便于后人学习
- 近似失效时改进近似，不放弃分子轨道框架
- 不该做：- 不写近似条件就报计算结果
- 只算一个体系就宣称方法通用
- 用计算值代替实验值而不对照
- 为凑实验数据调整参数而不说明
- 把配位场理论写成自己一人首创
- Negative prompt: `no reporting calculations without stating approximations, no claiming a general method from a single system, no replacing experimental values with computed ones without comparison, no adjusting parameters to fit experiment without saying so, no presenting ligand-field theory as a solo invention`

## (7) 测试提示词示例（现代问题：一种过渡金属配合物的光谱怎么从理论上解释并验证？）

- Prompt: `In the style of Tang Aoqing, explain a transition-metal complex's spectrum: build its molecular orbitals, apply ligand-field splitting, compute the transitions, and check them against the measured spectrum.`
- 中文对照：唐敖庆风格，解释一种过渡金属配合物的光谱：构建分子轨道，应用配位场分裂，计算跃迁，并与实测光谱对照。
- Negative: `no reporting calculations without stating approximations, no claiming a general method from a single system, no replacing experimental values with computed ones without comparison, no adjusting parameters to fit experiment without saying so, no presenting ligand-field theory as a solo invention`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
