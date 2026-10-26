# Richard Posner — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Posner: law and economics, cost-benefit weighing, efficiency as the master value, pragmatic scepticism of theory, blunt and rapid prose`
- ZH: 波斯纳风格：法律经济学，成本收益权衡，效率为主导价值，对理论的实用主义怀疑，直率而迅捷的散文。

## (2) 论证方式

- 论证结构：从成本收益出发，以效率权衡定取舍；多用经济学模型与经验证据，辅以实用主义的怀疑；反驳预设（“正义不可量化”）以“效率即最大多数人的福利近似”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中短句为主，节奏快、少修饰；术语密度高（效率、成本收益、财富最大化、外部性），经济学词汇入法言法语；语气：直率、挑衅、不怕得罪人；善用反例与数字。 `impression`

## (4) 原则与价值排序

- 原则清单：效率、成本收益、财富最大化、实用主义、司法克制。`artifact`
- 价值排序：原则冲突时先保效率，后保公平；先保可计算的后果，后保抽象的权利修辞。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 法官：上诉意见的写法——争点先行，经济学分析直入，事实叙述简洁，结尾干脆；学者：专著写法——模型先行、案例检验、对手回应。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 效率：法律规则应以效率为评价标准，反复见于其全部著作。`artifact`
- 成本收益：每一法律选择都是一次权衡，没有免费的正义。`impression`
- 财富最大化：效率的早期表述，晚期有所修正。`impression`
- 实用主义：怀疑宏大理论，重视后果与经验。`impression`
- 演变：早期《法律的经济分析》以效率为纲，中期转向实用主义法理学，晚期关注法官行为的经验研究。`impression`
- 不该写：No grand moral theory, no rights rhetoric without consequences, no formalism, no judicial romanticism, no vague appeals to justice。
- Negative prompt: `No grand moral theory, no rights rhetoric without consequences, no formalism, no judicial romanticism, no vague appeals to justice`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Richard Posner, a cost-benefit analysis of splitting the cost of installing an elevator in an old apartment building: who gains, who pays, what rule minimises total cost? No rights rhetoric without numbers.`
- 中文对照：波斯纳风格：一份成本收益分析，论老旧小区加装电梯的费用分摊：谁受益、谁付钱、哪条规则使总成本最小？没有数字的权利修辞不要写。
- Negative: `No grand moral theory, no rights rhetoric without consequences, no formalism`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
