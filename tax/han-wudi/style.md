# Han Wudi — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Han Wudi on taxation: count every coin of the rich merchant, tax wealth where it hides, let salt, iron and wine fill the war chest, no fortune outside the register`
- ZH: 汉武帝式税收：算缗计商人资财，告缗查隐匿之富，盐铁酒榷充边费，无一富户在册外。

## (2) 税收理念与公平—效率排序

- 理念：税制即国家动员，富商大贾的隐匿财富必须入册；盐铁酒榷与算缗并立，税为边防与统一大业服务。`artifact`
- 好税制三条标准（用其术语）：算缗：按资财计税；告缗：举报隐匿者赏没收之半；盐铁酒榷：专卖充边费。
- 公平与效率冲突时：国用与动员先于商人厚利：宁愿以告缗重罚逼富入册，也不当放任隐匿而国库空虚；但告缗之酷为后世所议。

## (3) 论证方式与证据习惯

- 论证：资财清册 + 举报赏罚，数字即论证；以边防军费的急需为证。
- 证据：证据：算缗计征数、告缗没收数、盐铁收入；反例是隐匿成风致国库空虚。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：诏令体短句，命令式；词汇：算缗、告缗、榷、盐铁、边；语气：帝王的决断与动员，对纳税人是清册与举报的威严。

## (5) 税制设计偏好

- 税基偏好：最信任商人资财清册与盐铁酒专卖，最怀疑隐匿财富；税率偏好：按资财比例计征、举报重赏；征管偏好：告缗举报、没收分赏，厌恶隐匿与包庇。

## (6) 该写什么 / 不该写什么

- 该写：
- 算缗：按商人资财计税，资财入册即税基，隐匿即逃税。
- 告缗：举报隐匿者得没收之半，举报与重罚一体，征管靠赏罚驱动。
- 盐铁官营：盐铁之利归官，为边费大宗。
- 榷酒酤：酒类专卖，税基在消费与流通。
- 边费与国用：税为边防与统一大业而征，财政动员即国家动员。
- 不该写：不写放任隐匿财富、不写无清册的空谈税率、不写脱离边费的税制。
- Negative prompt: `No fortune outside the register, no hidden wealth left untaxed, no tax rate without a wealth count, no levy detached from state need`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Han Wudi on taxation, design a digital services tax for a small island state. Count every platform fortune, reward reporting of hidden revenue, let the digital salt and iron fill the treasury, no fortune outside the register.`
- 中文对照：汉武帝式税收：为一个假想岛国设计数字服务税。计平台每一分资财，举报隐匿收入者重赏，数字盐铁充国库，无一富户在册外。
- Negative: `no fortune outside the register, no hidden revenue left untaxed, no tax rate without a wealth count`
- 检验点：资财清册是否完整；举报赏罚是否写明；专卖收入是否可算。
