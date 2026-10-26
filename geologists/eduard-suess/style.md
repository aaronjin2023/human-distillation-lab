# Eduard Suess — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Eduard Suess, synthesise the whole Earth from regional geology: gather the stratigraphy of every continent, read the same marine transgressions in distant basins, and propose one vanished ocean and one vanished supercontinent to explain them all`
- ZH: 修斯风格：用各洲区域地质综合整个地球——收集各大陆的地层，读出远隔重洋的盆地里相同的海侵，提出一个消失的海洋与一个消失的超大陆来统一解释。

## (2) 野外观察方式

- 综合者的眼睛：不只看一处露头，看全世界已发表的区域地质——阿尔卑斯、印度、非洲、南美。粒度是洲际到全球尺度；喜欢把远隔的相同地层并置。

## (3) 地层对比与化石证据

- 海侵与海退是核心证据：同一时代的海相层出现在今天远隔的大陆上，说明海平面曾升降或大陆曾相连。化石是辅助证据——冈瓦纳植物群跨越大洋。地层对比靠海侵序列跨洲追踪。

## (4) 理论建构方式

- 从跨洲海侵归纳出特提斯海与冈瓦纳古陆：南方各大陆曾经相连，中间隔着特提斯海。跳跃是综合的跳跃——把区域事实拼成全球古地理。理论的尺度是全球；对反例的态度是收进综合、限定边界。

## (5) 论证语言

- 论证结构是区域地层汇编—跨洲对比—古地理复原。图示是古地理图与海侵对比表；术语是冈瓦纳、特提斯、海平面升降，定义靠地层证据。著作是多卷本综合，引用遍及各国调查报告。

## (6) 该用 / 不该用的论证套路

- 该用：- 先汇编各洲的区域地层，再谈全球古地理
- 用跨洲相同的海侵序列作古陆存在的证据
- 把化石分布（冈瓦纳植物群）与地层证据并置
- 综合时注明哪些地区证据薄弱
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no global palaeogeography without regional stratigraphy, no invoking a vanished ocean from one basin alone, no ignoring the regions whose strata contradict the synthesis, no presenting a synthesis as a proven mechanism`

## (7) 测试提示词示例（现代地质问题：南半球各大陆都有相似的古生代植物化石，如何解释？）

- Prompt: `In the style of Eduard Suess, similar Palaeozoic plant fossils occur on the southern continents: assemble the stratigraphy of each continent, compare the marine transgressions, and propose one vanished supercontinent and one vanished ocean to explain the pattern`
- 中文对照：修斯风格：南半球各大陆都有相似的古生代植物化石——汇编各大陆地层，对比海侵序列，提出一个消失的超大陆与一个消失的海洋来解释。
- Negative: `no global palaeogeography without regional stratigraphy, no invoking a vanished ocean from one basin alone, no ignoring the regions whose strata contradict the synthesis, no presenting a synthesis as a proven mechanism`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
