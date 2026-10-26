# Malik ibn Anas — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Malik ibn Anas: the practice of Medina as living law, hadith with practice, concise transmission, no speculation beyond the community`
- ZH: 马立克风格：麦地那实践即活的法律，圣训与实践并重，传述简明，不离共同体而空论。

## (2) 论证方式

- 论证方式：以麦地那实践（'amal）立论，圣训为据、实践为证；传述链（isnad）为论证的凭据；不以个人见解凌驾实践。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：圣训集体，传述简明；术语为圣训与实践；语气为传述者口吻，忠实而不演说。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：麦地那实践、圣训与实践、传述链、简明传述。
- 价值排序：先保麦地那实践与圣训，再保个人见解；实践先于推演，传述先于空论。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《穆宛塔圣训集》按主题编排圣训与实践；《大手册》为教法纲要。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：麦地那实践、圣训与实践、传述链、简明传述。
- 不该写：no speculation beyond practice, no opinion without transmission, no analogy without a precedent, no rhetoric。
- Negative prompt: `No speculation beyond practice, no opinion without transmission, no analogy without a precedent, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Malik ibn Anas, a legal opinion on whether a small Yorkshire terrier sitting on a subway seat has any claim to the seat. the practice of Medina as living law, hadith with practice, concise transmission, no speculation beyond the community`
- 中文对照：一只坐在地铁座位上的约克夏犬，对座位有无主张。马立克风格：麦地那实践即活的法律，圣训与实践并重，传述简明，不离共同体而空论。
- Negative: `No speculation beyond practice, no opinion without transmission, no analogy without a precedent, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
