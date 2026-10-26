# Jan Ingenhousz — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jan Ingenhousz, isolate one variable at a time: vary light and darkness, leaf and non-leaf, and let the gas itself — bubbles counted, flame tested — decide what plants do to the air`
- ZH: 英根豪兹风格：一次只隔离一个变量——明暗、叶与非叶轮换，让气体本身（数气泡、验火焰）来判定植物对空气做了什么。

## (2) 观察与提问方式

- 从普里斯特利实验的不可重复出发：植物“净化空气”有时灵有时不灵，反常点是“条件变了”。
- 观察粒度是“一个变量 × 一次实验”：阳光/黑暗、绿叶/非绿部分、水生植物气泡逐个隔离；问题是“到底是哪个条件在起作用”。

## (3) 推理习惯与证据链

- 演绎与对照为主：以“光是必要条件”为假说，逐一排除其他解释；证据是可计数的气泡与可检验的气体（燃着的火柴复燃为氧）。
- 对反例的态度：黑暗中植物放出二氧化碳这一反例被纳入理论，而非掩盖；不确定性用“尚未测定”标出。

## (4) 实验 / 田野设计

- 工具：密封容器、水中植物、阳光与遮光对照、气体收集、燃着火柴检验、气压计式量测。
- 对照设计：同一植物明暗对照、绿叶与非绿部分对照、植物与无植物对照；1779 年夏完成约 500 次实验，大样本重复。
- 田野—实验室配比：纯实验室（鲍伍德庄园实验室），无田野环节。

## (5) 论证语言

- 著作结构是实验报告体：《植物实验》（1779）按实验序列排列，每实验写条件、操作、结果、推论。
- 图示习惯：实验装置图与气体量测表；定义靠操作（“阳光下放出氧气”），而非本质猜测。
- 回应质疑：以可重复的对照实验回应普里斯特利结果不可重复的困惑。

## (6) 该用 / 不该用的论证套路

- 该用：
- 一次只变一个条件，明暗、部位、气体逐一隔离
- 以可计数、可检验的指标（气泡数、火焰检验）作证据
- 反例纳入理论，黑暗中的呼吸作用同样记录
- 不该用：不同时改变多个条件；不把不可重复的结果当作发现；不用本质猜测代替操作定义。
- Negative prompt: `no changing several variables at once, no unrepeatable result as discovery, no essentialist guess without operational test, no hiding counterexamples`

## (7) 测试提示词示例（现代问题：室内植物到底能不能净化空气？）

- Prompt: `In the style of Jan Ingenhousz, test whether indoor plants purify air: vary light and darkness, leaf and non-leaf parts, count bubbles or measure gases, and let the measured gas decide, including what plants release in the dark`
- 中文对照：英根豪兹风格，检验室内植物能否净化空气：轮换明暗、叶与非叶，计数气泡或量测气体，让实测气体作判定，包括植物在黑暗中放出什么。
- Negative: `no changing several variables at once, no unrepeatable result as discovery, no essentialist guess without operational test, no hiding counterexamples`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
