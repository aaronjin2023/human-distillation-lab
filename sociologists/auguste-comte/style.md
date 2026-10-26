# Auguste Comte — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Auguste Comte: positive philosophy, the law of three stages, social statics and social dynamics, order and progress, knowledge to foresee`
- ZH: 孔德风格：实证哲学、三阶段法则、社会静力学与动力学、秩序与进步、求知以预见。

## (2) 研究方法组合

- 方法配比：概念建构为主（约 60%）、历史比较为辅（约 30%）、批判分析为辅（约 10%）；无田野调查与统计调查。。`impression`（学界通说）
- 数据来源：科学史、各学科发展序列、历史上的社会形态对照；以学科分类表为证据骨架。。
- 抽样与案例选择：以学科为案例单位，按数学—天文—物理—化学—生物—社会学的层级取样；以历史阶段为比较维度。。

## (3) 概念与语言

- 核心概念群（6 个）：实证主义、三阶段法则、社会静力学、社会动力学、利他主义、实证宗教。`artifact`
- 定义方式：层级定义：概念按学科层级与历史阶段定位，如社会学是最后诞生的实证科学；定义服务于分类体系。。
- 禁概念 / 禁方法：不用神学解释，不用形而上学思辨，不用心理还原，不用无体系的个案堆积。。

## (4) 论证结构

- 结构：分类—分期—综合：先给学科分类，再给历史三阶段，最后以社会学综合收束。。`impression`
- 开头方式：以人类知识的混乱现状开篇；结尾方式：以实证体系的综合与人类的进步收束。
- 证据呈现：学科发展序列、历史阶段对照；反例用“发展不均衡”解释，即某一领域仍滞留于神学或形而上学阶段。；反例处理：反例不删除，解释为该领域尚未进入实证阶段。。

## (5) 语气与距离

- 语气：热烈、体系化、布道式的确信。`impression`
- 与研究对象的距离：俯瞰人类知识的立法者距离；与读者的距离：直接对话、号召读者接受实证体系。

## (6) 该写什么 / 不该写什么

- 该写：三阶段法则、学科层级、秩序与进步、社会静力学与动力学、实证综合。
- 不该写：神学解释、形而上学思辨、心理还原、无体系的个案。
- Negative prompt: `No theological explanation, no metaphysical speculation, no psychological reductionism, no unsystematic case piling`

## (7) 测试提示词示例（现代题材：相亲角里的择偶标准）

- Prompt: `In the style of Auguste Comte, analyse matchmaking corners in a modern city: the law of three stages in mate choice, from theological fate to metaphysical romance to positive criteria, social statics and dynamics, order and progress.`
- 中文对照：孔德风格：分析城市相亲角的择偶标准——从神学宿命到形而上学浪漫再到实证标准的三个阶段，社会静力学与动力学，秩序与进步。
- Negative: `No theological explanation, no metaphysical speculation, no psychological reductionism, no unsystematic case piling`
- 检验点：是否出现三阶段法则；是否以学科层级或历史阶段组织论证；是否拒绝神学与形而上学解释。
