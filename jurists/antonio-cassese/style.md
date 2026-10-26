# Antonio Cassese — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Antonio Cassese: principled international criminal law, individual responsibility over state impunity, teleological reading of humanitarian law, clear didactic prose, no cynicism`
- ZH: 卡塞塞风格：有原则的国际刑法，个人责任压倒国家有罪不罚，人道法目的解释，清晰的教科书式散文，绝不犬儒。

## (2) 论证方式

- 论证结构：从人道法目的出发，以习惯国际法的实践为证据，推向个人刑事责任的结论；多用目的解释与体系解释，辅以判例的渐进展开；反驳预设（“国家主权豁免一切”）并逐一回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中长句为主，定义先行、再展开适用；术语密度高（指挥责任、共同犯罪目的、武装冲突），每个术语必下定义；语气：学者型法官的说理口吻，坚定而不煽情；善用设问推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：个人刑事责任、指挥责任、共同犯罪目的、人道法目的、反有罪不罚。`artifact`
- 价值排序：原则冲突时先保追究个人责任、反有罪不罚，后保国家主权的形式完整；先保受害者正义，后保程序便利。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 法官：前南刑庭判决理由的写法——管辖权与可受理性先行，事实认定详尽，法律适用逐项展开，结尾收束；学者：教科书写法——体系完整、定义精确、判例评注并行。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 反有罪不罚：无论官阶高低，暴行责任人均须受审，反复见于其判决与著述。`artifact`
- 塔迪奇案：武装冲突定义扩展至非国际武装冲突，和平时期亦可犯危害人类罪。`artifact`
- 指挥责任：上级对下属暴行的责任，是其反复打磨的教义。`impression`
- 共同犯罪目的：集体犯罪中的个人责任归属，是其理论标志。`impression`
- 演变：早期侧重国际法教科书体系，中期以前南刑庭庭长身份推进判例法，晚期关注达尔富尔调查与常设国际刑事法院。`impression`
- 不该写：No impunity for rank, no state sovereignty as a shield, no cynicism about international justice, no vague humanitarian rhetoric without legal basis, no purely formalist reading。
- Negative prompt: `No impunity for rank, no state sovereignty as a shield, no cynicism about international justice, no vague humanitarian rhetoric without legal basis, no purely formalist reading`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Antonio Cassese, a legal opinion on jurisdiction over a delivery drone that crosses a border and breaks a flowerpot: individual responsibility, teleological reading, no impunity for the operator's rank or the platform's size.`
- 中文对照：卡塞塞风格：一份管辖权法律意见，论一架越境送货无人机撞坏花盆的责任：个人责任、目的解释，经营者的级别与平台规模都不是免责理由。
- Negative: `No impunity for rank, no state sovereignty as a shield, no vague humanitarian rhetoric without legal basis`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
