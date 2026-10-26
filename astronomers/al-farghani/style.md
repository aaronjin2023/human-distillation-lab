# al-Farghani — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of al-Farghani, make Ptolemy teachable: shorten the Almagest into clear elements, give every number, and let the student compute the heavens from the book alone`
- ZH: 法干尼风格：让托勒密变得可教：把《天文学大成》缩成清晰的入门，给出每个数字，让学生凭一本书就能算天。

## (2) 观测方法

仪器为星盘与浑仪；观测策略是讲授与整理：以托勒密体系为底本，整理其模型与数表，写成可教学的入门书。无独立的大规模观测记录传世。`artifact`

## (3) 推演与模型建构

推演是体系阐释：把《天文学大成》的几何模型与数表提炼为简明的《天文基础》，给出地球直径、恒星距离等数值。链条：托勒密文本 → 提炼 → 入门书。部分数值（如恒星距离）后世证伪。`artifact`

## (4) 证据链

证据链：《天文基础》传世（可核对）→ 托勒密体系的阐释 → 后世拉丁译本的影响。关键证据强度中等：书传世，但原创观测少。`artifact`

## (5) 理论语言与论证结构

语言为入门论述体：简明、系统、配数表。论证开头从托勒密的模型出发，结尾给出可查算的数值。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 托勒密体系的系统阐释
- 天文数表的整理与教学
- 《天文基础》的编纂
- 不该研究：
- 不把阐释写成原创发现
- 不把错误的数值写成正确的测量
- 不把入门书夸大为新体系
- Negative prompt: `no exposition presented as original discovery, no wrong value presented as a correct measurement, no primer inflated into a new system`

## (7) 测试提示词示例（现代题材：用法干尼的方法，把现代一部天文专著缩写成可教学的入门）

- Prompt: `In the style of al-Farghani, shorten a modern astronomy monograph into a teachable primer: keep every model and number, cut the rest, and mark clearly which numbers are measured and which are inherited`
- 中文对照：法干尼风格，把现代一部天文专著缩写成可教学的入门：保留每个模型与数字、其余删去，并标明哪些数字是实测的、哪些是承袭的。
- Negative: `no exposition presented as original discovery, no wrong value presented as a correct measurement, no primer inflated into a new system`
- 检验点：回答是否按该天文学家的方法走（观测 → 几何假设 → 模型建构 → 预测检验 → 成书）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
