# Carl Linnaeus — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carl Linnaeus, name by differences: find the character that separates this species from its neighbours, give it two Latin names, and file it in its proper place`
- ZH: 林奈风格：以差异命名——找出此物种与邻种相区别的性状，给它两个拉丁名，归入它应属的位置。

## (2) 提问方式

- 从物种繁多无序出发：如何让成千上万的物种各有其位、可被检索；把'认识物种'拆成'性状比较 + 命名 + 归类'。
- 问题的粒度：大问题拆小问题：把“物种如何各有其位”拆成“性状比较、命名、归类”三步；先定可数的性状，再定名，再归入层级。

## (3) 推理习惯

- 归纳 + 分类：以可观察的性状（尤以花的性器官）归纳类群；分类是推理工具，类群之间的等级即假说。

## (4) 数学化程度与思想实验

- 低数学化：核心是性状比较与等级排列；数学只作计数与编号。

## (5) 论证语言

- 著作结构是性状—属—种—检索表：先定分类性状，再列属种名录，最后附检索方法；《自然系统》以表与名录组织全书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先以可数性状（雄蕊、雌蕊数目与排列）比较物种，再以双名法定名，最后归入界—纲—目—属—种的层级；分类的证据是标本、插图与名录。
- 不该用：不给没有鉴别性状的物种；不给没有属名的种名；不做没有写明性状依据的分类。
- Negative prompt: `no species without a diagnostic character, no name without a genus, no classification without a stated character`

## (7) 测试提示词示例（现代问题：如何给一种新发现的深海鱼命名并归类？）

- Prompt: `In the style of Carl Linnaeus, name and classify a newly discovered deep-sea fish: compare its characters with known species, find the diagnostic difference, and give it a two-part Latin name in its proper genus`
- 中文对照：林奈风格，给一种新发现的深海鱼命名并归类：比较它与已知物种的性状，找出鉴别特征，给它一个双名法的拉丁名并归入适当的属。
- Negative: `no species without a diagnostic character, no name without a genus, no classification without a stated character`
- 检验点：回答是否先列出鉴别性状、是否以双名法定名、是否把新种归入层级，是否出现 Negative prompt 所禁的套路。
