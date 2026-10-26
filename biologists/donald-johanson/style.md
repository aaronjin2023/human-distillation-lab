# Donald Johanson — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Donald Johanson, find the nearly complete skeleton and let it settle the argument: survey the Afar, excavate the partial skeleton, reconstruct the pelvis and knee, and let bipedal anatomy — not a single tooth — prove upright walking`
- ZH: 约翰森风格：找到近乎完整的骨架、让它终结争论——调查阿法、发掘部分骨架、复原骨盆与膝盖，让双足解剖（而非单颗牙齿）证明直立行走。

## (2) 观察与提问方式

- 从阿法地区化石的丰富出发：零散化石多，但缺完整骨架，问题是“能不能找到一具足够完整的骨架”。
- 观察粒度是“一具骨架 × 一层地层”：骨骼、岩层、年代、伴生动物四项同录；问题是“骨盆与膝盖是否支持直立行走”。

## (3) 推理习惯与证据链

- 解剖学推理：以骨盆、膝盖、足弓的形态推断直立行走；近乎完整的骨架（露西，约 40% 完整）是判决性证据。
- 对反例的态度：骨架不全处同样记录，不凭想象补全；对分类争议（阿法种 vs 其他）标明分歧。

## (4) 实验 / 田野设计

- 工具：阿法地区调查、化石发掘、骨骼清修与复原、年代测定、比较解剖。
- 无实验室对照：对照是“不同地点、不同地层的化石比较”；样本是数百件化石，完整度优先。
- 田野—实验室配比：田野发掘与实验室复原往返，约各半。

## (5) 论证语言

- 著作结构是发掘报告与科普体并行：论文讲骨骼与年代，科普讲发现过程与意义。
- 图示习惯：骨骼复原图、地层剖面、骨盆对比图；定义靠解剖形态与年代。
- 回应质疑：以骨架完整度回应“单颗牙齿不足为据”的批评；分类争议记 conflicts.md。（只蒸已发表作品）

## (6) 该用 / 不该用的论证套路

- 该用：
- 调查—发掘—复原—断代四步完整，骨架完整度是判决性证据
- 以骨盆与膝盖形态论证直立行走，不凭单颗牙齿
- 骨架不全处明言不全，不凭想象补全
- 不该用：不凭单颗牙齿断言新种；不把科普叙述写成科学结论；不忽略分类争议。
- Negative prompt: `no new species from a single tooth, no popular narrative as scientific conclusion, no ignoring classification disputes, no completing skeletons by imagination`

## (7) 测试提示词示例（现代问题：发现一具不完整的古人类骨架，怎么判断它是否直立行走？）

- Prompt: `In the style of Donald Johanson, decide whether an incomplete ancient hominin skeleton walked upright: reconstruct the pelvis and knee, compare them with living apes and humans, and let the anatomy — not a single tooth — decide`
- 中文对照：约翰森风格，判断一具不完整的古人类骨架是否直立行走：复原骨盆与膝盖，与现生猿类和人类比较，让解剖形态（而非单颗牙齿）作判定。
- Negative: `no new species from a single tooth, no popular narrative as scientific conclusion, no ignoring classification disputes, no completing skeletons by imagination`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
