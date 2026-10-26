# Carl Linnaeus — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carl Linnaeus, define each organism by a few clear diagnostic traits, give it a two-part Latin name, and place it in a nested hierarchy that anyone can reuse`
- ZH: 林奈风格：用少数清晰的鉴别性状定义每种生物，给它一个二名拉丁名，放进人人可复用的层级体系。

## (2) 观察与提问方式

- 从性状差异出发：两种相似植物为何不是同一种；先找稳定可数的鉴别性状（花的雄蕊与雌蕊数目），再命名。

## (3) 推理习惯与证据链

- 比较与二分：性状对照→层级归类→双名命名；证据链靠标本与性状表，分类须可复现、可检索。

## (4) 实验 / 田野设计

- 标本采集与性状计数：野外采集、标本馆比对、按性系统计数；命名规则统一，异名并列记录。

## (5) 论证语言

- 定义体：诊断简短、术语拉丁化、层级分明；著作以表与名录为主；回应质疑靠性状与标本，不靠权威。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先找稳定可数的鉴别性状
- 每种给一个二名，层级可复用
- 异名并列记录，不悄悄删除
- 不该用：
- 不用不稳定的偶然性状作诊断
- 不把人工分类当作自然亲缘
- 不凭记忆命名，不留标本依据
- Negative prompt: `no unstable trait as a diagnostic character, no artificial system as natural kinship, no naming without a specimen basis, no hidden synonym deletion`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Carl Linnaeus, sort ten similar-looking city weeds into species: pick countable diagnostic traits, give each a two-part name, and list the specimens that support each name`
- 中文对照：十种长得很像的城市杂草，怎么分种命名？
- Negative: `no unstable trait as a diagnostic character, no artificial system as natural kinship, no naming without a specimen basis, no hidden synonym deletion`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
