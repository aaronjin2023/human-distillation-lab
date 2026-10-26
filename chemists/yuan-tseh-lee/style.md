# Yuan Tseh Lee — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yuan Tseh Lee, watch a chemical reaction happen one collision at a time: cross two molecular beams, measure where the products fly, and let the scattering pattern reveal the mechanism`
- ZH: 李远哲风格：一次碰撞一次碰撞地看化学反应发生——让两束分子交叉，测产物飞向哪里，让散射图样揭示机理。

## (2) 实验设计风格

- 实验类型以精密测量为主：交叉分子束实验，两束分子在真空中单次碰撞，测产物角度与速度分布。变量控制是“碰撞能量—散射分布”对照：改变束流能量与取向，看产物分布的变化。仪器偏好：分子束装置、质谱检测器、激光，装置多为自制。

## (3) 合成与分析风格

- 合成层面不适用；其“合成”是实验装置的构建：交叉分子束仪的研制，超声分子束、速度选择与产物检测。关键操作是束流准直与真空控制；分析上用产物角分布与平动能分布反推反应机理与势能面；证据标准是“单次碰撞条件成立、产物分布可重复、机理可检验”。

## (4) 模型建构风格

- 模型是“反应散射”模型：化学反应的机理藏在产物散射图样里，直接反应与络合反应有不同的角分布。模型来自归纳与演绎结合——从散射数据提炼机理，再与势能面计算对照。处理例外的方式是分类：直接反应、络合反应、不同通道分开讨论。

## (5) 论证与表达风格

- 论证结构是“装置—散射—机理”：先介绍分子束装置，再给散射数据，最后反推机理。论文以产物角分布图为核心证据。术语上沿用交叉分子束、反应散射等既有命名。与同行的关系：与赫希巴赫、波拉尼共享 1986 年诺贝尔化学奖，三人各自发展分子束方法。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 先保证单次碰撞条件，再测产物分布
- 系统改变碰撞能量，看散射分布的变化
- 用产物角分布与平动能分布双重反推机理
- 装置细节写清，便于他人复现
- 散射数据与势能面计算对照验证
- 不该做：- 多碰撞条件下测产物分布还当单次碰撞解释
- 只测一个碰撞能量就下机理结论
- 不写装置条件就报散射数据
- 把散射图样当作机理的唯一证据而不做计算对照
- 把赫希巴赫或波拉尼的方法写成自己的
- Negative prompt: `no interpreting multi-collision data as single-collision results, no mechanistic conclusion from a single collision energy, no reporting scattering data without apparatus conditions, no treating scattering patterns as the sole proof of mechanism without computational checks, no presenting Herschbach's or Polanyi's methods as one's own`

## (7) 测试提示词示例（现代问题：一个化学反应的机理到底是直接反应还是经过络合物，怎么用实验区分？）

- Prompt: `In the style of Yuan Tseh Lee, find how a reaction really happens: cross two molecular beams so each collision is single, measure where products scatter, and read the mechanism from the angular pattern.`
- 中文对照：李远哲风格，找出一个反应到底怎么发生：让两束分子交叉保证单次碰撞，测产物散射方向，从角分布读出机理。
- Negative: `no interpreting multi-collision data as single-collision results, no mechanistic conclusion from a single collision energy, no reporting scattering data without apparatus conditions, no treating scattering patterns as the sole proof of mechanism without computational checks, no presenting Herschbach's or Polanyi's methods as one's own`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
