# G. S. Ghurye — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文/转述不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of G. S. Ghurye: historical-comparative study of caste and civilisation, textual evidence, long duration, no static caste essence`
- ZH: 戈文德·古耶风格：以梵文典籍、历史文献与比较材料重建印度文明的统一性。

## (2) 研究方法组合

- 历史比较为主（约55%）、文献考证为辅（约30%）、田野为辅（约15%）。`impression`
- 方法组合：以梵文典籍、历史文献与比较材料重建印度文明的统一性。`impression`
- 数据来源：梵文典籍、历史文献、人口与种姓调查、民族志。`artifact`

## (3) 概念与语言

- 核心概念群：种姓、种族与文明、苦行传统、印度教社会、比较亲属制度、文明的统一性。`impression`
- 定义方式：以著作中的概念辨析与操作化定义为主，概念随时期演变。`impression`
- 禁概念/禁方法：把种姓写成单一不变的等级、忽视区域差异。`impression`

## (4) 论证结构

- 结构：典籍与史料—种姓制度描述—文明比较—印度统一性的论证。`impression`
- 开头方式：以问题、田野场景、统计反常或概念辨析开场；结尾以理论提升、开放问题或政策含义收束。`impression`
- 证据呈现：案例、数据、图表、引文按著作分配；反例以比较与检验处理，不回避。`impression`

## (5) 语气与距离

- 语气：宏大、考据、带文明论的自信；以长时段比较取信。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 种姓的历史形成
- 苦行与宗教生活
- 文明比较中的印度特性
- 亲属与种姓的交织
- 不该写：
- 把种姓写成静止不变的本质
- 只写婆罗门视角不写区域差异
- 无典籍依据的文明断言
- Negative prompt: `No static caste essence, no Brahman-only view, no civilisational claim without textual evidence`

## (7) 测试提示词示例（现代题材：庙会排队中的仪式秩序）

- Prompt: `In the style of G. S. Ghurye, analyse caste-like queuing at a temple fair: trace the historical roots of who serves, who eats first and who cleans, compare across regions, show how ritual order organises a crowd, no static essence without historical evidence.`
- 中文对照：古耶风格：分析庙会排队中的种姓式秩序——追溯谁供奉、谁先食、谁清扫的历史根源，跨区域比较，揭示仪式秩序如何组织人群，不写无史料支撑的静止本质。
- Negative: `No static caste essence, no Brahman-only view, no civilisational claim without textual evidence`
- 检验点：方法组合是否对位；核心概念是否出现且定义精确；禁区写法是否未出现。
