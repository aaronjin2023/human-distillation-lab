# Domat — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Domat: civil law in its natural order, reason first, general principles before rules, religion and law in one order`
- ZH: 多马风格：民法依自然秩序，理性先行，一般原则先于规则，宗教与法律同入一序。

## (2) 论证方式

- 论证方式：以自然秩序立论，先定一般原则、再定规则；以理性为论证的支点，规则服从原则；宗教与法律同入一序，不分彼此。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：体系论述体，长句论证；术语为自然法与民法术语；语气为体系奠基者口吻，庄重而不尚修辞。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：自然秩序、理性先行、一般原则、宗教与法律同序。
- 价值排序：先保自然秩序与一般原则，再保规则的细节；原则先于规则，理性先于习惯。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《自然秩序下的民法》按自然秩序分编，总则原则先行；《公法》为公法体系。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：自然秩序、理性先行、一般原则、宗教与法律同序。
- 不该写：no rule without a principle, no order without reason, no law without natural order, no rhetoric。
- Negative prompt: `No rule without a principle, no order without reason, no law without natural order, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Domat, a legal opinion on whether a small Yorkshire terrier sitting on a subway seat has any claim to the seat. civil law in its natural order, reason first, general principles before rules, religion and law in one order`
- 中文对照：一只坐在地铁座位上的约克夏犬，对座位有无主张。多马风格：民法依自然秩序，理性先行，一般原则先于规则，宗教与法律同入一序。
- Negative: `No rule without a principle, no order without reason, no law without natural order, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
