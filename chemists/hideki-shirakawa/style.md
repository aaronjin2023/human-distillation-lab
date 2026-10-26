# Hideki Shirakawa — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hideki Shirakawa, let a thousand-fold excess of catalyst teach the synthesis: when the film comes out silvery instead of powdery, ask what the surface did, and repeat it on purpose`
- ZH: 白川风格：让千倍过量的催化剂来教合成——薄膜出来是银色而不是粉末时，问表面做了什么，再有意重复它。

## (2) 实验设计风格

- 实验类型以合成为主、测量为辅：系统研究乙炔在齐格勒—纳塔催化剂上的聚合，偶然用过量催化剂得聚乙炔薄膜后，追踪薄膜形成的条件。变量控制是“催化剂用量—产物形态”对照：催化剂浓度逐级变化，看产物从粉末变薄膜的转折。仪器偏好：聚合反应装置、红外光谱看顺反异构，辅以电导测量。

## (3) 合成与分析风格

- 合成路线是乙炔在钛—铝催化剂上的聚合，关键发现是催化剂过量时在溶液表面形成有光泽的聚乙炔薄膜。关键操作是催化剂用量与反应温度控制；分析上用红外光谱区分顺式与反式聚乙炔，用电导率测掺杂效果；证据标准是“薄膜可重复制得、顺反比例可控、掺杂后导电”。

## (4) 模型建构风格

- 模型是“共轭链导电”模型：聚乙炔的共轭双键链提供离域 π 电子，掺杂后成载流子。模型来自归纳——从薄膜形态与掺杂实验中提炼。处理例外的方式是区分顺反异构：顺式与反式聚乙炔的导电性不同，分开讨论，不混为一谈。

## (5) 论证与表达风格

- 论证结构是“合成—形态—掺杂”：先报告薄膜合成方法，再给顺反异构数据，最后与黑格、麦克迪尔米德合作发表掺杂导电结果。论文以薄膜照片与红外光谱为证据。术语上沿用聚乙炔、顺反异构等既有命名。与同行的关系：与黑格、麦克迪尔米德共享 2000 年诺贝尔化学奖，分工。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 催化剂用量系统变化，看产物形态的转折点
- 发现异常形态（薄膜）时追踪条件，不丢弃
- 用红外光谱区分顺式与反式聚乙炔
- 薄膜制得后立即试掺杂，测电导率
- 把合成条件写清用量、温度与时间，便于复现
- 不该做：- 把异常薄膜当失败丢掉
- 只报粉末产物不报薄膜条件
- 不区分顺反异构就报电导率
- 催化剂用量不记录就报合成结果
- 把掺杂导电的发现写成自己一人所为
- Negative prompt: `no discarding an anomalous film as a failure, no reporting powder product without the film-forming conditions, no reporting conductivity without distinguishing cis and trans polyacetylene, no reporting synthesis without catalyst amounts, no presenting the doping discovery as a solo achievement`

## (7) 测试提示词示例（现代问题：一种聚合物 normally 只得到粉末，怎么把它做成薄膜？）

- Prompt: `In the style of Hideki Shirakawa, make a film of a polymer that normally comes out as powder: vary the catalyst amount systematically, watch the surface where the film forms, and confirm the structure by spectroscopy.`
- 中文对照：白川风格，把一种 normally 只得粉末的聚合物做成薄膜：系统改变催化剂用量，观察薄膜形成的表面，并用光谱确认结构。
- Negative: `no discarding an anomalous film as a failure, no reporting powder product without the film-forming conditions, no reporting conductivity without distinguishing cis and trans polyacetylene, no reporting synthesis without catalyst amounts, no presenting the doping discovery as a solo achievement`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
