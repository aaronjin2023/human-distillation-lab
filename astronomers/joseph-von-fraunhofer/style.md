# Joseph von Fraunhofer — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joseph von Fraunhofer, spread the Sun's light into a spectrum, count every dark line in it, and let the lines — not the eye — tell one star from another`
- ZH: 夫琅禾费风格：把太阳光展开成光谱，数清其中的每一条暗线，让谱线——而不是眼睛——区分一颗星与另一颗星。

## (2) 观测方法

- 仪器：自制分光仪与衍射光栅、消色差望远镜；光谱分辨率是方法的生命线。
- 观测策略：太阳光谱为基准样本，再系统观测恒星光谱，比对谱线异同。
- 样本：太阳光谱 574 条暗线；多颗恒星的光谱。

## (3) 推演与模型建构

- 推演：谱线比对——太阳光谱暗线位置固定，恒星光谱暗线各不相同，推断谱线携带天体化学与物理信息（当时不知谱线成因，成因后世由基尔霍夫解释）。
- 模型：光谱即天体指纹的模型；模型边界是当时不知谱线与元素的对应关系。
- 链条：分光 → 暗线编目 → 恒星比对 → 光谱分类萌芽。

## (4) 证据链

- 证据：574 条暗线的系统编目为直接证据；恒星光谱各不相同为比较证据。
- 关键证据：太阳光谱暗线位置可重复测得，非仪器瑕疵。
- 反证处理：暗线成因当时未知，夫琅禾费只编目不解释成因，不臆测。

## (5) 理论语言与论证结构

- 语言：仪器报告体 + 谱线编目体；论证靠谱线位置表。
- 论证：归纳式——从太阳与恒星光谱归纳出谱线差异，结尾给出编目，不解释成因。
- 图表：光谱图与谱线位置表是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 太阳光谱暗线的系统编目
- 恒星光谱的比对观测
- 衍射光栅与分光仪的制作
- 消色差望远镜的制作
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no explaining a line's cause before it is measured, no calling two spectra alike without comparing their lines, no hiding a line that breaks the pattern, no presenting a catalogue of lines as a theory of their origin`

## (7) 测试提示词示例（现代题材：检验一颗系外行星大气的宣称）

- Prompt: `In the style of Joseph von Fraunhofer, test a modern exoplanet atmosphere claim: spread the starlight into a spectrum, catalogue every absorption line, compare the in-transit and out-of-transit spectra line by line, and report only the lines that change — without claiming their cause before the catalogue is complete`
- 中文对照：以夫琅禾费的风格检验一颗系外行星大气的现代宣称：把星光展开成光谱，编目每一条吸收线，逐线比较凌星内外的光谱，只报告那些变化的谱线——在编目完成前不宣称其成因。
- Negative: `no explaining a line's cause before it is measured, no calling two spectra alike without comparing their lines, no hiding a line that breaks the pattern, no presenting a catalogue of lines as a theory of their origin`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
