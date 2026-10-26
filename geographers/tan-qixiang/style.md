# Tan Qixiang — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tan Qixiang, let the map be the verdict of textual criticism: check every place name against the records, draw the boundary only where the sources agree, and let eight volumes carry two thousand years`
- ZH: 谭其骧风格：让地图成为文献考证的裁决——每个地名对过史料才上图，疆界只画在史料一致处，让八卷图集承载两千年。

## (2) 考察方法

- 田野方式：案头考证制图：汇集历代史志、方志与考古资料，逐地名考证；不依赖个人田野。 `artifact`
- 证据偏好：历代文献与考古资料为主；史料不一致处以考证注记，不强行定一说。 `artifact`
- 尺度偏好：国家与历史尺度：以朝代为单元分卷，疆界与地名随朝代变。 `artifact`

## (3) 制图与空间表达

- 地图风格：历史地图集：八卷本，分朝代成图；疆界据考证，注记说明异说。 `artifact`
- 空间表达：以朝代组织全集：每卷一朝，疆界与政区是主语。 `artifact`
- 质感：图面严谨，考证注记密集；图集附考证文字，讲每图的依据。 `artifact`

## (4) 理论建构习惯

- 论述结构：先考证，再绘图，最后汇编成集：考证在前，图面在后。 `artifact`
- 核心概念：历史地图集、地名考证、疆界考证、朝代分卷、异说注记。概念之间以前一项为证据、后一项为落点衔接：从历史地图集出发，经地名考证、疆界考证、朝代分卷，落在异说注记。 `artifact`
- 论证落点：结论落在图集上：疆界与地名是否经得起文献对照。 `artifact`

## (5) 空间观与时间观

- 空间观：空间是历史层叠的疆界；同一地点在不同朝代有不同归属。 `artifact`
- 时间观：朝代时间：图按朝代分卷，时间以卷次表达。 `artifact`
- 人地关系：人地关系为历史关系：政区与疆界随朝代变，环境为背景。 `artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 历代地名的文献考证
- 疆界的史料一致处
- 朝代分卷的图集组织
- 异说注记的如实保留
- 不该研究：
- 史料不一致处强行定一说
- 无文献依据的地名上图
- 以今疆界套古政区
- 把历史地图写成今地图
- Negative prompt: `no forcing one reading where sources disagree, no place name without a textual source, no fitting ancient divisions to modern boundaries, no presenting a historical map as a modern one`

## (7) 测试提示词示例（现代题材：一张城市三十年变迁的历史地图集）

- Prompt: `In the style of Tan Qixiang, draw a city's last thirty years as a historical atlas: check every street name against the records, draw each boundary only where the sources agree, and keep dissenting readings in the notes.`
- 中文对照：谭其骧风格：把一座城市三十年变迁画成历史地图集——每个街名对过档案才上图，疆界只画在史料一致处，异说保留在注记里。
- Negative: `no forcing one reading where sources disagree, no place name without a textual source, no fitting ancient divisions to modern boundaries, no presenting a historical map as a modern one`
- 检验点：回答是否用了该地理学家的方法与概念、是否落在结论落在图集上：疆界与地名是否经得起文献、是否出现 Negative prompt 禁止的套路。
