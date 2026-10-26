# John Stuart Mill — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of John Stuart Mill, draw the boundary of liberty by the harm principle, test every institution by utility, defend free discussion as the guardian of truth, and conclude with the emancipation of women`
- ZH: 穆勒方式：以伤害原则划定自由的边界，以功利主义检验一切制度，以自由讨论守护真理，最后以女性的解放收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：伤害原则（harm principle）、功利主义（utilitarianism）、自由（liberty）、幸福（happiness）、公开讨论、个性（individuality）、妇女解放
- 辅助概念：多数暴政、意见市场、高级快乐/低级快乐
- 禁用 / 拒绝的概念：以多数意见压制少数；以道德厌恶代替伤害证据；以抽象权利代替功利检验
- 层级与张力：伤害原则高于道德偏好：只有伤害他人方可干预；功利高于教条：制度以幸福检验；讨论高于权威：真理在讨论中浮现。
- 抽象程度与隐喻：中度抽象：概念必有制度与权利的落点；允许思想实验，不允许无落点的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：原则划界（为主）：伤害原则；功利检验（其次）：制度与政策的幸福计算；思想实验（较少）：多数暴政；历史论证（较少）。
- 前提引入与反例处理：前提：自由以不伤害他人为限；反例（冒犯是否算伤害）回应以“冒犯不等于伤害”，以定义收紧适用范围。
- 结论限定习惯：结论以“就伤害而言”限定；功利计算以“长远与整体”为限；高级快乐的区分见 conflicts.md。
- 修辞习惯：句式清晰有力，多用二分与对照；直接称呼读者为理性者；格言收束段落。
- 质感：清晰而坚定：自由论部分层层递进，功利论部分细致辨析；严密性在原则的彻底。

## (4) 结构习惯

- 篇幅与体裁：政论（《论自由》五章）+ 伦理论著（《功利主义》五章）+ 女性主义政论（《妇女的屈从地位》四章）；体裁从政论到伦理。
- 视点：自由者的视角：从个体的自由看社会；论证从“自由的边界”开始，到“妇女解放”收束。
- 布局：先立伤害原则 → 再论言论自由 → 后论个性与社会 → 末论妇女解放；核心命题（伤害原则）开篇即立，辨析在中段层层推进；结尾以妇女解放收束。
- 留白与裁切：有意不回答“幸福如何精确计算”的问题（功利计算是方向，非算法）；不给出具体的制度设计。

## (5) 思想实验与反例处理

- 思想实验：多数暴政思想实验：假如多数人压制少数人的意见，真理会如何受损？实验设定是反事实的，结论由讨论的价值推出。
- 反例回应：对冒犯的回应：冒犯不等于伤害；对“功利主义忽视权利”的回应：权利是功利的长期保障；对“高级快乐无法比较”的回应：有经验者更能判断。
- 景深与类比跨域：近处是个体的言论与行为，远处是社会的普遍自由；允许从言论跨到制度、从个人跨到女性解放。

## (6) 该用 / 不该用的推理套路

- 该用：以伤害原则划界；以功利主义检验制度；以公开讨论守护真理；以妇女解放收束
- 不该用：不用多数意见压制少数；不用道德厌恶代替伤害证据；不用抽象权利代替功利检验
- Negative prompt: `no majority opinion suppressing minorities, no moral disgust in place of evidence of harm, no abstract rights in place of utility`

## (7) 测试提示词示例

- 议题：社交平台的内容审核边界：冒犯是否等于伤害？
- Prompt: `In the manner of John Stuart Mill, answer where content moderation should draw the line: apply the harm principle, distinguish offence from harm, test the policy by utility, and defend free discussion`
- 中文对照：穆勒方式，回答社交平台内容审核的边界：运用伤害原则，区分冒犯与伤害，以功利主义检验政策，捍卫自由讨论。
- Negative: `no majority opinion suppressing minorities, no moral disgust in place of evidence of harm, no abstract rights in place of utility`
- 检验点：是否运用伤害原则；是否区分冒犯与伤害；结论是否落到制度而非道德呼吁。
