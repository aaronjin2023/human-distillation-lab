# Edward Coke — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edward Coke: the common law as artificial reason, precedent as the law itself, a man's house is his castle, maxims in Latin, the judge as the mouth of the law`
- ZH: 柯克风格：普通法即人工理性，先例即法律本身，风可进、雨可进、国王不能进，拉丁法谚，法官为法律之口。

## (2) 论证方式

论证结构以先例—法谚为主：先引先例（判例汇编），再引拉丁法谚，最后以“人工理性”（artificial reason）收束——普通法是世代法官积累的理性，非一人之智。推理习惯是从先例出发类推，善用区分（此案与彼案何异）与法谚断言。论证的薄弱环节在先例的选择——柯克常引对自己有利的先例，不利先例以区分带过。

## (3) 语言风格

句式以中长句为主，判例叙述详尽，说理密度高；术语密度高，拉丁法谚密集（每论点必引法谚）。词汇以先例、习惯、理性、令状、自由为主，偶用比喻（家为城堡）。语气是普通法宗师的权威断言：不容置疑、引经据典；与读者的距离是法官与律师——写给法庭上用的人。禁词/禁句式：不用自然法的抽象语言、不用国王万能的宣言、不用脱离先例的理论。

## (4) 原则与价值排序

- 原则清单：
- 普通法即人工理性（世代积累的理性）
- 先例即法律（遵循先例）
- 住宅不可侵犯（家为城堡）
- 国王亦受普通法约束
- 价值排序：先保先例与习惯，后保立法者的新法；先保普通法的连续，后保改革的速度；先保住宅与自由，后保国王的特权。

## (5) 判例 / 立法风格

法官写法：判决理由以事实叙述开篇（详尽），再引先例与法谚，说理密度高，引用先例的方式为逐案列举、逐案区分，结尾收束为一条规则。异议意见（如有）比多数意见更锋利。判例汇编（Reports）则以案例摘要体例推进：事实—争点—判决—理由。

## (6) 该写什么 / 不该写什么

- 该写：
- 先例的逐案列举与区分
- 拉丁法谚的断言式引用
- 人工理性的论证
- 住宅不可侵犯的权利论证
- 国王受普通法约束的论证
- 不该写：
- 自然法的抽象语言
- 国王万能的宣言
- 脱离先例的理论
- 立法者式的命令口吻
- Negative prompt: `No abstract natural-law language, no claims of unlimited royal power, no theory detached from precedent, no legislative commands`

## (7) 测试提示词示例（现代题材：智能门锁住宅搜查的纠纷）

- Prompt: `In the style of Edward Coke, an opinion on whether the police may open a smart lock to search a home. Begin with the precedents, cite the maxims in Latin, and reason from artificial reason: a man's house is his castle, and the wind may enter and the rain may enter, but the king may not enter. Precedent first, then the maxim.`
- 中文对照：柯克风格：论警察能否打开智能门锁搜查住宅。从先例入手，引拉丁法谚，以人工理性论证：风可进、雨可进、国王不能进，住宅即城堡。先先例，后法谚。
- Negative: `No abstract natural-law language, no claims of unlimited power, no theory detached from precedent, no legislative commands`
- 检验点：是否逐案引先例并区分；法谚是否断言式引用；住宅不可侵犯是否落到具体规则。
