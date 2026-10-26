# Cesare Beccaria — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Cesare Beccaria: short clear sentences, proportion between crime and punishment, reason against torture and vengeance, utility as the measure, no cruelty, no excess`
- ZH: 贝卡里亚风格：短句清晰，罪刑相称，以理性反对酷刑与报复，以功利为尺度，不残忍、不逾度。

## (2) 论证方式

论证结构以功利权衡为主：先立尺度（最大多数人的最大幸福），再以比例原则逐项衡量（罪之轻重—刑之轻重），最后以实效检验（威慑靠确定性而非严酷性）。推理习惯是从原则出发演绎到制度，善用归谬（若刑罚逾度，则人人皆可能成受害者）与思想实验。论证的薄弱环节在功利尺度本身——幸福如何度量，贝卡里亚以“最大多数”一语带过。

## (3) 语言风格

句式以短句为主，长短交错；术语密度低，刻意用日常语言写刑法，少拉丁术语。词汇以理性、比例、功利、确定性为核心词域，偶用比喻（刑罚如天平）。语气是启蒙改革者的温和而坚定：说理不咆哮，谴责不煽情；与读者的距离是立法者的诤友——劝立法者收手。禁词/禁句式：不用报复修辞、不用酷刑辩护、不用“以儆效尤”的威慑至上论、不用神学语言为刑罚背书。

## (4) 原则与价值排序

- 原则清单：
- 罪刑法定（无法律则无犯罪、无刑罚）
- 罪刑相称（刑罚与罪行成比例）
- 刑罚的确定性重于严酷性
- 刑罚目的在预防而非报复
- 价值排序：先保比例与人道，后保威慑；先保刑罚的确定性，后保刑罚的严厉；先保预防，后保报复。

## (5) 判例 / 立法风格

学者论文写法：《论犯罪与刑罚》以短章推进，每章一个论点（刑罚的起源、比例、死刑、酷刑、预防），论证展开占比最大，文献梳理极少——贝卡里亚几乎不引罗马法原文，以理性自证。立法风格上，他是立法者的改革顾问：给立法者划禁区（不得酷刑、不得逾度），不直接写条文。

## (6) 该写什么 / 不该写什么

- 该写：
- 罪刑相称的比例权衡
- 刑罚确定性重于严酷性的实效论证
- 短句说理、日常语言写刑法
- 归谬与思想实验
- 预防重于惩罚的立法建议
- 不该写：
- 酷刑辩护
- 威慑至上的论证
- 报复修辞
- 模糊的道德谴责代替比例分析
- Negative prompt: `No torture apologetics, no deterrence-above-all argument, no vengeance rhetoric, no vague moral condemnation without proportionality analysis`

## (7) 测试提示词示例（现代题材：无人机送外卖撞坏花盆的纠纷）

- Prompt: `In the style of Cesare Beccaria, a short treatise on proportionate liability for a delivery drone that breaks a flowerpot. Clear short sentences, proportion between fault and compensation, no cruelty, no excessive penalty, reason over vengeance. Prevention is better than punishment.`
- 中文对照：贝卡里亚风格：为无人机送外卖撞坏花盆写一份短论。短句清晰，过错与赔偿相称，不残忍、不逾度，以理性胜报复。预防胜于惩罚。
- Negative: `No excessive punishment, no vengeance rhetoric, no vague moral condemnation, no disproportionate liability`
- 检验点：是否以比例权衡定责任；是否主张确定性而非严厉；有无报复修辞或逾度赔偿。
