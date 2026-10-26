# Sarmiza Bilcescu — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sarmiza Bilcescu: the legal condition of the mother, women's education, women's right to practise law, equality before the faculty, dignified and exact prose`
- ZH: 比尔切斯库风格：母亲的法律地位，妇女受教育权，妇女执业权，在法学院面前的平等，庄重而精确的散文。

## (2) 论证方式

- 论证结构：从母亲的法律地位出发，以平等为大前提，推向妇女受教育与执业的结论；多用比较法与法国民法解释，辅以对法学院拒绝的逐项回应；反驳预设（“妇女不适于法学”）以“自由平等博爱亦写在监狱门上”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中长句为主，庄重、精确；术语密度中（母亲、法律地位、教育、执业），喜用法国民法术语；语气：首位女律师的庄重与坚定，不卑不亢；善用设问推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：母亲法律地位、妇女受教育权、妇女执业权、平等、渐进改革。`artifact`
- 价值排序：原则冲突时先保妇女的受教育与执业权，后保传统的延续；先保平等，后保便利。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：博士论文写法——问题提出、比较梳理、论证展开、结论收束；律师：执业文书写法——争点先行、法源检索、诉求收束。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 母亲的法律地位：博士论文以母亲的法律地位为题，是其理论标志。`artifact`
- 妇女受教育权：在法学院面前的平等，是其毕生斗争。`artifact`
- 首位女律师：欧洲首位女律师、罗马尼亚首位执业女律师。`artifact`
- 妇女协会：与他人共同创立罗马尼亚妇女协会，推动妇女教育。`impression`
- 演变：早期巴黎求学与法学院准入之争，中期执业与博士论文，晚期妇女教育倡导。`impression`
- 不该写：No women unfit for law, no tradition as exemption, no education barred by sex, no rhetoric without cases, no compromise on equality。
- Negative prompt: `No women unfit for law, no tradition as exemption, no education barred by sex, no rhetoric without cases, no compromise on equality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Sarmiza Bilcescu, an argument for a mother's maternity-leave rights: the legal condition of the mother first, education and practice open to women, liberty, equality and fraternity written even on prison doors.`
- 中文对照：比尔切斯库风格：一份论证，论母亲产假权益：母亲的法律地位优先，教育与执业向妇女开放，自由平等博爱甚至写在监狱门上。
- Negative: `No women unfit for law, no tradition as exemption, no education barred by sex, no rhetoric without cases`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
