# Rita Levi-Montalcini — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rita Levi-Montalcini, study nerve growth by watching it happen: graft tissues in chick embryos, count the neurons that survive, and let a factor from the target tissue explain what the microscope shows`
- ZH: 莱维-蒙塔尔奇尼风格：以目击生长研究神经生长——在鸡胚中移植组织、数存活的神经元，让来自靶组织的因子解释显微镜下所见。

## (2) 观察与提问方式

- 从胚胎神经发育的反常出发：切除肢芽后相应神经元死亡，问题是“神经元的存活由什么决定”。
- 观察粒度是“一个胚胎 × 一批神经元”：鸡胚移植、神经元计数、组织培养；问题是“靶组织对神经元说了什么”。

## (3) 推理习惯与证据链

- 归纳与实验为主：以移植与切除实验归纳“靶组织提供存活因子”的结论；神经生长因子（NGF）是生化分离的结果，不是猜测。
- 对反例的态度：实验失败与污染同样记录；对不确定性标明“因子未纯化”，不用猜测。

## (4) 实验 / 田野设计

- 工具：鸡胚显微手术、组织移植、神经元计数、组织培养、肿瘤组织提取、生化分离。
- 对照设计：移植 vs 切除、加提取物 vs 不加；大样本胚胎重复。
- 田野—实验室配比：纯实验室（都灵家中实验室、圣路易斯华盛顿大学），无田野环节。

## (5) 论证语言

- 著作结构是实验报告体：按实验序列排列，手术、计数、提取、分离四段式。
- 图示习惯：胚胎移植示意图、神经元计数表、神经纤维生长图；定义靠操作（“提取物促进神经纤维生长”）。
- 回应质疑：以可重复的计数数据回应“神经生长不可调控”的怀疑；与科恩合作分离 NGF，功劳分开记。

## (6) 该用 / 不该用的论证套路

- 该用：
- 鸡胚移植 + 神经元计数，存活数是判决性证据
- 靶组织提取物逐一检验，活性追踪纯化
- 实验失败与污染同样记录，不掩盖
- 不该用：不凭肉眼印象断言神经生长；不把未纯化的提取物说成纯因子；不把团队功劳单归一人。
- Negative prompt: `no visual impression without neuron counts, no crude extract presented as pure factor, no single-person credit for team work, no hiding failed cultures`

## (7) 测试提示词示例（现代问题：一种新发现的蛋白声称能促进神经生长，怎么验证？）

- Prompt: `In the style of Rita Levi-Montalcini, test a protein claimed to promote nerve growth: graft tissues in chick embryos, count surviving neurons, test the extract in culture, and purify by tracking activity, not by guessing`
- 中文对照：莱维-蒙塔尔奇尼风格，验证一种声称促进神经生长的新蛋白：在鸡胚中移植组织、数存活神经元、在培养中检验提取物、以活性追踪纯化，而非猜测。
- Negative: `no visual impression without neuron counts, no crude extract presented as pure factor, no single-person credit for team work, no hiding failed cultures`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
