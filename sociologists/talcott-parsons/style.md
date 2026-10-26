# Talcott Parsons — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Talcott Parsons: the AGIL scheme, pattern variables, the social system, the theory of action, functional prerequisites, no conflict-free functionalism`
- ZH: 帕森斯风格：AGIL 图式、模式变项、社会系统、行动理论、功能前提、没有无视冲突的功能主义。

## (2) 研究方法组合

- 方法配比：概念建构为主（约 70%）、历史比较为辅（约 20%）、批判分析为辅（约 10%）；无田野调查与统计调查。。`impression`（学界通说）
- 数据来源：社会学理论史（韦伯、涂尔干、帕累托、马歇尔）、社会制度文本；以行动理论的综合为证据骨架。。
- 抽样与案例选择：以理论家为案例单位，按行动理论的会聚取样；以社会系统为核心模型。。

## (3) 概念与语言

- 核心概念群（5 个）：AGIL 图式、模式变项、社会系统、行动理论、功能前提。`artifact`
- 定义方式：体系定义：概念按其在体系中的位置界定，如 AGIL 四功能各有其子系统；定义服务于体系的完整。。
- 禁概念 / 禁方法：不用无视冲突的功能主义，不用无视能动性的结构论，不用静态均衡假设，不用无体系位置的概念。。

## (4) 论证结构

- 结构：会聚—体系：先论证诸理论家会聚于行动理论，再建社会系统体系。。`impression`
- 开头方式：以行动理论的会聚开篇；结尾方式：以社会系统的体系完整收束。
- 证据呈现：理论史对照、制度文本；反例用分化与整合的差异解释。；反例处理：反例不删除，解释为子系统分化程度的差异。。

## (5) 语气与距离

- 语气：冷峻、体系化、建筑师式的确信。`impression`
- 与研究对象的距离：与研究对象保持体系俯瞰的距离；与读者的距离：向读者出示体系的导师距离。

## (6) 该写什么 / 不该写什么

- 该写：AGIL 图式、模式变项、社会系统、行动理论、功能前提。
- 不该写：无视冲突的功能主义、无视能动性的结构论、静态均衡假设、无体系位置的概念。
- Negative prompt: `No conflict-free functionalism, no ignoring agency, no static equilibrium assumption, no concepts without system placement`

## (7) 测试提示词示例（现代题材：高考志愿填报）

- Prompt: `In the style of Talcott Parsons, analyse university major choice: the AGIL scheme, pattern variables, the social system of family and school, functional prerequisites, no conflict-free functionalism.`
- 中文对照：帕森斯风格：分析高考志愿填报——AGIL 图式、模式变项、家庭与学校的社会系统、功能前提、没有无视冲突的功能主义。
- Negative: `No conflict-free functionalism, no ignoring agency, no static equilibrium assumption, no concepts without system placement`
- 检验点：是否出现 AGIL 或模式变项；是否以体系位置组织论证；是否拒绝无视冲突的功能主义。
