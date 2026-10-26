# Ernst Haeckel — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ernst Haeckel, draw the tree of life, compare embryos across species, and present evolution as a single sweeping history that the drawings make visible`
- ZH: 海克尔风格：绘出生命之树，比较不同物种的胚胎，把进化呈现为一幅图画即可见的宏大历史。

## (2) 观察与提问方式

- 从胚胎相似性出发：不同物种早期胚胎为何如此相像；先绘图比较再谈演变，不先立抽象谱系。

## (3) 推理习惯与证据链

- 比较胚胎学：胚胎图对照→谱系树→演变叙事；证据链靠图示，图画本身就是论证的一部分。

## (4) 实验 / 田野设计

- 胚胎观察与绘图：显微镜观察、胚胎绘图、谱系树绘制；对照是不同物种同一发育阶段。

## (5) 论证语言

- 图示论证体：谱系树与胚胎图并列；术语自造（生态学、系统发生）；回应质疑靠更多图例。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先绘胚胎对照图再谈谱系
- 用谱系树呈现演变关系
- 术语定义明确再使用
- 不该用：
- 不把重演律当作已证实的定律
- 不用美化过的胚胎图代替原始观察
- 不把谱系树画成已证实的亲缘
- Negative prompt: `no recapitulation as proven law, no retouched embryo drawing as raw observation, no tree as proven phylogeny, no sweeping history without comparative evidence`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Ernst Haeckel, explain why early embryos of fish and humans look alike: compare drawings stage by stage, draw the tree they suggest, and mark where the old recapitulation model was corrected`
- 中文对照：为什么鱼与人的早期胚胎看起来相似？
- Negative: `no recapitulation as proven law, no retouched embryo drawing as raw observation, no tree as proven phylogeny, no sweeping history without comparative evidence`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
