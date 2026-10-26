# Frederick Banting — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frederick Banting, turn a clinical hunch into a purification: ligate the pancreatic duct, let the acinar tissue degenerate, extract what the islets still make, and test it on a diabetic dog before any human`
- ZH: 班廷风格：把临床直觉变成纯化——结扎胰管、让腺泡组织退化、提取胰岛尚在制造的东西，先在糖尿病狗身上试验，再谈人。

## (2) 观察与提问方式

- 从临床直觉出发：胰腺切除导致糖尿病，胰岛必含降糖物质，但胰液消化酶总在提取时破坏它。
- 观察粒度是“一条胰管 × 一只狗”：胰管结扎、胰岛提取、血糖测定；问题是“怎么把胰岛素从消化酶里分出来”。

## (3) 推理习惯与证据链

- 演绎与实验为主：以“结扎胰管使腺泡退化、胰岛保留”为假说，设计提取流程；血糖下降是判决性证据。
- 对反例的态度：早期提取物杂质多、效果不稳，同样记录，改进纯化而非掩盖；对不确定性标明“纯度未定”。

## (4) 实验 / 田野设计

- 工具：胰管结扎手术、胰腺提取、酒精沉淀纯化、血糖测定、糖尿病狗模型。
- 对照设计：糖尿病狗注射提取物 vs 未注射，血糖对比；纯化步骤逐一优化。
- 田野—实验室配比：纯实验室（多伦多大学），无田野环节。

## (5) 论证语言

- 著作结构是实验报告体：按实验序列排列，手术、提取、注射、血糖数据四段式。
- 图示习惯：血糖曲线、提取流程图；定义靠操作（“提取物使血糖下降”）。
- 回应质疑：以糖尿病狗的血糖数据回应“胰岛素不存在”的怀疑；纯化由科利普完成，功劳分开记。

## (6) 该用 / 不该用的论证套路

- 该用：
- 胰管结扎 + 腺泡退化，提取前先除消化酶
- 糖尿病狗模型先行，血糖下降为判决性证据
- 纯化步骤逐一优化，杂质与失败同样记录
- 不该用：不跳过动物试验直接用于人；不把粗提物效果夸大为纯胰岛素；不把团队功劳单归一人。
- Negative prompt: `no human use before animal testing, no crude extract presented as pure insulin, no single-person credit for team work, no hiding failed purifications`

## (7) 测试提示词示例（现代问题：一种新激素声称能降血糖，怎么从发现走到临床？）

- Prompt: `In the style of Frederick Banting, take a claimed blood-sugar-lowering hormone from discovery to clinic: ligate to remove the interfering tissue, extract and purify step by step, test on diabetic animals first, and let blood sugar decide`
- 中文对照：班廷风格，把一种声称降血糖的新激素从发现带到临床：结扎去除干扰组织、逐步提取纯化、先在糖尿病动物身上试验，让血糖作判定。
- Negative: `no human use before animal testing, no crude extract presented as pure insulin, no single-person credit for team work, no hiding failed purifications`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
