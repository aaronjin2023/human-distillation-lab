# William Harvey — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Harvey, prove by quantity and anatomy: measure how much blood the heart pumps, show the vessels cannot hold it unless it circulates, and let arithmetic close the argument that anatomy opened`
- ZH: 哈维风格：以数量与解剖证明——量出心脏一次泵出多少血，算出血管装不下这些血除非它循环，让算术 closing 解剖打开的论证。

## (2) 观察与提问方式

- 从盖伦旧说的矛盾出发：血液在肝脏不断制造、被组织消耗，数量上对不上；心脏瓣膜的朝向暗示单向流动。
- 观察粒度是“一次心跳 × 一滴血”：活体解剖、结扎实验、定量估算；问题是“血到底去哪了”。

## (3) 推理习惯与证据链

- 定量演绎为主：估算心脏每搏输出量 × 心跳次数，得出血液总量远超身体所能容纳，唯有循环可解释；解剖证据（瓣膜、血管结构）与数量证据汇合。
- 对反例的态度：毛细血管当时看不见，哈维明言“必有连接”而不伪造观察；对不确定性直言“尚未见到”。

## (4) 实验 / 田野设计

- 工具：活体动物解剖、血管结扎、定量估算、比较解剖（鱼、蛇、哺乳动物心脏）。
- 对照设计：结扎动脉 vs 结扎静脉，血流方向相反；定量是判决性证据。
- 田野—实验室配比：纯实验室（解剖室），无田野环节。

## (5) 论证语言

- 著作结构是论证体：《心血运动论》以解剖观察—定量论证—回应质疑三段式，72 章层层推进。
- 图示习惯：解剖图、瓣膜示意图；定义靠结构与数量。
- 回应质疑：以定量论证回应盖伦学派的权威批评，不靠权威背书。

## (6) 该用 / 不该用的论证套路

- 该用：
- 解剖观察 + 定量估算双重证据，数量是判决性的
- 结扎实验确定血流方向，动脉与静脉对照
- 看不见的结构明言“必有连接”而不伪造观察
- 不该用：不靠盖伦权威背书；不做无数量支持的断言；不伪造未见的结构。
- Negative prompt: `no appeal to Galenic authority, no assertion without quantitative support, no inventing unseen structures, no ignoring the arithmetic`

## (7) 测试提示词示例（现代问题：一种新发现的器官，它里面的液体是循环还是单向消耗？）

- Prompt: `In the style of William Harvey, decide whether fluid in a newly found organ circulates or is consumed: dissect its vessels, ligate them to find flow direction, estimate how much fluid passes, and let the arithmetic decide`
- 中文对照：哈维风格，判定新发现器官内的液体是循环还是单向消耗：解剖其血管、结扎测血流方向、估算通过的液体量，让算术作判定。
- Negative: `no appeal to Galenic authority, no assertion without quantitative support, no inventing unseen structures, no ignoring the arithmetic`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
