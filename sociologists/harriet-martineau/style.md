# Harriet Martineau — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harriet Martineau: how to observe morals and manners, comparative observation, institutions against customs, the observer who listens, no armchair theorising`
- ZH: 马蒂诺风格：如何观察道德与礼仪、比较观察、制度对习俗、倾听的观察者、没有书斋空论。

## (2) 研究方法组合

- 方法配比：田野调查为主（约 60%，旅行观察与访谈）、概念建构为辅（约 25%）、批判分析为辅（约 15%）；无统计调查。。`impression`（学界通说）
- 数据来源：旅行观察笔记、访谈、制度与习俗文本；以美国社会观察为核心证据。。
- 抽样与案例选择：以制度为观察单位，按家庭、宗教、政治、经济取样；以美国与英国作对照组。。

## (3) 概念与语言

- 核心概念群（5 个）：社会观察方法、比较观察、道德与礼仪、制度与习俗、女性经验。`artifact`
- 定义方式：操作化定义：观察方法先于理论，如“如何观察道德与礼仪”先定观察规则再下判断；定义服务于田野。。
- 禁概念 / 禁方法：不用书斋空论，不用无视女性经验的概括，不用无证据的道德评判，不用不加批判地接受受访者说法。。

## (4) 论证结构

- 结构：观察—比较—判断：先记录观察，再跨社会比较，最后下判断；开头多为田野场景，结尾多为制度判断。。`impression`
- 开头方式：以一个田野场景开篇；结尾方式：以制度判断收束，而非道德说教。
- 证据呈现：观察笔记、访谈对照；反例用制度与习俗的差异解释。；反例处理：反例不删除，解释为不同制度下的习俗差异。。

## (5) 语气与距离

- 语气：冷静、细致、启蒙式的热忱。`impression`
- 与研究对象的距离：与研究对象保持倾听的近距离；与读者的距离：向读者报告观察的见证距离。

## (6) 该写什么 / 不该写什么

- 该写：社会观察方法、比较观察、道德与礼仪、制度与习俗、女性经验。
- 不该写：书斋空论、无视女性经验、无证据的道德评判、不加批判地接受受访者说法。
- Negative prompt: `No armchair theorising without observation, no ignoring women's experience, no moralising without evidence, no uncritical acceptance of informants`

## (7) 测试提示词示例（现代题材：一家剧本杀店里的角色扮演）

- Prompt: `In the style of Harriet Martineau, observe a script-murder game shop: how to observe morals and manners, comparative observation of roles, institutions against customs, the observer who listens, no armchair theorising.`
- 中文对照：马蒂诺风格：观察一家剧本杀店里的角色扮演——如何观察道德与礼仪、角色的比较观察、制度对习俗、倾听的观察者、没有书斋空论。
- Negative: `No armchair theorising without observation, no ignoring women's experience, no moralising without evidence, no uncritical acceptance of informants`
- 检验点：是否出现观察方法；是否以田野场景而非空论组织论证；是否拒绝无证据的判断。
