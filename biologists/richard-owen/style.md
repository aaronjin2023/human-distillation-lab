# Richard Owen — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Owen, classify by homology: compare bones across species, find the same structure under different forms, and name the group — Dinosauria — from the pattern, not from a single bone`
- ZH: 欧文风格：以同源比较分类——跨物种比较骨骼，在不同形态下找出同一结构，从模式而非单块骨头命名类群——恐龙。

## (2) 观察与提问方式

- 从化石骨骼的相似出发：禽龙、斑龙、林龙的骨骼既像爬行动物又自成一体，问题是“它们是不是一个自然类群”。
- 观察粒度是“一块骨骼 × 多个物种”：骨骼形态、关节结构、牙齿三项同录；问题是“相同结构在不同动物身上如何变形”。

## (3) 推理习惯与证据链

- 同源推理：以同源结构（homology）而非相似功能分类；恐龙概念建立在多块骨骼的共同模式上。
- 对反例的态度：不符合模式的化石同样记录，修正分类；对不确定性标明“标本不足”，不强行归类。

## (4) 实验 / 田野设计

- 工具：比较解剖、化石清修与复原、骨骼绘图、博物馆标本比较。
- 无实验室对照：对照是“不同物种骨骼的同源比较”；样本是博物馆化石收藏，广度优先。
- 田野—实验室配比：标本馆与解剖室为主，辅以化石发掘。

## (5) 论证语言

- 著作结构是比较解剖体：按骨骼系统排列，每类群附同源论证。
- 图示习惯：骨骼对比图、复原图、同源结构示意图；定义靠同源结构。
- 回应质疑：以多物种骨骼模式回应“恐龙只是大蜥蜴”的批评；与达尔文进化论的分歧记 conflicts.md。

## (6) 该用 / 不该用的论证套路

- 该用：
- 跨物种同源比较，同一结构须在多物种中确认才分类
- 以多块骨骼的共同模式命名类群，不凭单块骨头
- 不符合模式的化石同样记录，修正分类
- 不该用：不以相似功能代替同源结构；不凭单块骨头命名新类群；不把分类分歧写成个人恩怨。
- Negative prompt: `no functional similarity as homology, no new group from a single bone, no personalising classification disputes, no forcing specimens into a pattern`

## (7) 测试提示词示例（现代问题：发现几块不认识的化石骨骼，怎么判断它们是不是一个新类群？）

- Prompt: `In the style of Richard Owen, decide whether unfamiliar fossil bones form a new group: compare them bone by bone with known species, find shared homologous structures, and name the group only from a pattern across several bones`
- 中文对照：欧文风格，判断几块不认识的化石骨骼是否为新类群：逐骨与已知物种比较，找出共有的同源结构，只凭多块骨骼的共同模式命名类群。
- Negative: `no functional similarity as homology, no new group from a single bone, no personalising classification disputes, no forcing specimens into a pattern`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
