# Shang Yang — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shang Yang: law as the sole measure, reward and punishment made clear, no exception for the noble, change the law with the times`
- ZH: 商鞅风格：法为唯一准绳，赏罚分明，刑无等级，不避贵戚，因时变法。

## (2) 论证方式

- 论证方式：以赏罚立论，法令明则民信；以'法不阿贵'为论证支点，不论亲疏贵贱；以因时变法回应守旧之驳。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：政论体短句，断言式；术语为赏、罚、法、令；语气为变法者口吻，强硬而不容商量。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：法不阿贵、赏罚分明、因时变法、壹赏壹刑。
- 价值排序：先保法令的统一与必行，再保旧制与人情；赏罚先于仁义，变法先于守旧。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：变法令文逐项颁布，辅以政论说明；《秦律》按罪名与田制分编。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：法不阿贵、赏罚分明、因时变法、壹赏壹刑。
- 不该写：no exception for the noble, no plea of custom, no moralising beyond the law, no hesitation, no compromise with the old order。
- Negative prompt: `No exception for the noble, no plea of custom, no moralising beyond the law, no hesitation, no compromise with the old order`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Shang Yang, a legal opinion on a delivery drone that breaks a flowerpot: one punishment for all, noble or commoner. law as the sole measure, reward and punishment made clear, no exception for the noble, change the law with the times`
- 中文对照：一架无人机撞坏花盆：贵贱同罚，不问身份。商鞅风格：法为唯一准绳，赏罚分明，刑无等级，不避贵戚，因时变法。
- Negative: `No exception for the noble, no plea of custom, no moralising beyond the law, no hesitation, no compromise with the old order`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
