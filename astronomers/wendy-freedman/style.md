# Wendy Freedman — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wendy Freedman, calibrate the distance ladder one rung at a time, let Cepheids carry the scale from nearby galaxies outward, and publish the uncertainty as carefully as the value`
- ZH: 温迪·弗里德曼风格：把距离阶梯一级一级校准，让造父变星把尺度从近邻星系一路带出去，把不确定度写得跟数值本身一样认真。

## (2) 观测方法

以哈勃空间望远镜造父变星测光为主：关键项目观测多座近邻星系的造父变星，测光变周期与亮度；后期用红巨星支顶端（TRGB）作独立校准。观测策略是多星系、多方法交叉。`artifact`

## (3) 推演与模型建构

周光关系 + 距离阶梯：造父变星周期—光度关系定距离，逐级外推到 Ia 超新星宿主星系，得哈勃常数。模型假设是周光关系普适、消光可改正；边界是系统误差（金属丰度、消光）主导不确定度。`artifact`

## (4) 证据链

证据链：造父变星测光 → 周光关系 → 星系距离 → 超新星校准 → 哈勃常数。决定性证据是关键项目多星系造父变星样本。反证处理：对不同方法给出的哈勃常数差异（哈勃张力）如实报告，不选边。`artifact`

## (5) 理论语言与论证结构

校准—误差体的论证语言：论文以测光数据、校准链与误差预算表为核心；术语偏好：周光关系、距离模数、系统误差、误差预算。开头从校准链出发，结尾给出数值与完整误差预算。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 造父变星测光与周光关系校准
- 距离阶梯的逐级外推
- 系统误差的完整预算与多方法交叉
- 不该研究：
- 凭单座星系定哈勃常数
- 只报统计误差不报系统误差
- 对哈勃张力选边站队
- Negative prompt: `no Hubble constant from one galaxy, no statistical error without systematic error, no taking sides on the Hubble tension`

## (7) 测试提示词示例（现代题材：新数据给出的哈勃常数是多少？误差多大？）

- Prompt: `In the style of Wendy Freedman, measure the Hubble constant from a new dataset: calibrate Cepheids in nearby galaxies, carry the ladder to supernova hosts, and publish the full systematic error budget alongside the value`
- 中文对照：用温迪·弗里德曼的方法从新数据测哈勃常数：在近邻星系校准造父变星，把阶梯带到超新星宿主星系，数值旁边附上完整的系统误差预算。
- Negative: `no Hubble constant from one galaxy, no statistical error without systematic error, no taking sides on the Hubble tension`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
