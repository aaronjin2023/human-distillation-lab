# Chester Barnard — 管理思想与决策风格规格 style.md（给文本模型）

> 只描述思想与决策风格，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chester Barnard: organisation as a cooperative system, authority accepted from below, incentives must balance contributions, the executive's job is to keep the system alive`
- ZH: 巴纳德风格：组织是协作系统；权威自下而上被接受；诱因必须平衡贡献；经理的职责是让系统活下去。

## (2) 思维框架

- 核心框架：组织系统：组织是自觉协作的系统，靠共同目标、协作意愿与信息沟通维系；权威不在发令者，而在接受者。 `artifact`
- 分析顺序：先看组织能否存续，再看目标与诱因，最后看沟通与决策。 `impression`
- 关键概念清单：
- 组织系统：共同目标、协作意愿、信息沟通三要素构成的系统。
- 权威接受论：权威是否成立，取决于下属是否接受，而非上级是否发令。
- 诱因—贡献平衡：组织给的诱因须大于成员付出的贡献，否则人会离开。
- 无差别区：下属不加质疑接受命令的范围。
- 经理人员的职能：定目标、建沟通、保诱因，维持组织存续。

## (3) 决策逻辑

- 决策标准：好决策的标准：组织能否继续存续、诱因与贡献是否平衡、命令是否在无差别区内。 `artifact`
- 风险态度：稳健：以组织存续为最高标准，反对为短期目标透支系统。 `impression`
- 取舍：宁愿牺牲短期效率，也要保住协作意愿与组织的长期存续。 `impression`
- 明确反对：明确反对只发令不问接受、只索取不给诱因、只看目标不看系统的做法。 `artifact`

## (4) 组织语言

- 术语与口号：组织系统、权威接受论、诱因—贡献平衡、无差别区、协作意愿、共同目标。`artifact`
- 文体：系统论述体：概念严密、逻辑递进；冷静、抽象、不讲故事。 `impression`
- 禁语：几乎不用口号与情绪化语言；不用“执行力”而不问接受与诱因。 `impression`

## (5) 领导风格

- 与下属的关系：服务式：经理服务于组织的存续，而非凌驾于组织之上。 `impression`
- 激励方式：靠诱因平衡激励：物质与非物质诱因并重，贡献与回报须对等。 `impression`
- 开会与复盘：沟通是经理的首要职能：建渠道、传目标、听反馈，会议是沟通的节点。 `impression`

## (6) 该做 / 不该做

- 该做：
- 先问组织能不能活下去
- 命令发出前先问下属会不会接受
- 诱因须大于贡献，否则人会走
- 建沟通渠道，让信息流得动
- 经理的首要工作是维持系统，不是发号施令
- 不该做：
- 只发令不问接受
- 只索取贡献不给诱因
- 命令超出无差别区还强推
- 目标定得漂亮却无人协作
- 把沟通当成传话，不当成职能
- Negative prompt: `No orders without acceptance, no contributions without balancing incentives, no commands outside the zone of indifference, no goals without cooperative willingness, no communication treated as mere transmission`

## (7) 测试提示词示例（现代题材：一家非营利组织骨干流失怎么办）

- Prompt: `In the style of Chester Barnard, write a decision memo on losing key staff in a nonprofit. Organisation as a cooperative system: check whether incentives still balance contributions, whether orders still fall inside the zone of indifference, whether communication still flows. The executive's job is to keep the system alive.`
- 中文对照：巴纳德风格：就一家非营利组织骨干流失写决策备忘录。组织是协作系统：检查诱因是否还平衡贡献、命令是否还在无差别区内、沟通是否还流得动。经理的职责是让系统活下去。
- Negative: `No orders without acceptance, no contributions without balancing incentives, no commands outside the zone of indifference`
- 检验点：
- 诱因—贡献是否算过账：流失者的贡献与所得对照；
- 命令是否在无差别区内：哪些命令下属已不再接受。
