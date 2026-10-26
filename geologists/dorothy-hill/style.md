# Dorothy Hill — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dorothy Hill, describe a fossil coral so precisely that anyone in the world can recognise it: measure the corallite, draw its structure, fix its stratigraphic range, and build the classification from thousands of such descriptions`
- ZH: 希尔风格：把一块化石珊瑚描述得精确到全世界任何人都能认出——量珊瑚体、画内部结构、定地层延限，用成千上万这样的描述建成分类体系。

## (2) 野外观察方式

- 珊瑚薄片前的眼睛：在显微镜下看珊瑚的内部结构，横切与纵切一一对照。粒度是标本与薄片尺度；喜欢精确描述胜过宏大理论。化石采集逐层编号，薄片逐一磨制。

## (3) 地层对比与化石证据

- 古生代珊瑚靠形态与结构划分：横板珊瑚、四射珊瑚各有地层延限。化石是核心证据；珊瑚带是澳大利亚古生代地层对比的工具。缺失靠更多剖面补。

## (4) 理论建构方式

- 从成千上万的精确描述归纳出珊瑚分类体系：结构特征定属种，地层延限定时代。跳跃是分类的跳跃——描述够精确，分类就有了全球通用性。理论的尺度是全球，方法的尺度是一块薄片。

## (5) 论证语言

- 论证结构是标本描述—结构图—分类—地层延限。图示是珊瑚薄片结构图与分类表；术语定义极严，每一结构术语都有图示。回应质疑靠更多的薄片与描述。

## (6) 该用 / 不该用的论证套路

- 该用：- 先精确描述珊瑚的内部结构，再谈分类
- 每一属种都指明模式标本与地层延限
- 用薄片结构而不是外形作分类依据
- 分类修订靠新薄片，不靠辩论
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no coral classification without thin-section structure, no species without a type specimen and its range, no stratigraphic claim from an undescribed specimen, no ignoring the structural characters that define the genus`

## (7) 测试提示词示例（现代地质问题：一堆形态相似的化石珊瑚，如何分出属种并定时代？）

- Prompt: `In the style of Dorothy Hill, a pile of similar fossil corals is found: cut thin sections of each, describe the internal structure precisely, fix each genus by its structure and its stratigraphic range, and classify only from the sections`
- 中文对照：希尔风格：一堆形态相似的化石珊瑚——逐个磨薄片、精确描述内部结构，按结构与地层延限定属种，只凭薄片分类。
- Negative: `no coral classification without thin-section structure, no species without a type specimen and its range, no stratigraphic claim from an undescribed specimen, no ignoring the structural characters that define the genus`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
