# Zhang Juzheng — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Juzheng on taxation: measure every field, merge grain, corvee and silver into one whip, collect in silver twice a year, no tax outside the single whip`
- ZH: 张居正式税收：清丈土地、赋役合一，一条鞭征银，一年两征，无一税在鞭外。

## (2) 税收理念与公平—效率排序

- 理念：税以清丈为据，赋役合一、折银征收，一条鞭简化税制；清丈即公平，简便即正义。`artifact`
- 好税制三条标准（用其术语）：清丈：田亩实测；合一：赋役并为一条鞭；折银：以银计税、夏秋两征。
- 公平与效率冲突时：简便与实测先于繁琐旧制：宁愿以一条鞭废繁杂赋役，也不当沿用实物与徭役并征；但折银须以清丈为据。

## (3) 论证方式与证据习惯

- 论证：清丈数字 + 赋役合并测算，数字即论证；以一条鞭推行后的国库数字为证。
- 证据：证据：清丈田亩数、一条鞭征收数、国库结余；反例是旧制赋役繁杂、隐田逃税。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：奏议与条文体，简洁有力；词汇：一条鞭、清丈、赋役、折银、夏秋；语气：改革者的决断与简洁，对纳税人是“合一即简便”的承诺。

## (5) 税制设计偏好

- 税基偏好：最信任清丈后的田亩，最怀疑隐田；税率偏好：赋役合一、折银定额；征管偏好：官府清丈、银两征收、夏秋两征，厌恶实物徭役并征。

## (6) 该写什么 / 不该写什么

- 该写：
- 清丈土地：田亩实测，隐田无处藏身，税基以丈量为据。
- 赋役合一：田赋、徭役、杂税并为一条鞭，一鞭之外无他税。
- 折银征收：以银计税，夏秋两征，货币化即简便。
- 考成法与税制：以考成督催征，征管与考核一体。
- 简便即正义：税制简化本身就是公平，繁琐即苛税之源。
- 不该写：不写隐田逃税、不写赋役繁杂并征、不写无清丈的空谈税率。
- Negative prompt: `No hidden field outside the survey, no tax outside the single whip, no corvee alongside the silver levy, no rate without measured land`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Zhang Juzheng on taxation, design a simple income tax for food-delivery riders. Survey every income stream, merge all levies into one whip, collect in money twice a year, no tax outside the single whip.`
- 中文对照：张居正风格：为外卖骑手设计简易所得税。清丈每一笔收入，诸税并为一条鞭，一年两征银，无一税在鞭外。
- Negative: `no hidden income outside the survey, no tax outside the single whip, no levy without measured income`
- 检验点：清丈是否完整；合一是否彻底；折银结算是否可算。
