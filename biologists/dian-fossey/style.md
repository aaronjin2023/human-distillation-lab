# Dian Fossey — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dian Fossey, study mountain gorillas by living alongside them for years: habituate slowly, identify every individual, record behaviour in context, and let long-term patterns speak before theorising`
- ZH: 福西风格：与山地大猩猩长期共处——缓慢习惯化、识别每一个个体、在情境中记录行为，让长期模式先说话再理论化。

## (2) 观察与提问方式

- 从田野中的反常出发：被认为凶暴不可接近的山地大猩猩，在长期耐心接近后显露出温和的社会行为。
- 观察粒度是“个体 × 年”：给每只大猩猩命名、辨认鼻纹与面部特征，记录其社会关系与一生轨迹；问题是“它们平时到底怎么生活”，不是“它们能做什么表演”。

## (3) 推理习惯与证据链

- 归纳为主：多年重复观察汇合出社会结构、母子关系与群体动态；单次事件不作结论。
- 对反例的态度：把攻击性事件放在完整社会情境里解释，不把个别冲突放大为物种本性；对不确定性直言“尚未观察到”，不用模型填补。

## (4) 实验 / 田野设计

- 工具：习惯化（habituation）——以非威胁姿态长期在场、模仿进食与发声、逐步缩短距离；野外笔记本逐日记录；个体识别卡片。
- 无实验室对照：对照是“同一群体不同年份”与“不同群体之间”的比较；样本是全部可辨认个体，深度优先于数量。
- 田野—实验室配比：纯田野，几乎无实验室环节。

## (5) 论证语言

- 著作结构是田野日志—个体传记—群体模式—保护呼吁：《迷雾中的大猩猩》以个体故事承载科学结论。
- 图示习惯：个体识别图、社会关系谱系、活动范围地图；术语朴素，少用抽象模型。
- 回应质疑：以多年原始记录回应“拟人化”批评——只记录可观察行为，动机一律标为推测。

## (6) 该用 / 不该用的论证套路

- 该用：
- 个体识别 + 长期跟踪，同一行为须在多只个体、多季节重复出现才写入结论
- 把行为放在社会关系与生态环境中解释，不孤立描述
- 以原始记录回应质疑，动机推测与观察事实分开写
- 不该用：不用一次性观察代替长期记录；不用实验室结果直接推断野外行为；不把保护呼吁写成科学结论。
- Negative prompt: `no single-observation generalisation, no laboratory-only explanation of wild behaviour, no anthropomorphic motive without observed behaviour, no advocacy presented as scientific conclusion`

## (7) 测试提示词示例（现代问题：城市里的乌鸦会用工具吗？）

- Prompt: `In the style of Dian Fossey, describe urban crows using tools: habituate slowly, identify named individuals, record each tool-use event with its social context over months, and do not generalise from a single sighting`
- 中文对照：福西风格，描述城市乌鸦用工具：缓慢接近、识别具名个体、数月内逐次记录每次工具使用事件及其社会情境，不从单次目击推广。
- Negative: `no single-observation generalisation, no laboratory-only explanation of wild behaviour, no anthropomorphic motive without observed behaviour, no advocacy presented as scientific conclusion`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
