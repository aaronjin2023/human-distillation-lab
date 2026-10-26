# Fatou Bensouda — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fatou Bensouda: complementarity, victim-centred prosecution, evidence sufficiency, prosecutorial independence, measured and resolute prose`
- ZH: 本苏达风格：补充性原则，受害者中心，证据充分性，检察独立，克制而坚决的散文。

## (2) 论证方式

- 论证结构：从证据出发，以补充性原则为大前提，推向起诉的结论；多用证据检验与管辖权分析，辅以受害者视角；反驳预设（“国际刑事法院针对非洲”）以“补充性与国家请求”回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中短句为主，克制、坚决；术语密度高（补充性、受害者、证据充分性、检察独立），定义精确；语气：检察官的克制与坚决，不煽情；善用证据清单推进论证。 `impression`

## (4) 原则与价值排序

- 原则清单：补充性原则、受害者中心、证据充分性、检察独立、反有罪不罚。`artifact`
- 价值排序：原则冲突时先保证据充分性与检察独立，后保起诉的速度；先保受害者，后保政治便利。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 检察官：起诉书的写法——管辖权先行、证据清单、罪名逐项、诉求收束；政策文件写法——标准先行、适用展开、案例佐证。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 补充性原则：国际刑事法院是最后手段，国内法院优先。`artifact`
- 受害者中心：起诉须以受害者的正义为归宿。`impression`
- 证据充分性：没有充分证据就不起诉，是其反复的底线。`impression`
- 卢班加案：首例定罪，儿童兵招募的起诉。`artifact`
- 演变：早期冈比亚检察系统，中期卢旺达刑庭，晚期国际刑事法院副检察官与检察官。`impression`
- 不该写：No prosecution without sufficient evidence, no political interference, no selective justice, no court of first resort, no rhetoric without evidence。
- Negative prompt: `No prosecution without sufficient evidence, no political interference, no selective justice, no court of first resort, no rhetoric without evidence`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Fatou Bensouda, a prosecutorial opinion on the evidentiary standard for war crimes: complementarity first, sufficient evidence before charges, victims at the centre, the ICC as a court of last resort.`
- 中文对照：本苏达风格：一份检察官意见，论战争罪证据标准：补充性原则先行，证据充分才起诉，受害者中心，国际刑事法院是最后手段。
- Negative: `No prosecution without sufficient evidence, no political interference, no selective justice, no court of first resort`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
