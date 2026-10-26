# William Julius Wilson — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文/转述不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Julius Wilson: structural analysis of concentrated urban poverty, jobs and social isolation, no culture-of-poverty explanation`
- ZH: 威廉·朱利叶斯·威尔逊风格：以芝加哥内城调查为底：贫困是结构，不是文化。

## (2) 研究方法组合

- 统计与调查为主（约55%）、田野访谈为辅（约25%）、历史比较为辅（约20%）。`impression`
- 方法组合：以芝加哥内城调查为底：贫困是结构，不是文化。`impression`
- 数据来源：人口普查、调查问卷、深度访谈、就业统计。`artifact`

## (3) 概念与语言

- 核心概念群：真正处于不利地位者、集中贫困、工作消失、种族意义的衰落、社会隔离、城市贫困。`impression`
- 定义方式：以著作中的概念辨析与操作化定义为主，概念随时期演变。`impression`
- 禁概念/禁方法：贫困文化论、只谈种族不谈阶级与工作。`impression`

## (4) 论证结构

- 结构：贫困数据—工作消失的机制—社会隔离—政策含义。`impression`
- 开头方式：以问题、田野场景、统计反常或概念辨析开场；结尾以理论提升、开放问题或政策含义收束。`impression`
- 证据呈现：案例、数据、图表、引文按著作分配；反例以比较与检验处理，不回避。`impression`

## (5) 语气与距离

- 语气：冷静、数据驱动、带政策的紧迫感；以结构反驳文化解释。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 内城贫困的集中化
- 制造业岗位消失的后果
- 社会隔离与网络断裂
- 种族与阶级的结构分析
- 不该写：
- 把贫困写成文化缺陷
- 只谈种族不谈工作与阶级
- 无数据的贫困印象
- Negative prompt: `No culture-of-poverty explanation, no race without class and jobs, no poverty impression without data`

## (7) 测试提示词示例（现代题材：失去工厂工作的外卖骑手）

- Prompt: `In the style of William Julius Wilson, analyse delivery riders who lost factory jobs: census and survey data first, show how job disappearance concentrates disadvantage, interview the riders, no culture-of-poverty explanation without structural evidence.`
- 中文对照：威尔逊风格：分析失去工厂工作的外卖骑手——先看人口普查与调查数据，揭示工作消失如何集中不利处境，再访谈骑手；不写没有结构证据的贫困文化论。
- Negative: `No culture-of-poverty explanation, no race without class and jobs, no poverty impression without data`
- 检验点：方法组合是否对位；核心概念是否出现且定义精确；禁区写法是否未出现。
