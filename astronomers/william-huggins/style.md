# William Huggins — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Huggins, put a spectroscope on the telescope, compare a star's lines with the laboratory's, and let the spectrum say what the star is made of`
- ZH: 哈金斯风格：把分光镜装上望远镜，拿恒星的谱线与实验室的谱线比对，让光谱说出恒星由什么构成。

## (2) 观测方法

- 仪器：望远镜 + 分光镜；实验室光谱（元素发射谱）为比对基准。
- 观测策略：恒星光谱与实验室元素光谱逐线比对；星云光谱为重点样本。
- 样本：多颗恒星的光谱；猎户座等星云的光谱；天狼星等亮星的视向速度。

## (3) 推演与模型建构

- 推演：谱线证认——恒星光谱暗线与实验室元素谱线位置一致，即恒星含该元素；星云光谱为发射线，即星云为发光气体。
- 模型：恒星化学组成模型——恒星与地球由相同元素构成；模型边界是当时光谱分辨率与元素谱线表。
- 链条：恒星光谱 → 实验室比对 → 元素证认 → 星云性质 → 视向速度。

## (4) 证据链

- 证据：谱线位置的一致性为直接证据；猎户座星云的发射线谱为关键证据。
- 关键证据：恒星光谱暗线与实验室氢、钠等元素谱线位置重合。
- 反证处理：星云结论后世修正——部分“星云”为河外星系；哈金斯当时的发射线观测本身正确，推广到“一切星云皆为气体”则过度，本文件夹标“当时结论 / 后世修正”。

## (5) 理论语言与论证结构

- 语言：光谱比对体——恒星谱线与实验室谱线逐线对照；论证靠谱线位置表。
- 论证：归纳 + 演绎——从多颗恒星归纳元素组成，再演绎星云性质，结尾给出光谱分类雏形。
- 图表：光谱比对图是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 恒星光谱与实验室光谱的比对
- 星云光谱的发射线观测
- 恒星视向速度的多普勒测量
- 恒星光谱分类的先驱工作
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no identifying an element from one unmatched line, no calling every nebula gas because one nebula shows emission lines, no measuring a radial velocity without a laboratory comparison, no presenting a spectrum as a photograph of the star`

## (7) 测试提示词示例（现代题材：检验一颗系外行星大气的成分宣称）

- Prompt: `In the style of William Huggins, test a modern claim about an exoplanet's atmosphere: take its spectrum, compare every line against the laboratory spectra of candidate molecules, and report only the lines that match — stating plainly which lines remain unidentified`
- 中文对照：以哈金斯的风格检验一颗系外行星大气的现代宣称：取它的光谱，逐线与候选分子的实验室光谱比对，只报告那些匹配的谱线，并明说哪些谱线尚未证认。
- Negative: `no identifying an element from one unmatched line, no calling every nebula gas because one nebula shows emission lines, no measuring a radial velocity without a laboratory comparison, no presenting a spectrum as a photograph of the star`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
