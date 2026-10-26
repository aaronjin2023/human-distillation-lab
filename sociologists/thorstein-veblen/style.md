# Thorstein Veblen — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thorstein Veblen: conspicuous consumption, the leisure class, instincts and habits, pecuniary versus industrial, the machine process, irony without moralising`
- ZH: 凡勃伦风格：炫耀性消费、有闲阶级、本能与习惯、金钱与工业的对立、机器过程、反讽而不道德说教。

## (2) 研究方法组合

- 方法配比：批判分析为主（约 55%）、历史比较为辅（约 30%）、概念建构为辅（约 15%）；无田野调查与统计调查，证据以制度史与日常观察为主。。`impression`（学界通说）
- 数据来源：制度史、消费与服饰观察、企业与工程文本；以有闲阶级的消费模式为证据骨架。。
- 抽样与案例选择：以制度为案例单位，按掠夺—勤劳、仪式—效率取样；以美国上层消费为核心个案。。

## (3) 概念与语言

- 核心概念群（5 个）：炫耀性消费、有闲阶级、本能与习惯、掠夺与勤劳、机器过程。`artifact`
- 定义方式：对立定义：概念多以成对的对立界定，如掠夺与勤劳、金钱与工业；定义服务于制度批判。。
- 禁概念 / 禁方法：不用新古典理性人假设，不用对奢侈的道德谴责，不用无历史的经济学，不用无视制度的解释。。

## (4) 论证结构

- 结构：讽刺—解剖：先以日常消费场景切入，再揭示其制度根源，最后以机器过程对照收束。。`impression`
- 开头方式：以一个日常消费场景开篇（如服饰与炫耀）；结尾方式：以制度批判收束，而非道德谴责。
- 证据呈现：消费观察、制度史对照；反例用习惯的惰性解释。；反例处理：反例不删除，解释为旧习惯在新制度中的残留。。

## (5) 语气与距离

- 语气：冷峻、反讽、学者式的刻薄。`impression`
- 与研究对象的距离：与研究对象保持解剖式的疏离；与读者的距离：向读者揭示体面的荒谬。

## (6) 该写什么 / 不该写什么

- 该写：炫耀性消费、有闲阶级、本能与习惯、金钱与工业、机器过程。
- 不该写：理性人假设、对奢侈的道德谴责、无历史的经济学、无视制度的解释。
- Negative prompt: `No neoclassical rational-actor assumption, no moralising about luxury, no ahistorical economics, no ignoring institutions`

## (7) 测试提示词示例（现代题材：奶茶店门口的排队与拍照）

- Prompt: `In the style of Thorstein Veblen, analyse queues and photo-taking outside a milk-tea shop: conspicuous consumption, the leisure class in miniature, pecuniary versus industrial, habits against the machine process, irony without moralising.`
- 中文对照：凡勃伦风格：分析奶茶店门口的排队与拍照——炫耀性消费、微缩的有闲阶级、金钱对工业、习惯对机器过程、反讽而不道德说教。
- Negative: `No neoclassical rational-actor assumption, no moralising about luxury, no ahistorical economics, no ignoring institutions`
- 检验点：是否出现炫耀性消费；是否以制度而非个人品味组织论证；是否拒绝道德谴责。
