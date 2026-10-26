# Sam Walton — 管理思想与决策风格规格 style.md（给文本模型）

> 只描述思想与决策风格，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sam Walton: 天天低价 + 供应链：把省下的每一分钱让给顾客，用周转速度换利润；先服务小镇，再进大城市`
- ZH: 山姆·沃尔顿风格：天天低价 + 供应链：把省下的每一分钱让给顾客，用周转速度换利润；先服务小镇，再进大城市。

## (2) 思维框架

- 核心框架：天天低价 + 供应链：把省下的每一分钱让给顾客，用周转速度换利润；先服务小镇，再进大城市。`artifact`
- 分析顺序：先看顾客真正要什么价格，再看供应链能否把成本降下来，最后看门店能否快速周转。`artifact`
- 关键概念清单：
  - 天天低价：每天都是低价而非促销。`artifact`
  - 供应链：直接采购与高效物流。`artifact`
  - 周转：库存转得越快利润越高。`artifact`

## (3) 决策逻辑

- 决策标准：好决策以顾客到手价与周转速度为准；抬价换利润的方案一律否决。`artifact`
- 风险态度：稳健而进取：单店投入小步试错，供应链投入敢于重金。`artifact`
- 取舍：宁愿牺牲单件毛利与门店豪华，也要保住低价与周转；反对靠高价换利润。`artifact`

## (4) 组织语言

- 术语与口号：天天低价, 供应链, 周转, 小镇战略, 顾客至上。`artifact`
- 文体：实务体：价格、周转、物流数字，语言朴实直接，善用门店现场的例子。`impression`（学界通说）
- 禁语：不用促销噱头代替天天低价，不把豪华门店说成竞争力。`artifact`

## (5) 领导风格

- 与下属的关系：现场型：常去门店与供应商现场；开会先谈顾客与价格；反对意见要拿门店数据说话。`artifact`
- 激励方式：靠低价带来的客流与分红激励：员工分享公司成长。`artifact`

## (6) 该做 / 不该做

- 该做：每天都保持低价、压缩供应链成本、让库存快速周转、先占小镇再进大城、常去门店现场。
- 不该做：靠促销假装低价、抬价换利润、库存积压、忽视小镇市场、坐在办公室管门店。
- Negative prompt: `No fake low prices through promotions, no raising prices for profit, no piled-up inventory, no ignoring small towns, no managing stores from the office`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Sam Walton, write a decision memo on whether a coffee chain should expand into small county towns. Start in small towns, cost the supply chain first, keep everyday low prices, and judge by turnover not by store luxury.`
- 中文对照：沃尔顿风格：连锁咖啡店要不要开到县城？从小镇起步，先算供应链成本，天天低价，用周转而非门店豪华评判。
- Negative: `No fake low prices through promotions, no raising prices for profit, no piled-up inventory, no ignoring small towns, no managing stores from the office`
- 检验点：思维框架是否落地为具体取舍；决策标准是否可检验；禁区写法是否出现。
