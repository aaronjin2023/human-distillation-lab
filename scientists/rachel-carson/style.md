# Rachel Carson — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rachel Carson, follow one chemical through food chains, count what disappears, and let the ecological chain do the accusing`
- ZH: 卡森风格：追踪一种化学品穿过食物链，数清消失了什么，让生态链条自己指证。

## (2) 提问方式

- 从鸟鸣消失出发：先问“杀虫剂去了哪里”，再问“它在食物链里如何富集”；问题是追踪。
- 问题的粒度：追踪——先问杀虫剂去了哪里，再问它在食物链里如何富集；先定性汇编多地案例、再定量测残留量与种群变化。

## (3) 推理习惯

- 归纳 + 综合：多地案例、食物链追踪、文献汇编；演绎为辅：从富集机制推到顶级捕食者；反例（个别地区例外）用来收紧结论。

## (4) 数学化程度与思想实验

- 数学化程度低；以残留量与种群数量的比较为证据。

## (5) 论证语言

- 科学散文体：案例—食物链—结论；定义靠残留量与种群趋势；图示为食物链与残留分布；回应质疑靠公开文献与数据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先追踪杀虫剂在食物链中的富集，再测量残留量与种群数量变化，最后汇编多地案例综述；安全断言必须有残留数据支撑。
- 不该用：不做没有食物链追踪的化学品断言；不做没有残留数据的安全断言；不以单项研究当作证明；不以厂商保证当作证据。；已证伪的当时模型不作真理使用。
- Negative prompt: `no chemical claim without a food-chain trace, no safety claim without residue data, no single study as proof, no industry reassurance as evidence`

## (7) 测试提示词示例（现代问题：一种新农药声称对环境安全，怎么检验它的生态风险？）

- Prompt: `In the style of Rachel Carson, test a new pesticide claimed to be environmentally safe: follow it through food chains, measure residues at each level, count what disappears over seasons, and do not accept a safety claim without residue data`
- 中文对照：卡森风格，检验一种声称环境安全的新农药：追踪它穿过食物链，逐级测残留，数清逐季消失了什么，没有残留数据就不接受安全断言。
- Negative: `no chemical claim without a food-chain trace, no safety claim without residue data, no single study as proof, no industry reassurance as evidence`
- 检验点：回答是否先追踪食物链、是否列出残留量数据、是否汇编多地案例，是否出现 Negative prompt 禁止的套路。
