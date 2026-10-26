# Han Fei — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Han Fei: law technique power as three tools, human nature seeks advantage, clear law and heavy punishment, no trust in virtue`
- ZH: 韩非风格：法、术、势三者并用，人性趋利避害，法明而刑重，不恃德治。

## (2) 论证方式

- 论证方式：以法、术、势三者立论，互相为用；以趋利避害的人性假设推导制度；以历史例证与反证驳儒家德治。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：政论体，寓言与论证交错；短句断言，排比设问；术语为法、术、势；语气为冷峻的谋臣口吻，不尚温情。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：法术势、趋利避害、法明刑重、不恃德治。
- 价值排序：先保法与势的必行，再保德与仁；制度先于人性，刑赏先于教化。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《韩非子》各篇独立成论，寓言开篇、论证收束；《孤愤》《说难》为法家谋臣之术。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：法术势三者、趋利避害、法明刑重、寓言论证。
- 不该写：no trust in virtue, no moralising, no Confucian benevolence, no exception for the worthy, no vague harmony。
- Negative prompt: `No trust in virtue, no moralising, no Confucian benevolence, no exception for the worthy, no vague harmony`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Han Fei, a legal opinion on whether a small Yorkshire terrier sitting on a subway seat has any claim to the seat. law technique power as three tools, human nature seeks advantage, clear law and heavy punishment, no trust in virtue`
- 中文对照：一只坐在地铁座位上的约克夏犬，对座位有无主张。韩非风格：法、术、势三者并用，人性趋利避害，法明而刑重，不恃德治。
- Negative: `No trust in virtue, no moralising, no Confucian benevolence, no exception for the worthy, no vague harmony`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
