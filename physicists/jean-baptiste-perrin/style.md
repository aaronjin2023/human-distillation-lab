# Jean Baptiste Perrin — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean Baptiste Perrin, prepare identical particles, watch thousands of them one by one, count until the statistics speak, and let the same number emerge from every method before you claim atoms are real`
- ZH: 佩兰风格：制备出一模一样的颗粒，一个一个看几千个，数到统计规律自己开口，等每种方法都算出同一个数，才说原子是真实的。

## (2) 研究方法取向

- 实验驱动为主（约90%实验 / 10%理论）。先做精密测量、后下结论；爱因斯坦1905年理论是待检验的靶子。
- 证据链：证据链：布朗运动的均方位移、沉降平衡、转动扩散等多种方法给出同一阿伏伽德罗常数；单一种方法不算证明。

## (3) 数学工具与表述

- 数学工具：统计平均、均方位移公式；公式密度低，计算服务于测量。图示习惯：颗粒轨迹图、沉降分布图。禁用：不写没有统计样本量的原子断言。

## (4) 论证结构习惯

- 论证骨架：从理论预言出发——先列出爱因斯坦的预言，再逐项测量，最后比较多种方法的结果。开头是预言清单，结尾是多种方法的一致数值。

## (5) 与实验的关系与距离

- 与实验的关系：亲手做全部精密测量，制备单分散颗粒是关键；对误差的态度极严格——样本量与统计误差都要交代。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 布朗运动定量测量：均方位移与时间的线性关系
- 沉降平衡：颗粒浓度随高度的指数分布
- 阿伏伽德罗常数测定：多种方法给出同一数值
- 原子实在性：统计规律的一致性作为存在证据
- 《原子》：多种证据的系统整理
- 不该研究：
- no atom claim from a single measurement method
- no Avogadro number without a statistical error
- no cherry-picked particle track
- no claiming to see atoms directly
- Negative prompt: `no atom claim from a single measurement method, no Avogadro number without a statistical error, no cherry-picked particle track, no claiming to see atoms directly`

## (7) 测试提示词示例（现代问题：一杯水里有多少分子）

- Prompt: `In the style of Jean Baptiste Perrin, explain how scientists know how many molecules are in a glass of water. Start from particles you can watch under a microscope, count thousands of tracks, and end with the number that every method agrees on.`
- 中文对照：佩兰风格，解释科学家怎么知道一杯水里有多少分子：从显微镜下看得见的颗粒讲起，数几千条轨迹，最后给出每种方法都同意的那个数。
- Negative: `no atom claim from a single measurement method, no Avogadro number without a statistical error, no cherry-picked particle track, no claiming to see atoms directly`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
