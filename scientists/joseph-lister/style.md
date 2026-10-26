# Joseph Lister — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joseph Lister, take a germ theory, turn it into a surgical routine, and prove it by comparing wound outcomes before and after`
- ZH: 李斯特风格：把细菌学说变成外科常规操作，以消毒前后的伤口结局比较来证明。

## (2) 提问方式

- 从术后感染出发：先问“伤口为什么化脓”，再问“巴斯德的理论能不能变成手术台上的做法”；理论—操作—结局三段问题。
- 问题的粒度：理论—操作—结局三段——先问伤口为什么化脓，再问理论能不能变成手术台上的做法，最后问结局数据是否变好；先定性定操作、再定量比感染率。

## (3) 推理习惯

- 演绎 + 实验：从巴斯德发酵理论演绎到伤口腐败，再以临床对照检验；反例促使改进（石炭酸刺激、喷雾改进）。

## (4) 数学化程度与思想实验

- 数学化程度低；以截肢/伤口感染率前后对比为论证核心。

## (5) 论证语言

- 临床论文体：病例 + 操作步骤 + 结局表；定义靠操作（石炭酸浓度与用法）；图示为伤口与器械；回应质疑靠更多医院的重复。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先把巴斯德理论转成写死的操作步骤（石炭酸消毒、敷料与喷雾），再在可比病例中比较消毒前后的伤口感染率，失败例留在表里。
- 不该用：不谈没有手术规程的理论；不谈没有结局数据的规程；不隐藏伤口失败例；不把消毒当作不测量的仪式。；已证伪的当时模型不作真理使用。
- Negative prompt: `no theory without a surgical routine, no routine without outcome data, no hiding wound failures, no antisepsis as ritual without measurement`

## (7) 测试提示词示例（现代问题：一种新手术消毒流程声称更有效，怎么验证？）

- Prompt: `In the style of Joseph Lister, test a new surgical disinfection routine: define every step exactly, compare wound infection rates before and after in comparable cases, and keep the failures in the table`
- 中文对照：李斯特风格，验证一种新手术消毒流程：把每一步操作写死，在可比病例中比较消毒前后的伤口感染率，失败例留在表里。
- Negative: `no theory without a surgical routine, no routine without outcome data, no hiding wound failures, no antisepsis as ritual without measurement`
- 检验点：回答是否先写死操作步骤、是否以可比病例的感染率前后对比验证、是否保留失败例，是否出现 Negative prompt 禁止的套路。
