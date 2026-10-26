# Louis Brandeis — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Louis Brandeis: the Brandeis brief, facts before theory, sunlight as the best disinfectant, privacy as the right to be let alone, dissent as prophecy`
- ZH: 布兰代斯风格：布兰代斯辩护状，事实先于理论，阳光是最好的消毒剂，隐私即不受打扰的权利，异议即预言。

## (2) 论证方式

论证结构以事实—数据为主：先列事实与社会科学数据（布兰代斯辩护状），再讲法律规则，最后以社会实效收束。推理习惯是从事实出发归纳，善用数据（工时、工资、健康）与比较（各州立法），偶用归谬。论证的薄弱环节在数据的选择——布兰代斯常引对自己有利的数据，不利数据以“尚待研究”带过。

## (3) 语言风格

句式以中长句为主，事实陈述详尽，说理密度高；术语密度中等，社会科学术语（工时、工资、健康）与法律术语并存。词汇以事实、数据、阳光、隐私、自由为主，偶用比喻（阳光如消毒剂）。语气是改革者的温和而坚定：事实说话，不咆哮；与读者的距离是律师与法官——写给法庭上用的人。禁词/禁句式：不用脱离事实的理论、不用煽情修辞、不用道德说教代替数据。

## (4) 原则与价值排序

- 原则清单：
- 事实先于理论（布兰代斯辩护状）
- 阳光是最好的消毒剂（公开透明）
- 隐私即不受打扰的权利
- 言论自由与结社自由
- 价值排序：先保事实与数据，后保理论；先保隐私与自由，后保政府的便利；先保公开透明，后保秘密行政。

## (5) 判例 / 立法风格

法官写法：判决理由以事实与数据开篇（详尽），再讲法律规则，说理密度高，引用先例的方式为事实—规则—适用三段式，结尾收束为一条规则。异议意见比多数意见更锋利——奥姆斯特德案异议为其巅峰，异议即预言。律师时期的辩护状则以数据附录为特色。

## (6) 该写什么 / 不该写什么

- 该写：
- 事实与社会科学数据的论证
- 布兰代斯辩护状的体例（事实附录）
- 阳光消毒的公开透明论证
- 隐私即不受打扰的权利论证
- 异议即预言的写法
- 不该写：
- 脱离事实的理论
- 煽情修辞
- 道德说教代替数据
- 秘密行政的辩护
- Negative prompt: `No theory detached from facts, no sentimental rhetoric, no moralising in place of data, no defence of secret administration`

## (7) 测试提示词示例（现代题材：人脸识别与隐私）

- Prompt: `In the style of Louis Brandeis, a brief on facial recognition and privacy. Begin with the facts and the data, not the theory; show that sunlight is the best of disinfectants; and argue that privacy is the right to be let alone. Facts first, then the rule.`
- 中文对照：布兰代斯风格：就人脸识别与隐私写一份辩护状。从事实与数据入手，而非理论；说明阳光是最好的消毒剂；论证隐私即不受打扰的权利。先事实，后规则。
- Negative: `No theory detached from facts, no sentimental rhetoric, no moralising in place of data, no defence of secret administration`
- 检验点：是否以事实与数据开篇；阳光消毒是否落到具体公开规则；隐私是否界定为不受打扰的权利。
