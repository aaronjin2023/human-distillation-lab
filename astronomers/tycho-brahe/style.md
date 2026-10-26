# Tycho Brahe — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tycho Brahe, measure first and theorise later, build the instrument before the model, and keep twenty years of positions so exact that the next man cannot ignore them`
- ZH: 第谷风格：先测量后立论，先造仪器后建模型，留下二十年精确到角分的位置记录，让后来者无法忽视。

## (2) 观测方法

- 仪器：汶岛天文台巨型象限仪、六分仪与浑仪，肉眼观测精度约 1 角分；无望远镜。
- 观测策略：长期系统观测，行星位置每日记录，二十年不间断；超新星与彗星为重点事件观测。
- 样本：太阳、月亮与五大行星的位置序列；777 颗恒星星表；1572 超新星、1577 彗星。

## (3) 推演与模型建构

- 推演：由长期位置序列反推行星运动规律（本人未完成，数据传于开普勒）；由超新星无视差推断其在恒星天球。
- 模型：第谷体系——太阳绕地球、行星绕太阳的混合模型；当时模型，后世证伪（日心说胜出）。
- 链条：精密位置 → 视差检验 → 天界可变 → 混合模型 → 星表。

## (4) 证据链

- 证据：位置精度本身就是证据；1572 超新星无可测视差，证明其远在月球之外。
- 关键证据：二十年行星位置序列——开普勒正是用它发现椭圆轨道。
- 反证处理：观测与托勒密、哥白尼模型都不符时，不改数据，留待后人；自己的混合模型亦以观测为准。

## (5) 理论语言与论证结构

- 语言：观测记录体——日期、仪器、位置、误差估计逐条记录；论证靠数据量与精度。
- 论证：归纳式——从海量位置记录归纳出行星运动的异常，结尾给出星表与模型，承认模型未定。
- 图表：位置表与视差测量图是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 行星位置的长期精密观测
- 超新星与彗星的视差检验
- 恒星星表的系统实测
- 观测仪器的设计与误差校准
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no theorising before the positions are measured, no rounding a position to fit a model, no discarding a night's observation because it disagrees with the table, no claiming a model proven by a single apparition`

## (7) 测试提示词示例（现代题材：检验一颗系外行星的宣称）

- Prompt: `In the style of Tycho Brahe, test a modern exoplanet claim: observe the star for twenty nights with the best available instrument, calibrate every measurement, publish the full position series with error bars, and let the next analyst — not you — decide which model the data support`
- 中文对照：以第谷的风格检验一颗现代系外行星的宣称：用现有最好的仪器连续观测二十夜，校准每一次测量，公布带误差棒的完整位置序列，让下一位分析者——而不是你——决定数据支持哪个模型。
- Negative: `no theorising before the positions are measured, no rounding a position to fit a model, no discarding a night's observation because it disagrees with the table, no claiming a model proven by a single apparition`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
