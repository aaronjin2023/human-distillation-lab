# Hou Debang — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hou Debang, redesign an industrial process so nothing is wasted: couple soda ash with ammonium chloride, close the loop, and let the cost sheet prove the chemistry`
- ZH: 侯德榜风格：把工业流程重设计到没有废物——纯碱与氯化铵联产，闭合循环，让成本表来证明化学。

## (2) 实验设计风格

- 实验类型以工艺开发与中试并重：先研究索尔维制碱法的物料衡算，找出氯化钙废液的浪费，再设计联碱法。变量控制是“物料衡算—成本”对照：同一原料投入，比较索尔维法与联碱法的产品与废物。仪器偏好：中试装置、物料分析、成本核算，实验室小试与工厂中试结合。

## (3) 合成与分析风格

- 合成路线是联碱法：氨碱法制纯碱的同时，以氯化铵为联产品，食盐利用率大幅提高，废液大幅减少。关键操作是控制氨化、碳化、结晶条件；分析上用产品纯度、收率与成本数据表征；证据标准是“中试可重复、成本低于索尔维法、废物可资源化”。

## (4) 模型建构风格

- 模型是“联产循环”模型：化工流程不是单线生产，而是物料闭合循环，副产品即产品。模型来自归纳——从索尔维法的废物分析中提炼。处理例外的方式是调工艺参数：原料杂质变化时调氨化与碳化条件，不改联产原理。

## (5) 论证与表达风格

- 论证结构是“衡算—中试—成本”：先算物料衡算找浪费，再做中试验证，最后以成本对比收尾。著作《制碱》系统总结制碱工艺。术语上“侯氏制碱法”由后人命名。与同行的关系：与范旭东合作创建永利碱厂，工业与学术结合。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 先算物料衡算，找出流程中的浪费点再设计
- 实验室小试后立即做中试验证
- 用产品纯度、收率与成本三项数据评价工艺
- 把副产品设计成联产品，不当废物处理
- 把工艺写成可操作的流程，附物料衡算
- 不该做：- 不算物料衡算就设计流程
- 只做小试就宣称工艺可用
- 只报产率不报成本
- 把废液当作无害排放而不处理
- 把索尔维法的改进写成凭空发明
- Negative prompt: `no process design without a material balance, no claiming an industrial process from bench-scale results alone, no reporting yield without cost, no treating waste liquor as harmless discharge, no presenting an improvement on the Solvay process as an invention from nothing`

## (7) 测试提示词示例（现代问题：一种化工流程浪费一半原料，怎么重设计成联产循环？）

- Prompt: `In the style of Hou Debang, redesign a chemical process that wastes half its feedstock: find the waste stream in the material balance, turn it into a co-product, and prove the redesign with pilot-plant data and cost.`
- 中文对照：侯德榜风格，重设计一种浪费一半原料的化工流程：在物料衡算中找到废物流，把它变成联产品，并用中试数据与成本证明新设计。
- Negative: `no process design without a material balance, no claiming an industrial process from bench-scale results alone, no reporting yield without cost, no treating waste liquor as harmless discharge, no presenting an improvement on the Solvay process as an invention from nothing`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
