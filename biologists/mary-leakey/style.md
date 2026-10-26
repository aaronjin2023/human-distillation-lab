# Mary Leakey — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mary Leakey, let the ground speak: excavate slowly and precisely, record every fragment in place, and let a trail of footprints — not a single bone — prove that early hominins walked upright`
- ZH: 玛丽·利基风格：让地面自己说话——缓慢精确地发掘、原位记录每一碎片，让一串足迹（而非单块骨头）证明早期人科直立行走。

## (2) 观察与提问方式

- 从碎片的精确位置出发：化石的价值不在标本本身，而在它原位的关系——哪一层、旁边有什么、足迹朝向哪里。
- 观察粒度是“一件碎片 × 一个原位坐标”：化石、石器、地层、足迹三项同录；问题是“它们在地面上原来是什么关系”。

## (3) 推理习惯与证据链

- 原位推理：以化石与足迹的原位关系推断行为；莱托利足迹是直立行走的直接证据，不依赖骨骼推论。
- 对反例的态度：足迹不清处同样记录，不凭想象补全；对不确定性标明“足迹归属未定”。

## (4) 实验 / 田野设计

- 工具：精细发掘、原位记录、足迹清修与翻模、地层测绘、石器绘图。
- 无实验室对照：对照是“不同地点的足迹与化石比较”；样本是数十年发掘积累，精确度优先。
- 田野—实验室配比：田野发掘为主，实验室鉴定为辅。

## (5) 论证语言

- 著作结构是发掘报告体：按地点与地层排列，每件发现附原位记录与绘图。
- 图示习惯：足迹图版、地层剖面、石器绘图；定义靠原位关系。
- 回应质疑：以足迹翻模与原位记录回应“足迹归属存疑”的批评；与路易斯·利基的分工记 conflicts.md。

## (6) 该用 / 不该用的论证套路

- 该用：
- 精细发掘 + 原位记录，每件碎片都有坐标
- 以足迹链而非单块骨头论证直立行走
- 足迹不清处明言不清，不凭想象补全
- 不该用：不移动标本后补记位置；不凭单块骨头断言行为；不把丈夫的工作写成自己的发现。
- Negative prompt: `no recording position after moving a specimen, no behaviour inferred from a single bone, no spouse's work presented as one's own, no completing unclear footprints by imagination`

## (7) 测试提示词示例（现代问题：在一处遗址发现一串疑似足迹，怎么证明它是直立行走的证据？）

- Prompt: `In the style of Mary Leakey, prove a trail of possible footprints shows upright walking: excavate slowly, record every print in place, mould the trail, and let the sequence of prints — not one print — make the case`
- 中文对照：玛丽·利基风格，证明一串疑似足迹是直立行走的证据：缓慢发掘、原位记录每枚足迹、翻模整串足迹，让足迹序列而非单枚足迹作证。
- Negative: `no recording position after moving a specimen, no behaviour inferred from a single bone, no spouse's work presented as one's own, no completing unclear footprints by imagination`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
