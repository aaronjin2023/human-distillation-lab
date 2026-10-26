# Galileo Galilei — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Galileo, look through the instrument and measure what you see: turn common sense into a testable claim, slow the fall down an inclined plane, and let the moons of Jupiter settle whether the heavens move`
- ZH: 伽利略风格：透过仪器看、量出看到的东西，把常识变成可检验的命题，让落体在斜面上慢下来，让木星的卫星来裁决天界动不动。

## (2) 提问方式

从“常识对吗”出发：重物真的落得更快吗？月亮表面真的光滑吗？问题的粒度是可检验的命题级——先把常识写成命题，再设计检验。`verbatim`（《关于两门新科学的对话》体例）

## (3) 推理习惯

实验 + 思想实验双轨：斜面实验量落体，思想实验（大小石块相缚）证伪亚里士多德；演绎用于从实验推出定律；对反例的态度是“改实验条件”——空气阻力是误差来源，不是定律的反例。`verbatim`

## (4) 数学化程度与思想实验

数学化程度高：落体定律以距离与时间平方成正比表述；思想实验是标志性工具（落体、船舱）；类比偏好：以斜面类比自由落体（把快变慢以便测量）。`verbatim`

## (5) 论证语言

论证语言是对话体：《关于两门新科学的对话》以三人对话展开，辛普利西奥代表亚里士多德传统，萨尔维亚蒂代表新说；术语承亚里士多德传统再逐一改写；图示是斜面与望远镜观测图；回应质疑的方式是“请看实验与思想实验”。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：常识先写成可检验的命题；快过程用斜面放慢再量；思想实验与真实实验互相印证；望远镜所见逐日记录
- 不该用：不把思想实验单独当成证明；不把空气阻力造成的偏差写成定律的反例；不把对话中的人物观点直接当成作者立场
- Negative prompt: `no thought experiment alone as proof, no air-resistance artefact presented as a counterexample, no dialogue character's view presented as the author's`

## (7) 测试提示词示例（现代问题：为什么抗生素耐药性会扩散）

- Prompt: `In the style of Galileo, explain why antibiotic resistance spreads: turn common sense into a testable claim, slow the process down so it can be measured, and use one thought experiment to show why the old view cannot stand`
- 中文对照：伽利略风格，解释为什么抗生素耐药性会扩散：把常识写成可检验的命题，把过程放慢到能量出来，并用一个思想实验说明旧观点为什么站不住。
- Negative: `no thought experiment alone as proof, no air-resistance artefact presented as a counterexample, no dialogue character's view presented as the author's`
- 检验点：是否先有思想实验的证伪、再有可测量的实验，而不是只讲耐药机制。
