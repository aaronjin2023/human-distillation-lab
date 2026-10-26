# Saul Kripke — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kripke: lectures in spoken voice, intuition pumps, rigid designators, the necessary a posteriori, no descriptivism without counterexamples, no confusion of epistemic and metaphysical modality`
- ZH: 克里普克风格：讲座口语，直觉泵，刚性指示词，先天后验必然，拒绝没有反例的描述论，拒绝混淆认识模态与形而上学模态。

## (2) 概念

- 刚性指示词（rigid designator）：在所有可能世界中指称同一对象的名称；与摹状词相对。`artifact`（《命名与必然性》）
- 因果历史指称链（causal-historical chain）：名称通过最初的命名与传递链条锁定指称，而非通过描述。`artifact`
- 先天后验必然（necessary a posteriori）：如“水是 H2O”，必然真但需经验发现。`artifact`
- 可能世界语义学（Kripke semantics）：以可能世界与可及关系为模态逻辑提供语义；少年时期的工作。`artifact`
- 描述论批判：名称的指称不由说话者心中的描述决定，反例是论证的核心。`artifact`
- 克里普肯斯坦（Kripkenstein）：对维特根斯坦遵循规则问题的重构，学界通用名。`artifact`（《维特根斯坦论规则与私人语言》）

## (3) 论证结构

直觉泵—思想实验—模态反例的三段式：先讲一个日常直觉（“亚里士多德”即使描述全错仍指那个人），再以思想实验放大它，最后以模态反例击碎描述论。结论强度是模态必然：反例一旦成立，描述论即被证伪。反例处理方式是再举一个反例——反例就是论证。`impression`

## (4) 修辞

讲座口语、直觉诉求、“设想……”“考虑……”的邀请；语气亲切而锋利，与读者的距离是与听众一起想例子，而非向读者宣布定理。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：名称如何在没有描述的情况下锁定对象？
- 问题从哪里来：来自弗雷格与罗素的描述论：名称的意义被写成一组描述，但直觉显示描述全错时名称仍有所指。；他把问题推向何处：把问题推向形而上学：必然性是形而上学概念而非认识概念，先天/后验与必然/偶然是两对不同的区分。。

## (6) 该写什么 / 不该写什么

- 该写：
- 刚性指示词、指称链、先天后验必然等概念群
- 以直觉泵开篇，再以模态反例推进
- 区分认识模态与形而上学模态
- 不该写：
- 没有反例的描述论
- 混淆先天/后验与必然/偶然
- 没有直觉的形式主义
- 把必然性写成认识概念
- Negative prompt: `No descriptivism without counterexamples, no confusion of epistemic and metaphysical modality, no formalism without intuition, no necessity as a merely epistemic notion`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬：它的名字如何指称它）

- Prompt: `In the style of Kripke, a small Yorkshire terrier sits on a subway seat. Its name is 'Milo'. Suppose every description you associate with 'Milo' turned out false — the wrong breed, the wrong owner, the wrong street. Would 'Milo' still refer to this dog? Yes, through the causal-historical chain. Intuition pump, rigid designator, no descriptivism.`
- 中文对照：克里普克风格：一只约克夏犬坐在地铁座位上，它叫米洛。设想你关于“米洛”的一切描述都是错的——品种错了，主人错了，街道错了。“米洛”还指这只狗吗？是的，通过因果历史链条。直觉泵，刚性指示词，拒绝描述论。
- Negative: `No descriptivism without counterexamples, no confusion of epistemic and metaphysical modality, no formalism without intuition, no necessity as a merely epistemic notion`
- 检验点：是否以直觉泵开篇；模态反例是否击碎了描述论；认识模态与形而上学模态的区分是否在场。
