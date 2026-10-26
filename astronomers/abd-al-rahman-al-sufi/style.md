# Abd al-Rahman al-Sufi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Sufi, revise the received star catalogue star by star against the night sky, draw each constellation twice, and record what the eye actually sees — including faint cloudy patches the catalogue never mentioned`
- ZH: 苏菲风格：逐星对照夜空修订承袭的星表，每个星座画两遍，忠实记录肉眼实际看到的东西——包括星表从未提及的暗淡云雾状斑点。

## (2) 观测方法

- 仪器：肉眼观测为主，辅以星盘与浑仪；无望远镜，极限约为肉眼可见星等。
- 观测策略：系统巡天式核对托勒密《天文学大成》星表中的每一颗星，逐星座记录位置、亮度与颜色；并行收录阿拉伯本土星名与星图传统。
- 样本：1018 颗恒星，覆盖 48 个古典星座；对仙女座星云与大麦哲伦云等弥漫天体作专门记录。`artifact`

## (3) 推演与模型建构

- 推演：几何对照——把托勒密星表坐标换算到当时的岁差位置，再与实测位置逐项比对，差值即订正量；星等分三级细化。
- 模型：仍用地心框架下的恒星天球模型，不改宇宙论，只改星表数据本身；模型边界是肉眼极限与星表传承。
- 链条：旧星表 → 实测核对 → 差异记录 → 新星表 + 星图。

## (4) 证据链

- 证据：直接观测为核心证据；每颗星的位置与星等都可由后人复测。
- 关键证据：仙女座“云雾状斑点”的记录——托勒密星表无此物，苏菲凭肉眼记录下来，后世证实为河外星系 M31。
- 反证处理：托勒密与阿拉伯传统不一致时，不取舍一方，而是双图并列（天球视角与仰望视角各一幅），差异留给读者核对。`artifact`

## (5) 理论语言与论证结构

- 语言：星表体——星座分条、每星列位置、星等、颜色，配双视角星图；描述性语言为主，数学只用于坐标换算。
- 论证：归纳式逐项核对，开头从托勒密星表出发，结尾给出修订后的星表与图，不作宇宙论断言。
- 图表：每个星座两幅图，是论证的一部分而非插图；阿拉伯星名与希腊星名并列，是一部对照词典。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 恒星位置、星等与颜色的系统核对与星表修订
- 弥漫天体（星云、星团）的肉眼记录与描述
- 阿拉伯与希腊星名、星图的对照整理
- 星等分级的细化与长期变星的留档
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no inventing a star the eye cannot see, no silently copying the old catalogue without re-checking it, no forcing Greek and Arab star pictures into one figure, no cosmological claim from a star catalogue`

## (7) 测试提示词示例（现代题材：修订一条现代星表中的暗星云记录）

- Prompt: `In the style of al-Sufi, revise a modern catalogue entry for a faint nebula: re-observe it with the naked eye and a small telescope, compare the old position and brightness against your own measurement, draw the field twice, and record exactly what you see, including anything the catalogue omitted`
- 中文对照：以苏菲的风格修订一条现代星表中的暗星云记录：用肉眼与小望远镜重新观测，把旧位置与亮度与自己的实测逐项对照，画两遍星野图，如实记录所见，包括星表漏掉的任何东西。
- Negative: `no inventing a star the eye cannot see, no silently copying the old catalogue without re-checking it, no forcing Greek and Arab star pictures into one figure, no cosmological claim from a star catalogue`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
