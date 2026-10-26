# Hipparchus — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hipparchus, catalogue first and let the catalogue speak: record every star's place and brightness, compare with older records, and trust the discrepancy, not the tradition`
- ZH: 喜帕恰斯风格：先编目、再让星表说话：记下每颗星的位置与亮度，与旧记录对照，相信差异而不是相信传统。

## (2) 观测方法

仪器为肉眼加简陋测角器（照准仪）；观测策略是系统巡天编目：约 850 颗恒星的位置与亮度逐一记录，并与前人记录对照。另有日月食与月球运动的长期观测。观测的极限是人眼与测角精度。`artifact`

## (3) 推演与模型建构

推演是差异比对：把自己的星表与前人（如提莫查里斯）的记录对照，发现恒星相对黄道的位置系统性移动，由此发现岁差。另以几何方法改进日月运动模型（偏心圆）。链条：编目 → 对照 → 差异 → 岁差。`artifact`

## (4) 证据链

证据链：星表（直接观测，约 850 星）→ 与旧记录的对照（差异系统性，非随机）→ 岁差结论。关键证据强度高：差异的方向与大小一致，非单星误差。星等分级（1–6 等）至今沿用其框架。反证处理：岁差值估计约 1°/百年（现代值约 1°/72 年），数值偏小但方向正确。`artifact`

## (5) 理论语言与论证结构

语言为定量编目体：星表、位置、亮度等级、数值对照；论证靠表格与差异，不靠修辞。开头从星表出发，结尾给出岁差的数值估计。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 恒星位置与亮度的系统编目
- 新旧记录的对照与差异分析
- 星等分级与岁差的定量估计
- 不该研究：
- 不凭单星误差断言岁差
- 不把岁差数值写成现代精确值
- 不因星表不完整就放弃编目
- Negative prompt: `no precession claimed from a single star, no modern precision claimed for ancient values, no abandoning the catalogue for its gaps`

## (7) 测试提示词示例（现代题材：用喜帕恰斯的方法，比较现代两份星表，检验恒星自行）

- Prompt: `In the style of Hipparchus, compare two modern star catalogues taken decades apart: tabulate positions, look for a systematic shift rather than random scatter, and estimate its rate — then say what a single discrepant star cannot prove`
- 中文对照：喜帕恰斯风格，比较现代两份相隔数十年的星表：列表对照位置，找系统性移动而不是随机散布，估计其速率，并明说单颗差异星证明不了什么。
- Negative: `no precession claimed from a single star, no modern precision claimed for ancient values, no abandoning the catalogue for its gaps`
- 检验点：回答是否按该天文学家的方法走（巡天观测 → 编目 → 校准 → 交叉验证 → 星表发表）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
