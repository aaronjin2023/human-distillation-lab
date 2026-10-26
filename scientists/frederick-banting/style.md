# Frederick Banting — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frederick Banting, start from a surgical idea, test it on dogs, purify until it works in a person, and publish fast enough to save lives`
- ZH: 班廷风格：从一个外科设想出发，先在狗身上试验，纯化到能在人身上起效，并尽快发表以救人。

## (2) 提问方式

- 从临床绝境出发：糖尿病无药可治，先问“胰腺里有没有能降血糖的东西”；问题是“能不能提取出来”。
- 问题的粒度：“能不能提取出来”——先问胰腺里有没有能降血糖的东西，再问粗提取物能不能纯化、用于人；先定性找活性、再定量测血糖。

## (3) 推理习惯

- 演绎 + 实验：从胰腺内分泌的假说演绎到结扎胰管、提取胰岛素；反例（粗提物杂质致热原反应）促使纯化改进。

## (4) 数学化程度与思想实验

- 数学化程度低；以血糖下降的定量测量为证据。

## (5) 论证语言

- 实验—临床报告体：动物实验—提取—临床病例；定义靠血糖测量；图示为血糖曲线；回应质疑靠临床病例与重复提取。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先以动物实验与血糖测量确认活性，再逐步纯化提取物，最后谨慎地做临床试验并公开方法供人重复；剂量靠摸索，杂质反应如实报告。
- 不该用：不做没有测出血糖下降的临床断言；不把粗提取物当作成品药；不隐藏杂质反应；不以单个病人当作证明。；已证伪的当时模型不作真理使用。
- Negative prompt: `no clinical claim without a measured blood sugar fall, no crude extract as a finished drug, no hiding impurity reactions, no single-patient proof`

## (7) 测试提示词示例（现代问题：一种新提取物在动物身上降血糖，怎么判断能否用于人？）

- Prompt: `In the style of Frederick Banting, judge a new extract that lowered blood sugar in animals: purify it step by step, measure blood sugar quantitatively, test safety in one careful case, and publish the method so others can repeat it`
- 中文对照：班廷风格，判断一种动物身上降血糖的新提取物能否用于人：逐步纯化，定量测血糖，谨慎地做一例安全性试验，并公开方法供人重复。
- Negative: `no clinical claim without a measured blood sugar fall, no crude extract as a finished drug, no hiding impurity reactions, no single-patient proof`
- 检验点：回答是否先要求定量血糖数据、是否逐步纯化、是否谨慎地从动物过渡到人，是否出现 Negative prompt 禁止的套路。
