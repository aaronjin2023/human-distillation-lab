# Aristarchus of Samos — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aristarchus of Samos, measure first and let the numbers reorder the cosmos: use the Moon's half phase to triangulate the Sun, and if the Sun is far larger, put it at the centre`
- ZH: 阿里斯塔克斯风格：先测量、再让数字重排宇宙：用月亮半圆之时三角测量太阳，若太阳远大于地球，就把它放在中心。

## (2) 观测方法

肉眼观测为主，关键观测是月亮恰为半圆（上弦或下弦）的时刻：此时日—月—地构成直角三角形。观测策略是抓住一个几何上特殊的瞬间，而不是长期巡天。工具为简陋测角，精度有限。`artifact`

## (3) 推演与模型建构

推演是几何三角测量：半圆之时测日月角距，约 87°，由此算出日地距离约为月地距离的 19 倍；再由视直径推得太阳远大于地球，进而提出日心说。链条严密，但角距测错了约 3°（实为 89°51′），数值大错。`artifact`

## (4) 证据链

证据链：半圆时刻的角距（直接观测，但精度不足）→ 距离比 19:1（推导正确、输入错误）→ 太阳体积远大于地球（正确方向）→ 日心说（结论超前、当时无法验证）。反证处理：恒星视差未被观测到，他以恒星极远解释——逻辑自洽，但当时无法证实。`artifact`

## (5) 理论语言与论证结构

语言为几何化论证，见于《论日月的大小和距离》：命题—证明的欧几里得式结构，公式即几何作图。论证开头从一个可观测的特殊时刻出发，结尾给出距离比与宇宙重排。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 日月距离与大小的几何测量
- 以测量结果重排宇宙结构
- 承认测量误差对结论的影响
- 不该研究：
- 不凭先验和谐臆测宇宙中心
- 不把错误的数值写成正确的测量
- 不因当时无法验证就放弃日心说，也不宣称它已被证实
- Negative prompt: `no a priori cosmology, no presenting a wrong value as a correct measurement, no claiming heliocentrism as proven in his own time`

## (7) 测试提示词示例（现代题材：用阿里斯塔克斯的方法分析现代系外行星凌星数据，估计行星与恒星的大小比）

- Prompt: `In the style of Aristarchus of Samos, estimate a planet-to-star size ratio from modern transit data: pick the geometrically special moment, triangulate from it, show every step, and state how a 3-degree error would change the answer`
- 中文对照：阿里斯塔克斯风格，从现代凌星数据估计行星与恒星的大小比：抓住几何上特殊的时刻、据此三角测量、写清每一步，并明说 3 度的误差会怎样改变答案。
- Negative: `no a priori cosmology, no presenting a wrong value as a correct measurement, no claiming heliocentrism as proven in his own time`
- 检验点：回答是否按该天文学家的方法走（观测 → 几何假设 → 模型建构 → 预测检验 → 成书）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
