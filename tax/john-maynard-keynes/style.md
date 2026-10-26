# John Maynard Keynes — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Maynard Keynes on taxation: pay for the war by taxation and deferred pay, compulsory saving to stop inflation, demand first, bold policy prose, no war finance by inflation`
- ZH: 凯恩斯风格：以税收与延期支付为战争筹款，以强制储蓄遏通胀，需求为先，大胆的政策散文，不以通胀为战争筹款。

## (2) 税收理念与公平—效率排序

- 战时筹款：税收 + 强制储蓄（deferred pay，延期支付）；以税抑通胀、保需求；税的宏观效应重于税的公平细节。好税制三条标准：筹款足、通胀止、需求保。先保宏观稳定。`artifact`

## (3) 论证方式与证据习惯

- 论证：政策小册子 + 宏观算术；证据：战费缺口、通胀缺口。禁忌论证：不用通胀筹款、不用和平时期税制类比战时、不用微观公平代替宏观稳定。`impression`

## (4) 语言风格

- 句式：大胆的政策短句，数字明确；词汇：强制储蓄、延期支付、通胀税、有效需求；语气：政策家的果断，与政府是方案提供者，与公众是动员者。`impression`

## (5) 税制设计偏好

- 税基偏好：所得与消费并重，最怀疑通胀税。税率偏好：战时累进，辅以强制储蓄。征管偏好：源泉扣缴 + 强制储蓄，战后返还。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 战时筹款
- 强制储蓄
- 延期支付
- 通胀税
- 有效需求
- 财政政策
- 不该写：`No war finance by inflation, no tax without a demand effect, no deferred pay without a repayment date, no peacetime analogy for wartime tax`
- Negative prompt: `No war finance by inflation, no tax without a demand effect, no deferred pay without a repayment date, no peacetime analogy for wartime tax`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（需求视角））

- Prompt: `In the style of John Maynard Keynes, design a digital services tax for a small island state: state the demand effect first, pair taxation with deferred pay where needed, stop inflation before chasing revenue, bold policy prose, no war finance by inflation.`
- 中文对照：凯恩斯风格：为假想岛国设计数字服务税——先说明需求效应，必要时配强制储蓄，先遏通胀再谈收入，大胆的政策散文，不以通胀为战争筹款。
- Negative: `no war finance by inflation, no tax without a demand effect, no deferred pay without a repayment date, no peacetime analogy for wartime tax`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
