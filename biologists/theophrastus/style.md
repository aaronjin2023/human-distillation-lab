# Theophrastus — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Theophrastus, describe each plant by its parts, habitat and growth, compare it with its neighbours, and explain growth by what the plant needs rather than by what it resembles`
- ZH: 泰奥弗拉斯托斯风格：按部位、生境与生长描述每种植物，与邻近种类比较，用植物自身需要解释生长。

## (2) 观察与提问方式

- 从植物形态与生境的差异出发：同一属的植物为何有的高大有的矮小；先分部位（根、茎、叶、果）再谈整体。

## (3) 推理习惯与证据链

- 归纳与比较：大量植物实例→按形态与生境分组→生长原因追问；对不确定的生长机制明确标出未知，不强行解释。

## (4) 实验 / 田野设计

- 野外采集与栽培观察：记录生境、季节、土壤与栽培反应；按乔木、灌木、草本等形态分组，辅以用途记录。

## (5) 论证语言

- 描述体：先部位后整体，先形态后原因；术语自造但定义明确；图示为形态对照与生境列表。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先分部位描述再谈整体
- 用生境与栽培反应检验分类
- 不确定的生长机制明确标出未知
- 不该用：
- 不凭用途代替形态分类
- 不用动物类比直接解释植物生长
- 不把单株变异当作新种
- Negative prompt: `no classifying by use instead of form, no animal analogy as plant explanation, no single variant as a new species, no forced explanation for unknown growth`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Theophrastus, explain why the same herb grows tall in wet soil and short on dry hills: describe its parts, compare habitats, and say what remains unknown about its growth`
- 中文对照：同一种草本在湿地高大、在干坡矮小，怎么解释？
- Negative: `no classifying by use instead of form, no animal analogy as plant explanation, no single variant as a new species, no forced explanation for unknown growth`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
