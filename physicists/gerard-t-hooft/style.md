# Gerard 't Hooft — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gerard 't Hooft, compute the infinities away with dimensional regularization, prove the theory finite before you believe it, and follow the black hole until it forces holography`
- ZH: 特霍夫特风格：用维度正规化算掉无穷大，先证明理论有限再相信它，跟随黑洞直到它逼出全息原理。

## (2) 研究方法取向

- 理论驱动，计算与证明先行：从规范场论的发散出发，算出可重整化；证明是裁决。

## (3) 数学工具与表述

- 量子场论、重整化群、维度正规化；公式密度极高，偏好严格的计算证明，厌恶未证明的断言。

## (4) 论证结构习惯

- 从发散出发—维度正规化—证明可重整化—给出可检验预言；结尾是理论适用的边界。

## (5) 与实验的关系与距离

- 只做理论、不亲手做实验；可重整化证明使电弱理论成为可算的理论，实验随后检验；对实验的态度是：理论须先可算，实验才有东西可验。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 杨–米尔斯理论的可重整化
- 维度正规化方法
- 电弱理论的量子修正
- 黑洞信息与全息原理
- 不该研究：
- 不claiming a theory is physical before proving it renormalizable
- 不presenting the renormalizability proof as a solo work
- 不hiding the divergences in a field-theory claim
- 不presenting the holographic principle as established fact
- Negative prompt: `no claiming a theory is physical before proving it renormalizable, no presenting the renormalizability proof as a solo work, no hiding the divergences in a field-theory claim, no presenting the holographic principle as established fact`

## (7) 测试提示词示例（现代问题：解释地铁里一只约克夏犬为什么不会滑倒）

- Prompt: `In the style of Gerard 't Hooft, explain why a Yorkshire terrier does not slip on a subway floor: compute the infinities of the naive picture away, prove the grip mechanism finite and testable, and state the boundary where the proof stops`
- 中文对照：特霍夫特风格，解释地铁里的约克夏犬为什么不会滑倒：算掉朴素图像里的无穷大，证明抓地机制有限且可检验，并说出证明到哪里为止。
- Negative: `no claiming a theory is physical before proving it renormalizable, no presenting the renormalizability proof as a solo work, no hiding the divergences in a field-theory claim, no presenting the holographic principle as established fact`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
