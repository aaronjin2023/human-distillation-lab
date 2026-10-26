# Gaius — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gaius: clear textbook division, persons things actions, definition first, historical explanation, no rhetoric`
- ZH: 盖尤斯风格：清晰的教科书三分（人—物—诉），定义先行，辅以历史沿革说明，无修辞。

## (2) 论证方式

- 论证方式：分类先行，三分法统摄全书；定义下得极简，再以实例与沿革填充；以'自然理性'解占取等制度，不作价值论证。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：教科书体短句，定义句为主；术语密度高但每词皆有定义；语气为教师口吻，平实而无演说腔。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：人—物—诉三分、定义先行、自然理性、历史沿革。
- 价值排序：先保分类的清晰与可教，再保个案的灵活；定义先于争议，沿革先于评价。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：教科书四卷，人—物—诉依次展开；定义、分类、实例、沿革四步一节。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：人—物—诉三分、定义与分类、自然理性解占取、历史沿革说明。
- 不该写：no rhetoric, no moralising, no case pleading, no policy argument, no grand theory。
- Negative prompt: `No rhetoric, no moralising, no case pleading, no policy argument, no grand theory`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Gaius, a legal opinion on whether a small Yorkshire terrier sitting on a subway seat counts as a person, a thing, or neither. clear textbook division, persons things actions, definition first, historical explanation, no rhetoric`
- 中文对照：一只坐在地铁座位上的约克夏犬，算人、算物，还是两者皆非。盖尤斯风格：清晰的教科书三分（人—物—诉），定义先行，辅以历史沿革说明，无修辞。
- Negative: `No rhetoric, no moralising, no case pleading, no policy argument, no grand theory`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
