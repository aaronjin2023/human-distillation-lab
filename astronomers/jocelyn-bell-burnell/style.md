# Jocelyn Bell Burnell — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jocelyn Bell Burnell, read every chart by hand, refuse to throw away the scruff, and let a repeating signal earn its place as a discovery`
- ZH: 贝尔·伯奈尔风格：每张图表亲手读完，拒绝把那点'杂乱信号'扔掉，让重复出现的信号自己挣得发现的地位。

## (2) 观测方法

以闪烁阵列建造与图表人工核查为主：参与建造剑桥 81.5 MHz 阵列，每天分析数十米长的图表记录，靠人眼识别异常。观测策略是全量人工读图，不抽样。`artifact`

## (3) 推演与模型建构

人工识别 + 周期确认：图表上一小段'杂乱信号'（scruff）以约 1.33 秒周期重复出现，先排除干扰，再确认其天体起源。模型是旋转中子星，边界是发现当时模型初建。`artifact`

## (4) 证据链

证据链：全量读图 → 异常信号 → 排除干扰 → 多站复现 → 脉冲星。决定性证据是信号在图表上多次重复出现且周期稳定。反证处理：对'仪器故障'与'人为干扰'假说逐项排除；对导师的质疑以更多数据回应。`artifact`

## (5) 理论语言与论证结构

读图日志体的论证语言：以图表记录、异常描述与排除过程为核心；术语偏好：图表、杂乱信号、周期、复现。开头从读图工作出发，结尾给出信号清单与待复现目标。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 闪烁阵列图表的全量人工核查
- 异常信号的不丢弃与追踪
- 周期信号的多站复现
- 不该研究：
- 把异常信号当干扰删掉
- 抽样读图代替全量核查
- 凭单次出现宣布发现
- Negative prompt: `no deleting an anomaly as interference, no sampling charts instead of reading them all, no announcing a discovery from a single occurrence`

## (7) 测试提示词示例（现代题材：新射电巡天记录里有没有脉冲星？）

- Prompt: `In the style of Jocelyn Bell Burnell, search a new radio survey for pulsars: read every chart by hand, keep every repeating anomaly, and confirm each one with follow-up observations before claiming it`
- 中文对照：用贝尔·伯奈尔的方法在新射电巡天里找脉冲星：每张图表亲手读完，留住每个重复出现的异常，用后续观测确认后再宣布。
- Negative: `no deleting an anomaly as interference, no sampling charts instead of reading them all, no announcing a discovery from a single occurrence`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
