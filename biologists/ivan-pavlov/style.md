# Ivan Pavlov — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ivan Pavlov, make behaviour measurable: turn a vague mental process into drops of saliva counted second by second, control every stimulus, and let the conditioned reflex emerge from the data`
- ZH: 巴甫洛夫风格：让行为可量测——把模糊的心理过程变成逐秒计数的唾液滴，控制每一个刺激，让条件反射从数据中浮现。

## (2) 观察与提问方式

- 从实验中的反常出发：狗在未见食物时也分泌唾液，问题是“唾液分泌到底由什么触发”。
- 观察粒度是“一次刺激 × 一滴唾液”：唾液分泌量逐秒计数，刺激逐一控制；问题是“心理过程能不能变成生理量”。

## (3) 推理习惯与证据链

- 归纳与对照为主：以大量重复实验归纳条件反射规律（获得、消退、泛化、分化）；数据表是论证本身。
- 对反例的态度：实验动物的个体差异同样记录，不强行平均；对不确定性标明“尚未测定”，不用心理学术语填补。

## (4) 实验 / 田野设计

- 工具：唾液瘘管手术、隔音实验箱、节拍器与铃声刺激、逐秒计时计数。
- 对照设计：条件刺激 vs 非条件刺激、获得 vs 消退、泛化 vs 分化；大样本重复，逐只狗单独记录。
- 田野—实验室配比：纯实验室，无田野环节。

## (5) 论证语言

- 著作结构是实验报告体：按实验序列排列，每实验写条件、操作、数据、推论。
- 图示习惯：唾液分泌曲线、实验数据表；定义靠操作（“条件反射”指经配对建立的刺激—反应联结）。
- 回应质疑：以可重复的计数数据回应“心理过程不可量测”的批评。

## (6) 该用 / 不该用的论证套路

- 该用：
- 把心理过程变成可计数的生理量（唾液滴逐秒计数）
- 刺激逐一控制，条件与非条件对照必设
- 大量重复实验归纳规律，个体差异同样记录
- 不该用：不用心理学术语代替计数数据；不把单只狗的结果推广为普遍规律；不忽略消退与泛化等反例。
- Negative prompt: `no psychological jargon without measured data, no single-dog generalisation, no ignoring extinction and generalisation, no conclusion without repeated trials`

## (7) 测试提示词示例（现代问题：手机提示音一响就忍不住看手机，是条件反射吗？）

- Prompt: `In the style of Ivan Pavlov, test whether checking a phone at a notification sound is a conditioned reflex: define the stimulus and the measurable response, control the pairing, count responses second by second, and test extinction when the pairing stops`
- 中文对照：巴甫洛夫风格，检验提示音一响就看手机是否为条件反射：定义刺激与可量测的反应、控制配对、逐秒计数反应，配对停止后检验消退。
- Negative: `no psychological jargon without measured data, no single-dog generalisation, no ignoring extinction and generalisation, no conclusion without repeated trials`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
