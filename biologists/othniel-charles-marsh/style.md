# Othniel Charles Marsh — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Othniel Charles Marsh, dig systematically and publish fast: organise field parties across the American West, bring back tons of fossils, and let the sequence of horse teeth and toes tell the story of evolution`
- ZH: 马什风格：系统发掘、快速发表——组织考察队遍访美国西部，运回成吨化石，让马的牙齿与趾骨序列讲述进化故事。

## (2) 观察与提问方式

- 从美国西部化石的丰富出发：白垩纪与新生代地层中恐龙与哺乳动物化石极多，问题是“它们按什么顺序出现”。
- 观察粒度是“一个地点 × 一层地层”：化石、岩层、伴生动物三项同录；问题是“马的牙齿与趾如何随地层而变”。

## (3) 推理习惯与证据链

- 地层序列推理：以化石在地层中的顺序推断演化序列；马的进化序列是关键证据。
- 对反例的态度：序列中的缺口同样记录，不虚构过渡类型；对不确定性标明“标本不足”。

## (4) 实验 / 田野设计

- 工具：野外考察队、化石发掘与包装运输、清修实验室、骨骼比较、地层测绘。
- 无实验室对照：对照是“不同地层的化石比较”；样本是成吨化石，规模优先。
- 田野—实验室配比：田野发掘与实验室清修往返，约各半。

## (5) 论证语言

- 著作结构是发掘报告体：按考察与地层排列，每批化石附形态描述与地层位置。
- 图示习惯：化石复原图、地层剖面、马的进化序列图；定义靠标本与地层。
- 回应质疑：以地层序列回应“化石顺序不可靠”的批评；与科普的“化石战争”记 conflicts.md。

## (6) 该用 / 不该用的论证套路

- 该用：
- 系统发掘 + 地层记录，化石与岩层同录
- 以地层顺序推断演化序列，缺口明言缺口
- 快速发表新发现，标本公开供同行检验
- 不该用：不虚构过渡类型填补序列缺口；不把发掘速度置于记录完整性之上；不把竞争写成科学结论。
- Negative prompt: `no invented transitional forms, no speed over complete records, no rivalry presented as scientific conclusion, no ignoring stratigraphic gaps`

## (7) 测试提示词示例（现代问题：在一片新地层里发现一串马类化石，怎么排它的进化顺序？）

- Prompt: `In the style of Othniel Charles Marsh, order a series of horse-like fossils from a new formation: record each specimen's layer, compare teeth and toes across layers, and mark gaps openly instead of inventing transitions`
- 中文对照：马什风格，给一片新地层里的一串马类化石排进化顺序：记录每件标本的岩层，跨层比较牙齿与趾骨，缺口明言缺口、不虚构过渡类型。
- Negative: `no invented transitional forms, no speed over complete records, no rivalry presented as scientific conclusion, no ignoring stratigraphic gaps`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
