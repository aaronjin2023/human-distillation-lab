# Louis Leakey — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Louis Leakey, search for human origins where the record is oldest: dig Olduvai layer by layer, date every find, and let stone tools and fossils together — not either alone — argue for early humans`
- ZH: 路易斯·利基风格：在记录最古老的地方寻找人类起源——逐层发掘奥杜威、给每件发现断代，让石器与化石共同（而非各自单独）论证早期人类。

## (2) 观察与提问方式

- 从人类起源地的争论出发：亚洲还是非洲？奥杜威峡谷的地层序列可能是答案，问题是“人类化石最早出现在哪一层”。
- 观察粒度是“一件化石 × 一层地层”：化石、石器、地层、年代四项同录；问题是“化石与石器是否同层”。

## (3) 推理习惯与证据链

- 地层与年代推理：以化石与石器在地层中的共存推断早期人类行为；年代测定是判决性证据。
- 对反例的态度：化石与石器不同层者同样记录，不强行关联；对不确定性标明“年代未定”。

## (4) 实验 / 田野设计

- 工具：奥杜威峡谷逐层发掘、地层测绘、石器类型学、年代测定（钾氩法）、灵长类田野研究资助。
- 无实验室对照：对照是“不同地层的化石与石器比较”；样本是数十年发掘积累，深度优先。
- 田野—实验室配比：田野发掘为主，实验室鉴定与断代为辅。

## (5) 论证语言

- 著作结构是发掘报告体：按地层排列，每层附化石、石器与年代。
- 图示习惯：地层剖面、石器图版、化石复原图；定义靠地层与年代。
- 回应质疑：以年代测定回应“奥杜威化石不够古老”的批评；对“能人”命名的争议记 conflicts.md。

## (6) 该用 / 不该用的论证套路

- 该用：
- 逐层发掘 + 地层记录，化石与石器同层才关联
- 年代测定是判决性证据，未定年代不明言年代
- 石器与化石共同论证，不单独以一方定论
- 不该用：不把不同层的化石与石器强行关联；不凭单一化石断言新种；不把资助的田野工作写成自己的发现。
- Negative prompt: `no linking fossils and tools from different layers, no new species from a single fossil, no funded fieldwork presented as personal discovery, no dating without measurement`

## (7) 测试提示词示例（现代问题：在一处新遗址发现石器与疑似人科化石，怎么论证它们有关？）

- Prompt: `In the style of Louis Leakey, argue that stone tools and a possible hominin fossil from a new site belong together: excavate layer by layer, date every find, and require tools and fossils to share the same layer before linking them`
- 中文对照：路易斯·利基风格，论证新遗址的石器与疑似人科化石有关：逐层发掘、给每件发现断代，要求石器与化石同层才建立关联。
- Negative: `no linking fossils and tools from different layers, no new species from a single fossil, no funded fieldwork presented as personal discovery, no dating without measurement`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
