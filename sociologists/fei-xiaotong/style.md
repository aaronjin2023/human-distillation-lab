# Fei Xiaotong — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文/转述不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fei Xiaotong: village fieldwork first, differential mode of association, ritual order, concepts grown from the ground, no abstract model without fieldwork`
- ZH: 费孝通风格：以村庄为单位的社区研究：进村、住下、看全村的生活。

## (2) 研究方法组合

- 田野调查为主（约65%）、概念建构为辅（约25%）、历史比较为辅（约10%）；统计为辅证。`impression`
- 方法组合：以村庄为单位的社区研究：进村、住下、看全村的生活。`impression`
- 数据来源：参与观察、访谈、家谱、土地与赋税档案、村庄经济账目。`artifact`

## (3) 概念与语言

- 核心概念群：差序格局、乡土社会、礼治秩序、长老统治、血缘与地缘、社区研究。`impression`
- 定义方式：以著作中的概念辨析与操作化定义为主，概念随时期演变。`impression`
- 禁概念/禁方法：脱离田野的抽象模型、西方概念的生搬硬套、礼治即落后。`impression`

## (4) 论证结构

- 结构：田野场景—村庄全貌—概念提炼（差序格局）—中西比较—理论提升。`impression`
- 开头方式：以问题、田野场景、统计反常或概念辨析开场；结尾以理论提升、开放问题或政策含义收束。`impression`
- 证据呈现：案例、数据、图表、引文按著作分配；反例以比较与检验处理，不回避。`impression`

## (5) 语气与距离

- 语气：平实、克制、同情而疏离；用田野细节说话，不煽情。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 村庄的亲属、土地与权力关系
- 差序格局的推衍
- 礼治与法治的对照
- 田野细节支撑的概念
- 不该写：
- 脱离田野的抽象模型
- 把乡土写成静止落后的本质
- 用西方团体格局直接套中国村庄
- 无田野依据的政策断言
- Negative prompt: `No abstract model without fieldwork, no Western concept imposed on the village, no static backward countryside, no policy claim without fieldwork`

## (7) 测试提示词示例（现代题材：地铁口共享单车的停放秩序）

- Prompt: `In the style of Fei Xiaotong, analyse a shared-bike parking pile outside a subway station as a village-like order: concentric circles of users, keepers and officials, ritual-like queuing rules, differential association. Fieldwork detail first, concepts from the ground, no abstract model without fieldwork.`
- 中文对照：费孝通风格：把地铁口的共享单车堆放写成村庄式秩序——使用者、管理员与官方的差序圈子、礼俗般的停放规则；先写田野细节，再从地面提炼概念，不写脱离田野的抽象模型。
- Negative: `No abstract model without fieldwork, no Western concept imposed on the village, no static backward countryside, no policy claim without fieldwork`
- 检验点：方法组合是否对位；核心概念是否出现且定义精确；禁区写法是否未出现。
