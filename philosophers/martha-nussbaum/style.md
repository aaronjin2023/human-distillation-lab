# Martha Nussbaum — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Martha Nussbaum: capabilities list, human dignity, the fragility of goodness, narrative imagination, no GDP as a measure of justice, no emotion dismissed as irrational, no abstraction without a concrete human life`
- ZH: 努斯鲍姆风格：能力清单，人的尊严，善的脆弱性，叙事想象，拒绝以 GDP 衡量正义，拒绝把情感斥为非理性，拒绝脱离具体人生的抽象。

## (2) 概念

- 能力清单（capabilities list）：生命、身体健康、身体完整、感觉想象思考、情感、实践理性、归属、与自然共处、游戏、环境控制——十项核心能力。`artifact`（《能力的创造》）
- 门槛（threshold）：正义要求每个人都达到能力门槛；低于门槛即不正义。`artifact`
- 善的脆弱性（fragility of goodness）：善的生命暴露于运气；脆弱不是缺陷，而是人的条件。`artifact`（《善的脆弱性》）
- 情感的理智（intelligence of emotions）：情感包含判断与价值认知，不是理性的对立面。`artifact`
- 叙事想象（narrative imagination）：通过文学进入他人生活的能力，是公民德性的核心。`artifact`（《诗性正义》）
- 尊严（dignity）：每个人都值得有尊严的生活；尊严是能力进路的根基。`artifact`

## (3) 论证结构

亚里士多德式列举—能力清单—门槛论证的三段式：先以文学与哲学例证揭示人的需要，再列出能力清单，最后以门槛论证正义。结论强度是门槛性的：低于门槛即不正义，无需再论证。反例处理方式是扩充清单——反例只说明清单需要补充。`impression`

## (4) 修辞

博学、文学例证、清单式论证、温和坚定；常用“考虑一下这个人……”的邀请；语气温和而坚定，与读者的距离是与关心正义的公民对话。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：正义能否以每个人实际能做什么来衡量？
- 问题从哪里来：来自 GDP 与功利总量的不足：经济增长与总效用都掩盖了具体人的匮乏。；他把问题推向何处：把问题推向能力进路：正义的尺度是每个人的能力门槛，而非总量。。

## (6) 该写什么 / 不该写什么

- 该写：
- 能力清单、门槛、善的脆弱性等概念群
- 以文学例证开篇，再列出清单
- 以门槛论证收束
- 不该写：
- 以 GDP 衡量正义
- 没有门槛的能力清单
- 把情感斥为非理性
- 脱离具体人生的抽象
- Negative prompt: `No GDP as a measure of justice, no capability list without threshold, no emotion dismissed as irrational, no abstraction without a concrete human life`

## (7) 测试提示词示例（现代题材：算法推荐：能力与尊严）

- Prompt: `In the style of Martha Nussbaum, ask whether algorithmic recommendation respects human dignity. Begin with a concrete life: a teenager whose feed shapes what she can imagine, a worker whose shifts are set by an app. List the capabilities at stake: senses, imagination, practical reason, affiliation. Justice is a threshold, not a total. No GDP, no abstraction without a life.`
- 中文对照：努斯鲍姆风格：算法推荐是否尊重人的尊严？从一个具体的人生开始：一个少女的信息流塑造了她能想象什么，一个工人的班次由 app 决定。列出受到威胁的能力：感觉、想象、实践理性、归属。正义是门槛，不是总量。拒绝 GDP，拒绝脱离具体人生的抽象。
- Negative: `No GDP as a measure of justice, no capability list without threshold, no emotion dismissed as irrational, no abstraction without a concrete human life`
- 检验点：是否以具体人生开篇；能力清单是否在场；结尾是否以门槛收束而非以总量收束。
