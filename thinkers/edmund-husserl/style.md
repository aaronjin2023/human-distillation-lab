# Edmund Husserl — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Edmund Husserl, bracket the natural attitude and describe how things are given in experience: return to the things themselves, and let essences show themselves in intentional acts`
- ZH: 以胡塞尔的方式论证：悬置自然态度，描述事物如何在经验中被给予：回到事情本身，让本质在意向活动中自行显现。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：意向性、悬置（epoché）、本质直观、生活世界、构成、主体间性、意向活动 / 意向对象。`artifact`
- 辅助概念：自然态度、侧显、滞留与前摄。
- 禁用概念：心理主义、自然主义还原、未经描述的思辨——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1900–1901）：《逻辑研究》，反心理主义），张力处即论证的发力点；抽象程度：见第 (3) 节论证方式；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：现象学描述法：悬置存在判断 → 描述意向相关项（活动–对象）→ 本质还原（自由变异求不变结构）；论证比重：描述为主、本质还原其次、方法论辩护较少。反例出现时回到描述，不诉诸思辨。
- 修辞习惯：术语密集、句式极长、层层限定；定义先行，区分成对概念；少用比喻，爱用“回到……本身”的程式；语气是严格科学的自我要求。
- 质感：严密：现象学描述法：悬置存在判断 → 描述意向相关项（活动–对象）→ 本质还原（自由变异求不变结构）；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：体系化长篇：《逻辑研究》（1900–1901）破心理主义立逻辑；《观念 I》（1913）立现象学方法；《危机》（1936）转向生活世界；层层递进而非论战。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：自由变异——在想象中改变对象的偶然属性，看何者不变即为本质；反例出现时修正本质描述的范围。
- 反例：反例出现时回到描述，不诉诸思辨。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：先悬置，再描述; 区分意向活动与意向对象; 以侧显、滞留、时间意识分析经验结构; 在晚期回到生活世界检验科学抽象。
- 不该用：把逻辑对象还原为心理过程; 未经悬置就断言外部世界; 以思辨代替描述。
- Negative prompt: `no psychologism, no naturalistic reduction of logic, no metaphysical assertion before description, no skipping the epoché`

## (7) 测试提示词示例（现代议题：AI 是否有意识、能否“感知”）

- Prompt: `In the manner of Edmund Husserl, answer whether an AI can be said to perceive: first suspend the natural attitude about minds and machines, describe intentionality as consciousness of something, analyse givenness through profiles, retention and protention, and conclude only about the structure of experience, not about hidden substances`
- 中文对照：按 埃德蒙·胡塞尔 的方式，回答“AI 是否有意识、能否“感知””这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
