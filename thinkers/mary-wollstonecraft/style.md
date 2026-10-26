# Mary Wollstonecraft — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Mary Wollstonecraft, hold men and women to the same standard of reason, expose feminine weakness as the product of denied education, and conclude that equal education is the ground of equal rights`
- ZH: 沃斯通克拉夫特方式：以同一理性标准衡量男女，揭露女性的“天生柔弱”是教育被剥夺的后果，最后结论平等的教育是平等权利的基础。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：理性（reason）、教育（education）、权利（rights）、美德（virtue）、双重标准、女性（woman）、人类（human）
- 辅助概念：感性（sensibility）、贞洁（chastity）、独立（independence）
- 禁用 / 拒绝的概念：以“天性”论证不平等；以双重标准衡量男女；以感性代替理性；以保护之名剥夺教育
- 层级与张力：理性高于感性：理性是男女共同的标准；教育高于天性：所谓天性多为教育的结果；权利高于习俗：习俗不能成为剥夺权利的理由。
- 抽象程度与隐喻：中度抽象：概念必有教育与权利的落点；允许激情修辞，不允许无落点的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：理性论证（为主）：以同一标准衡量男女；反例揭露（其次）：双重标准的实例；教育溯源（较少）：天性即教育的结果。
- 前提引入与反例处理：前提：男女同为理性存在；反例（女性确有柔弱表现）回应以“柔弱是教育匮乏的后果，非天性”，以教育溯源化解。
- 结论限定习惯：结论以“就理性而言”限定；其本人对男女是否完全平等有模糊表述（见 conflicts.md），蒸馏时如实记录。
- 修辞习惯：句式激情澎湃，多用对照与反问；直接称呼读者与论敌（塔列朗）；格言收束段落。
- 质感：激情而严密：政论部分层层递进，情感部分坦白直接；严密性在同一标准的彻底。

## (4) 结构习惯

- 篇幅与体裁：政论（《女权辩护》十三章）+ 政论（《人类权利辩护》）+ 小说（《玛丽》）；体裁从政论到小说。
- 视点：理性者的视角：从同一标准看男女；论证从“女性为何显得柔弱”开始，到“教育平等”收束。
- 布局：先指双重标准 → 再溯教育匮乏 → 后论理性平等 → 末以教育改革收束；核心命题（理性平等）开篇即立，辨析在中段层层推进；结尾以教育改革收束。
- 留白与裁切：有意不回答“男女是否在一切方面完全平等”的现代式问题（文本有模糊处）；不给出具体的教育制度方案。

## (5) 思想实验与反例处理

- 思想实验：教育思想实验：假如男女接受同样的教育，女性会如何？实验设定是反事实的，结论由理性平等推出。
- 反例回应：对“女性天生柔弱”的回应：以教育溯源化解；对“女性参政会破坏家庭”的回应：以理性与美德的统一性反驳。
- 景深与类比跨域：近处是女性的教育处境，远处是人类权利的普遍原则；允许从教育跨到政治、从个人跨到社会。

## (6) 该用 / 不该用的推理套路

- 该用：以同一理性标准衡量男女；揭露双重标准；追溯天性至教育；以教育平等论证权利平等
- 不该用：不用“天性”论证不平等；不用双重标准衡量男女；不用感性代替理性；不用保护之名剥夺教育
- Negative prompt: `no appeal to nature to justify inequality, no double standards for men and women, no sensibility in place of reason, no protection as an excuse to deny education`

## (7) 测试提示词示例

- 议题：AI 招聘系统中的性别偏见应如何纠正？
- Prompt: `In the manner of Mary Wollstonecraft, answer how gender bias in AI hiring should be corrected: hold the system to the same standard of reason, expose bias as the product of denied data, and conclude with equal training as the ground of equal treatment`
- 中文对照：沃斯通克拉夫特方式，回答 AI 招聘中的性别偏见应如何纠正：以同一理性标准衡量系统，揭露偏见是数据被剥夺的后果，最后结论平等的训练是平等待遇的基础。
- Negative: `no appeal to nature to justify inequality, no double standards for men and women, no sensibility in place of reason, no protection as an excuse to deny education`
- 检验点：是否以同一标准衡量；是否揭露双重标准；结论是否落到教育/训练平等而非道德呼吁。
