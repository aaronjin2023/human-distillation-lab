# Heike Kamerlingh Onnes — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Heike Kamerlingh Onnes: build the coldest laboratory on earth first, measure resistance as the temperature falls degree by degree, and let the sudden disappearance of resistance at 4.2 K speak for itself`
- ZH: 昂内斯方法：先建成地上最冷的实验室，再一度一度降温测电阻，让电阻在 4.2 K 突然消失这件事自己说话。

## (2) 合成路线偏好

- 低温实验为主：液化氦气制冷，汞样品降温到 4.2 K 以下；‘合成’即低温装置与纯净样品制备：氦液化器、杜瓦瓶、电阻测量回路。

## (3) 表征手段组合

- 电阻—温度曲线是核心表征：从室温到液氦温区连续测电阻，4.2 K 处电阻骤降为零；先测电阻再谈超导，不靠推测。

## (4) 理论模型与图表风格

- 超导唯象描述：用电阻—温度曲线讲超导转变，用临界温度 Tc 标定材料；图表以电阻—温度曲线为主；理论解释留给后人（BCS），本文件夹只蒸发现方法。

## (5) 性能指标与取舍

- 优先保住低温测量的精确性与可重复性，牺牲实验速度：降温慢、测点密，换来转变点的精确定位；保住电阻为零的判据，牺牲对机理的解释。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先建成可靠的低温装置再做样品测量；一度一度降温，连续测电阻—温度曲线；以电阻骤降为零作超导判据；用不同纯度样品重复验证转变点；把低温技术从汞推广到其他金属与合金。
- 不该做：不做无低温装置的超导宣称；不跳过电阻测量直接谈超导；不把电阻小当作电阻为零；不以单次测量冒充可重复转变；不脱离温度标定谈临界温度。
- Negative prompt: `no superconductivity claims without a cryogenic setup, no superconductivity without resistance measurement, no small resistance presented as zero resistance, no single measurement presented as a reproducible transition, no critical temperature claims without temperature calibration`

## (7) 测试提示词示例（现代题材：为深海探测器设计一种低温超导传感材料）

- Prompt: `In the method of Heike Kamerlingh Onnes, design a low-temperature superconducting sensing material for a deep-sea probe. Build the cold setup first, measure resistance degree by degree as temperature falls, and let the sudden drop to zero decide whether the material superconducts.`
- 中文对照：用昂内斯的方法，为深海探测器设计一种低温超导传感材料：先建成可靠的低温装置，再一度一度降温测电阻，让电阻突然降为零来判定材料是否超导。
- Negative: `no superconductivity claims without a cryogenic setup, no superconductivity without resistance measurement, no small resistance presented as zero resistance, no single measurement presented as a reproducible transition, no critical temperature claims without temperature calibration`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
