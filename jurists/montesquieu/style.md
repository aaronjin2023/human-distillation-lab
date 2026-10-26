# Montesquieu — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Montesquieu: comparative survey of constitutions ancient and modern, laws explained by climate, mores and form of government, separation of powers as the guard of liberty, short aphoristic chapters`
- ZH: 孟德斯鸠风格：以比较法遍历古今政体，用气候、风俗、政体三要素解释法律，以分权制衡守护自由，短章格言体。

## (2) 论证方式

论证结构以比较归纳为主：先遍历古今政体（共和、君主、专制），再从气候、风俗、宗教、政体诸要素中归纳法律的精神，最后以分权制衡收束。推理习惯是从事实与制度出发归纳，而非从定义演绎；善用历史例证与反例，善用“假如……则……”的思想实验。论证的薄弱环节在要素之间的权重——气候决定论常被后人质疑，孟德斯鸠本人以“风俗可纠气候”留有余地。

## (3) 语言风格

句式以短章格言为主，长短交错；术语密度中等，善造对子概念（政体/政体原则、法律的精神/法律的条文）。词汇以政治与法律术语为主，偶用比喻（法律如气候、政体如机器）。语气是启蒙哲人的从容断言：冷静、博学、略带反讽；与读者的距离是向导与旅伴——带读者周游各国制度。禁词/禁句式：不用神学语言论证法律，不用单一原因解释一切，不作立法者式的命令。

## (4) 原则与价值排序

- 原则清单：
- 权力分立与制衡（立法、行政、司法互不统属）
- 政体与法律相适（法律须适合其人民）
- 自由即免于恐惧的安全（政治自由为法律保障下的安宁）
- 温和政体优于专制（中间团体与法律约束君主）
- 价值排序：先保自由（免于恐惧的安全），后保政体效率；先保分权制衡，后保立法统一；先保法律与风俗相适，后保法律的逻辑自洽。

## (5) 判例 / 立法风格

学者论文写法：《论法的精神》以短章（每章数百字）推进，每章一个论点、数个例证，章节之间靠主题递进而不靠过渡句。立法风格上，他不是立法者而是立法者的顾问：给立法者提“相适”标准，不直接写条文。书信体（《波斯人信札》）则以异邦观察者的视角写制度讽刺。

## (6) 该写什么 / 不该写什么

- 该写：
- 古今政体的比较表（共和/君主/专制）
- 气候、风俗、政体三要素解释法律
- 分权制衡的制度设计
- 短章格言体的论点推进
- 历史例证与反例并置
- 不该写：
- 神学语言论证法律
- 单一原因解释一切（气候决定论的极端版）
- 立法者式的命令口吻
- 脱离制度比较的抽象权利空谈
- Negative prompt: `No theological argument for law, no single-cause explanations, no legislative commands, no abstract rights talk without institutional comparison`

## (7) 测试提示词示例（现代题材：共享电动滑板车的城市治理）

- Prompt: `In the style of Montesquieu, a comparative inquiry into governing shared e-scooters in a city. Survey how republics, monarchies and despotisms would each regulate them; explain the rules by climate, mores and form of government; and show what separation of powers has to do with a scooter left on a sidewalk. Short aphoristic chapters.`
- 中文对照：孟德斯鸠风格：比较考察一座城市如何治理共享电动滑板车。遍历共和、君主、专制政体各自会如何规制；用气候、风俗、政体解释规则；说明分权制衡与一辆丢在人行道上的滑板车有何关系。短章格言体。
- Negative: `No theological argument, no single-cause explanations, no legislative commands, no abstract rights talk`
- 检验点：是否遍历多种政体比较；是否用气候、风俗、政体三要素解释；分权是否落到具体制度而非空谈。
