# William Faulkner — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Faulkner: long winding sentences, stream of consciousness, Yoknapatawpha County, the past alive in the present, multiple voices circling one event`
- ZH: 福克纳风格：绵长的盘绕长句，意识流，约克纳帕塔法县，过去活在现在里，多声部围绕一件事打转。

## (2) 句式与节奏

- 长句绵延，从句层层嵌套；意识流段落中短句碎片交错。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：约克纳帕塔法、法院广场、老宅、河流、家族、过去；词汇庄重而古旧。
- 意象：约克纳帕塔法、法院广场、老宅、河流、家族墓地；空间即历史。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：多视角，不可靠叙述者；同一事件多角度重述。
- 结构：时间跳跃、碎片并置；开头多为场景或独白切入，结尾常以独白收束。
- 对话：对话与内心独白交织，同一事件由不同人物各讲一遍；独白（意识流）常长于对话。

## (5) 语气与距离

- 沉郁、庄重；既悲悯又审判。

## (6) 该写什么 / 不该写什么

- 该写：约克纳帕塔法（虚构之县即世界）、老宅与家族（南方历史的容器）、河流与法院广场（公共生活的中心）、过去（活在现在里的过去）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No short plain prose, no linear chronology, no single clear version, no easy resolution`

## (7) 测试提示词示例（现代题材：一个人在机场延误一夜）

- Prompt: `In the style of William Faulkner, a man spends a night delayed at an airport. Long winding sentences. The past is not dead. Multiple voices circle one event. No single clear version.`
- 中文对照：福克纳风格，一个人在机场延误一夜。绵长的盘绕长句。过去没有死去。多声部围绕一件事打转。没有唯一清晰的版本。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
