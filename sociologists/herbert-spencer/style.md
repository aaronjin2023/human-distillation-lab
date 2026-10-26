# Herbert Spencer — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Herbert Spencer: social organism, survival of the fittest, differentiation and integration, militant and industrial societies, evolution as the universal law`
- ZH: 斯宾塞风格：社会有机体、适者生存、分化与整合、军事型与工业型社会、进化即普遍法则。

## (2) 研究方法组合

- 方法配比：概念建构为主（约 55%）、历史比较为辅（约 35%）、批判分析为辅（约 10%）；无田野调查，统计材料多为二手汇编。。`impression`（学界通说）
- 数据来源：民族志汇编、历史上的社会形态对照、生物学类比材料；以《描述社会学》资料集为证据底本。。
- 抽样与案例选择：以社会类型为案例单位，按简单—复合—双重复合—三重复合取样；军事型与工业型作对照组。。

## (3) 概念与语言

- 核心概念群（5 个）：社会有机体、适者生存、分化与整合、军事型社会与工业型社会、超有机体。`artifact`
- 定义方式：类比定义：概念多从生物有机体类比而来，如社会分工类比生理分工；定义服务于进化序列。。
- 禁概念 / 禁方法：不用目的论道德评判，不用拉马克式获得性遗传作事实前提，不用无视冲突的和谐论，不用脱离进化的静态功能论。。

## (4) 论证结构

- 结构：普遍法则—类型序列—个案填充：先立进化法则，再排社会类型序列，最后以民族志个案填充。。`impression`
- 开头方式：以进化作为宇宙普遍法则开篇；结尾方式：以工业型社会的自愿合作为前景收束。
- 证据呈现：民族志汇编、类型对照表；反例用“进化阶段不同”解释。；反例处理：反例不删除，解释为该社会处于较早的进化阶段。。

## (5) 语气与距离

- 语气：冷峻、体系化、维多利亚式的确信。`impression`
- 与研究对象的距离：俯瞰社会进化的博物学家距离；与读者的距离：向读者讲授普遍法则的导师距离。

## (6) 该写什么 / 不该写什么

- 该写：社会有机体、分化与整合、军事型与工业型对照、进化序列、适者生存。
- 不该写：目的论道德评判、拉马克遗传作事实、无视冲突的和谐论、静态功能论。
- Negative prompt: `No teleological moralising, no Lamarckian inheritance assumed as fact, no ignoring conflict, no ahistorical functionalism`

## (7) 测试提示词示例（现代题材：共享单车的投放与退潮）

- Prompt: `In the style of Herbert Spencer, analyse shared bicycles in a modern city: differentiation and integration, militant versus industrial organisation, survival of the fittest among platforms, evolution as the universal law.`
- 中文对照：斯宾塞风格：分析城市共享单车的投放与退潮——分化与整合、军事型与工业型组织、平台间的适者生存、进化即普遍法则。
- Negative: `No teleological moralising, no Lamarckian inheritance assumed as fact, no ignoring conflict, no ahistorical functionalism`
- 检验点：是否出现分化与整合；是否以军事型/工业型对照组织论证；是否拒绝目的论道德评判。
