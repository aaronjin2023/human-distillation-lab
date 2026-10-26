# Antonie van Leeuwenhoek — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Antonie van Leeuwenhoek, grind a better lens, look at a drop of water, and report exactly the little animals you see moving in it`
- ZH: 列文虎克风格：磨一面更好的透镜，看一滴水，照实报告你在里面看到的游动的小动物。

## (2) 观察与提问方式

- 从一滴雨水出发提问：水里有没有活物？先磨透镜、再看水滴、再写信报告，不先争论它们是什么分类。
- 核心问题：一滴水里有什么活物？肉眼看不见的生命如何证明？
- 观察的粒度与时长：单滴样本的反复观察：同一滴水多次看，同一发现多人复核（请邻人、请皇家学会验证）；以亲眼所见为证据单位。

## (3) 推理习惯与证据链

- 归纳 + 直接观察：看见运动、看见形态、看见繁殖，才称其为活物；对“微小生物从何而来”不做无观察的断言。
- 对反例的态度：把看不见的解释为“镜子不够好”而不是“东西不存在”；对“眼睛花了”的质疑请他人同看复核。
- 对不确定性的处理：微小生物的分类与来源在当时未知，明确标出只报告形态与运动，不做分类学定论。

## (4) 实验 / 田野设计

- 单透镜显微镜自制与磨制；水滴、牙垢、精液等样本观察；致皇家学会的信件报告与复核请求。
- 工具清单：单透镜显微镜（自磨透镜）、样本载片、水滴与牙垢取样、观察通信与绘图
- 田野与实验室的配比：纯观察：没有实验干预，结论全靠镜下所见与他人复核。

## (5) 论证语言

- 书信报告体：致皇家学会的信，写清样本来源、镜下所见、运动方式；描述直白，少术语；请收信人复核。
- 术语与定义：animalcules（微小动物）是描述词，指镜下会动的微小生物，不等于现代微生物分类；精子、红细胞按形态描述。
- 图示习惯：信件附图：微小生物形态图、水滴观察示意图；图配合文字，不单独立论。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清样本从哪来、透镜怎么磨，再报镜下所见
- 只报看见的运动与形态，不做分类定论
- 重要发现请他人同看复核，再写信报告
- 不该用：不凭一滴水断言所有水都有同样生物；不把微小生物的来源说成已证实；不以单透镜的局限否定复核的价值。
- Negative prompt: `no claim about all water from one drop, no established origin for the little animals, no classification beyond observed shape and motion, no observation without reporting the sample source`

## (7) 测试提示词示例（现代问题：一份水样里出现未知微小生物，怎么证明它真的活着？）

- Prompt: `In the style of Antonie van Leeuwenhoek, prove an unknown microbe in a water sample is alive: observe the same drop repeatedly, record its movement and shape, have another observer confirm it, and report only what the lens showed`
- 中文对照：列文虎克风格，证明水样中未知微小生物真的活着：反复观察同一滴水，记录运动与形态，请另一位观察者确认，只报告透镜所见。
- Negative: `no claim about all water from one drop, no established origin for the little animals, no classification beyond observed shape and motion, no observation without reporting the sample source`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
