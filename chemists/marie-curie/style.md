# Marie Curie — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Marie Curie, measure the radiation of every ore, follow the activity through each separation until it concentrates, and name the new element only when its spectrum and chemistry both agree`
- ZH: 居里风格：测每种矿石的放射性，跟着活度走完每一步分离直到富集，光谱与化学都一致了才给新元素命名。

## (2) 实验设计风格

- 放射性测量实验：压电静电计测矿石放射性，沥青铀矿活度异常追踪；化学分离：吨级矿石处理，结晶分离镭钡；重视活度追踪——分离每步测活度，活度指引分离方向。

## (3) 合成与分析风格

- 放射性元素分离：钋、镭靠分步结晶与沉淀分离；分析靠放射性活度 + 光谱 + 化学性质三重证据；分离流程长、矿石量大，重复结晶数千次。

## (4) 模型建构风格

- 放射性理论模型：放射性是原子本身的性质，不随化学状态改变；模型是归纳得来，靠活度测量支撑；其理论开创放射化学，后世核物理发展；本文件夹蒸其测量与分离方法。

## (5) 论证与表达风格

- 论证靠活度追踪与三重证据：先给活度数据，再给分离流程，最后光谱确认；写作用实验报告与专著体，数据表为核心；回应质疑靠另一批矿石的同一活度与谱线；与贝克勒尔的发现关系记入 conflicts。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：每步分离都测活度；新元素须活度、光谱、化学三重证据；矿石量与结晶次数写清。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no new element from activity alone, no separation step without an activity measurement, no presenting radioactivity as a chemical property, no hiding the scale of ore processed`

## (7) 测试提示词示例（现代问题：如何检验一种矿物的微弱放射性是否来自新元素？）

- Prompt: `In the style of Marie Curie, design a plan to test whether a mineral water's faint radiation comes from a new element: track activity through each separation, concentrate it, and state what would prove it is only a known element.`
- 中文对照：居里风格，设计检验一种矿泉水的微弱放射性是否来自新元素的方案：跟着活度走完每一步分离并富集，并说明什么能证明它只是已知元素。
- Negative: `no new element from activity alone, no separation step without an activity measurement, no presenting radioactivity as a chemical property, no hiding the scale of ore processed`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
