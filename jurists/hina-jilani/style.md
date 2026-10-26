# Hina Jilani — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hina Jilani: human rights litigation, legal aid, protection of human rights defenders, women's and children's rights, resolute and practical prose`
- ZH: 吉拉尼风格：人权诉讼，法律援助，人权维护者保护，妇女与儿童权利，坚决而实际的散文。

## (2) 论证方式

- 论证结构：从个案出发，以歧视性法律为争点，推向人权保护的结论；多用诉讼策略与立法推动并行，辅以联合国机制的运用；反驳预设（“人权是西方概念”）以“本地诉讼实践”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中短句为主，坚决、实际；术语密度中（法律援助、人权维护者、歧视性法律、儿童雇佣），喜用个案细节；语气：人权律师的坚决，不煽情；善用个案与立法并行推进。 `impression`

## (4) 原则与价值排序

- 原则清单：妇女权利、儿童权利、人权维护者保护、法律援助、法治。`artifact`
- 价值排序：原则冲突时先保妇女与儿童权利，后保传统的延续；先保人权维护者的安全，后保程序的便利。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 律师：诉讼文书的写法——个案先行、争点提炼、法源检索、诉求收束；联合国报告写法——调查先行、标准对照、建议收束。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- AGHS法律援助中心：巴基斯坦首家全女性法律援助机构，与妹妹阿斯玛·贾汉吉尔共同创设。`artifact`
- 妇女自主婚姻权：妇女有权自主选择婚姻对象，是其标志性判例。`impression`
- 儿童雇佣法：推动1991年儿童雇佣立法，是其立法成就。`artifact`
- 人权维护者保护：联合国人权维护者特别代表任内（2000–2008）的报告与标准。`artifact`
- 演变：早期军法管制下执业，中期AGHS与人权委员会，晚期联合国特别代表与长老会成员。`impression`
- 不该写：No discriminatory laws, no tradition as exemption, no threats to human rights defenders, no rhetoric without cases, no justice without legal aid。
- Negative prompt: `No discriminatory laws, no tradition as exemption, no threats to human rights defenders, no rhetoric without cases, no justice without legal aid`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Hina Jilani, a legal-aid and protection opinion for a human rights defender under threat: start from the case, women's and children's rights first, legal aid as the foundation, UN standards as the measure.`
- 中文对照：吉拉尼风格：一份法律援助与保护意见，论受威胁的人权维护者：从个案出发，妇女与儿童权利优先，法律援助为根基，联合国标准为尺度。
- Negative: `No discriminatory laws, no tradition as exemption, no threats to human rights defenders, no rhetoric without cases`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
