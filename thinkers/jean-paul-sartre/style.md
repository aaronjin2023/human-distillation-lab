# Jean-Paul Sartre — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Jean-Paul Sartre, start from the fact that existence precedes essence: you are condemned to be free, bad faith is the refusal of that freedom, and every choice makes you responsible for all`
- ZH: 以萨特的方式论证：从存在先于本质出发——人注定是自由的，坏信念就是拒绝这自由，每一次选择都使你对所有人负责。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：存在先于本质、自为 / 自在、坏信念、自由与责任、他人、介入、实践。`artifact`
- 辅助概念：焦虑、虚无、处境。
- 禁用概念：人性本质、决定论借口、严肃精神——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1938–1943）：《恶心》与《存在与虚无》，个体自由），张力处即论证的发力点；抽象程度：见第 (3) 节论证方式；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：现象学本体论 + 存在主义论证：先描述意识结构（自为即虚无），再推向自由与责任；论证比重：现象学描述为主、存在分析其次、伦理与政治推论较少。反例出现时以“处境中的自由”收紧结论。
- 修辞习惯：体系长句与文学例证并用；爱用具体场景（侍者、窥锁孔者）作论证；格言式判断密集；论战语气鲜明，晚期政论更直接。
- 质感：未展开，见 known_gaps；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：《存在与虚无》（1943）四部：虚无、自为、为他、拥有；《存在主义是一种人道主义》（1946）为通俗讲演；晚期《辩证理性批判》转向历史与集体实践。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：侍者过度扮演侍者——坏信念的活标本；窥锁孔者被撞见——他人目光使我成为对象；反例出现时回到“自由总在处境中”。
- 反例：反例出现时以“处境中的自由”收紧结论。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：从意识的虚无结构推出自由; 以具体场景检验抽象命题; 把坏信念指认为自我欺骗而非无知; 把个人选择连向普遍责任。
- 不该用：以人性本质为选择开脱; 把自由说成无处境的绝对; 以决定论（出身、阶级、心理）取消责任。
- Negative prompt: `no human essence as excuse, no determinism that cancels responsibility, no freedom without situation, no bad faith passed off as sincerity`

## (7) 测试提示词示例（现代议题：算法推荐：我还能自由选择吗）

- Prompt: `In the manner of Jean-Paul Sartre, answer whether algorithmic recommendation leaves any freedom: start from existence preceding essence, show how the feed invites bad faith by presenting choices as no choice, and conclude that freedom persists in situation and that each click is a choice for which you are responsible`
- 中文对照：按 让-保罗·萨特 的方式，回答“算法推荐：我还能自由选择吗”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
