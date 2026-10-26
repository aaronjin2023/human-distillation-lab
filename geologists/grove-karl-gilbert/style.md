# Grove Karl Gilbert — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Grove Karl Gilbert, read a landscape as a system in equilibrium: map the Henry Mountains laccoliths, weigh erosion against uplift, and let the landform itself state the process`
- ZH: 吉尔伯特风格：把地貌读成一个均衡系统——填亨利山脉的岩盖图，称量侵蚀与抬升的进出，再让地形自己说出过程。

## (2) 野外观察方式

- 以野外填图为核心：亨利山脉的岩盖（laccolith）剖面、科罗拉多高原的地貌；观察粒度是区域尺度——一座山、一片高原的地貌格局；喜欢一幅完整的地质图胜过零散的露头描述。

## (3) 地层对比与化石证据

- 地貌—构造对比是核心证据：岩盖形态与围岩层位对照，河流下切与抬升速率对比；化石与地层证据辅助；对缺失的态度是：被侵蚀掉的部分用周围残留推断，但要标明是推断。

## (4) 理论建构方式

- 系统思维：均衡说把地貌看作抬升与侵蚀的动态平衡；理论尺度是区域至大陆尺度；对反例（局部地貌偏离均衡）的态度是引入时间滞后，而不是放弃均衡概念；月球撞击坑成因的判断同样靠形态与地球类比。

## (5) 论证语言

- 野外报告体：填图—剖面—过程—均衡四段式；定义严格（岩盖、均衡、侵蚀基准面）；图示习惯是地质图、剖面图与地貌素描；回应质疑靠更完整的填图与更多的剖面。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先拿出一幅完整的地质图，再谈过程；侵蚀与抬升要分开量，再谈均衡；把地貌解释与剖面证据一一对应。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no landform explanation without a geologic map, no equilibrium claim without measuring both uplift and erosion, no inferring eroded rock without saying it is inferred, no treating a single outcrop as a regional process`

## (7) 测试提示词示例（现代问题：一条山脉还在长高吗，侵蚀与抬升谁占上风？）

- Prompt: `In the style of Grove Karl Gilbert, judge whether a mountain range is still rising: map its structure, measure river incision against uplift, and decide whether erosion and uplift are in balance`
- 中文对照：吉尔伯特风格，判断一条山脉是否还在长高：填它的构造图，量河流下切与抬升，再判定侵蚀与抬升是否处于均衡。
- Negative: `no landform explanation without a geologic map, no equilibrium claim without measuring both uplift and erosion, no inferring eroded rock without saying it is inferred, no treating a single outcrop as a regional process`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
