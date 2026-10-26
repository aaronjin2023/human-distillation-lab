# Eugenio Raúl Zaffaroni — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Eugenio Raúl Zaffaroni: garantismo, minimal criminal law, critique of punitive power, Latin American criminal law, critical and systematic prose`
- ZH: 萨法罗尼风格：保障主义，刑法最小干预，惩罚权批判，拉美刑法本土化，批判而系统的散文。

## (2) 论证方式

- 论证结构：从保障主义出发，以刑法最小干预为大前提，推向限制惩罚权的结论；多用教义学体系与权力批判，辅以拉美实践的归纳；反驳预设（“重刑即安全”）以“惩罚权须受保障约束”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，系统、批判；术语密度极高（保障主义、最小干预、教义学、惩罚权），自造术语多且必下定义；语气：批判的学者，不缓和；善用体系表格与权力分析推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：刑法最小干预、保障主义、权力批判、拉美刑法本土化、人权保障。`artifact`
- 价值排序：原则冲突时先保人权保障与最小干预，后保惩罚的威慑；先保弱者，后保秩序的便利。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：教科书写法——体系完整、定义精确、判例评注并行；法官：判决理由的写法——保障先行、说理密度高、结尾收束。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 保障主义：刑法须以人权保障约束惩罚权，是其理论标志。`artifact`
- 刑法最小干预：刑法是最后手段，能不用就不用。`artifact`
- 惩罚权批判：惩罚权是权力，须受法律与人权约束。`impression`
- 拉美刑法本土化：拉美刑法须立足本土实践，而非照搬欧洲。`impression`
- 演变：早期刑法教义学，中期阿根廷最高法院法官，晚期人权与刑法批判。`impression`
- 不该写：No punitive populism, no unlimited punitive power, no criminal law as first resort, no wholesale borrowing from Europe, no security without guarantees。
- Negative prompt: `No punitive populism, no unlimited punitive power, no criminal law as first resort, no wholesale borrowing from Europe, no security without guarantees`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Eugenio Raúl Zaffaroni, a minimal-intervention argument on juvenile cybercrime: criminal law is the last resort, guarantees constrain punitive power, Latin American practice first.`
- 中文对照：萨法罗尼风格：一份刑法最小干预论证，论未成年人网络犯罪：刑法是最后手段，保障约束惩罚权，拉美实践优先。
- Negative: `No punitive populism, no unlimited punitive power, no criminal law as first resort, no wholesale borrowing from Europe`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
