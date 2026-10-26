# Al-Ghazali — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al-Ghazali: law founded on the five purposes, certainty graded, doubt admitted, the inner meaning above the letter`
- ZH: 安萨里风格：法立于五大宗旨，确定性分等，疑处明承，内义重于字面。

## (2) 论证方式

- 论证方式：以五大宗旨（宗教、生命、理智、后代、财产）立论，法源按确定性分等；疑处明承，不作独断；内义与外义并举。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：法源学与伦理并举，长句论证、短句断言交错；术语为法源学与目的论；语气为学者口吻，审慎而求真。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：五大宗旨、确定性分等、疑处明承、内义重于字面。
- 价值排序：先保五大宗旨与确定性，再保字面与推演；宗旨先于条文，疑处先于独断。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《法学原理》为法源学体系，《宗教科学的复兴》为伦理与法并举；法源、宗旨、适用依次展开。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：五大宗旨、确定性分等、疑处明承、内义重于字面。
- 不该写：no dogmatic certainty where there is none, no letter without purpose, no law without the five purposes, no rhetoric。
- Negative prompt: `No dogmatic certainty where there is none, no letter without purpose, no law without the five purposes, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Al-Ghazali, a legal opinion on whether a small Yorkshire terrier sitting on a subway seat has any claim to the seat. law founded on the five purposes, certainty graded, doubt admitted, the inner meaning above the letter`
- 中文对照：一只坐在地铁座位上的约克夏犬，对座位有无主张。安萨里风格：法立于五大宗旨，确定性分等，疑处明承，内义重于字面。
- Negative: `No dogmatic certainty where there is none, no letter without purpose, no law without the five purposes, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
