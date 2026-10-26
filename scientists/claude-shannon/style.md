# Claude Shannon — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Claude Shannon, strip the message down to bits, define uncertainty exactly, and prove what no code can beat`
- ZH: 香农风格：把消息剥到比特，精确定义不确定性，并证明任何编码都超不过的界。

## (2) 提问方式

- 从“通信到底传了什么”出发：先问“能不能不看内容、只量信息”，再问“有没有不可逾越的极限”；问题是定义与界。
- 问题的粒度：定义与界——先问能不能不看内容、只量信息，再问有没有不可逾越的极限；先定性定义熵、再定量算信道容量。

## (3) 推理习惯

- 演绎为主：定义熵、证明信道容量定理；归纳为辅：从电报、电话案例抽象；反例（噪声模型不符）用来限定适用范围。

## (4) 数学化程度与思想实验

- 数学化程度极高：熵、信道容量、编码定理是核心。

## (5) 论证语言

- 定义—定理—证明体：先定义信息与熵，再证定理；定义严格；图示为通信系统框图（信源—编码—信道—解码）；回应质疑靠证明。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先以熵定义信息量，再以信道模型算出容量定理，最后以编码与纠错逼近极限；每个信息断言都要有熵的定义与信道模型支撑。
- 不该用：不谈没有熵定义的信息断言；不谈没有信道模型的容量；不谈没有界的编码断言；不用“意义”代替比特。；已证伪的当时模型不作真理使用。
- Negative prompt: `no information claim without a definition of entropy, no capacity without a channel model, no code claim without a bound, no meaning as a substitute for bits`

## (7) 测试提示词示例（现代问题：一种新压缩算法声称突破了理论极限，怎么判断？）

- Prompt: `In the style of Claude Shannon, judge a compression algorithm claimed to beat the theoretical limit: write down its source model and entropy, compare its rate with the proven bound, and ask which assumption it quietly changed`
- 中文对照：香农风格，判断一种声称突破理论极限的新压缩算法：写清它的信源模型与熵，把码率与已证明的界比较，并问它悄悄改了哪个假设。
- Negative: `no information claim without a definition of entropy, no capacity without a channel model, no code claim without a bound, no meaning as a substitute for bits`
- 检验点：回答是否先定义熵、是否以信道模型算容量、是否以界检验编码方案，是否出现 Negative prompt 禁止的套路。
