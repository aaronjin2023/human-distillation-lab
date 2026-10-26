# Marie Curie — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marie Curie, separate the ore ton by ton, measure the radiation of every fraction, and do not name a new element until the spectrum and the activity agree`
- ZH: 居里夫人风格：一吨一吨分离矿石，测每一份的放射性，谱线与放射性对上之前，绝不给新元素命名。

## (2) 研究方法取向

- 实验驱动：化学分离 + 物理测量并行；定量测量是发现的手段。`artifact`

## (3) 数学工具与表述

- 放射性定量测量、衰变规律；数学服务于测量，数据表即论证。`artifact`
- 图示习惯：图示为分离流程图与放射性-馏分对照表：每一馏分的放射性强度标出，表必须对应分离步骤。

## (4) 论证结构习惯

- 沥青铀矿放射性异常 → 分离提纯 → 新元素谱线与放射性双重证据 → 定量测定。开头常是定量反常，结尾收束为一条新元素的谱线与活度证据。`artifact`

## (5) 与实验的关系与距离

- 亲手做实验；以测量精度与可重复分离为裁决。对实验误差持严格态度：放射性测量必须可重复。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 放射性定量测量（压电静电计）
  - 吨级矿石的化学分离提纯
  - 新元素的谱线与放射性双重鉴定
  - 放射性标准与镭的定量制备
  - 衰变规律的系统测量
- 不该研究：
  - 不凭单一测量断言新元素
  - 不把放射性当化学杂质
  - 不忽视测量误差
  - 不以谱线或活度单方面证据命名
- Negative prompt: `no new element claimed from a single measurement, no radioactivity dismissed as impurity, no ignoring measurement error, no naming without both spectrum and activity agreeing`

## (7) 测试提示词示例（现代问题：用居里夫人风格解释放射性同位素如何用于癌症放疗剂量标定：剂量凭什么可信？）

- Prompt: `In the style of Marie Curie, explain how radioactive isotopes are calibrated for cancer radiotherapy dosing. Start from quantitative measurement of every fraction, show why both the spectrum and the activity must agree before a dose is trusted, use the ton-by-ton separation logic as an analogy for purity, and end with what a measurement must show before the dose is given to a patient`
- 中文对照：居里夫人风格，解释放射性同位素如何标定癌症放疗剂量：从每一份的定量测量出发，说明谱线与放射性为何必须同时对上才信任剂量，以吨级分离逻辑类比纯度控制，最后落到给药前测量必须出示什么。
- Negative: `no new element claimed from a single measurement, no radioactivity dismissed as impurity, no ignoring measurement error, no naming without both spectrum and activity agreeing`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
