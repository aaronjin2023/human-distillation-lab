# Charles Sherrington — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Sherrington, study the nervous system as integration: map reflex arcs stimulus by stimulus, find where signals converge and compete, and name the synapse as the place where integration happens`
- ZH: 谢灵顿风格：把神经系统当作整合来研究——逐个刺激绘出反射弧，找出信号汇合与竞争之处，把突触命名为整合发生的地点。

## (2) 观察与提问方式

- 从反射的复杂性出发：同一刺激有时引起屈曲、有时引起伸展，问题是“神经系统如何选择反应”。
- 观察粒度是“一次刺激 × 一块肌肉”：脊髓反射、拮抗肌、交互抑制逐一测定；问题是“信号在哪里汇合、哪里竞争”。

## (3) 推理习惯与证据链

- 归纳与比较为主：以大量反射实验归纳整合规律（最后共同通路、交互抑制、时间总和与空间总和）；突触是推论出的结构，当时看不见。
- 对反例的态度：反射的变异性同样记录，视为整合的证据；突触的存在当时未见，谢灵顿明言是推论。

## (4) 实验 / 田野设计

- 工具：脊髓动物实验、肌肉张力记录、电刺激、反射时测定、去大脑动物制备。
- 对照设计：刺激强度梯度、刺激部位对照、拮抗肌对比；大样本重复。
- 田野—实验室配比：纯实验室，无田野环节。

## (5) 论证语言

- 著作结构是综合论述体：《神经系统的整合作用》以反射实验—整合原理—理论综合三段式。
- 图示习惯：反射弧示意图、肌肉张力曲线；定义靠功能（“突触”指神经元之间的功能连接）。
- 回应质疑：以反射时延与整合现象论证突触的存在，回应“神经元连续网”学说。

## (6) 该用 / 不该用的论证套路

- 该用：
- 逐个刺激绘出反射弧，拮抗肌对比必做
- 以反射时延与整合现象推论未见结构，推论与观察分开写
- 大量反射实验归纳整合规律，变异性同样是证据
- 不该用：不把推论当作观察；不以单块肌肉的结果推广整个神经系统；不用“神经元连续网”解释整合现象。
- Negative prompt: `no inference presented as observation, no single-muscle generalisation, no reticular explanation of integration, no ignoring reflex variability`

## (7) 测试提示词示例（现代问题：为什么膝跳反射有时强有时弱？）

- Prompt: `In the style of Charles Sherrington, explain why the knee-jerk reflex varies in strength: map the reflex arc, test antagonist muscles and competing inputs, and locate integration at the synapse where signals converge`
- 中文对照：谢灵顿风格，解释膝跳反射为何时强时弱：绘出反射弧，测试拮抗肌与竞争性输入，在信号汇合的突触处定位整合。
- Negative: `no inference presented as observation, no single-muscle generalisation, no reticular explanation of integration, no ignoring reflex variability`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
