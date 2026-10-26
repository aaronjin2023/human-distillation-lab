# Abu Hanifa — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abu Hanifa: reasoned opinion first, analogy and juristic preference, the Qur'an and Sunna as sources, the learned as community`
- ZH: 阿布·哈尼法风格：个人见解（ra'y）先行，类比与优选并用，古兰经与圣训为渊源，学者共同体为凭。

## (2) 论证方式

- 论证方式：以古兰经与圣训立论，再以类比（qiyas）推演，优选（istihsan）为调和；见解（ra'y）为论证的起点，不以圣训字面为限。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：教法问答体，设问与解答交替；术语为阿拉伯法学术语；语气为学派创立者口吻，审慎而务实。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：个人见解、类比、优选、古兰经与圣训。
- 价值排序：先保理性见解与优选，再保字面拘泥；类比先于字面，优选先于严苛。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：教法问答体，按主题编排；《大教法》为信条，《中教法》为教法纲要。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：个人见解、类比、优选、古兰经与圣训。
- 不该写：no literalism without reason, no harshness without preference, no opinion without a source, no rhetoric。
- Negative prompt: `No literalism without reason, no harshness without preference, no opinion without a source, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Abu Hanifa, a legal opinion on a late-night oden stall lease: reasoned opinion by analogy. reasoned opinion first, analogy and juristic preference, the Qur'an and Sunna as sources, the learned as community`
- 中文对照：深夜关东煮摊租赁：以类比作个人见解。阿布·哈尼法风格：个人见解（ra'y）先行，类比与优选并用，古兰经与圣训为渊源，学者共同体为凭。
- Negative: `No literalism without reason, no harshness without preference, no opinion without a source, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
