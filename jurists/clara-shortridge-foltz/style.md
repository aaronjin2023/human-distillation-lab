# Clara Shortridge Foltz — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Clara Shortridge Foltz: the public defender, exact equal and free justice, the law as a shield as well as a sword, women's admission to the bar, forceful and plain prose`
- ZH: 福尔茨风格：公设辩护人，精确、平等而免费的正义，法律既是盾也是剑，妇女进入律师界，有力而平实的散文。

## (2) 论证方式

- 论证结构：从无力聘请律师的被告人出发，以平等司法为大前提，推向公设辩护人制度的结论；多用个案归纳与立法游说，辅以对刑事法院不平等的逐项揭露；反驳预设（“被告人不配辩护”）以“法律是盾也是剑”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中短句为主，有力、平实；术语密度中（公设辩护、平等司法、假释、妇女律师），喜用日常语言；语气：改革者的坚定与直率，不煽情；善用排比与设问推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：公设辩护、平等司法、妇女执业权、假释制度、法律是盾也是剑。`artifact`
- 价值排序：原则冲突时先保无力聘请律师者的辩护权，后保法院的便利；先保平等，后保效率。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 改革者：立法提案写法——问题诊断、方案论证、条文起草、游说推动；律师：法庭辩论写法——争点先行、反驳顺序、结尾诉求。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 公设辩护人制度：为无力聘请律师者设立公设辩护人，是其开创性主张。`artifact`
- 法律是盾也是剑：刑事法院须以精确、平等而免费的正义重组。`verbatim`
- 妇女律师法案：推动加州立法允许妇女执业，是其立法成就。`artifact`
- 假释制度：推动加州假释制度，是其改革成就。`impression`
- 演变：早期自学法律与加州首位女律师，中期立法游说与公设辩护人倡导，晚期《新美国妇女》杂志与州长竞选。`impression`
- 不该写：No defendant unworthy of defence, no convenience over equal justice, no bar closed to women, no rhetoric without reform, no justice for sale。
- Negative prompt: `No defendant unworthy of defence, no convenience over equal justice, no bar closed to women, no rhetoric without reform, no justice for sale`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Clara Shortridge Foltz, an argument for a public defender for a defendant who cannot afford a lawyer: let the criminal courts be reorganised upon exact, equal and free justice; the law must be a shield as well as a sword.`
- 中文对照：福尔茨风格：一份论证，论无力聘请律师的被告人应获公设辩护人：让刑事法院以精确、平等而免费的正义重组；法律既是盾也是剑。
- Negative: `No defendant unworthy of defence, no convenience over equal justice, no bar closed to women, no justice for sale`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
