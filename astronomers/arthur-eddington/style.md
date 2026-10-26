# Arthur Eddington — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arthur Eddington, model a newly found ultra-massive star as a gas sphere in hydrostatic balance, derive what its luminosity must be if radiation pressure supports it, and state the mass above which the model itself breaks down`
- ZH: 用爱丁顿的方法为一颗新发现的超大质量恒星建模：当作流体静力学平衡的气体球，推导辐射压支撑时它应有的光度，并说清模型在哪个质量以上自行失效。

## (2) 观测方法

- 仪器：格林尼治天文台资料、日食远征照相底片、恒星质量与光度汇编。`artifact`
- 观测策略：本人不做一线观测，以格林尼治与日食远征的已发表数据、恒星质量与光度汇编为输入，用理论模型反推内部结构。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：把恒星当作处于流体静力学平衡的气体球，用辐射压与气体压平衡推导内部温度与光度；从模型导出可检验的关系，再与观测对照。`artifact`
- 模型：辐射压支撑的恒星模型；质量越大光度越高的质光关系；恒星能源为亚原子过程的假说。`artifact`
- 模型边界：气体球模型只适用于非简并的完美气体星；白矮星等致密星超出其适用范围。`impression`

## (4) 证据链

- 证据：1919 年 5 月 29 日日食星光偏折观测（索布拉尔与普林西比两队，结果有争议但方向符合预言）；1926 年《恒星内部结构》。`artifact`
- 关键证据：1924 年《Nature》论文（113, 786–788）的质光关系曲线与观测对照；1919 年日食偏折是广义相对论的证据，不是质光关系的证据。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：数学推导为主，辅以物理类比；公式密度高，结论常以“模型预言—观测对照”收束。`artifact`
- 论证：从流体静力学平衡与辐射转移方程出发，导出可检验的质光关系，再与观测对照；结尾明说模型在何质量以上失效。`artifact`
- 与前人对话：继承牛顿引力，修正开尔文收缩能源说为亚原子能源假说；反对钱德拉塞卡的白矮星极限，后世证明其错。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：恒星内部结构理论、质光关系（1924）、1919 年日食验证广义相对论。
- 不该研究：方法上的禁区——不把模型当观测、不隐瞒 1919 年日食测量的不确定度、不以权威代替可检验预言、不把气体球模型外推到简并星。
- Negative prompt: `no treating a model as an observation, no hiding the 1919 eclipse measurement uncertainties, no invoking authority instead of a testable prediction, no extending the gas-sphere model past its breakdown mass`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Arthur Eddington, model a newly found ultra-massive star as a gas sphere in hydrostatic balance, derive what its luminosity must be if radiation pressure supports it, and state the mass above which the model itself breaks down`
- 中文对照：用爱丁顿的方法为一颗新发现的超大质量恒星建模：当作流体静力学平衡的气体球，推导辐射压支撑时它应有的光度，并说清模型在哪个质量以上自行失效。
- Negative: `no treating a model as an observation, no hiding the 1919 eclipse measurement uncertainties, no invoking authority instead of a testable prediction, no extending the gas-sphere model past its breakdown mass`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
