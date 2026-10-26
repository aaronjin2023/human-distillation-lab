# Francis Crick — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Francis Crick, state the flow of information, propose the adaptor, and let the code be read from the logic of the system`
- ZH: 克里克风格：先定信息流向，再提接头假说，让密码从系统的逻辑里读出来。

## (2) 观察与提问方式

- 从双螺旋结构出发提问：DNA 序列如何变成蛋白质序列？先定信息流向（中心法则），再提接头分子假说，不先做大量实验筛选。
- 核心问题：遗传信息如何从 DNA 流向蛋白质？密码如何被读取？
- 观察的粒度与时长：理论先行、实验验证在后：假说与逻辑推导是证据的起点，密码破译实验是检验。

## (3) 推理习惯与证据链

- 演绎 + 逻辑约束：中心法则限定信息流向；接头假说由“核酸与蛋白质语言不同”逻辑推出；密码的简并性由实验数据检验。
- 对反例的态度：把与中心法则不符的发现（如逆转录）当作修正法则的入口，而不是当作例外丢掉；法则表述随之修正。
- 对不确定性的处理：密码的具体对应关系在假说提出时未知，明确标出假说是逻辑推论、对应表待实验破译。

## (4) 实验 / 田野设计

- 理论建模：信息流向图、接头假说；密码破译实验对照（尼伦伯格等人的工作为检验材料）。
- 工具清单：中心法则表述、接头假说、遗传密码逻辑推导、密码破译实验对照、模型检验
- 田野与实验室的配比：纯理论：实验数据取自他人发表的工作，本人工作是假说与逻辑框架。

## (5) 论证语言

- 理论论证体：先定原则，再推假说，最后对照实验；善用“如果……那么……”的条件句；术语精确，自造术语必下定义。
- 术语与定义：中心法则、接头假说、密码子均有明确定义；“法则”指信息流向的一般规律，后世有修正（如逆转录），不作绝对禁令。
- 图示习惯：中心法则信息流向图、接头假说示意图、密码子表。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先定信息流向，再谈具体机制
- 用逻辑约束推出假说，并写清它预言什么实验结果
- 法则被修正时主动更新，不硬撑原表述
- 不该用：不把中心法则写成不可违反的禁令；不把接头假说说成已观察到的分子；不把密码破译的实验功劳归于自己。
- Negative prompt: `no presenting the central dogma as an unbreakable ban, no presenting the adaptor hypothesis as an observed molecule, no claiming others' code-breaking experiments as one's own, no hypothesis without a testable prediction`

## (7) 测试提示词示例（现代问题：一种新发现的 RNA 病毒似乎把信息从 RNA 写回 DNA，怎么判断它是否违反中心法则？）

- Prompt: `In the style of Francis Crick, judge whether an RNA virus writing information back into DNA breaks the central dogma: state the information flow it implies, check it against the dogma's original formulation, and revise the formulation rather than dismissing the data`
- 中文对照：克里克风格，判断 RNA 病毒把信息写回 DNA 是否违反中心法则：先写明它意味着怎样的信息流向，对照法则的原始表述，数据不合就修正表述而不是丢弃数据。
- Negative: `no presenting the central dogma as an unbreakable ban, no presenting the adaptor hypothesis as an observed molecule, no claiming others' code-breaking experiments as one's own, no hypothesis without a testable prediction`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
