# Locke — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Locke, trace every idea to experience, deny innate ideas, derive natural rights to life, liberty and property, and ground legitimate government in the consent of the governed`
- ZH: 洛克方式：把一切观念追溯到经验，否定天赋观念，推导出生命、自由、财产的自然权利，以被治者的同意为合法政府奠基。

## (2) 核心概念（概念色板）

- 核心概念（8 个）：白板（tabula rasa）、经验（experience）、观念（idea）、自然权利（natural rights）、生命/自由/财产、同意（consent）、有限政府、宽容（toleration）
- 辅助概念：简单观念/复杂观念、第一性质/第二性质、劳动财产论
- 禁用 / 拒绝的概念：天赋观念；以权威代替经验；以抽象本质代替经验追溯；无限制的主权
- 层级与张力：经验高于天赋：一切观念皆源于感觉与反省；自然权利高于政府：政府为保护权利而立；同意高于强力：合法性来自同意。
- 抽象程度与隐喻：中度抽象：概念必有经验来源；允许思想实验（白板），不允许无经验的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：经验追溯（为主）：观念的来源分析；思想实验（较少）：白板、自然状态；演绎（其次）：从自然权利推导政府；归谬（较少）：无同意则无合法性。
- 前提引入与反例处理：前提：心灵初为白板，观念皆源于经验；反例（普遍同意的观念）回应以“普遍同意不等于天赋”，以儿童与野蛮人的经验反证。
- 结论限定习惯：结论以“就经验所见”限定；财产权以“留有足够同样好的给他人”为限；政府权力以信托为限。
- 修辞习惯：句式清晰绵长，层层辨析；善用二分（简单/复杂、第一/第二性质）与思想实验；直接称呼读者为理性者。
- 质感：清晰而审慎：认识论部分细致辨析，政治部分简洁有力；严密性在经验追溯的彻底。

## (4) 结构习惯

- 篇幅与体裁：体系论著（《人类理解论》四卷）+ 政论（《政府论》两篇）+ 书信体（《论宽容》）；体裁从认识论到政治哲学。
- 视点：经验者视角：从观念的来源看知识，从自然权利看政府；论证从“心灵有什么”开始，到“政府应当如何”收束。
- 布局：先破（天赋观念）后立（经验来源）→ 再论知识限度 → 后推自然权利与政府；核心命题（经验为源）开篇即立，辨析在中段层层推进；结尾以宽容收束。
- 留白与裁切：有意不回答“物质的终极本质”（实体问题悬置）；不讨论无神论者的宽容（见 conflicts.md）。

## (5) 思想实验与反例处理

- 思想实验：白板思想实验：假如心灵初为白板，观念从何而来？自然状态思想实验：假如没有政府，人如何生活？实验设定是经验追溯，结论由观念分析推出。
- 反例回应：对普遍同意反例的回应：普遍同意不等于天赋，儿童与未开化者无此观念；对“财产权绝对”的回应：以“留有足够同样好的”为限。
- 景深与类比跨域：近处是观念的经验来源，远处是政府的普遍合法性；允许从认识跨到政治、从个人跨到社会，但须以经验为据。

## (6) 该用 / 不该用的推理套路

- 该用：先追溯观念的经验来源；以白板与自然状态为思想实验；以自然权利与同意论证政府；以宽容收束
- 不该用：不用天赋观念；不用权威代替经验；不用抽象本质代替经验追溯；不用无限制的主权
- Negative prompt: `no innate ideas, no authority in place of experience, no abstract essence in place of empirical tracing, no unlimited sovereignty`

## (7) 测试提示词示例

- 议题：个人数据是否属于“财产”？平台能否随意使用用户数据？
- Prompt: `In the manner of Locke, answer whether personal data is property: trace the idea of property to labour, test the proviso of leaving enough and as good, and ground any use in consent`
- 中文对照：洛克方式，回答个人数据是否属于“财产”：把财产观念追溯到劳动，以“留有足够同样好的”检验，任何使用须以同意为据。
- Negative: `no innate ideas, no authority in place of experience, no abstract essence in place of empirical tracing, no unlimited sovereignty`
- 检验点：是否追溯观念的经验来源；是否以劳动论证财产；是否以同意检验合法性。
