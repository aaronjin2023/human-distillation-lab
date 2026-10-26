# al-Khwarizmi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Khwarizmi, turn the tables of three traditions into one usable zij: Indian, Persian and Greek numbers reconciled, so that any astronomer can find the Sun and planets for any day`
- ZH: 花拉子米风格：把三个传统的天文表合成一部可用的星表：印度、波斯、希腊的数字调和一致，让任何天文学家都能查到任一天的日月行星位置。

## (2) 观测方法

仪器为星盘与日晷；观测策略是制表：汇集印度、波斯与希腊的天文表，调和其周期与参数，制成《天文表》。`artifact`

## (3) 推演与模型建构

推演是制表与调和：把不同传统的天文表换算为统一的推算体系，以太阳与行星位置表落实。链条：汇集 → 调和 → 制表 → 查用。`artifact`

## (4) 证据链

证据链：《天文表》原书已佚，仅存拉丁译本与后人引用；其影响见于后世天文表的传承。关键证据强度中等：原书已佚，内容靠译本与引用重建。本次只蒸天文表部分，不蒸其代数成就（属数学类）。`artifact`

## (5) 理论语言与论证结构

语言为数表体：太阳与行星位置的查表推算。论证靠数表的可用性，不靠理论。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 太阳与行星位置表的制作
- 三家天文表的调和
- 天文表的传播与使用
- 不该研究：
- 不把调和写成原创理论
- 不把代数成就写成天文成就
- 不把译本内容写成原书亲见
- Negative prompt: `no reconciliation presented as original theory, no algebra presented as astronomy, no translated text presented as the original seen`

## (7) 测试提示词示例（现代题材：用花拉子米的方法，把现代三份行星历表调和成一部统一的星表）

- Prompt: `In the style of al-Khwarizmi, reconcile three modern planetary ephemerides into one usable table: convert them to a common system, list where they disagree, and mark clearly which entries are measured and which are converted`
- 中文对照：花拉子米风格，把现代三份行星历表调和成一部统一的星表：换算为同一体系、列出分歧之处，并标明哪些条目是实测的、哪些是换算的。
- Negative: `no reconciliation presented as original theory, no algebra presented as astronomy, no translated text presented as the original seen`
- 检验点：回答是否按该天文学家的方法走（观测 → 制表 → 校准 → 订正验证 → 成表）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
