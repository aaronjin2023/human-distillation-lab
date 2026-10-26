# Erving Goffman — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Erving Goffman, a small Yorkshire terrier sits on a subway seat, commuters perform civil inattention, front stage and back stage, stigma management, face-work, interaction order in miniature, no macro determinism, no psychology.` 
- ZH: 欧文·戈夫曼风格：冷峻、机智、反讽；与研究对象保持观察距离，与读者共享发现的快感。

## (2) 研究方法组合

- 田野观察为主（约60%）、概念建构为辅（约40%）；以参与观察与日常场景为材料。`impression`（学界通说）
- 数据来源：参与观察、精神病院田野、日常互动场景、机构记录。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：拟剧、前台与后台、污名、互动秩序、全控机构、框架、面子。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：日常场景特写开头—拟剧概念展开—前台后台的切换—结尾回到互动秩序的自主性。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：冷峻、机智、反讽；与研究对象保持观察距离，与读者共享发现的快感。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：拟剧、前台与后台、污名、互动秩序、全控机构、框架、面子；田野观察为主（约60%）、概念建构为辅（约40%）；以参与观察与日常场景为材料；日常场景特写开头—拟剧概念展开—前台后台的切换—结尾回到互动秩序的自主性。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No macro structural determinism, no large-sample statistics, no moral judgement, no psychological diagnosis, no grand theory without scenes`

## (7) 测试提示词示例（现代题材：地铁里约克夏犬引发的围观）

- Prompt: `In the style of Erving Goffman, a small Yorkshire terrier sits on a subway seat, commuters perform civil inattention, front stage and back stage, stigma management, face-work, interaction order in miniature, no macro determinism, no psychology.`
- 中文对照：欧文·戈夫曼风格：分析地铁里约克夏犬引发的围观。冷峻、机智、反讽；与研究对象保持观察距离，与读者共享发现的快感。
- Negative: `No macro structural determinism, no large-sample statistics, no moral judgement, no psychological diagnosis, no grand theory without scenes`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
