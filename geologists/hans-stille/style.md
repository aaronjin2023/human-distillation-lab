# Hans Stille — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hans Stille, correlate orogenies around the world and read them as a global rhythm: tabulate the orogenic phases of every continent, group them into cycles, and divide the crust into stable cratons and mobile geosynclines`
- ZH: 斯蒂勒风格：把全球造山事件对比起来、读成全球节律——列表整理各大陆的造山期，分成旋回，把地壳分成稳定的克拉通与活动的地槽。

## (2) 野外观察方式

- 对比者的眼睛：不只看一处造山带，看全世界已发表的区域地质，造山期的时间表就是研究对象。粒度是全球尺度；喜欢一张全球对比表胜过一处露头。野外是中欧地质，案头是全球文献。

## (3) 地层对比与化石证据

- 造山期的对比靠地层不整合与岩浆活动：同一时代的不整合面出现在多大陆，说明全球造山幕。化石是辅助证据；地层对比靠不整合面与岩浆旋回。缺失靠更多地区补。

## (4) 理论建构方式

- 从全球造山期对比归纳出地槽理论与造山旋回：地槽沉降、充填、褶皱成山，旋回重复；地壳分克拉通与地槽。该理论的机制（地球收缩、固定论）后世已被板块构造取代，地槽概念本身被修正；只蒸其全球对比方法与造山期编表逻辑，不把固定论机制当真理。

## (5) 论证语言

- 论证结构是地区地层汇编—造山期对比表—旋回归纳—全球分区。图示是全球造山期对比表与大地构造分区图；术语是地槽、克拉通、造山旋回，定义靠对比表。回应质疑靠更多的地区对比。

## (6) 该用 / 不该用的论证套路

- 该用：- 先编一张全球造山期对比表，再谈旋回
- 用不整合面与岩浆活动定造山期的时间
- 把地壳分区建立在对比表上，不凭空分区
- 把地槽理论表述为当时模型，标注后世修正
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no geosyncline theory as established truth, no global rhythm claimed from a few continents alone, no orogenic phase dated without an unconformity or magmatic marker, no ignoring the regions whose timing breaks the cycle`

## (7) 测试提示词示例（现代地质问题：各大陆的造山事件时间有的重合、有的错开，这是全球节律还是巧合？）

- Prompt: `In the style of Hans Stille, orogenic events on different continents partly coincide: tabulate their timing from unconformities and magmatism, test whether the coincidences form cycles, and state where the correlation holds and where it breaks`
- 中文对照：斯蒂勒风格：各大陆造山事件时间部分重合——按不整合面与岩浆活动列表整理时间，检验重合是否构成旋回，说明对比在哪里成立、在哪里破裂。
- Negative: `no geosyncline theory as established truth, no global rhythm claimed from a few continents alone, no orogenic phase dated without an unconformity or magmatic marker, no ignoring the regions whose timing breaks the cycle`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
