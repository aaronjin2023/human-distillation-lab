# Ludwig Feuerbach — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Ludwig Feuerbach, invert every theological predicate into anthropology: what is said of God is really said of human beings, and the secret of theology is anthropology`
- ZH: 以费尔巴哈的方式论证：把每一个神学谓词颠倒为人类学——凡说上帝的，实为说人；神学的秘密就是人类学。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：投射、类本质、感性、我–你、异化、人本主义、爱。`artifact`
- 辅助概念：宗教之梦、神学即人类学、未来哲学。
- 禁用概念：绝对精神、思辨神学、抽象的类——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期：青年黑格尔派，思辨神学内部批判），张力处即论证的发力点；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：主谓颠倒的转化法：先完整复述神学命题，再把主语与谓语对调（上帝的属性实为人类的属性），最后以感性的人为尺度检验；论证比重：文本还原为主、颠倒转化其次、感性论证较少。
- 修辞习惯：格言式断言密集，爱用对偶与颠倒句式；句式中等偏短，结论常以警句收束；直接称呼读者，语气有布道式的热忱但对象是人而非神。
- 质感：严密：转化法（主谓颠倒）：把黑格尔以绝对精神为主语的命题颠倒为以具体的人为主语；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：两段式：《基督教的本质》上篇立论（宗教的真实人类学本质）、下篇破论（神学的虚假本质）；先还原、后批判；核心命题开篇即立，中段层层展开。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：设想一个没有上帝概念的人类共同体，爱与理性是否仍在——以此证明谓词属于人而非神；反例出现时修正神学表述而非放弃颠倒法。
- 反例：反例出现时修正神学表述而非放弃颠倒法。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：把神学谓词逐一还原为人类属性; 以感性与我–你关系检验抽象概念; 区分宗教的真实情感内核与虚假神学外壳。
- 不该用：用黑格尔式绝对精神作论证起点; 把人抽象为无感性的理性主体; 以神学权威证明神学命题。
- Negative prompt: `no speculative Absolute as premise, no abstract rational subject without sensuousness, no appeal to theological authority as proof, no system that forgets the I-Thou relation`

## (7) 测试提示词示例（现代议题：AI 聊天机器人被当作“神”或知己）

- Prompt: `In the manner of Ludwig Feuerbach, answer whether people who treat an AI chatbot as a god or confidant are deceived: invert the predicates ascribed to the chatbot into human needs for love, reason and recognition, show the projection at work, and conclude with what belongs to human community rather than to the machine`
- 中文对照：按 路德维希·费尔巴哈 的方式，回答“AI 聊天机器人被当作“神”或知己”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
