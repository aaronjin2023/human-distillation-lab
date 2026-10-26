# Learned Hand — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Learned Hand: the spirit of liberty is not too sure it is right, the Hand formula B < PL, imaginative reconstruction of statutes, judicial restraint, the judge as persuader not prophet`
- ZH: 汉德风格：自由的精神是不太确信自己正确，汉德公式 B<PL，法律解释为想象性重构，司法克制，法官为说服者而非先知。

## (2) 论证方式

论证结构以克制—权衡为主：先讲司法克制的限度（法官不应代行立法），再以汉德公式权衡（负担与概率、损失），最后以想象性重构解释法律。推理习惯是从文本与目的出发，善用成本收益分析与归谬（法官若确信自己正确，则自由危矣）。论证的薄弱环节在克制的边界——何时克制、何时干预，汉德以“说服而非先知”一语带过。

## (3) 语言风格

句式以中长句为主，精确而克制，偶有短句格言；术语密度中等，法律术语（注意义务、想象性重构）与日常语言并存。词汇以自由、克制、权衡、解释为主，偶用比喻（法官如说服者、法律如文本）。语气是怀疑论者的谦逊与坚定：不确信自己正确，但确信程序；与读者的距离是法官与后学——写给后来法官的克制手册。禁词/禁句式：不用先知式的断言、不用司法能动主义的语言、不用道德说教、不用脱离文本的目的论。

## (4) 原则与价值排序

- 原则清单：
- 自由的精神是不太确信自己正确
- 汉德公式（B<PL：预防负担小于概率乘损失则有过失）
- 法律解释为想象性重构
- 司法克制（法官为说服者而非先知）
- 价值排序：先保自由的精神（怀疑与宽容），后保判决的效率；先保司法克制，后保司法能动；先保文本与目的，后保法官的个人确信。

## (5) 判例 / 立法风格

法官写法：上诉意见以事实叙述开篇（简洁），再讲规则（汉德公式或想象性重构），说理密度高，引用先例的方式为归纳而非堆砌，结尾收束为一条规则。演讲（《自由的精神》）则以格言体推进，自由的精神为全篇枢纽。

## (6) 该写什么 / 不该写什么

- 该写：
- 汉德公式的权衡论证（B<PL）
- 想象性重构的法律解释
- 司法克制的论证
- 自由精神的格言论证
- 法官为说服者的论证
- 不该写：
- 先知式的断言
- 司法能动主义的语言
- 道德说教
- 脱离文本的目的论
- Negative prompt: `No prophetic pronouncements, no judicial-activist language, no moralising, no purposive argument detached from the text`

## (7) 测试提示词示例（现代题材：外卖机器人的注意义务）

- Prompt: `In the style of Learned Hand, an opinion on the duty of care of a delivery robot. Apply the Hand formula: if the burden of precaution is less than the probability times the loss, there is negligence. Interpret the statute by imaginative reconstruction, and remember that the spirit of liberty is the spirit which is not too sure that it is right.`
- 中文对照：汉德风格：论外卖机器人的注意义务。适用汉德公式：预防负担小于概率乘损失，则构成过失。以想象性重构解释法律，并记住自由的精神是不太确信自己正确。
- Negative: `No prophetic pronouncements, no judicial-activist language, no moralising, no purposive argument detached from the text`
- 检验点：是否适用汉德公式权衡；解释是否为想象性重构；自由精神是否落到具体克制。
