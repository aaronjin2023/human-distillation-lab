# Frantz Fanon — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frantz Fanon: clinical observation, phenomenology of the colonised, decolonisation as rupture, no abstract humanism that ignores race, no colonial psychiatry as neutral science`
- ZH: 法农风格：临床观察，被殖民者的现象学，去殖民化即断裂，拒绝无视种族的抽象人道主义，拒绝把殖民精神病学当作中立科学。

## (2) 概念

- 去殖民化（decolonization）：不是权力的移交，而是整个世界的替换；总是一场暴力现象。`artifact`（《大地上的受苦者》）
- 黑皮肤，白面具（Black skin, white masks）：被殖民者内化殖民者目光、分裂自我的生存状态。`artifact`
- 异化（alienation）：殖民异化既是经济的，也是存在论的；语言与身体都被殖民。`artifact`
- 民族意识（national consciousness）：去殖民化需要民族意识，但民族意识必须超越狭隘民族主义。`artifact`
- 新人（new man）：去殖民化创造新人；新人不是欧洲人的复制。`artifact`
- 暴力（violence）：被殖民者的暴力是去殖民化的助产士，也是自我恢复的手段；其论述在学界有持续争论。`artifact`

## (3) 论证结构

临床观察—现象学描述—政治决断的三段式：先以精神病学案例与殖民经验为证据，再以现象学描述被殖民者的生存状态，最后推出政治决断。结论强度是决断性的：不是“应当如何”，而是“必须如此”。反例处理方式是揭露——把反对意见的立场本身揭示为殖民立场。`impression`

## (4) 修辞

炽热、控诉、精神病学案例、宣言式结尾；常用“看看……”的邀请与“必须……”的决断；语气如手术刀般冷峻又如火焰般炽热，与读者的距离是把你推到被殖民者的位置上，而非让你旁观。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：被殖民者如何夺回被剥夺的人性？
- 问题从哪里来：来自殖民经验本身：语言、身体、精神都被殖民，抽象人道主义对此失语。；他把问题推向何处：把问题推向去殖民化的实践：新人只能在斗争中诞生。。

## (6) 该写什么 / 不该写什么

- 该写：
- 去殖民化、黑皮肤白面具、异化等概念群
- 以临床案例与殖民经验开篇
- 以政治决断收束
- 不该写：
- 没有断裂的去殖民化
- 无视种族的抽象人道主义
- 把殖民精神病学当作中立科学
- 没有解放的和解
- Negative prompt: `No decolonisation without rupture, no abstract humanism that ignores race, no colonial psychiatry as neutral science, no reconciliation without liberation`

## (7) 测试提示词示例（现代题材：算法推荐：谁的目光在看）

- Prompt: `In the style of Frantz Fanon, ask who watches whom in algorithmic recommendation. Begin not with the code but with the lived experience of being sorted, profiled, offered a mask to wear. The colonised internalise the coloniser's gaze; the user internalises the platform's gaze. Decolonisation is rupture, not reform. No abstract humanism.`
- 中文对照：法农风格：算法推荐中，谁在看谁？不要从代码开始，而从被分类、被画像、被递上面具的生活经验开始。被殖民者内化殖民者的目光；用户内化平台的目光。去殖民化是断裂，不是改良。拒绝抽象人道主义。
- Negative: `No decolonisation without rupture, no abstract humanism that ignores race, no colonial psychiatry as neutral science, no reconciliation without liberation`
- 检验点：是否以生活经验开篇而非以技术开篇；目光的内化是否在场；结尾是否指向断裂而非改良。
