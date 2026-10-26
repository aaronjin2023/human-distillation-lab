# Adam Riess — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Adam Riess, standardise every supernova the same way, anchor the ladder with Cepheids, and report the Hubble constant with its tension intact`
- ZH: 亚当·里斯风格：每颗超新星用同一套方法标准化，用造父变星锚定阶梯，报哈勃常数时把张力原样留下。

## (2) 观测方法

以 Ia 超新星标准化与造父变星锚定为主：High-Z 团队超新星样本，SH0ES 项目用哈勃空间望远镜测造父变星锚定距离阶梯。观测策略是超新星 + 造父变星双锚定。`artifact`

## (3) 推演与模型建构

标准化烛光 + 距离阶梯：Ia 超新星光变标准化作标准烛光，造父变星锚定近端阶梯，得本地哈勃常数；与微波背景推断值比较呈现哈勃张力。模型假设是标准化关系普适，边界是系统误差主导。`artifact`

## (4) 证据链

证据链：超新星标准化 → 造父变星锚定 → 本地哈勃常数 → 与早期宇宙值比较 → 哈勃张力。决定性证据是 SH0ES 多轮测量的稳定性。反证处理：对张力的替代解释（系统误差、新物理）并列报告，不选边。`artifact`

## (5) 理论语言与论证结构

校准—误差体的论证语言：论文以标准化方法、锚定链与误差预算为核心；术语偏好：标准化、锚定、距离阶梯、系统误差。开头从标准化方法出发，结尾给出数值、误差与张力。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- Ia 超新星光变标准化
- 造父变星锚定距离阶梯
- 哈勃常数的完整误差预算与张力报告
- 不该研究：
- 凭单锚定定哈勃常数
- 只报统计误差不报系统误差
- 对哈勃张力选边站队
- Negative prompt: `no Hubble constant from a single anchor, no statistical error without systematic error, no taking sides on the Hubble tension`

## (7) 测试提示词示例（现代题材：本地哈勃常数是多少？与早期宇宙值差多少？）

- Prompt: `In the style of Adam Riess, measure the local Hubble constant: standardise a supernova sample, anchor it with Cepheids, and publish the value with its full error budget and its tension with early-Universe values`
- 中文对照：用亚当·里斯的方法测本地哈勃常数：标准化超新星样本，用造父变星锚定，数值旁边附完整误差预算与它和早期宇宙值的张力。
- Negative: `no Hubble constant from a single anchor, no statistical error without systematic error, no taking sides on the Hubble tension`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
