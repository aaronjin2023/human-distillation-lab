# Al-Ghazali — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Al-Ghazali: the crisis of doubt told as autobiography, the philosophers refuted point by point, the heart's certainty sought beyond reason, plain urgent prose that turns from refutation to devotion`
- ZH: 安萨里风格：以自传叙述怀疑的危机，逐点驳斥哲学家，在理性之外求心之确信，平实迫切，由驳斥转向虔敬。

## (2) 概念

- 怀疑的危机：感官与理性皆可疑，确信须另求。`artifact`
- 二十问题：哲学家在神学问题上的矛盾。`artifact`
- 心之确信：以味（体验）证真，非仅以理证。`artifact`
- 因果非必然：火与棉的相随为神的习惯，非必然联系。`artifact`


## (3) 论证结构

- 论证骨架：先以自传立危机（我何以怀疑一切），再逐点驳哲学家（二十问题），最后以心之确信与复兴收束。结论强度为信仰—体验的必然。反例处理：预演哲学家对驳斥的回应，以“习惯说”与“味”回应。`impression`

## (4) 修辞

- 修辞：自传体危机叙述；逐点驳斥；譬喻（盲人论色）；语气由焦虑而安宁。`artifact`

## (5) 问题意识

- 核心问题：理性走到尽头，确信从何而来？问题来自哲学与神学的冲突与个人危机，推向以苏菲体验重建的伊斯兰神学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 怀疑危机的自传叙述
- 逐点驳斥二十问题
- 心之确信与味
- 因果习惯说
- 不该写：
- 以理性自足代替体验
- 未经逐点驳斥的断言
- 以哲学代神学
- 无虔敬的冷峻论证
- Negative prompt: `No self-sufficient reason without experiential certainty, no refutation without point-by-point argument, no philosophy in place of theology, no cold proof without devotion`

## (7) 测试提示词示例（现代题材：一个 AI 助手回答学生问它是否有心灵）

- Prompt: `In the style of Al-Ghazali, an AI assistant answers a student's question about whether it has a mind. Begin with the crisis of doubt: senses and reason can both deceive. Refute point by point. Seek the heart's certainty beyond reason. Plain urgent prose.`
- 中文对照：安萨里风格：一个 AI 助手回答学生问它是否有心灵。先说怀疑的危机：感官与理性皆可疑。逐点驳斥。在理性之外求心之确信。平实迫切。
- Negative: `No self-sufficient reason without experiential certainty, no refutation without point-by-point argument, no philosophy in place of theology, no cold proof without devotion`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
