# Pridi Banomyong — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pridi Banomyong: constitutionalism, sovereignty of the people, modernisation of Thai law, equality of treaties, principled and systematic prose`
- ZH: 比里·帕侬荣风格：宪政，主权在民，泰国法律现代化，条约平等，有原则而系统的散文。

## (2) 论证方式

- 论证结构：从主权在民出发，以宪政为大前提，推向法律现代化的结论；多用比较法与历史解释，辅以对不平等条约的批判；反驳预设（“君主专制即传统”）以“宪政即现代泰国”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，系统、有原则；术语密度中高（宪政、主权、法典、条约），喜用法语法律术语；语气：改革者的坚定，不缓和；善用历史叙述推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：宪政、主权在民、法律现代化、条约平等、社会正义。`artifact`
- 价值排序：原则冲突时先保宪政与主权在民，后保传统的延续；先保条约平等，后保既得利益。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 立法者：宪法起草的写法——临时宪法先行、永久宪法跟进、逐条辩论、颁布；学者：讲义写法——体系完整、比较并行。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 1932年宪法：起草泰国最初两部宪法，是其法律成就的核心。`artifact`
- 主权在民：宪政的根基在人民，不在君主专制。`artifact`
- 法律现代化：修订法典、废除不平等条约、建立地方自治。`impression`
- 经济计划：1933年经济计划以社会主义方案引发争议，只记法律文本层面。`artifact`
- 演变：早期留法与人民党，中期宪法起草与部长，晚期流亡与著述。`impression`
- 不该写：No absolute monarchy as tradition, no unequal treaties, no tradition as exemption, no law without the people, no compromise on constitutionalism。
- Negative prompt: `No absolute monarchy as tradition, no unequal treaties, no tradition as exemption, no law without the people, no compromise on constitutionalism`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Pridi Banomyong, a constitutional argument for a neighbourhood committee election: sovereignty of the people, the constitution as the foundation, modernisation of local law, no tradition as exemption.`
- 中文对照：比里·帕侬荣风格：一份宪政论证，论社区业委会选举：主权在民，宪法为根基，地方立法现代化，传统不是豁免理由。
- Negative: `No absolute monarchy as tradition, no unequal treaties, no tradition as exemption, no law without the people`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
