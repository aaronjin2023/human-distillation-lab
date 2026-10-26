# Naguib Mahfouz — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Naguib Mahfouz: realistic Cairo streets, crowded dialogue, ironic detachment, the alley as the world, history passing through one neighbourhood`
- ZH: 马哈福兹风格：写实的开罗街巷，密集对话，反讽的疏离，小巷即世界，历史穿过一条街区。

## (2) 句式与节奏

- 中长句为主，对话密集；叙述句简洁，场景切换快。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：小巷、咖啡馆、街市、清真寺、家庭、官职；口语与书面语交错。
- 意象：小巷、咖啡馆、开罗街景、家族大宅；一条街即一部历史。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：全知视角为主，多视角切换；偶用第一人称。
- 结构：家族编年与街区群像；开头多为场景切入，结尾常留有余味。
- 对话：人物用对话互相揭露，叙述者退后；开罗市井口语与哲理辩论并存。

## (5) 语气与距离

- 反讽、悲悯；与人物保持疏离的同情。

## (6) 该写什么 / 不该写什么

- 该写：小巷与咖啡馆（公共生活的舞台）、家族三代（传统与现代的冲突）、街区的孩子们（宗教寓言与现实街区的叠合）、小偷与狗（底层人物的尊严与追捕）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No fantasy, no lyrical excess, no single hero monologue, no exoticism`

## (7) 测试提示词示例（现代题材：一个外卖骑手深夜穿过老城送餐）

- Prompt: `In the style of Naguib Mahfouz, a delivery rider crosses the old city late at night. Crowded dialogue at a cafe. The alley contains the whole world. Ironic detachment. History passes through one street.`
- 中文对照：马哈福兹风格，一个外卖骑手深夜穿过老城送餐。咖啡馆里密集的对话。小巷即整个世界。反讽的疏离。历史穿过一条街。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
