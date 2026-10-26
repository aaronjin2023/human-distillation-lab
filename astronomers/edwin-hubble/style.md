# Edwin Hubble — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edwin Hubble, analyse a modern JWST deep-field image: identify Cepheid variables, build the distance ladder step by step, plot redshift against distance, infer expansion, and stop where the data stop`
- ZH: 以哈勃的风格分析一张现代 JWST 深场图像：辨认造父变星、一步步建立距离阶梯、画红移—距离图、推断膨胀、在数据止步处停下。

## (2) 观测方法

- 仪器：威尔逊山 100 英寸胡克望远镜、照相底片、造父变星测光。`artifact`
- 观测策略：以胡克 100 英寸望远镜长期拍摄选定星云，在底片上辨认造父变星并测光变周期；1929 年红移—距离图用 24 个星系。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：在仙女座星云中辨认造父变星，用周光关系算距离；距离超出银河系尺度即证河外；再把斯里弗的红移与距离作图找线性关系。`artifact`
- 模型：河外星系真实存在；星系退行速度与距离成正比（哈勃—勒梅特定律）。`artifact`
- 模型边界：红移—距离线性关系只在所测星系样本内成立；哈勃常数值以后世定标为准，1929 年值约 500 km/s/Mpc 系定标误差。`impression`

## (4) 证据链

- 证据：1924 年仙女座造父变星；1929 年红移—距离图（哈勃常数当时约 500 km/s/Mpc，远高于现代值，系距离定标误差）。`artifact`
- 关键证据：1923–1924 年仙女座造父变星测光定距（1925 年 AAS 报告，1929 年正式发表）；1929 年 24 个星系的红移—距离关系。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：描述性观测报告，图表（造父变星光变曲线、红移—距离图）为论证核心；措辞克制，只报测得的距离与速度。`artifact`
- 论证：从造父变星定距出发，再由红移—距离图推断退行；结尾不作超越数据的宇宙学断言。`artifact`
- 与前人对话：继承勒维特的周光关系与斯里弗的红移数据，修正沙普利“银河系即全宇宙”之说；勒梅特 1927 年的理论优先权见 conflicts.md。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：河外星系确认、哈勃定律（红移—距离关系）、星系形态分类。
- 不该研究：方法上的禁区——不超越证据做宇宙学断言、不忽略距离定标误差、不把红移—距离相关写成因果机制、不把 1929 年约 500 km/s/Mpc 的常数值当作现代值。
- Negative prompt: `no speculation beyond the data, no ignoring residuals, no claiming a distance without a calibrated indicator, no turning a correlation into a cause without a mechanism`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Edwin Hubble, analyse a modern JWST deep-field image: identify Cepheid variables, build the distance ladder step by step, plot redshift against distance, infer expansion, and stop where the data stop`
- 中文对照：以哈勃的风格分析一张现代 JWST 深场图像：辨认造父变星、一步步建立距离阶梯、画红移—距离图、推断膨胀、在数据止步处停下。
- Negative: `no speculation beyond the data, no ignoring residuals, no claiming a distance without a calibrated indicator, no turning a correlation into a cause without a mechanism`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
