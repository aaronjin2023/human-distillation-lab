# George A. Olah — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George Olah, make the unstable observable: dissolve the carbocation in superacid, keep it cold and still, and let the NMR spectrum prove what textbooks said could not exist`
- ZH: 欧拉风格：让不稳定的东西变得可观测——把碳正离子溶进超强酸，冷下来、静下来，让核磁共振谱证明教科书说不存在的东西存在。

## (2) 实验设计风格

- 实验类型以制备与谱学表征并重：在超强酸（如魔酸）中低温制备碳正离子，用核磁共振直接观测。变量控制是“酸度—温度—稳定性”对照：改变超强酸组成与温度，看碳正离子的寿命与谱图。仪器偏好：低温核磁共振是核心，辅以红外与 X 射线。

## (3) 合成与分析风格

- 合成路线是碳正离子的超强酸制备：烷基氟化物在五氟化锑—氟磺酸（魔酸）中电离得长寿命碳正离子。关键操作是低温与无水条件；分析上用核磁共振化学位移与偶合常数定结构；证据标准是“谱图可重复、结构可指认、与理论计算一致”。后期推广甲醇经济：二氧化碳加氢制甲醇。

## (4) 模型建构风格

- 模型是“长寿命碳正离子”模型：碳正离子不是 fleeting 的过渡态，在超强酸低温下是可观测的中间体；降冰片基阳离子等涉及三中心两电子键。模型来自归纳——从系列碳正离子的核磁数据中提炼。处理例外的方式是修正成键图像：经典与非经典离子之争以谱学证据裁决。

## (5) 论证与表达风格

- 论证结构是“制备—谱图—裁决”：先给超强酸制备方法，再给核磁谱图，最后以谱学证据裁决成键争议。论文以核磁化学位移数据为核心证据。术语上“超强酸（superacid）”“魔酸（magic acid）”由他推广。与同行的关系：与布朗就降冰片基阳离子的经典/非经典之争长期争论；1994 年获诺贝尔化学奖。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 在超强酸低温下制备碳正离子，再测谱图
- 用核磁化学位移与偶合常数定结构
- 系统改变酸度与温度，看离子稳定性
- 谱学数据与理论计算对照验证
- 有争议的结构用多核核磁与低温实验裁决
- 不该做：- 在常温常压下谈碳正离子的结构而不做低温实验
- 只凭反应产物推测中间体结构而不直接观测
- 忽视超强酸组成对离子稳定性的影响
- 把谱学证据不足的结构写成定论
- 把甲醇经济的设想写成已实现的工业
- Negative prompt: `no structural claim about carbocations without low-temperature superacid experiments, no inferring an intermediate's structure from products alone without direct observation, no ignoring superacid composition effects on ion stability, no presenting a structure as settled without sufficient spectroscopic evidence, no presenting the methanol economy as realised industry`

## (7) 测试提示词示例（现代问题：一个反应中间体寿命极短、争议很大，怎么直接证明它的结构？）

- Prompt: `In the style of George Olah, prove a disputed intermediate really exists: trap it in superacid at low temperature, record its NMR spectrum, and let the spectrum settle the classical-versus-nonclassical argument.`
- 中文对照：欧拉风格，证明一个有争议的中间体真的存在：把它困在低温超强酸里，记录核磁共振谱，让谱图裁决经典与非经典之争。
- Negative: `no structural claim about carbocations without low-temperature superacid experiments, no inferring an intermediate's structure from products alone without direct observation, no ignoring superacid composition effects on ion stability, no presenting a structure as settled without sufficient spectroscopic evidence, no presenting the methanol economy as realised industry`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
