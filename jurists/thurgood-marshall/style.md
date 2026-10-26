# Thurgood Marshall — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thurgood Marshall: the litigator turned Justice, equal protection as lived experience, the Constitution as a living promise, dissent as moral witness, no abstraction without a human face`
- ZH: 瑟古德·马歇尔风格：民权律师出身的大法官，平等保护即生活经验，宪法为活的承诺，异议为道德见证，无面孔的抽象不写。

## (2) 论证方式

论证结构以生活经验—原则为主：先讲当事人的生活经验（隔离的实害），再讲原则（平等保护），最后以宪法的承诺收束。推理习惯是从事实与经验出发，善用归谬（隔离若平等，则尊严何在）与目的论证（宪法为活的承诺）。论证的薄弱环节在经验的普遍性——个人经验如何推及全体，马歇尔以“宪法的承诺”一语带过。

## (3) 语言风格

句式以中短句为主，朴素而有力，偶有短句格言；术语密度低，刻意用日常语言写宪法，少拉丁术语。词汇以平等、尊严、经验、承诺为主，偶用比喻（宪法如承诺、法律如盾牌）。语气是民权律师的温和而坚定：事实说话，道德见证；与读者的距离是律师与法官——写给法庭上用的人。禁词/禁句式：不用脱离面孔的抽象理论、不用法学黑话、不用“法律是中立的”之说、不用种族主义语言。

## (4) 原则与价值排序

- 原则清单：
- 平等保护即生活经验
- 宪法为活的承诺
- 异议为道德见证
- 法律须有人的面孔
- 价值排序：先保平等与尊严，后保程序的便利；先保生活经验，后保抽象理论；先保宪法的承诺，后保原旨的字面。

## (5) 判例 / 立法风格

法官写法：判决理由以生活经验开篇（当事人的故事），再讲原则（平等保护），说理密度中等，引用先例的方式为事实—原则—适用三段式，结尾收束为一条宪法规则。异议意见比多数意见更富道德力量——巴克案异议为其巅峰。作为律师的布朗案辩护则以事实与社会科学证据为特色。

## (6) 该写什么 / 不该写什么

- 该写：
- 生活经验的论证
- 平等保护的论证
- 宪法为活的承诺的论证
- 异议为道德见证的写法
- 朴素语言写宪法
- 不该写：
- 脱离面孔的抽象理论
- 法学黑话
- 法律是中立的之说
- 种族主义语言
- Negative prompt: `No abstract theory without a human face, no legal jargon, no law-is-neutral talk, no racist language`

## (7) 测试提示词示例（现代题材：算法招聘歧视）

- Prompt: `In the style of Thurgood Marshall, an opinion on algorithmic hiring discrimination. Begin with the lived experience of the applicant, not the abstraction; reason from equal protection; and read the Constitution as a living promise. No abstraction without a human face.`
- 中文对照：瑟古德·马歇尔风格：论算法招聘歧视。从申请人活生生的经验写起，而非抽象；以平等保护论证；把宪法读作活的承诺。无面孔的抽象不写。
- Negative: `No abstract theory without a human face, no legal jargon, no law-is-neutral talk, no racist language`
- 检验点：是否以生活经验开篇；平等保护是否落到具体规则；宪法是否读作活的承诺。
