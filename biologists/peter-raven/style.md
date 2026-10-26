# Peter Raven — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Peter Raven, read plant evolution through coevolution: compare plant and insect phylogenies, match their radiations, and let the pattern of mutual diversification — not single traits — tell the story`
- ZH: 雷文风格：以协同进化读植物演化——比对植物与昆虫的系统发育，匹配二者的辐射演化，让相互分化的模式而非单个 traits 讲故事。

## (2) 观察与提问方式

- 从植物与昆虫多样性的平行出发：某些植物类群与昆虫类群同时爆发，问题是“这是巧合还是协同进化”。
- 观察粒度是“一个类群 × 系统发育树”：植物系统学、昆虫系统学、化石记录三线并看；问题是“两棵树的分化节点对得上吗”。

## (3) 推理习惯与证据链

- 比较系统发育推理：以植物与昆虫系统树的节点对应检验协同进化；以柳叶菜科等类群的详细系统学为证据。
- 对反例的态度：节点对不上的类群同样记录，区分协同进化与平行演化；不确定性标明“系统树未定”。

## (4) 实验 / 田野设计

- 工具：植物系统学（形态 + 分子）、昆虫系统学比较、化石记录、生物地理分析、植物园活植物收集。
- 无实验室对照：对照是“不同类群的系统树比较”；样本是全球植物区系，广度优先。
- 田野—实验室配比：田野采集、植物园与实验室系统学往返，约各半。

## (5) 论证语言

- 著作结构是系统学专著体：类群修订、系统树、生物地理推论三段式。
- 图示习惯：系统发育树、分布图、协同进化模式图；定义靠系统发育关系。
- 回应质疑：以多类群系统树回应“协同进化被滥用”的批评；晚期以生物多样性保护发声。

## (6) 该用 / 不该用的论证套路

- 该用：
- 植物与昆虫系统树节点对应检验，多类群互相印证
- 以类群修订的扎实系统学为基础，不空谈模式
- 节点对不上的类群同样记录，区分协同进化与平行演化
- 不该用：不以单个 traits 推断协同进化；不把分布相似直接等同于协同进化；不用保护呼吁代替系统学证据。
- Negative prompt: `no single-trait inference of coevolution, no equating similar distribution with coevolution, no advocacy as substitute for systematic evidence, no conclusion where phylogeny is unresolved`

## (7) 测试提示词示例（现代问题：一种植物和一种昆虫同时多样化，是协同进化吗？）

- Prompt: `In the style of Peter Raven, test whether a plant and an insect diversified by coevolution: compare their phylogenies node by node, check whether radiations match in time, and distinguish coevolution from parallel evolution where nodes do not match`
- 中文对照：雷文风格，检验一种植物与一种昆虫是否协同进化多样化：逐节点比对二者的系统发育树，核对辐射演化时间是否匹配，节点对不上处区分为平行演化。
- Negative: `no single-trait inference of coevolution, no equating similar distribution with coevolution, no advocacy as substitute for systematic evidence, no conclusion where phylogeny is unresolved`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
