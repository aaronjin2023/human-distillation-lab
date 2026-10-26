# Lu Jiaxi — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lu Jiaxi, read a crystal structure as a chemical sentence: let the cluster geometry explain the bonding, and test the explanation by building a model of nitrogen fixation`
- ZH: 卢嘉锡风格：把晶体结构读成化学句子——让簇合物的几何解释成键，再用固氮模拟来检验这个解释。

## (2) 实验设计风格

- 实验类型以结构测定与模型构建并重：用 X 射线晶体学测定簇合物结构，再以结构为依据构建氮固定模拟体系。变量控制是“结构—成键—反应性”对照：同一簇合物家族内改变金属与配体，看结构与固氮活性的变化。仪器偏好：X 射线衍射仪、光谱，辅以理论计算。

## (3) 合成与分析风格

- 合成路线是簇合物的合成：多核金属簇合物（如铁、钼簇合物）的制备与结构测定，模拟固氮酶活性中心。关键操作是控制合成条件得单晶；分析上用衍射定结构、谱学测电子结构、反应实验测固氮模拟活性；证据标准是“结构可解析、模拟反应可重复”。

## (4) 模型建构风格

- 模型是“簇合物成键”模型：多核金属簇的成键由金属—金属键与桥联配体共同决定，簇结构决定其模拟固氮的能力。模型来自归纳——从系列簇合物结构数据中提炼。处理例外的方式是分类：不同核数的簇合物分开讨论，不强求统一成键图像。

## (5) 论证与表达风格

- 论证结构是“结构—成键—模拟”：先给晶体结构，再分析成键，最后以固氮模拟反应验证。论文以衍射结构图为核心证据。术语上沿用簇合物、结构化学等既有命名。与同行的关系：与唐敖庆等共同奠基中国结构化学，重视学科建设与人才培养。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 合成簇合物后先做单晶衍射定结构
- 用结构数据分析成键，不凭空推测
- 以固氮模拟反应检验结构解释
- 系统改变簇合物组成，看结构与活性的关系
- 把不同核数的簇合物分类讨论
- 不该做：- 结构未定就谈成键机理
- 只合一个簇合物就下普适结论
- 用模拟反应活性代替结构证据
- 忽视桥联配体对簇结构的影响
- 把固氮酶本身的研究写成自己的模拟工作
- Negative prompt: `no bonding mechanism without a solved structure, no general conclusion from a single cluster, no replacing structural evidence with model-reaction activity, no ignoring bridging-ligand effects on cluster structure, no presenting nitrogenase research itself as one's own modelling work`

## (7) 测试提示词示例（现代问题：怎么用合成的金属簇合物模拟固氮酶的工作？）

- Prompt: `In the style of Lu Jiaxi, test a model of nitrogen fixation: synthesise a metal cluster, solve its crystal structure, analyse the bonding, and check whether it can mimic the enzyme's chemistry.`
- 中文对照：卢嘉锡风格，检验一种固氮模型：合成金属簇合物，解析晶体结构，分析成键，再看它能否模拟固氮酶的化学。
- Negative: `no bonding mechanism without a solved structure, no general conclusion from a single cluster, no replacing structural evidence with model-reaction activity, no ignoring bridging-ligand effects on cluster structure, no presenting nitrogenase research itself as one's own modelling work`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
