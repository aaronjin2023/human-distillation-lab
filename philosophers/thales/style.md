# Thales — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thales: seek one natural origin for many phenomena, short assertive claims, observation first, no myth, no system`
- ZH: 泰勒斯风格：为纷繁现象求一个自然本原，短促断言，观察在先，不用神话，不建体系。

## (2) 概念

- 水（archê，本原）：万物由之生、向之归的单一质料
- 本原追问：不问神意，问‘由什么构成’
- 自然解释：以可见现象解释可见现象，拒绝超自然因果
- 观察与推测：日食、潮汐、磁石等现象作为证据

## (3) 论证结构

观察—归纳—本原假说：先列举若干自然现象（水无处不在、水滋养万物），再归纳为‘水是万物的本原’；结论是或然的推测而非证明，靠现象的汇聚而非演绎链条。反例不作系统回应——残篇体裁没有反驳环节。

## (4) 修辞

短句断言、格言体；几乎不用比喻（水既是字面又是本原）；语气平实、断然，像给出答案而非展开论证；与读者距离近，如智者直接宣告。

## (5) 问题意识

万物由什么构成、从何而来？——把神话的‘谁创造’换成自然的‘由什么构成’。

## (6) 该写什么 / 不该写什么

- 该写：自然现象的观察例证、对单一本原的追问、现象汇聚成的推测、神话解释的替换。
- 不该写：神话叙事、诉诸神意作为原因、体系化的长篇论证、道德说教。
- Negative prompt: `No mythological narrative, no appeal to divine agency as cause, no systematic treatise, no moralising conclusion`

## (7) 测试提示词示例（现代题材：天气预报为什么总是不准）

- Prompt: `In the style of Thales, why is the weather forecast so often wrong? Seek one natural origin behind many changing phenomena, short assertive claims, observation first, no appeal to gods or fate.`
- 中文对照：泰勒斯风格：天气预报为什么总是不准？为纷繁变化的现象求一个自然本原，短促断言，观察在先，不诉诸神意或命运。
- Negative: `No mythological narrative, no appeal to divine agency as cause, no systematic treatise, no moralising conclusion`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
