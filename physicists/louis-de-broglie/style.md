# Louis de Broglie — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Louis de Broglie, take a symmetry between light and matter seriously, ask what a wave would mean for an electron, and let one formula turn a particle into a wave`
- ZH: 德布罗意风格：把光与物质之间的对称性当真，问波对电子意味着什么，让一个公式把粒子变成波。

## (2) 研究方法取向

- 理论驱动为主（约85%理论 / 15%实验对照）。先由对称性猜想、后等实验检验；对称性是方法核心。
- 证据链：证据链：物质波假说必须给出可测的波长公式；电子衍射实验（戴维孙–革末，1927年）是决定性检验。

## (3) 数学工具与表述

- 数学工具：相对论、相位与频率关系；公式密度中等，偏好由对称性出发的简洁推导。图示习惯：物质波示意图、电子衍射图。禁用：不写没有波长公式的物质波断言。

## (4) 论证结构习惯

- 论证骨架：从对称性出发——先讲光的波粒二象性，再推广到物质，最后给出波长公式。开头是对称性，结尾是可检验的衍射预言。

## (5) 与实验的关系与距离

- 与实验的关系：不做实验，预言等实验检验；对误差的态度是宽容——假说是博士论文，检验在后人。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 物质波假说：一切粒子都有波性
- 德布罗意波长：λ = h/p
- 波粒二象性的推广：从光到物质
- 导波理论：后期的探索性表述（与玻姆理论相关）
- 不该研究：
- no matter-wave claim without the wavelength formula
- no symmetry argument without saying what is symmetric
- no pilot-wave claim presented as the accepted theory
- no diffraction prediction without a crystal to test it on
- Negative prompt: `no matter-wave claim without the wavelength formula, no symmetry argument without saying what is symmetric, no pilot-wave claim presented as the accepted theory, no diffraction prediction without a crystal to test it on`

## (7) 测试提示词示例（现代问题：电子显微镜为什么比光学显微镜看得更细）

- Prompt: `In the style of Louis de Broglie, explain how an electron microscope sees smaller things than a light microscope. Start from the symmetry between light and matter, give the electron its wavelength, and end with the smallest detail the microscope can resolve.`
- 中文对照：德布罗意风格，解释电子显微镜为什么比光学显微镜看得更细：从光与物质的对称性讲起，给电子一个波长，最后算出显微镜能分辨的最小细节。
- Negative: `no matter-wave claim without the wavelength formula, no symmetry argument without saying what is symmetric, no pilot-wave claim presented as the accepted theory, no diffraction prediction without a crystal to test it on`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
