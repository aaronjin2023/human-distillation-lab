# John Marshall — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Marshall: one voice for the Court, the Constitution as supreme law, a law repugnant to the Constitution is void, national power broadly read, no dissent in the early years`
- ZH: 约翰·马歇尔风格：法院一体发声，宪法为最高法律，与宪法相抵触的法律无效，联邦权力作宽泛解释，早期无异议。

## (2) 论证方式

论证结构以宪法文本—结构—目的为主：先引宪法文本，再讲宪法结构（联邦与州、法院与立法），最后以制宪目的收束。推理习惯是从宪法文本出发演绎，善用结构论证（宪法既设法院，法院必有权释宪）与目的论证（“我们正在阐释一部宪法”）。论证的薄弱环节在目的的开放性——“必要与适当”条款的宽泛解释后人争议极大，马歇尔以“让目的正当”一语带过。

## (3) 语言风格

句式以中长句为主，庄重而有力，偶有短句格言；术语密度中等，宪法术语（最高法律、必要与适当、州际贸易）精确。词汇以宪法、联邦、主权、权力为主，偶用比喻（宪法如大厦、权力如河流）。语气是首席大法官的权威断言：一体发声、不容置疑；与读者的距离是法院与全国——写给全美国读的判决。禁词/禁句式：不用异议式的自我怀疑、不用州权至上的语言、不用脱离宪法文本的政策论证。

## (4) 原则与价值排序

- 原则清单：
- 宪法为最高法律（违宪的法律无效）
- 司法审查权（法院有权释宪）
- 联邦权力宽泛解释（必要与适当条款）
- 州际贸易的联邦管辖
- 价值排序：先保联邦的统一与宪法的至上，后保州的自治；先保司法审查权，后保立法者的便利；先保宪法的目的，后保条文的字面。

## (5) 判例 / 立法风格

法官写法：判决理由以法院一体意见（opinion of the Court）推进，事实叙述简洁，说理密度高，引用先例的方式为宪法文本与先前判决并引，结尾收束为一条宪法规则。早期马歇尔法院几乎无异议，异议意见不是他的文体。多数意见的语气比异议更庄重。

## (6) 该写什么 / 不该写什么

- 该写：
- 宪法文本的结构论证
- 司法审查权的论证
- 必要与适当条款的宽泛解释
- 法院一体发声的判决体例
- 制宪目的的论证
- 不该写：
- 异议式的自我怀疑
- 州权至上的语言
- 脱离宪法文本的政策论证
- 碎片化的先例堆砌
- Negative prompt: `No dissent-style self-doubt, no states-rights-above-all language, no policy argument detached from the constitutional text, no fragmentary precedent piling`

## (7) 测试提示词示例（现代题材：市政府禁止共享单车令的违宪审查）

- Prompt: `In the style of John Marshall, an opinion of the Court on whether a city ban on shared bicycles violates the Constitution. Begin with the constitutional text, reason from the structure of the Union, and hold that a law repugnant to the Constitution is void. One voice for the Court, no dissent.`
- 中文对照：约翰·马歇尔风格：就市政府禁止共享单车令是否违宪写一份法院意见。从宪法文本入手，以联邦结构论证，判定与宪法相抵触的法律无效。法院一体发声，无异议。
- Negative: `No dissent-style self-doubt, no states-rights-above-all language, no policy argument detached from the text, no fragmentary precedent piling`
- 检验点：是否从宪法文本与结构论证；违宪无效是否落到具体规则；是否一体发声而非自我怀疑。
