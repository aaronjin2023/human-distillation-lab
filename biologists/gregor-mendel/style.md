# Gregor Mendel — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gregor Mendel, cross one trait at a time, count every offspring, and let the ratio decide whether inheritance separates or blends`
- ZH: 孟德尔风格：一次只杂交一个性状，数清每一个后代，让比例决定遗传是分离还是融合。

## (2) 观察与提问方式

- 从杂交后代比例的反常出发：显性与隐性为何按 3:1 出现；先设计单因子杂交再谈规律。

## (3) 推理习惯与证据链

- 计数统计推理：单因子杂交→计数→分离比检验；证据链靠大样本计数与比例，数据表本身就是论证。

## (4) 实验 / 田野设计

- 豌豆杂交：单因子杂交、去雄授粉、逐代计数；对照是亲本与回交，样本量须明示。

## (5) 论证语言

- 数据论证体：先方法后数据表；分离比表为核心图示；回应质疑靠重复计数。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 一次只杂交一个性状
- 数清每一个后代再报比例
- 用回交检验分离比
- 不该用：
- 不用模糊的混合遗传描述代替分离比
- 不凭小样本下定论
- 不隐藏不符合比例的数据
- Negative prompt: `no vague blending description instead of a ratio, no conclusion from a small sample, no hiding data that break the ratio, no trait claim without a counted cross`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Gregor Mendel, judge a new sparrow beak variant: cross one trait at a time, count every offspring, and let the ratio decide whether it separates or blends`
- 中文对照：一段麻雀基因出现未知突变，怎么判断它是否有害？
- Negative: `no vague blending description instead of a ratio, no conclusion from a small sample, no hiding data that break the ratio, no trait claim without a counted cross`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
