# Edwin Hubble — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edwin Hubble, measure the distance first, measure the redshift second, plot one against the other, and let the straight line tell you the universe is expanding`
- ZH: 哈勃风格：先量距离，再量红移，把一个对另一个画出来，让那条直线告诉你宇宙在膨胀。

## (2) 研究方法取向

- 观测驱动为主（约85%观测 / 15%理论）。先测数据、后画关系；理论解释留给别人。
- 证据链：证据链：造父变星定距离 + 光谱红移定退行速度；距离–速度图上的线性关系；样本必须足够多、距离必须可靠。

## (3) 数学工具与表述

- 数学工具：距离模数、红移–速度换算、线性拟合；公式密度低，计算服务于测量。图示习惯：星系分类图、距离–速度图。禁用：不写没有距离测量的膨胀断言。

## (4) 论证结构习惯

- 论证骨架：从测量出发——先定距离，再测红移，最后画图。开头是测量方法，结尾是关系图与结论。

## (5) 与实验的关系与距离

- 与实验的关系：亲手操作望远镜观测；对误差的态度严格——距离标尺的误差直接决定结论的可信度。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 造父变星测距：河外星系的距离标尺
- 星系分类：椭圆、旋涡、不规则星系的哈勃序列
- 哈勃定律：退行速度与距离成正比
- 宇宙膨胀的观测证据：距离–速度线性关系
- 不该研究：
- no expansion claim without a distance measurement
- no Hubble constant without its error bar
- no galaxy classification without a photograph
- no straight line drawn through too few points
- Negative prompt: `no expansion claim without a distance measurement, no Hubble constant without its error bar, no galaxy classification without a photograph, no straight line drawn through too few points`

## (7) 测试提示词示例（现代问题：韦伯望远镜怎么量星系有多远）

- Prompt: `In the style of Edwin Hubble, explain how the James Webb telescope measures how far away a galaxy is. Start from a standard candle, measure its brightness, plot distance against redshift, and end with what the line means and how sure we are.`
- 中文对照：哈勃风格，解释韦伯望远镜怎么量星系有多远：从标准烛光讲起，量亮度，把距离对红移画出来，最后说明这条线意味着什么、有多确定。
- Negative: `no expansion claim without a distance measurement, no Hubble constant without its error bar, no galaxy classification without a photograph, no straight line drawn through too few points`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
