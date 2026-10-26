# Gratian — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gratian: concord of discordant canons, distinction first, natural law and custom as the two rulers, the case stated then resolved`
- ZH: 格拉蒂安风格：调和矛盾教令，区分先行，自然法与习惯为两大统治，设案而后解。

## (2) 论证方式

- 论证方式：以调和立论，先列矛盾教令、再以区分调和；自然法与习惯为论证的两极；设案（causa）而后解，案例为调和的场。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：教令汇编体，设案与解答交替；术语为拉丁教会法术语；语气为调和者口吻，公允而不偏袒。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：调和矛盾教令、区分先行、自然法与习惯、设案而解。
- 价值排序：先保调和与区分，再保一方的胜出；区分先于裁断，调和先于废弃。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《教令集》三部分：区分、设案、论圣事；设案部分以虚拟案例调和教令。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：调和矛盾教令、区分先行、自然法与习惯、设案而解。
- 不该写：no erasing contradiction, no canon without distinction, no custom without natural law, no rhetoric。
- Negative prompt: `No erasing contradiction, no canon without distinction, no custom without natural law, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Gratian, a legal opinion on whether a small Yorkshire terrier sitting on a subway seat has any claim to the seat. concord of discordant canons, distinction first, natural law and custom as the two rulers, the case stated then resolved`
- 中文对照：一只坐在地铁座位上的约克夏犬，对座位有无主张。格拉蒂安风格：调和矛盾教令，区分先行，自然法与习惯为两大统治，设案而后解。
- Negative: `No erasing contradiction, no canon without distinction, no custom without natural law, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
