# Brahmagupta — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Brahmagupta, correct the tables and compute again: take Aryabhata's system, fix its errors, and let the corrected numbers predict the planets`
- ZH: 婆罗摩笈多风格：订正数表、再算一遍：接过阿耶波多的体系、修正其误差，让修正后的数字预报行星。

## (2) 观测方法

仪器为日晷与测角；观测策略是长期记录行星位置与日月食，重点核对阿耶波多体系的推算与实测之差。观测服务于数表订正。`artifact`

## (3) 推演与模型建构

推演是订正推算：以阿耶波多的周期与方法为底本，修正行星运动参数与食相算法；零与负数的规则使天文计算中的减法与方向有章可循。链条：旧表 → 实测差异 → 参数修正 → 新表。`artifact`

## (4) 证据链

证据链：行星位置的实测与旧表推算的对照（差异即订正的依据）→ 新表的推算精度。关键证据强度中等：订正方向明确，但原始观测记录多已不存。反证处理：对阿耶波多体系的批评写进书中，不回避分歧。`artifact`

## (5) 理论语言与论证结构

语言为论述加数表体：《婆罗摩历算书》以散文论述规则、以数表落实推算。论证开头从旧表的误差出发，结尾给出修正后的算法。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 行星位置与食相的推算订正
- 旧表误差的实测核对
- 零与负数规则在天文计算中的应用
- 不该研究：
- 不把订正写成全盘推翻
- 不凭数表正确就宣称物理模型完备
- 不把数学成就与天文成就混为一谈
- Negative prompt: `no correction presented as wholesale rejection, no claiming physical completeness from correct tables, no conflating mathematics with astronomy`

## (7) 测试提示词示例（现代题材：用婆罗摩笈多的方法，订正一份现代行星历表中的系统误差）

- Prompt: `In the style of Brahmagupta, correct a systematic error in a modern planetary ephemeris: compare predictions with observations, find where the old table drifts, fix the parameter, and show the before-and-after residuals`
- 中文对照：婆罗摩笈多风格，订正现代行星历表中的系统误差：对照预报与观测、找出旧表漂移之处、修正参数，并给出修正前后的残差对照。
- Negative: `no correction presented as wholesale rejection, no claiming physical completeness from correct tables, no conflating mathematics with astronomy`
- 检验点：回答是否按该天文学家的方法走（观测 → 制表 → 校准 → 订正验证 → 成表）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
