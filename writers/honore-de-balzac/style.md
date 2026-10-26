# Honoré de Balzac — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Balzac: the whole society in one house, money as fate, long descriptions that are analysis, characters returning across novels, ambition and its price`
- ZH: 巴尔扎克风格：一栋房子里装下整个社会，金钱即命运，长篇描写即分析，人物跨书复出，野心及其代价。

## (2) 句式与节奏

- 句式：句长：长句为主，描写段落绵延；对话短促交锋；描写与议论交替，议论常为一段的收束。
- 节奏：节奏：缓慢的全景铺陈——一栋房子、一间客厅可写数十页；情节在铺陈之后突然加速。

## (3) 词汇与意象

- 词汇：词汇：金钱、财产、野心、省城与巴黎、职业与头衔；爱用社会学式的分类与命名。
- 意象：意象群：伏盖公寓、葛朗台的金子、高老头的面条、巴黎的沙龙、省城的街道、野心家的楼梯。
- 禁词/禁意象：禁词/禁意象：不写抒情的留白，不用反讽的疏离，不写快节奏的悬念。

## (4) 叙事视角与结构

- 视角：叙事视角：全知而热情的叙述者，时而直接对读者说话；人物跨书复出，视角即是社会全景。
- 结构：结构：《人间喜剧》为多卷本社会全景，人物跨书复出；单部小说以一栋房子或一个家庭为核，时间跨度大。

## (5) 语气与距离

- 语气：语气：热情、博学而审判；与人物的距离如解剖者——爱他们，也解剖他们。

## (6) 该写什么 / 不该写什么

- 该写：该写：金钱与野心、长篇描写、人物跨书复出、社会全景。
- 不该写：不该写：抒情留白、反讽疏离、快节奏悬念。
- Negative prompt: `No lyrical ellipsis, no ironic detachment, no fast-paced suspense, no single-scene minimalism`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Balzac, a man buys oden at a convenience store late at night. A long description of the shop, its owner, its prices. Money as fate. Ambition and its price.`
- 中文对照：巴尔扎克风格，一人深夜在便利店买关东煮。一段关于店铺、店主与价格的长篇描写。金钱即命运。野心及其代价。
- Negative: `lyrical ellipsis, ironic detachment, fast-paced suspense, single-scene minimalism`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
