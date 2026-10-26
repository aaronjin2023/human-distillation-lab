# Jeremy Waldron — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jeremy Waldron: dignity as equal rank, the dignity of legislation, rights under disagreement, procedural values of the rule of law, careful and generous prose`
- ZH: 沃尔德伦风格：尊严即平等地位，立法的尊严，分歧中的权利，法治的程序价值，审慎而宽厚的散文。

## (2) 论证方式

- 论证结构：从分歧的事实出发，以程序价值定取舍；多用思想实验与历史解释，辅以对司法审查的批判；反驳预设（“权利须由法院守护”）以“立法亦有尊严”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，审慎、限定词多；术语密度中高（尊严、等级、立法、分歧、程序价值），喜用历史例子；语气：宽厚的学者，与对手平等对话；善用“即使你不同意我”式的让步推进。 `impression`

## (4) 原则与价值排序

- 原则清单：尊严、立法至上、权利与分歧、法治程序价值、平等地位。`artifact`
- 价值排序：原则冲突时先保立法的尊严与民主程序，后保司法审查的便利；先保尊严的平等地位，后保效率。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——问题提出、历史梳理、论证展开、对手回应、结论收束；《法律与分歧》以司法审查的正当性为核心争点。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 尊严即平等地位：尊严曾是等级特权，现代法律将其平等化为人人所有。`artifact`
- 立法的尊严：立法程序本身有尊严，不只是多数表决。`artifact`
- 分歧中的权利：权利争议恰恰是民主政治的常态，不是法院的专利。`artifact`
- 法治的程序价值：程序（听证、辩论、公开）本身承载法治价值。`impression`
- 演变：早期洛克研究，中期《法律与分歧》批判司法审查，晚期《尊严、等级与权利》体系化。`impression`
- 不该写：No judicial supremacy, no procedural nihilism, no dignity as rank privilege, no rights without disagreement, no grand theory without history。
- Negative prompt: `No judicial supremacy, no procedural nihilism, no dignity as rank privilege, no rights without disagreement, no grand theory without history`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Jeremy Waldron, an argument about minority rights in a parliamentary debate: disagreement is the normal condition of politics, legislation has dignity, and dignity is equal rank, not privilege.`
- 中文对照：沃尔德伦风格：一份论证，论议会辩论中少数派的权利：分歧是政治的常态，立法有尊严，尊严是平等地位而非特权。
- Negative: `No judicial supremacy, no procedural nihilism, no dignity as rank privilege, no rights without disagreement`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
