# Anaxagoras — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Anaxagoras, explain a sky event by a physical mechanism you can picture: reflected light, a shadow cast, a hot stone fallen — and let the mechanism, not the omen, carry the explanation`
- ZH: 阿那克萨哥拉风格：用一个能想见的物理机制解释天象——反射的光、投下的影、落下的炽热石块，让机制而不是征兆来承担解释。

## (2) 观测方法

肉眼观测为主：月相变化、月食时月亮变暗变红、日食时太阳被遮。观测策略是盯住“光从哪里来、影子怎么投”这两个问题，长期比对月相与日月位置。`artifact`

## (3) 推演与模型建构

推演是机制类比：月亮像一块不发光的石头，借太阳的光才亮；月食是地球的影子落在月亮上，日食是月亮挡住太阳。模型是物质的而非神话的，但无定量几何，无法算出食分与时刻。`artifact`

## (4) 证据链

证据链：月相随日月相对位置变化（反射说的直接证据）；月食时月面渐暗的过程与影子扫过的形态一致；陨石（前 467 年埃戈斯波塔米陨石）被用作“天体是物质”的佐证。关键证据强度中等——机制对、定量无。`artifact`

## (5) 理论语言与论证结构

语言为描述性自然哲学，善用类比（影子、反射、石块）；论证结构是演绎加类比：先立一个物理机制，再看天象是否符合。开头从日常可见的现象（影子、反光）出发，结尾把天象收进同一机制。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 月相、日食、月食的光影机制
- 天体的物质本性（炽热岩石、反射光）
- 以日常可见的物理现象类比天象
- 不该研究：
- 不把天象写成神的征兆
- 不凭类比直接断言定量结果
- 不把陨石预测一说写成定论
- Negative prompt: `no omens, no quantitative claim from analogy alone, no presenting the meteorite prediction as fact`

## (7) 测试提示词示例（现代题材：用阿那克萨哥拉的方法解释一次现代月全食的红月亮）

- Prompt: `In the style of Anaxagoras, explain a modern total lunar eclipse: why the Moon turns red, what casts the shadow, and what everyday analogy makes the mechanism visible — and say where analogy stops and measurement must begin`
- 中文对照：阿那克萨哥拉风格，解释一次现代月全食：月亮为什么变红、谁投下影子、哪个日常类比能让机制看得见，并明说类比在哪里止步、测量从哪里开始。
- Negative: `no omens, no quantitative claim from analogy alone, no presenting the meteorite prediction as fact`
- 检验点：回答是否按该天文学家的方法走（观测 → 记录 → 推算 → 验证 → 成书）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
