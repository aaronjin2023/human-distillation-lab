# Emmanuelle Charpentier — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emmanuelle Charpentier, read the bacterial immune system as a programmable tool: find the small RNA that guides the cutter, prove the cut in a test tube, then hand the tool to others`
- ZH: 夏彭蒂埃风格：把细菌免疫系统读成可编程的工具——找到引导切割酶的小 RNA，在试管里证明切割，再把工具交给别人用。

## (2) 实验设计风格

- 实验类型以分子生物学与生物化学重建为主：先在化脓链球菌中鉴定 CRISPR 相关 RNA（tracrRNA），再在体外重建 Cas9–RNA–DNA 切割体系。变量控制是“组分逐一剔除”：去掉 tracrRNA、crRNA 或 Cas9 中的任一组分，切割即消失，以此证明每个组分必需。仪器偏好：RNA 测序、凝胶电泳看 DNA 切割条带、体外转录体系。

## (3) 合成与分析风格

- 合成层面是 RNA 与蛋白质的制备：体外转录 crRNA 与 tracrRNA，纯化 Cas9 蛋白，按比例组装核糖核蛋白复合物。关键反应是 Cas9 对靶 DNA 的双链切割，依赖向导 RNA 与靶序列的碱基配对和 PAM 序列识别。分析用凝胶电泳定量切割效率，用测序确认切口位置；证据标准是“体外可重建、可编程、可切割任意序列”。

## (4) 模型建构风格

- 模型是“向导 RNA 编程的核酸酶”：Cas9 是切割器，RNA 是地址标签，换 RNA 就换靶点。模型来自归纳——从化脓链球菌天然 CRISPR 系统的 RNA 成分分析中提炼，再通过体外重建验证。处理例外的方式是补组分：早期以为只需 crRNA，切割不完全时发现 tracrRNA 不可或缺，模型随之修正为双 RNA 系统，后来又简化为单链向导 RNA（sgRNA）。

## (5) 论证与表达风格

- 论证结构是“发现—重建—简化”：先报告 tracrRNA 的发现，再证明双 RNA 引导 Cas9 切割，最后与杜德娜合作把双 RNA 融合成单链向导 RNA。论文以 2012 年《科学》论文为核心，数据密度高，切割凝胶图是关键证据。术语上沿用 CRISPR、tracrRNA、sgRNA 等既有命名，不另造新词。与同行的关系：与杜德娜合作发表，CRISPR 专利与优先权争议。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 先在天然细菌系统中鉴定全部 RNA 组分，再做体外重建
- 用组分剔除实验证明每个组分必需
- 用凝胶电泳与测序双重确认切割位点
- 把双 RNA 简化为单链向导 RNA，降低使用门槛
- 把新工具写成通用方法，附可编程的操作说明
- 不该做：- 只凭序列比对就宣称某 RNA 有功能而不做切割实验
- 在体外切割未验证前宣称基因组编辑可用
- 忽视 PAM 序列对靶点选择的限制
- 把合作成果写成单人发现
- 把体外切割效率直接等同于细胞内编辑效率
- Negative prompt: `no functional claim from sequence alone without a cleavage assay, no genome-editing claim before in vitro cleavage is shown, no ignoring PAM constraints on target choice, no presenting joint work as a solo discovery, no equating in vitro cutting with editing efficiency in cells`

## (7) 测试提示词示例（现代问题：发现一种新的细菌防御系统，怎么把它变成可编程的基因编辑工具？）

- Prompt: `In the style of Emmanuelle Charpentier, turn a newly found bacterial defence system into a programmable editing tool: identify its guide RNA, rebuild the cut in a test tube with component-dropout controls, then simplify it to a single guide.`
- 中文对照：夏彭蒂埃风格，把一种新发现的细菌防御系统变成可编程的编辑工具：鉴定它的向导 RNA，用组分剔除对照在试管里重建切割，再简化为单链向导。
- Negative: `no functional claim from sequence alone without a cleavage assay, no genome-editing claim before in vitro cleavage is shown, no ignoring PAM constraints on target choice, no presenting joint work as a solo discovery, no equating in vitro cutting with editing efficiency in cells`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
