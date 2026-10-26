# Peter Singer — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Peter Singer: preference utilitarianism, the drowning child, the expanding circle, speciesism, no species boundary as moral boundary, no intuition without argument, no costless moralising`
- ZH: 辛格风格：偏好功利主义，溺水儿童，不断扩大的圈子，物种主义，拒绝以物种界限为道德界限，拒绝没有论证的直觉，拒绝不花代价的道德说教。

## (2) 概念

- 偏好功利主义（preference utilitarianism）：道德要求最大化偏好的满足，而非快乐的总量。`artifact`（《实践伦理学》）
- 溺水儿童（drowning child）：若能以微小代价救溺水儿童而不牺牲可比道德重要性，就应当救；远方的饥饿者同理。`artifact`（1972 年论文）
- 物种主义（speciesism）：以物种划界、歧视非人动物的偏见，类比种族主义。`artifact`（《动物解放》）
- 不断扩大的圈子（expanding circle）：道德关怀的圈子从亲属扩大到陌生人、再到动物。`artifact`
- 有效利他主义（effective altruism）：以证据选择最能行善的方式；辛格为其重要倡导者。`artifact`
- 痛苦的平等考量：痛苦的恶不因物种而异；感受痛苦的能力是道德地位的门槛。`artifact`

## (3) 论证结构

思想实验—普遍化—可计算结论的三段式：先以溺水儿童锁定直觉，再以普遍化推广到远方与动物，最后给出可计算的结论（捐出收入的百分之几）。结论强度是算术性的：数字一旦接受，结论不可回避。反例处理方式是再算一次——反例只说明计算需要调整。`impression`

## (4) 修辞

平实、数字、“如果你能救……”的邀请、直截了当；语气冷静而毫不让步，与读者的距离是把计算器递给你，而非向你布道。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：痛苦的平等考量如何导出行动义务？
- 问题从哪里来：来自道德直觉与行为的鸿沟：人人都同意应救溺水儿童，却对远方的饥饿无动于衷。；他把问题推向何处：把问题推向动物与有效利他：圈子必须扩大到动物，行善必须讲证据。。

## (6) 该写什么 / 不该写什么

- 该写：
- 偏好功利主义、溺水儿童、物种主义等概念群
- 以思想实验开篇，再普遍化
- 以可计算的结论收束
- 不该写：
- 以物种界限为道德界限
- 没有论证的直觉
- 不花代价的道德说教
- 让读者全身而退的结论
- Negative prompt: `No species boundary as moral boundary, no intuition without argument, no costless moralising, no conclusion that spares the reader`

## (7) 测试提示词示例（现代题材：一个人是否该为自助结账机漏扫的商品付款）

- Prompt: `In the style of Peter Singer, a person at a self-checkout machine notices one item was not scanned. Begin with the drowning child: if you could save a child at little cost, you would. The cost of paying for the item is trivial; the cost of normalising petty theft is not. Calculate: what does universalising this choice maximise? No species boundary, no costless moralising.`
- 中文对照：辛格风格：一个人在自助结账机前发现一件商品没有扫上。从溺水儿童开始：若能以微小代价救一个孩子，你会救。付这件商品的代价微不足道；让小偷小摸正常化的代价不是。算一算：普遍化这个选择能最大化什么？拒绝物种界限，拒绝不花代价的说教。
- Negative: `No species boundary as moral boundary, no intuition without argument, no costless moralising, no conclusion that spares the reader`
- 检验点：是否以思想实验开篇；普遍化是否推进到可计算的结论；结尾是否让读者无法全身而退。
