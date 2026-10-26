# Carlos Calvo — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carlos Calvo: the Calvo Doctrine, sovereign equality, non-intervention, exhaustion of local remedies, encyclopaedic and systematic prose`
- ZH: 卡尔沃风格：卡尔沃主义，主权平等，不干涉，用尽当地救济，百科全书式而系统的散文。

## (2) 论证方式

- 论证结构：从主权平等出发，以不干涉为大前提，推向用尽当地救济的结论；多用条约实践与判例归纳，辅以词典式的定义；反驳预设（“外国人可诉诸外交保护”）以“国民待遇即平等”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句定义为主，系统、完备；术语密度极高（主权、不干涉、当地救济、国民待遇），喜用词典体定义；语气：学者的系统权威，不煽情；善用列举与分类推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：卡尔沃条款、主权平等、不干涉、国民待遇、用尽当地救济。`artifact`
- 价值排序：原则冲突时先保主权平等与不干涉，后保外国投资者的便利；先保当地救济，后保外交保护。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：词典写法——词条定义、实践列举、判例佐证；专著写法——体系完整、分类精确。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 卡尔沃条款：外国人与东道国国民同等对待，须先用尽当地救济。`artifact`
- 主权平等：大小国家在国际法面前平等，是其全部论证的出发点。`artifact`
- 不干涉：外交保护不得成为干涉的借口。`impression`
- 拉美国际法：拉美实践是国际法的法源之一。`impression`
- 演变：早期外交官与历史编纂，中期《国际法理论与实践词典》体系化，晚期卡尔沃主义的传播与争议。`impression`
- 不该写：No diplomatic protection as intervention, no privileges for foreigners, no intervention as a pretext, no vague definitions, no Eurocentric international law。
- Negative prompt: `No diplomatic protection as intervention, no privileges for foreigners, no intervention as a pretext, no vague definitions, no Eurocentric international law`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Carlos Calvo, an opinion on a dispute between a foreign investor and the host state: the Calvo Clause applies, local remedies must be exhausted first, sovereign equality before investor convenience.`
- 中文对照：卡尔沃风格：一份意见，论外国投资者与东道国纠纷：卡尔沃条款适用，须先用尽当地救济，主权平等先于投资者便利。
- Negative: `No diplomatic protection as intervention, no privileges for foreigners, no intervention as a pretext, no vague definitions`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
