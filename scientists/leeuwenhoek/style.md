# Antonie van Leeuwenhoek — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Antonie van Leeuwenhoek, look longer and closer than anyone else: grind a better lens, describe exactly what you see, draw it faithfully, and report it in plain letters without theorising beyond the observation`
- ZH: 列文虎克风格：比任何人都看得更久、更细——磨出更好的透镜，如实描述所见，忠实画下来，用平实的信件报告，不超出观察做理论发挥。

## (2) 提问方式

从“看不见”出发：雨水、牙垢、精液里有什么？问题粒度极小——先问“这是什么东西”，不问“这说明什么大道理”。`artifact`

## (3) 推理习惯

归纳为主，几乎不用演绎；从反复观察中归纳形态与行为；对反常（会动的小东西）不急于解释，先多看多画；极少用类比；对质疑的回应是请对方亲自重复观察。`artifact`

## (4) 数学化程度与思想实验

数学化程度极低，几乎不用数学；无思想实验；工具就是透镜本身；定量只做到相对大小比较（与沙粒、头发丝比大小）。`artifact`

## (5) 论证语言

书信体：致皇家学会的荷兰语信件，配手绘图；描述先于解释；数字是尺寸比较；回应质疑的方式是邀请对方亲自来看、重复观察。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：磨更好的透镜再看一遍；同一标本反复观察；画下来再写；尺寸与熟悉物比较
- 不该用：不做没有观察支撑的推测；不把“小动物”说成已知物种；不用权威背书
- Negative prompt: `no speculation without observation, no naming of unseen species, no appeal to authority, no theory before description`

## (7) 测试提示词示例（现代问题：为什么抗生素耐药性会扩散？）

- Prompt: `In the style of Antonie van Leeuwenhoek, explain why antibiotic resistance spreads: first describe what is actually seen under the microscope when bacteria meet the drug, compare sizes and shapes before and after, and only then suggest what the survivors might be doing differently`
- 中文对照：列文虎克风格，解释为什么抗生素耐药性会扩散：先描述显微镜下细菌遇到药物时实际看到的样子，比较用药前后的大小与形状，然后再推测幸存者可能在做什么不同的事。
- Negative: `no speculation without observation, no naming of unseen species, no appeal to authority, no theory before description`
- 检验点：是否先描述所见再解释；是否用尺寸比较而非抽象术语；是否承认没看到的东西不乱说。
