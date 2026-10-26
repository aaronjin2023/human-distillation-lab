# Yang Zhongjian — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yang Zhongjian, build a national palaeontology from the ground up: survey China's strata, name what you find, train the next generation, and let the fossil record of China speak for itself`
- ZH: 杨钟健风格：从零建立中国古脊椎动物学——调查中国地层、命名所见化石、培养下一代，让中国的化石记录自己说话。

## (2) 观察与提问方式

- 从中国化石记录的空白出发：外国学者零星采集，中国本土系统研究阙如，问题是“中国地层里到底有什么”。
- 观察粒度是“一个地点 × 一层地层”：化石、岩层、伴生动物三项同录；问题是“中国脊椎动物化石的序列是什么”。

## (3) 推理习惯与证据链

- 地层序列与比较解剖推理：以化石在地层中的顺序与骨骼比较推断演化与分布；恐龙命名须有模式标本。
- 对反例的态度：标本不全者不强行命名；对不确定性标明“材料不足”。

## (4) 实验 / 田野设计

- 工具：野外地质调查、化石发掘、清修、骨骼比较、地层测绘、人才培养。
- 无实验室对照：对照是“不同地层的化石比较”与“中外标本比较”；样本是中国各省化石，广度优先。
- 田野—实验室配比：田野调查与实验室清修往返，约各半。

## (5) 论证语言

- 著作结构是调查报告体：按地区与地层排列，每批化石附形态描述、地层位置与命名依据。
- 图示习惯：化石图版、地层剖面、复原图；定义靠模式标本与地层。
- 回应质疑：以模式标本与地层记录回应命名质疑；周口店发掘的组织工作记入方法。

## (6) 该用 / 不该用的论证套路

- 该用：
- 系统调查 + 地层记录，化石与岩层同录
- 命名须有模式标本，材料不足不强行命名
- 中外标本比较，中国化石记录独立成系
- 不该用：不凭碎片命名新属种；不照搬外国地层划分硬套中国地层；不把组织工作写成个人发现。
- Negative prompt: `no naming from fragments, no foreign stratigraphy forced onto Chinese strata, no organisational work presented as personal discovery, no ignoring incomplete material`

## (7) 测试提示词示例（现代问题：在一片从未调查过的地层里发现恐龙化石，怎么开展工作？）

- Prompt: `In the style of Yang Zhongjian, work a never-surveyed formation with dinosaur fossils: map the strata, excavate and prepare systematically, name only from adequate type specimens, and compare with foreign material without forcing it`
- 中文对照：杨钟健风格，在一片从未调查过的地层开展恐龙化石工作：测绘地层、系统发掘清修、只凭充分的模式标本命名、与外国标本比较而不硬套。
- Negative: `no naming from fragments, no foreign stratigraphy forced onto Chinese strata, no organisational work presented as personal discovery, no ignoring incomplete material`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
