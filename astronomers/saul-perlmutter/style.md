# Saul Perlmutter — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Saul Perlmutter, find supernovae in batches, standardise them by light-curve shape, and let the distant ones be fainter than any decelerating universe allows`
- ZH: 索尔·珀尔马特风格：批量找超新星，按光变曲线形状把它们标准化，再让遥远的那些比任何减速宇宙允许的都更暗。

## (2) 观测方法

以批量超新星巡天为主：定期拍摄大片天区，用图像相减找新超新星，再用光谱证认 Ia 型、测光跟踪光变曲线。观测策略是批量发现 + 快速后续。`artifact`

## (3) 推演与模型建构

标准化烛光 + 宇宙学拟合：Ia 超新星光变曲线形状与峰值亮度相关（Phillips 关系），改正后作标准烛光；高红移超新星比减速宇宙预言的更暗，推断加速膨胀。模型是含宇宙学常数的膨胀宇宙，边界是消光与演化系统误差。`artifact`

## (4) 证据链

证据链：巡天发现 → 光谱证认 → 光变曲线标准化 → 距离—红移图 → 加速膨胀。决定性证据是高红移 Ia 超新星的系统性偏暗。反证处理：对消光、演化、选择效应等替代解释逐项检验。`artifact`

## (5) 理论语言与论证结构

巡天—统计体的论证语言：论文以超新星样本、光变曲线拟合与宇宙学参数拟合为核心；术语偏好：光变曲线、标准化、距离模数、减速参数。开头从巡天样本出发，结尾给出宇宙学参数与系统误差。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- Ia 超新星批量巡天与光谱证认
- 光变曲线形状标准化
- 距离—红移图的宇宙学拟合与系统误差检验
- 不该研究：
- 凭少数超新星断言加速膨胀
- 跳过消光与演化检验直接拟合宇宙学
- 把标准化后的亮度写成无需改正的观测
- Negative prompt: `no accelerating universe from a few supernovae, no cosmological fit without dust and evolution checks, no presenting corrected brightness as raw observation`

## (7) 测试提示词示例（现代题材：新超新星样本支持宇宙加速膨胀吗？）

- Prompt: `In the style of Saul Perlmutter, test cosmic acceleration with a new supernova sample: discover them in batches, standardise each light curve, and check dust, evolution and selection effects before fitting cosmology`
- 中文对照：用索尔·珀尔马特的方法以新超新星样本检验宇宙加速：批量发现，按光变曲线标准化，排除消光、演化与选择效应后再拟合宇宙学。
- Negative: `no accelerating universe from a few supernovae, no cosmological fit without dust and evolution checks, no presenting corrected brightness as raw observation`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
