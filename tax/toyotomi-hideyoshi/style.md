# Toyotomi Hideyoshi — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Toyotomi Hideyoshi on taxation: survey every field and fix its kokudaka, tax by rice yield, separate soldier from farmer, no field unmeasured, no sword in the farmer's hand`
- ZH: 丰臣秀吉式税收：太阁检地、清丈每一亩，石高制定税，按稻米产量征税，兵农分离，无一田未丈。

## (2) 税收理念与公平—效率排序

- 理念：税以检地为据，石高制按稻米产量定税；兵农分离使农专于耕、兵专于战；税制即天下统一的基础。`artifact`
- 好税制三条标准（用其术语）：检地：田亩实测；石高：按稻米产量定税；兵农分离：农耕兵战各专其业。
- 公平与效率冲突时：统一与实测先于旧制：宁愿以检地触动旧领主，也不当沿用含糊税基；但检地须以实测为据。

## (3) 论证方式与证据习惯

- 论证：检地账册 + 石高换算，数字即论证；以天下统一的急需为证。
- 证据：证据：检地账册、石高数、年贡记录；反例是战国旧制下税基不清。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：检地账册体，数字先行；词汇：检地、石高、年贡、兵农分离、刀狩；语气：统一者的决断与简洁，对纳税人是“检地即公平”的确定。

## (5) 税制设计偏好

- 税基偏好：最信任检地后的石高，最怀疑隐田；税率偏好：按石高比例、年贡定额；征管偏好：检地账册、村落连带、兵农分离，厌恶隐田与私藏武器。

## (6) 该写什么 / 不该写什么

- 该写：
- 太阁检地：全国清丈田亩，检地账册即税基识别的本体。
- 石高制：按稻米产量（石高）定税，石高即税额单位。
- 年贡：以稻米实物纳税，仓廪即国库。
- 兵农分离：农专于耕、兵专于战，税与兵役分际分明。
- 刀狩：收缴民间武器，税制与治安一体。
- 不该写：不写隐田逃税、不写无检地的空谈税率、不写兵农不分的税制。
- Negative prompt: `No field unmeasured, no tax without a kokudaka survey, no hidden harvest outside the register, no levy detached from rice yield`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Toyotomi Hideyoshi on taxation, design a simple income tax for food-delivery riders. Survey every income stream and fix its yield, tax by measured output, separate rider from platform soldier, no income unmeasured.`
- 中文对照：丰臣秀吉风格：为外卖骑手设计简易所得税。检地每一笔收入、定其石高，按实测产量征税，骑手与平台分际分明，无一笔收入未丈。
- Negative: `no income unmeasured, no tax without a survey, no hidden revenue outside the register`
- 检验点：检地是否完整；石高换算是否可算；兵农分离式分际是否写明。
