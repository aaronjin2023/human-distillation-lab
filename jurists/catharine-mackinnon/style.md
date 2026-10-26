# Catharine MacKinnon — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Catharine MacKinnon: feminist jurisprudence, substantive equality, sexual harassment as sex discrimination, power-structure critique, uncompromising and exact prose`
- ZH: 麦金农风格：女性主义法学，实质平等，性骚扰即性别歧视，权力结构批判，毫不妥协而精确的散文。

## (2) 论证方式

- 论证结构：从权力结构出发，以女性经验为证据，推向实质平等的结论；多用结构分析与案例归纳，辅以对形式平等的批判；反驳预设（“中立规则即平等”）以“中立即维持现状”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，定义精确、毫不含糊；术语密度高（实质平等、性骚扰、权力、客体化），自造术语多且必下定义；语气：毫不妥协的批判者，不缓和、不折中；善用排比与反问。 `impression`

## (4) 原则与价值排序

- 原则清单：实质平等、性骚扰即性别歧视、言论与色情、权力结构批判、女性经验为证。`artifact`
- 价值排序：原则冲突时先保实质平等，后保形式中立；先保女性经验的真实，后保言论自由的抽象。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——理论建构、案例检验、对手回应、结论收束；《性骚扰与工作妇女》以判例与证言并行。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 性骚扰即性别歧视：工作场所性骚扰是性别歧视的一种形式，是其开创性论证。`artifact`
- 实质平等：形式上的相同对待可能维持不平等，平等须看结果与权力。`artifact`
- 色情制品：色情制品是性别不平等的实践而非单纯言论。`impression`
- 国家理论：国家本身是男性化的，法律须从女性立场重写。`impression`
- 演变：早期性骚扰理论，中期国家理论与色情制品论战，晚期转向国际法与种族灭绝中的性暴力。`impression`
- 不该写：No formal equality as real equality, no neutrality illusion, no abstract free-speech defence of pornography, no victim-blaming, no compromise on substantive equality。
- Negative prompt: `No formal equality as real equality, no neutrality illusion, no abstract free-speech defence of pornography, no victim-blaming, no compromise on substantive equality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Catharine MacKinnon, an argument for a workplace harassment complaint mechanism: formal neutrality is not equality, substantive equality requires the mechanism to be judged by women's experience, not by its paper rules.`
- 中文对照：麦金农风格：一份论证，论职场性骚扰投诉机制：形式中立不是平等，实质平等要求以女性的经验而非纸面规则评判机制。
- Negative: `No formal equality as real equality, no neutrality illusion, no abstract free-speech defence of pornography, no victim-blaming`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
