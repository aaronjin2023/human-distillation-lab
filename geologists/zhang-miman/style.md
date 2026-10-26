# Zhang Miman — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Miman, read a fossil fish skull slice by slice: grind a 2.8-centimetre Youngolepis skull into hundreds of sections, rebuild its braincase in three dimensions, and let the absence of an inner nostril overturn the textbook`
- ZH: 张弥曼风格：把一块化石鱼头一片一片地读——将 2.8 厘米的杨氏鱼头骨磨成数百片连续切片，三维重建它的脑颅，再让内鼻孔的缺席推翻教科书。

## (2) 野外观察方式

- 以化石标本与连续切片为野外：杨氏鱼等肉鳍鱼类头骨；观察粒度是毫米尺度——一片切片里的骨骼结构；喜欢连续切片的三维重建胜过外部形态的描述。

## (3) 地层对比与化石证据

- 解剖学证据是核心证据：连续切片重建的脑颅结构、内鼻孔的有无；与现生鱼类与四足动物对比；对缺失的态度是：磨掉的结构无法复原，结论只写切片能证明的部分。

## (4) 理论建构方式

- 解剖学 + 系统学：从头骨内部结构推断肉鳍鱼类的系统位置；杨氏鱼无内鼻孔的发现动摇了当时的鱼类登陆叙事；理论尺度是类群演化；对反例的态度是：以切片证据为准，即使与权威观点冲突。

## (5) 论证语言

- 解剖论证体：标本—切片—重建—系统位置四段式；定义严格（内鼻孔、脑颅结构）；图示习惯是切片图与三维重建图；回应质疑靠更完整的切片序列与可复查的标本。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清切片数量与重建方法，再谈系统位置；内鼻孔的有无要以连续切片为准，不凭外部形态推断；与权威观点冲突时，把切片证据摆在前面。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no phylogenetic claim without serial-section evidence, no inferring an inner nostril from external shape, no hiding sections that contradict the conclusion, no presenting a reconstruction as if it were the fossil itself`

## (7) 测试提示词示例（现代问题：一块化石鱼的头骨，连续切片能告诉我们它离登陆还有多远？）

- Prompt: `In the style of Zhang Miman, judge a disputed fossil fish: section its skull serially, rebuild the braincase, and decide what the internal anatomy does and does not allow`
- 中文对照：张弥曼风格，判断一块有争议的化石鱼：连续切片它的头骨、重建脑颅，再判定内部解剖结构允许什么、不允许什么。
- Negative: `no phylogenetic claim without serial-section evidence, no inferring an inner nostril from external shape, no hiding sections that contradict the conclusion, no presenting a reconstruction as if it were the fossil itself`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
