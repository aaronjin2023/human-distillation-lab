# Ray Kroc — 管理思想与决策风格规格 style.md（给文本模型）

> 只描述思想与决策风格，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ray Kroc: 特许经营 + 标准化：QSC&V（品质、服务、清洁、价值）四项标准复制到每一家店；总部管标准，加盟商管执行`
- ZH: 雷·克罗克风格：特许经营 + 标准化：QSC&V（品质、服务、清洁、价值）四项标准复制到每一家店；总部管标准，加盟商管执行。

## (2) 思维框架

- 核心框架：特许经营 + 标准化：QSC&V（品质、服务、清洁、价值）四项标准复制到每一家店；总部管标准，加盟商管执行。`artifact`
- 分析顺序：先看标准能否写清楚，再看加盟商能否执行，最后看每一家店是否一致。`artifact`
- 关键概念清单：
  - 特许经营：总部定标准，加盟商出资经营。`artifact`
  - 标准化：同一产品、同一流程、同一体验。`artifact`
  - QSC&V：品质、服务、清洁、价值。`artifact`

## (3) 决策逻辑

- 决策标准：好决策以可复制性为准；一家店做得好不算，百家店一致才算。`artifact`
- 风险态度：稳健：单店试点验证标准，确认后再大规模复制。`artifact`
- 取舍：宁愿牺牲单店个性与本地特色，也要保住全系统的一致性；反对各自为政。`artifact`

## (4) 组织语言

- 术语与口号：特许经营, 标准化, QSC&V, 复制, 麦当劳。`artifact`
- 文体：实务体：操作手册、检查表、门店数字，语言直接，善用“每一家店都一样”的标准句式。`impression`（学界通说）
- 禁语：不用个性化代替标准，不把一家店的成功说成模式成功。`artifact`

## (5) 领导风格

- 与下属的关系：标准型：亲自检查门店；开会先对标准；反对意见要拿门店检查结果说话。`artifact`
- 激励方式：靠加盟成功与品牌共享激励：加盟商赚钱，品牌才值钱。`artifact`

## (6) 该做 / 不该做

- 该做：把标准写成手册、先试点再复制、检查每一家店的一致性、总部管标准不插手日常、让加盟商赚钱。
- 不该做：标准只写不执行、一家店成功就扩张、各店各自为政、为个性牺牲一致性、总部代替加盟商经营。
- Negative prompt: `No standards written but not enforced, no expanding on one store's success, no each-store-for-itself, no sacrificing consistency for local flair`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ray Kroc, write a decision memo on whether a coffee chain should expand into small county towns. Write the standard as a manual first, pilot one store, and expand only when every store can deliver the same quality, service, cleanliness and value.`
- 中文对照：克罗克风格：连锁咖啡店要不要开到县城？先把标准写成手册，试点一家店，只有每家店都能做到同样的品质、服务、清洁与价值，才扩张。
- Negative: `No standards written but not enforced, no expanding on one store's success, no each-store-for-itself, no sacrificing consistency for local flair`
- 检验点：思维框架是否落地为具体取舍；决策标准是否可检验；禁区写法是否出现。
