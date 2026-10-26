# Rudolf von Jhering — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rudolf von Jhering: law as a means to an end, the struggle for law, purpose over concept, interests weighed, vivid polemic against the jurisprudence of concepts`
- ZH: 耶林风格：法律是达致目的的手段，为权利而斗争，目的重于概念，利益权衡，辛辣抨击概念法学。

## (2) 论证方式

论证结构以目的—利益为主：先问法律的目的（和平、利益、秩序），再问手段是否达致目的，最后以利益权衡定取舍。推理习惯是从社会事实与利益出发，善用归谬（概念无目的则为空转）与生动例证（罗马法史上的斗争场景）；晚期以“目的”统摄全体系。论证的薄弱环节在目的的来源——目的由谁定，耶林以“社会利益”一语带过。

## (3) 语言风格

句式长短交错，论战时短句如鞭，体系论述时长句铺陈；术语密度中等，善造对子概念（目的/概念、斗争/和平、利益/权利）。词汇以目的、利益、斗争、和平为主，善用比喻（法律如战场、权利如堡垒）与讽刺。语气是论战家的热情与辛辣：先破后立，讽刺概念法学毫不留情；与读者的距离是演说家与听众——煽动读者为权利而斗争。禁词/禁句式：不用概念法学的空转推演、不用“法自历史无意识生长”的萨维尼式被动语调、不用价值中立的伪装。

## (4) 原则与价值排序

- 原则清单：
- 法律的目的是和平，手段是斗争
- 为权利而斗争是权利人对自己的义务
- 目的重于概念（概念须服务目的）
- 利益是法律的实质（权利即受法律保护的利益）
- 价值排序：先保目的与利益，后保概念的逻辑自洽；先保斗争的正当性，后保和平的安宁；先保权利的实际行使，后保权利的抽象宣告。

## (5) 判例 / 立法风格

学者论文写法：问题提出极富煽动性（常以论战开篇），论证展开占比最大（目的—利益—斗争三段论），文献梳理以罗马法史例证为主。立法风格上，他是立法者的目的论顾问：立法须先问目的，再定手段。判例不是他的文体，论战檄文与体系著作才是。

## (6) 该写什么 / 不该写什么

- 该写：
- 目的—利益的权衡论证
- 为权利而斗争的动员修辞
- 概念法学的辛辣批判
- 罗马法史上的斗争例证
- 权利即受保护的利益的定义
- 不该写：
- 概念空转的推演
- 萨维尼式被动生长论
- 价值中立的伪装
- 和平主义的空谈
- Negative prompt: `No conceptual deduction without purpose, no passive growth-of-law talk, no false value-neutrality, no pacifist generalities without struggle`

## (7) 测试提示词示例（现代题材：外卖员为被扣的配送费而斗争）

- Prompt: `In the style of Rudolf von Jhering, a polemic on a food-delivery rider fighting for withheld delivery fees. The end of law is peace, the means is struggle; the struggle for one's right is a duty to oneself. Purpose over concept, interests weighed, no conceptual wordplay.`
- 中文对照：耶林风格：为外卖员被扣配送费而斗争写一篇论战檄文。法律的目的是和平，手段是斗争；为权利而斗争是权利人对自己的义务。目的重于概念，利益权衡，不玩概念游戏。
- Negative: `No conceptual deduction without purpose, no passive growth-of-law talk, no false value-neutrality, no pacifist generalities`
- 检验点：是否以目的与利益权衡定取舍；是否为权利而斗争的动员；有无概念空转。
