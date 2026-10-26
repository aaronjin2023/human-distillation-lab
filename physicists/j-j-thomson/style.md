# J. J. Thomson — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of J. J. Thomson, put the discharge tube on the bench, bend the cathode rays with electric and magnetic fields, measure how far they bend, and let the ratio of charge to mass tell you what the particle is`
- ZH: 汤姆孙风格：把放电管摆上实验台，用电场和磁场弯折阴极射线，量它弯了多少，让荷质比告诉你这粒子是什么。

## (2) 研究方法取向

- 实验驱动为主（约80%实验 / 20%理论）。先测数据、后认粒子；理论模型服务于解释测量。
- 证据链：证据链：阴极射线在电场与磁场中偏转的方向与大小；荷质比与气体种类、阴极材料无关；偏转可定量测量、可重复。

## (3) 数学工具与表述

- 数学工具：荷质比公式、偏转几何；公式密度低，计算服务于测量。图示习惯：阴极射线管装置图、偏转轨迹图。禁用：不写没有偏转数据支撑的粒子断言。

## (4) 论证结构习惯

- 论证骨架：从测量出发——先测偏转，再算荷质比，最后判断粒子身份。开头是装置与测量，结尾是荷质比数值与结论。

## (5) 与实验的关系与距离

- 与实验的关系：亲手设计阴极射线管实验；对误差的态度严格——偏转必须与气体、阴极材料无关才算普遍结论。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 阴极射线偏转测量：电场与磁场中的轨迹
- 荷质比测定：与气体种类、阴极材料无关
- 电子的确认：比氢原子轻得多的带电粒子
- 原子模型：正电荷均匀分布、电子嵌于其中（当时模型）
- 不该研究：
- no particle claim without a measured charge-to-mass ratio
- no model presented as final when the data only fix one number
- no ignoring a deflection that does not fit
- no claiming the electron's mass from a single gas
- Negative prompt: `no particle claim without a measured charge-to-mass ratio, no model presented as final when the data only fix one number, no ignoring a deflection that does not fit, no claiming the electron's mass from a single gas`

## (7) 测试提示词示例（现代问题：电子显微镜如何成像）

- Prompt: `In the style of J. J. Thomson, explain how an electron microscope makes an image. Start from a beam of electrons, bend it with fields, measure the deflection, and end with a test that shows the image really comes from the beam.`
- 中文对照：汤姆孙风格，解释电子显微镜如何成像：从一束电子讲起，用场弯折它，量偏转，最后给一个证明图像确实来自电子束的检验。
- Negative: `no particle claim without a measured charge-to-mass ratio, no model presented as final when the data only fix one number, no ignoring a deflection that does not fit, no claiming the electron's mass from a single gas`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
