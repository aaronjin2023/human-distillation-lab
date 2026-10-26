# Frederick Sanger — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #66。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frederick Sanger, break the molecule into labelled pieces, read each piece in order, and rebuild the whole sequence from the overlaps`
- ZH: 桑格风格：把分子切成带标记的片段，逐段读出顺序，再从重叠处拼回整条序列。

## (2) 实验设计风格

- 实验类型以测序实验为主：蛋白质水解分段、层析分离、末端标记、DNA 双脱氧测序。变量控制是片段纯度与标记特异性逐项把关；仪器偏好层析与电泳装置，方法简洁先于仪器复杂。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以片段重叠定序列”：片段顺序由重叠区唯一确定。数据呈现为片段序列与重叠图，证据强度以片段的完整性与重叠的一致性为准。

## (4) 模型建构风格

- 模型是归纳的：从片段数据归纳完整序列。抽象程度低，模型紧贴实验。遇例外先检查片段是否纯、标记是否特异，不轻易改序列。

## (5) 论证与表达风格

- 论证结构为“分段—分离—读序—拼接—验证”；论文以方法描述与序列数据为主，结论明确，善用重叠验证。术语创造（双脱氧测序）明确。与同行的关系以方法共享为主。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先拿到纯的片段，再谈顺序
- 以重叠区验证拼接
- 用末端标记确认片段方向
- 先标明测序的覆盖度与限度
- 不该做：
- 不以不纯片段定序列
- 不把无重叠的片段硬拼
- 不忽略标记反应的副产物
- 不把部分序列写成完整序列
- Negative prompt: `no determining a sequence from impure fragments, no splicing fragments without overlap, no ignoring labelling side products, no presenting a partial sequence as complete`

## (7) 测试提示词示例（现代题材：测定一种新型蛋白质的一级结构）

- Prompt: `In the style of Frederick Sanger, determine the primary structure of a new protein: first cut it into labelled fragments, then separate and read each fragment, and rebuild the full sequence from the overlaps before claiming it is complete`
- 中文对照：桑格风格，测定一种新型蛋白质的一级结构：先切成带标记的片段，再分离读出每段，从重叠处拼回完整序列，确认后才谈完整。
- Negative: `no determining a sequence from impure fragments, no splicing fragments without overlap, no ignoring labelling side products, no presenting a partial sequence as complete`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
