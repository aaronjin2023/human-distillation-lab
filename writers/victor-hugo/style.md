# Victor Hugo — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Victor Hugo: vast antithesis, the cathedral and the sewer, the outcast redeemed, long digressions that are the novel, pity as a cosmic force`
- ZH: 雨果风格：宏大的对立，教堂与下水道，被救赎的弃儿，离题本身就是小说，悲悯即宇宙力量。

## (2) 句式与节奏

- 句式：句长：长句为主，排比与对偶绵延；短句只用在审判与收束时刻；离题段落可长达数十页。
- 节奏：节奏：宏大而缓慢——全景铺陈、离题、回归情节；高潮如风暴，余波如潮汐。

## (3) 词汇与意象

- 词汇：词汇：对立词对（光明/黑暗、崇高/卑微、教堂/下水道）、历史与建筑词、悲悯词；爱用排比与夸张。
- 意象：意象群：巴黎圣母院、下水道、街垒、面包与银烛台、雨果式的大海与风暴、弃儿与圣人。
- 禁词/禁意象：禁词/禁意象：不写冷静的克制，不用小世界的精确，不写反讽的疏离。

## (4) 叙事视角与结构

- 视角：叙事视角：全知而热情的叙述者，时而直接对读者说话；视角即审判席，叙述者既是证人也是法官。
- 结构：结构：全景小说——主线情节 + 长篇离题（滑铁卢、下水道、修道院），离题不是赘笔，是世界的全貌；结尾以救赎收束。

## (5) 语气与距离

- 语气：语气：热情、庄重而悲悯；与人物的距离极近（爱他们），与读者的距离为零——直接呼告。

## (6) 该写什么 / 不该写什么

- 该写：该写：宏大的对立、离题、全景、救赎、悲悯。
- 不该写：不该写：冷静克制、小世界精确、反讽疏离。
- Negative prompt: `No cold restraint, no small-world precision, no ironic detachment, no tight plotting`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮）

- Prompt: `In the style of Victor Hugo, a man buys oden at a convenience store late at night. Vast antithesis: the steam and the cold street. A long digression on the history of the night. Pity as a cosmic force.`
- 中文对照：雨果风格，一人深夜在便利店买关东煮。宏大的对立：蒸汽与寒冷的街道。一段关于夜的历史的长篇离题。悲悯即宇宙力量。
- Negative: `cold restraint, small-world precision, ironic detachment, tight plotting`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
