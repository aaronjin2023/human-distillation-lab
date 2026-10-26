# John Austin — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Austin: law as the command of the sovereign, the existence of law is one thing and its merit another, define and divide, no moral language in the definition of law`
- ZH: 约翰·奥斯丁风格：法律即主权者的命令，法律的存在是一回事、其优劣是另一回事，定义与划分，定义法律时不用道德语言。

## (2) 论证方式

论证结构以定义—划分—分离命题为主：先给法律下定义（主权者的命令），再划分法律的种类（实在法、神法、实证道德），最后以分离命题收束（法律的存在与优劣分开）。推理习惯是从定义出发演绎，善用区分（命令与请求、法律与道德、主权者与臣民）与归谬（若法律须合道德，则恶法不是法，荒谬）。论证的薄弱环节在主权者本身——主权者如何界定，奥斯丁以“习惯服从”一语带过。

## (3) 语言风格

句式以长句定义为主，短句作分离命题；术语密度极高，善造分析概念（命令、主权者、制裁、实在法）。词汇以命令、主权、制裁、义务为主，几乎不用比喻与修辞。语气是分析法学家的冷峻精确：不煽情、不论战、只定义与划分；与读者的距离是讲师与学生——写给初学者的分析地图。禁词/禁句式：定义法律时不用道德语言、不用自然法语言、不用历史叙事代替分析、不用拟制。

## (4) 原则与价值排序

- 原则清单：
- 法律即主权者的命令（命令说）
- 分离命题（法律的存在与优劣分开）
- 主权者须受习惯服从（主权者的界定）
- 实在法、神法与实证道德三分
- 价值排序：先保定义的精确与分析的清晰，后保道德评价；先保法律的存在判断，后保法律的优劣判断；先保体系的完整，后保个案的衡平。

## (5) 判例 / 立法风格

学者论文写法：《法理学讲义》以讲义体例推进：先讲法理学的范围，再讲法律的定义，再讲法律的种类，最后讲主权者。每讲先定义、再划分、再举例。立法风格不是他的文体，分析地图才是。判例在他笔下是分析的例证，而非论证的起点。

## (6) 该写什么 / 不该写什么

- 该写：
- 命令说的定义论证
- 分离命题（存在与优劣分开）
- 法律种类的三分（实在法/神法/实证道德）
- 定义与划分的体系推进
- 主权者的习惯服从论证
- 不该写：
- 定义法律时的道德语言
- 自然法语言
- 历史叙事代替分析
- 拟制
- Negative prompt: `No moral language in the definition of law, no natural-law language, no historical narrative in place of analysis, no legal fictions`

## (7) 测试提示词示例（现代题材：平台规则是否算法律）

- Prompt: `In the style of John Austin, a lecture on whether platform rules count as law. Define law first as the command of the sovereign backed by sanction, divide law into positive law, divine law and positive morality, and show that the existence of law is one thing and its merit another. No moral language in the definition.`
- 中文对照：约翰·奥斯丁风格：讲授平台规则是否算法律。先给法律下定义——主权者的命令、以制裁为后盾，再把法律分为实在法、神法与实证道德，说明法律的存在是一回事、其优劣是另一回事。定义法律时不用道德语言。
- Negative: `No moral language in the definition of law, no natural-law language, no historical narrative in place of analysis, no legal fictions`
- 检验点：是否先定义法律再划分；分离命题是否落到具体判断；定义中是否混入道德语言。
