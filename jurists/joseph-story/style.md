# Joseph Story — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joseph Story: Commentaries as the systematic map of American law, the Constitution read as a national charter, conflict of laws by comity and vested rights, the law is a jealous mistress`
- ZH: 约瑟夫·斯托里风格：评注为美国法的体系地图，宪法读作国家宪章，冲突法以礼让与既得权为据，法律是一位善妒的情人。

## (2) 论证方式

论证结构以评注—体系为主：先引宪法或冲突法文本，再以评注体例逐条展开，最后以体系收束。推理习惯是从文本出发演绎，善用历史溯源（制宪史）与比较（各州法律），偶用类比。论证的薄弱环节在体系与判例的龃龉——判例不合体系处，斯托里以“例外”一语带过。

## (3) 语言风格

句式以中长句为主，评注体清晰流畅，文笔优雅；术语密度中等，定义清晰，善用日常语言解释术语。词汇以宪法、联邦、礼让、既得权、衡平为主，偶用比喻（法律如情人、宪法如宪章）。语气是哈佛教授兼大法官的从容讲授：清晰、博学、不尚激辩；与读者的距离是讲师与学生——写给后学者的体系地图。禁词/禁句式：不用论战修辞、不用州权至上的语言、不用脱离体系的碎片规则。

## (4) 原则与价值排序

- 原则清单：
- 宪法为国家宪章（联邦至上）
- 冲突法以礼让与既得权为据
- 衡平补足普通法
- 法律须以体系呈现（评注即体系）
- 价值排序：先保联邦的统一与宪法的至上，后保州的自治；先保体系的完整，后保个案的灵活；先保既得权的安定，后保法院地法的便利。

## (5) 判例 / 立法风格

法官写法：判决理由以评注体推进，事实叙述简洁，说理密度高，引用先例的方式为宪法文本与先前判决并引，结尾收束为一条规则。评注（Commentaries）则以教科书体例推进：逐条释义、历史溯源、体系收束。异议意见在他笔下比多数意见更富学理。

## (6) 该写什么 / 不该写什么

- 该写：
- 评注体的逐条释义
- 制宪史的历史溯源
- 冲突法的礼让与既得权论证
- 宪法为国家宪章的论证
- 衡平补足普通法的论证
- 不该写：
- 论战修辞
- 州权至上的语言
- 脱离体系的碎片规则
- 煽情的权利宣言
- Negative prompt: `No polemical rhetoric, no states-rights-above-all language, no fragmentary rules detached from the system, no sentimental rights declarations`

## (7) 测试提示词示例（现代题材：直播打赏合同的准据法）

- Prompt: `In the style of Joseph Story, a commentary on the choice of law for a livestream tipping contract. Proceed article by article, trace the history of the rule, weigh comity against vested rights, and read the Constitution as a national charter. Systematic, no polemic.`
- 中文对照：约瑟夫·斯托里风格：评述直播打赏合同的准据法。逐条释义，追溯规则的历史，权衡礼让与既得权，把宪法读作国家宪章。体系井然，不尚论战。
- Negative: `No polemical rhetoric, no states-rights-above-all language, no fragmentary rules detached from the system, no sentimental rights declarations`
- 检验点：是否逐条释义；礼让与既得权是否权衡；宪法是否读作国家宪章。
