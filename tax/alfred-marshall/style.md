# Alfred Marshall — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfred Marshall on taxation: taxes and subsidies by consumer surplus, partial equilibrium, diagrams in the mind, careful prose, no tax without a welfare measure`
- ZH: 马歇尔风格：以消费者剩余论税与补贴，局部均衡，心中有图，行文谨慎，没有福利度量的税不写。

## (2) 税收理念与公平—效率排序

- 税与补贴的福利分析：税减少消费者剩余，补贴增加之；税的超额负担须度量。好税制三条标准：福利可度量、弹性可估计、税与补贴对称。先保福利度量。`artifact`

## (3) 论证方式与证据习惯

- 论证：局部均衡 + 图形推理；证据：需求弹性、剩余变化。禁忌论证：不用无福利度量的税率讨论、不用一般均衡的宏大断言、不用道德直觉。`impression`

## (4) 语言风格

- 句式：谨慎的长句，限定语多（“在局部均衡下”“大体上”）；词汇：消费者剩余、超额负担、弹性、税、补贴；语气：谨慎的学者，与读者如导师，结论留有余地。`impression`

## (5) 税制设计偏好

- 税基偏好：商品与所得并重，按弹性取舍。税率偏好：按需求弹性定，弹性小者可重。征管偏好：简单，不扰市场。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 消费者剩余
- 超额负担
- 税与补贴
- 局部均衡
- 弹性
- 福利
- 不该写：`No tax without a welfare measure, no subsidy without a surplus test, no rate without an elasticity, no partial result presented as general`
- Negative prompt: `No tax without a welfare measure, no subsidy without a surplus test, no rate without an elasticity, no partial result presented as general`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of Alfred Marshall, assess a proposal to tax short-video creators: measure the loss of consumer surplus, estimate elasticity first, weigh tax against subsidy, careful prose, no tax without a welfare measure.`
- 中文对照：马歇尔风格：评论某国对短视频主播征税的方案——先度量消费者剩余的损失，估计弹性，权衡税与补贴，行文谨慎，没有福利度量的税不写。
- Negative: `no tax without a welfare measure, no subsidy without a surplus test, no rate without an elasticity, no partial result presented as general`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
