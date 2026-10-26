# Sun Yat-sen — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sun Yat-sen on taxation: let land value created by society return to society, tax the unearned increment, equalise land rights, no fortune from land speculation untaxed`
- ZH: 孙中山式税收：平均地权，土地涨价归公，征土地增值税，社会创造的地价归社会，不征投机之利不归公之税。

## (2) 税收理念与公平—效率排序

- 理念：土地涨价归公，平均地权；土地增值税征不劳而获的涨价部分，税为民生主义服务。`artifact`
- 好税制三条标准（用其术语）：平均地权：地权归公；涨价归公：土地增值归社会；土地增值税：征不劳而获部分。
- 公平与效率冲突时：民生先于投机之利：宁愿以土地增值税抑投机，也不当放任地价暴涨而民生困苦；但征税须以地价申报为据。

## (3) 论证方式与证据习惯

- 论证：民生主义演绎 + 各国地价比较，以地价涨幅数字为证；理想与实证并重。
- 证据：证据：地价申报数、土地涨幅、各国土地税比较；反例是投机致地价暴涨。
- 禁忌论证：不用数学模型推导最优税率，不用后世归宿分析，不以空言论税。

## (4) 语言风格

- 句式：演说与论述体，理想主义而条理清晰；词汇：平均地权、涨价归公、民生、地价、增值税；语气：革命者的理想与号召，对纳税人是“地价归公”的正义。

## (5) 税制设计偏好

- 税基偏好：最信任土地价值与涨价部分，最怀疑投机所得；税率偏好：土地增值税、累进；征管偏好：地价申报、照价征税、照价收买，厌恶投机逃税。

## (6) 该写什么 / 不该写什么

- 该写：
- 平均地权：土地权利归公，地权平等是税制的政治前提。
- 涨价归公：土地因社会发展而涨价的部分归社会，不归投机者。
- 土地增值税：征土地涨价部分，税率随涨幅而定。
- 地价申报：业主自报地价，照价征税、照价收买，申报即税基。
- 民生主义：税为民生服务，节制资本、平均地权一体。
- 不该写：不写放任土地投机、不写无申报的空谈税率、不写脱离民生的税制。
- Negative prompt: `No fortune from land speculation untaxed, no land increment kept private, no rate without a declared land value, no tax detached from livelihood`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of Sun Yat-sen on taxation, assess a tax on short-video creators. Let the platform value created by society return to society, tax the unearned increment of attention, no fortune from speculation untaxed.`
- 中文对照：孙中山风格：评论对短视频主播征税的方案。社会创造的平台价值归社会，征注意力不劳而获的增值，不征投机之利不归公之税。
- Negative: `no fortune from speculation untaxed, no increment kept private, no rate without a declared value`
- 检验点：涨价归公是否可算；申报机制是否写明；民生挂钩是否具体。
