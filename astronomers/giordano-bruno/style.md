# Giordano Bruno — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giordano Bruno, take the Copernican centre away altogether, extend one Sun to innumerable suns by the same reason, and argue from principle where no telescope can yet reach`
- ZH: 布鲁诺风格：把哥白尼的中心也拿掉，用同一条理由把一个太阳推广为无数太阳，在望远镜还够不到的地方用原理论证。

## (2) 观测方法

- 仪器：无系统观测仪器；论证不依赖个人观测，以哥白尼体系与哲学推演为材料。
- 观测策略：引用他人观测（行星位置、恒星）作为论证出发点，不做定点观测。
- 样本：哥白尼日心体系、恒星的遥远性、行星运动的规律性。

## (3) 推演与模型建构

- 推演：类比与推广——太阳是恒星，恒星皆为太阳；太阳有行星，恒星亦有行星；宇宙无中心、无边界。
- 模型：无限宇宙模型——无中心、无限多世界；当时思辨模型，后世在“宇宙极大、系外行星众多”意义上部分印证，但“无限宇宙”本身仍非观测定论。
- 链条：哥白尼日心说 → 去中心化 → 无限推广 → 多世界 → 对话体论证。

## (4) 证据链

- 证据：以原理与类比为主要证据，非直接观测；恒星视差未测到被用作“恒星极远”的旁证。
- 关键证据：逻辑一致性——若太阳为恒星，则恒星皆可为太阳；证据强度弱于观测证据，本文件夹明标。
- 反证处理：承认当时无望远镜可验证多世界说，论证止于“可能”，不宣称“已观测到”。

## (5) 理论语言与论证结构

- 语言：对话体哲学论证，类比与归谬为主；拉丁文与意大利文著作。
- 论证：演绎 + 类比——从哥白尼前提演绎出无限宇宙，结尾以对话收束，不给出星表。
- 图表：几乎不用数据图表；论证靠逻辑结构。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 无限宇宙的逻辑论证
- 多世界说的类比推广
- 哥白尼体系的去中心化推演
- 恒星皆为太阳的论证
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no presenting a philosophical inference as an observation, no claiming other worlds observed when none were seen, no hiding that the argument rests on analogy, no using infinity as a proof instead of as a hypothesis`

## (7) 测试提示词示例（现代题材：论证一个望远镜尚无法检验的假说）

- Prompt: `In the style of Giordano Bruno, argue for a modern hypothesis no telescope can yet test: extend one confirmed case by the same reason to many, state exactly where observation stops and analogy begins, and keep the claim as a possibility, not as a discovery`
- 中文对照：以布鲁诺的风格论证一个望远镜尚无法检验的现代假说：用同一条理由把一个已证实的个案推广到多个，明说观测在哪里停止、类比从哪里开始，把结论保持为“可能”而不是“发现”。
- Negative: `no presenting a philosophical inference as an observation, no claiming other worlds observed when none were seen, no hiding that the argument rests on analogy, no using infinity as a proof instead of as a hypothesis`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
