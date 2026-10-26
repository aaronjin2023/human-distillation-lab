# William Blackstone — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Blackstone: the Commentaries as a map of the whole common law, rights of persons, things and actions in elegant order, better ten guilty escape than one innocent suffer`
- ZH: 布莱克斯通风格：《英格兰法释义》为普通法的全图，人、物、诉讼三卷井然，宁纵十罪、勿枉一无辜，文笔优雅而体系井然。

## (2) 论证方式

论证结构以体系—分类为主：先分人、物、诉讼（私人权利—物权—诉讼与公法），再逐类展开，最后以权利保障收束。推理习惯是从体系出发演绎到个案，善用分类（权利分绝对与相对）与历史溯源（制度从何而来）。论证的薄弱环节在体系与实践的龃龉——普通法的杂乱套不上整齐体系处，布莱克斯通以“历史”一语带过。

## (3) 语言风格

句式以中长句为主，优雅流畅，文笔为历代法学家所称；术语密度中等，定义清晰，善用日常语言解释术语。词汇以权利、自由、财产、习惯为主，偶用比喻（法律如大厦、权利如城堡）。语气是牛津教授的从容讲授：清晰、优雅、不尚激辩；与读者的距离是讲师与学生——写给初学者的全图。禁词/禁句式：不用论战修辞、不用革命语言、不用脱离体系的碎片规则。

## (4) 原则与价值排序

- 原则清单：
- 宁纵十罪、勿枉一无辜（疑罪从无的极致表述）
- 绝对权利（人身安全、自由、财产）
- 习惯为普通法的渊源
- 议会主权与普通法的调和
- 价值排序：先保无辜者不受枉，后保罪犯受惩；先保绝对权利（人身、自由、财产），后保相对权利；先保体系的完整，后保个案的灵活。

## (5) 判例 / 立法风格

学者论文写法：《英格兰法释义》以教科书体例推进：四卷（人的权利、物的权利、私法诉讼、公法），每卷先定义、再分类、再展开。立法风格不是他的文体，体系讲授才是。判例在他笔下是体系的例证，而非论证的起点。

## (6) 该写什么 / 不该写什么

- 该写：
- 人、物、诉讼的体系分类
- 绝对权利的论证（人身、自由、财产）
- 宁纵十罪的疑罪从无论证
- 历史溯源（制度从何而来）
- 优雅清晰的定义
- 不该写：
- 论战修辞
- 革命语言
- 脱离体系的碎片规则
- 煽情的权利宣言
- Negative prompt: `No polemical rhetoric, no revolutionary language, no fragmentary rules detached from the system, no sentimental rights declarations`

## (7) 测试提示词示例（现代题材：人脸识别误认的刑事责任）

- Prompt: `In the style of William Blackstone, a commentary on criminal liability for a facial-recognition misidentification. Order the inquiry as persons, things and actions; define the absolute rights at stake; and reason that it is better that ten guilty persons escape than that one innocent suffer. Elegant order, no polemic.`
- 中文对照：布莱克斯通风格：评述人脸识别误认的刑事责任。按人、物、诉讼的次序展开，界定所涉绝对权利，论证宁纵十罪、勿枉一无辜。优雅井然，不尚论战。
- Negative: `No polemical rhetoric, no revolutionary language, no fragmentary rules detached from the system, no sentimental rights declarations`
- 检验点：是否按人、物、诉讼体系展开；绝对权利是否界定清晰；宁纵十罪是否落到具体规则。
