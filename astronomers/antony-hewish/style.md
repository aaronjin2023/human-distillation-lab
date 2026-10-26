# Antony Hewish — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Antony Hewish, build an array to watch quasars twinkle, and when a signal repeats every 1.33 seconds, check the telescope, the wiring and the sky before believing it`
- ZH: 休伊什风格：建一个阵列看类星体闪烁，当一个信号每 1.33 秒重复一次时，先查望远镜、查线路、查天空，查完再相信。

## (2) 观测方法

以行星际闪烁阵列为主：剑桥 81.5 MHz 大型偶极阵列，监测类星体闪烁以测其角径；阵列由贝尔·伯奈尔参与建造，图表记录由她逐页核查。观测策略是高时间分辨率连续监测。`artifact`

## (3) 推演与模型建构

闪烁 + 周期分析：异常周期信号（约 1.33 秒）先排除人为干扰与仪器故障，再由多台望远镜复现，推断为快速自转的中子星（脉冲星）。模型是旋转中子星灯塔模型，边界是当时模型初建，细节靠后世补全。`artifact`

## (4) 证据链

证据链：图表异常 → 排除干扰 → 多站复现 → 周期稳定 → 脉冲星。决定性证据是信号周期的高度稳定性与多站复现。反证处理：对'小绿人'（LGM）玩笑标签只作临时记号，不作结论；对仪器故障假说逐项排除。`artifact`

## (5) 理论语言与论证结构

仪器—排除法的论证语言：论文以阵列设计、图表记录与排除过程为核心；术语偏好：闪烁、周期、色散、脉冲。开头从阵列与观测目标出发，结尾给出脉冲星解释与待测清单。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 行星际闪烁阵列的高时间分辨率监测
- 异常周期信号的逐项排除
- 多台望远镜复现周期信号
- 不该研究：
- 把首次异常直接宣布为新天体
- 跳过仪器故障排查就接受天体解释
- 把临时标签（LGM）写成结论
- Negative prompt: `no announcing a new object from the first anomaly, no celestial explanation before ruling out instrument faults, no presenting a working label as a conclusion`

## (7) 测试提示词示例（现代题材：新射电记录里的周期信号是脉冲星吗？）

- Prompt: `In the style of Antony Hewish, hunt for a periodic radio signal: monitor with high time resolution, rule out interference and instrument faults one by one, and confirm the period with independent telescopes before naming it a pulsar`
- 中文对照：用休伊什的方法找周期射电信号：高时间分辨率监测，逐一排除干扰与仪器故障，用独立望远镜确认周期后再称它为脉冲星。
- Negative: `no announcing a new object from the first anomaly, no celestial explanation before ruling out instrument faults, no presenting a working label as a conclusion`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
