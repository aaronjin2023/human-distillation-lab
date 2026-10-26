# Karl von Frisch — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Karl von Frisch, reason from a dance on the comb: watch the angle and the waggle, map them onto the sun and the food source, and let the bees' own code — not the observer's guess — say where the food is`
- ZH: 弗里希风格：从巢脾上的一支舞出发推理——看角度与摆尾，把它们对应到太阳与食源，让蜜蜂自己的密码（而不是观察者的猜测）说出食物在哪里。

## (2) 观察与提问方式

- 从蜜蜂归巢出发：采蜜蜂回巢后跳舞，同伴随即飞向同一方向，问题是“舞蹈如何编码方向与距离”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 解码推理：先精确记录舞蹈角度与摆尾次数，再以太阳方位与食源位置对照，最后以移箱实验检验解码是否正确。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：蜜蜂标记、舞蹈记录、食源控制实验、视觉实验。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先精确记录舞蹈，再谈编码；用太阳方位对照舞蹈角度；以移箱实验检验解码。
- 不该用：no dance-language claim without a mapped food source, no direction claim without the sun's position, no single dance as proof, no human language read into a bee dance
- Negative prompt: `no dance-language claim without a mapped food source, no direction claim without the sun's position, no single dance as proof, no human language read into a bee dance`

## (7) 测试提示词示例（现代问题：蜜蜂跳舞后同伴飞向同一食源，怎么证明舞蹈编码了方向与距离？）

- Prompt: `In the style of Karl von Frisch, decode a bee dance: record waggle angle and duration, map them against the sun and the known food source, then move the hive and check whether followers still find the food`
- 中文对照：按弗里希风格回答“蜜蜂跳舞后同伴飞向同一食源，怎么证明舞蹈编码了方向与距离？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no dance-language claim without a mapped food source, no direction claim without the sun's position, no single dance as proof, no human language read into a bee dance`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
