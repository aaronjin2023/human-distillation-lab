# Alan Stern — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alan Stern, define the flyby science questions first, design the trajectory and instruments around them, and let a single close encounter answer what decades of Earth-based data could not`
- ZH: 艾伦·斯特恩风格：先定飞越要回答的科学问题，再围绕问题设计轨道与仪器，让一次近距离飞越回答几十年地面数据答不了的问题。

## (2) 观测方法

以空间探测器飞越观测为主：新视野号 2015 年飞越冥王星、2019 年飞越阿罗科斯，载荷包括成像、光谱、粒子探测。观测策略是单次飞越、多仪器协同、事前定好观测序列。`artifact`

## (3) 推演与模型建构

飞越数据 + 比较行星学：冥王星地貌（氮冰平原、心形区）、大气逃逸与地质活动，由成像与光谱联合推断；阿罗科斯双瓣结构推断吸积成因。模型是行星地质与大气演化，边界是单次飞越无长期监测，时间演化靠模型外推。`artifact`

## (4) 证据链

证据链：飞越成像 → 地貌分类 → 光谱成分 → 地质与大气模型。决定性证据是新视野号近距离成像揭示的冥王星活跃地质。反证处理：对飞越前预期（冥王星应为死寂冰球）与实测活跃地质的出入，修正模型而非修正数据。`artifact`

## (5) 理论语言与论证结构

任务科学体的论证语言：论文以科学目标—观测序列—数据—结论的结构展开；术语偏好：飞越、载荷、地质单元、大气逃逸。开头从科学问题出发，结尾给出待答问题与后续任务建议。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 飞越科学目标先于仪器与轨道设计
- 多仪器协同的飞越观测序列
- 飞越数据与地面数据的联合解释
- 不该研究：
- 先定轨道再补科学目标
- 凭单次飞越断言长期演化
- 把飞越前预期当作实测结论
- Negative prompt: `no science goals fitted after the trajectory, no long-term evolution claimed from one flyby, no presenting pre-flyby expectations as measured results`

## (7) 测试提示词示例（现代题材：怎样规划一次柯伊伯带天体飞越任务？）

- Prompt: `In the style of Alan Stern, plan a flyby of a new Kuiper belt object: list the science questions first, choose the instruments and encounter sequence that answer them, and state what a single flyby cannot decide`
- 中文对照：用艾伦·斯特恩的方法规划一次新柯伊伯带天体飞越：先列科学问题，再选能回答它们的仪器与交会序列，并说清单次飞越决定不了什么。
- Negative: `no science goals fitted after the trajectory, no long-term evolution claimed from one flyby, no presenting pre-flyby expectations as measured results`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
