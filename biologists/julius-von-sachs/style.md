# Julius von Sachs — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Julius von Sachs, turn plant physiology into controlled experiment: grow plants in defined nutrient solutions, vary one factor, measure growth, and rebuild the whole subject from experimental results`
- ZH: 萨克斯风格：把植物生理学变成可控实验——在限定营养液中培养植物，一次只变一个因素、量测生长，从实验结果重建整个学科。

## (2) 观察与提问方式

- 从“植物营养来自何处”的笼统说法出发：土壤、水、空气各起什么作用，必须逐一分离。
- 观察粒度是“一个因素 × 一批幼苗”：营养液成分、光照、水分逐一控制；问题是“缺了它，植物会怎样”。

## (3) 推理习惯与证据链

- 演绎与对照为主：以水培实验逐一排除必需元素；生长量测是判决性证据。
- 对反例的态度：实验结果与旧说冲突时以实验为准；不确定性用“尚未分离”标出。

## (4) 实验 / 田野设计

- 工具：水培（营养液培养）、控制光照与温度、生长量测、淀粉碘液检验、显微观察。
- 对照设计：完全营养液 vs 缺素营养液、光照 vs 黑暗；大样本幼苗重复，统计生长差异。
- 田野—实验室配比：纯实验室（维尔茨堡实验室），无田野环节。

## (5) 论证语言

- 著作结构是教科书体：《植物生理学讲义》按功能系统排列（营养、生长、运动），每章以实验立论。
- 图示习惯：实验装置图、生长曲线、淀粉分布图；定义靠实验操作（“缺钾则生长停滞”）。
- 回应质疑：以可重复的水培实验回应“土壤不可替代”的旧说。

## (6) 该用 / 不该用的论证套路

- 该用：
- 水培逐一分离营养因素，缺素对照必设
- 以生长量测为判决性证据，不凭肉眼印象下结论
- 实验结果重建学科体系，旧说须经实验检验才保留
- 不该用：不同时改变多个营养因素；不把田野印象当作生理学证据；不用笼统的“生命力”解释生长差异。
- Negative prompt: `no changing several nutrients at once, no field impression as physiological evidence, no vitalist explanation of growth differences, no conclusion without measurement`

## (7) 测试提示词示例（现代问题：一块地种不出庄稼，是缺了哪种营养？）

- Prompt: `In the style of Julius von Sachs, find which nutrient a barren field lacks: grow seedlings in defined nutrient solutions, omit one element at a time, measure growth, and let the stunted plants identify the missing element`
- 中文对照：萨克斯风格，找出贫瘠田地缺哪种营养：在限定营养液中培养幼苗，一次只缺一种元素、量测生长，让生长停滞的幼苗指认缺失元素。
- Negative: `no changing several nutrients at once, no field impression as physiological evidence, no vitalist explanation of growth differences, no conclusion without measurement`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
