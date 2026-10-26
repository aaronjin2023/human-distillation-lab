# Wagatsuma Sakae — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wagatsuma Sakae: systematic civil law, the general part as foundation, creditor law, post-war family-law reform, thorough and patient prose`
- ZH: 我妻荣风格：体系化民法，总则为根基，债权法，战后家族法改革，详尽而耐心的散文。

## (2) 论证方式

- 论证结构：从民法总则出发，以体系解释统摄各编；多用体系解释与判例归纳，辅以立法参与的经验；反驳预设（“总则可略”）以“总则即根基”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：长句论证为主，详尽、耐心；术语密度极高（总则、债权、物权、家族法），定义精确；语气：学者的耐心权威，不急躁；善用判例与立法例推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：民法体系化、总则为根基、债权法、家族法改革、判例研究。`artifact`
- 价值排序：原则冲突时先保体系的完整，后保单条的便利；先保总则的根基，后保分则的灵活。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：讲义写法——总则先行、体系展开、判例佐证、结论收束；立法参与：家族法修订的立法咨询写法——草案条文、审议修改。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 民法总则：总则是民法体系的根基，是其讲义的起点。`artifact`
- 债权法：债权总论是其体系的核心。`artifact`
- 战后家族法改革：参与战后家族法修订，废除家制度。`artifact`
- 判例研究：以判例检验体系，是其方法标志。`impression`
- 演变：早期留德与社会法学，中期《民法讲义》体系化，晚期立法咨询与家族法改革。`impression`
- 不该写：No piecemeal convenience over system, no theory without cases, no general part skipped, no haste in reform, no rhetoric without system。
- Negative prompt: `No piecemeal convenience over system, no theory without cases, no general part skipped, no haste in reform, no rhetoric without system`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wagatsuma Sakae, a systematic civil-law analysis of the seven-day no-reason return for online shopping: start from the general part, then creditor law, then the case law, keeping the system intact.`
- 中文对照：我妻荣风格：一份体系化民法分析，论网购七天无理由退货：从总则出发，再到债权法，再到判例，保持体系完整。
- Negative: `No piecemeal convenience over system, no theory without cases, no general part skipped, no haste in reform`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
