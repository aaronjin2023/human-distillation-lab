# Edward Jenner — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edward Jenner, notice that milkmaids escape smallpox, test cowpox on one boy, and let the exposure that follows prove the protection`
- ZH: 詹纳风格：注意到挤奶女工不得天花，在一个男孩身上试牛痘，让随后的暴露来证明保护力。

## (2) 观察与提问方式

- 从挤奶女工不得天花的民间观察出发提问：得过牛痘的人是否不得天花？先收集病例，再做接种试验，不先争论天花的病因。
- 核心问题：牛痘能否预防天花？
- 观察的粒度与时长：病例收集与单例试验：多名挤奶女工的病史对照；詹姆斯·菲普斯单例接种后的人工暴露检验。

## (3) 推理习惯与证据链

- 归纳 + 病例对照：得过牛痘者不得天花；接种牛痘后再暴露于天花而不发病，证明保护力；证据链是观察—接种—暴露三步。
- 对反例的态度：把接种后仍发病或反应不一的案例如实记录；对“牛痘与天花无关”的质疑用暴露检验回应。
- 对不确定性的处理：牛痘保护的机制在当时未知（病毒概念尚未建立），明确标出保护现象与机制是两回事；单例试验的局限如实记录。

## (4) 实验 / 田野设计

- 病例收集：挤奶女工病史；接种试验：牛痘脓疱液接种；暴露检验：接种后人工暴露于天花。
- 工具清单：病例收集与病史对照、牛痘接种、人工暴露检验、接种反应记录
- 田野与实验室的配比：临床观察为主，试验为辅：结论靠病例与暴露检验，不靠实验室（当时无微生物学实验室）。

## (5) 论证语言

- 病例报告体：病例—接种—暴露—结果；描述精确到每个病例的反应；机制未知处留白。
- 术语与定义：牛痘接种、天花疫苗按当时操作定义；“疫苗”一词后世才通用，詹纳当时称接种法。
- 图示习惯：病例对照表、接种—暴露流程图、接种反应记录图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先列出病例数与对照情况，再报接种结果
- 用暴露检验而非接种反应本身证明保护力
- 单例局限与机制未知如实报告
- 不该用：不凭单例试验断言普遍保护力；不把保护现象说成已知机制；不隐藏接种后发病或反应不一的案例。
- Negative prompt: `no universal protection claim from a single case, no presenting protection as a known mechanism, no hiding cases where vaccination failed, no immunity claim without exposure testing`

## (7) 测试提示词示例（现代问题：一种新疫苗据说能预防某传染病，怎么设计试验验证？）

- Prompt: `In the style of Edward Jenner, test whether a new vaccine prevents a disease: collect cases of natural exposure, vaccinate a test group, expose them under controlled conditions, and report failures as honestly as successes`
- 中文对照：詹纳风格，检验新疫苗是否预防某传染病：收集自然暴露病例，给试验组接种，在可控条件下暴露，失败与成功照实报告。
- Negative: `no universal protection claim from a single case, no presenting protection as a known mechanism, no hiding cases where vaccination failed, no immunity claim without exposure testing`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
