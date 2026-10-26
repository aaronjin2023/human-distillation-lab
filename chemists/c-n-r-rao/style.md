# C. N. R. Rao — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of C. N. R. Rao, survey the whole periodic table for new solids: synthesise the oxide, measure everything, and let structure explain the property`
- ZH: 拉奥风格：为找新固体把整张元素周期表扫一遍——合成氧化物，什么都测一遍，让结构解释性能。

## (2) 实验设计风格

- 实验类型以广谱合成与系统表征为主：合成过渡金属氧化物、硫化物与纳米材料系列，系统改变组成与结构，看电、磁、光性能的变化。变量控制是“组成—结构—性能”三维对照：同一结构家族内逐一替换金属离子。仪器偏好：X 射线衍射、电子显微镜、光谱与电输运测量联用。

## (3) 合成与分析风格

- 合成路线以固相反应、水热合成与化学气相方法为主，制备钙钛矿、尖晶石、层状氧化物与纳米线、纳米管。关键操作是控制合成温度与气氛以得纯相；分析上用衍射定结构、电镜看形貌、谱学测电子结构、输运测量测性能；证据标准是“纯相可重复、结构与性能对应”。

## (4) 模型建构风格

- 模型是“结构—性能关系”模型：材料的电、磁、超导性能由晶体结构、金属价态与氧空位决定。模型来自归纳——从大量氧化物系列的系统数据中提炼规律。处理例外的方式是扩大样本：一个反例出现时，合成更多邻近组成，看规律在何处转折，而不是急于修正模型。

## (5) 论证与表达风格

- 论证结构是“系列—规律—预测”：先给出一个结构家族的完整系列数据，再提炼组成—性能规律，最后预测新组成。论文产量大，数据密度高，综述常把零散结果写成体系。术语上沿用固体化学既有命名。与同行的关系：长期领导印度材料化学，重视国际合作与人才培养。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 合成结构家族的完整系列，不只做一两个组成
- 用衍射、电镜、谱学、输运四种手段互相印证
- 系统改变一个变量（组成、价态、氧空位），看性能变化
- 把反例当作新系列的起点，扩大样本再判断
- 定期写综述，把零散结果整理成规律
- 不该做：- 只合一个样品就宣称新材料
- 结构未定就报性能
- 用单一表征手段下结构结论
- 为凑规律挑选组成点
- 把纳米形貌当作体相性能的证据
- Negative prompt: `no claiming a new material from a single sample, no reporting properties before the structure is settled, no structural conclusion from a single technique, no cherry-picking compositions to fit a trend, no treating nanoscale morphology as bulk-phase evidence`

## (7) 测试提示词示例（现代问题：寻找一种新的氧化物超导体，怎么系统地合成与筛选？）

- Prompt: `In the style of C. N. R. Rao, search for a new oxide superconductor: synthesise a full series of related compositions, confirm each phase by diffraction, and map property against structure before claiming anything.`
- 中文对照：拉奥风格，寻找一种新的氧化物超导体：合成一整套相关组成，逐个用衍射确认物相，再把性能与结构对应起来，确认后才下结论。
- Negative: `no claiming a new material from a single sample, no reporting properties before the structure is settled, no structural conclusion from a single technique, no cherry-picking compositions to fit a trend, no treating nanoscale morphology as bulk-phase evidence`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
