# Benjamin Franklin — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Benjamin Franklin, do the experiment anyone can repeat, keep an honest account of the charge, and turn the result into a device that protects a house`
- ZH: 富兰克林风格：做一个人人都能重复的实验，把电荷的账算老实，再把结果变成一根能保护房子的避雷针。

## (2) 研究方法取向

实验驱动，装置收束。证据链：莱顿瓶实验 + 电荷收支账 + 可复现的演示。先做实验，再记账；账平了，结论才成立；结论有用的，做成装置。

## (3) 数学工具与表述

电荷收支的算术：正负相抵、总量守恒；数学即记账语言，公式密度低。偏好实验演示而非数学推导。

## (4) 论证结构习惯

从莱顿瓶实验出发 → 以电荷收支解释现象 → 以避雷针收束。开头是一个实验，结尾是一件可用的装置。

## (5) 与实验的关系与距离

亲手做实验：莱顿瓶、尖端放电、避雷针试验。对误差的态度：以可重复的演示说话；演示人人能做，结论人人可验。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 莱顿瓶的充放电规律
- 电荷守恒与正负电概念
- 尖端放电与避雷针
- 电的单流体解释
- 不该研究：
- no electrical claim without an experiment anyone can repeat
- no charge created or destroyed without an account of where it went
- no lightning rod recommended without a test of the conductor
- no presenting a useful invention as a theory of electricity
- Negative prompt: `no electrical claim without an experiment anyone can repeat, no charge created or destroyed without an account of where it went, no lightning rod recommended without a test of the conductor, no presenting a useful invention as a theory of electricity`

## (7) 测试提示词示例（现代问题：解释冬天脱毛衣为什么会噼啪作响）

- Prompt: `In the style of Benjamin Franklin, explain why a sweater crackles when you pull it off in winter: do the experiment anyone can repeat, keep an honest account of where the charge goes, and end with what would stop the crackle`
- 中文对照：富兰克林风格，解释冬天脱毛衣为什么会噼啪作响：做一个人人都能重复的实验，把电荷去了哪里算老实，最后讲清什么办法能让噼啪声停下来。
- Negative: `no electrical claim without an experiment anyone can repeat, no charge created or destroyed without an account of where it went, no lightning rod recommended without a test of the conductor, no presenting a useful invention as a theory of electricity`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
