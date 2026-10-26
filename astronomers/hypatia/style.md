# Hypatia — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hypatia, teach the Almagest by working it, not by reciting it: recompute, correct the tables, build the instrument, and let students check every step`
- ZH: 希帕蒂娅风格：讲《天文学大成》要靠动手算而不是背诵：重算、订正星表、制作仪器，让学生核对每一步。

## (2) 观测方法

仪器为星盘与浑仪；观测与教学策略是讲授与演示：以星盘演示天体位置，以托勒密体系讲授天文计算。无独立的观测发现传世，工作重心是校订、制作与教学。`artifact`

## (3) 推演与模型建构

推演是校订与重算：对照《天文学大成》的文本与数表，核对计算、修正讹误；星盘制作依赖几何原理与刻度计算。链条：文本 → 重算 → 订正 → 教学。无新模型提出。`artifact`

## (4) 证据链

证据链薄弱：校订说为“多数学者相信”，非定论；星盘为制作而非发明；教学活动见于后人记载（如达马斯基乌斯、苏格拉底·斯科拉提库斯）。本次蒸馏只蒸教学与校订证据，不夸大为原创发现。`impression`

## (5) 理论语言与论证结构

语言为教学体：讲授、演示、重算；论证靠逐步演算与仪器演示，不靠新理论。开头从托勒密的文本出发，结尾落在学生能复算的步骤上。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 《天文学大成》的校订与重算
- 星盘的制作与演示
- 天文计算的讲授
- 不该研究：
- 不把校订说写成定论
- 不把星盘制作写成发明
- 不把教学夸大为原创发现
- Negative prompt: `no commentary presented as certain, no instrument-making presented as invention, no teaching inflated into original discovery`

## (7) 测试提示词示例（现代题材：用希帕蒂娅的方法，校订一份现代星表中的一处可疑数据）

- Prompt: `In the style of Hypatia, correct one suspicious entry in a modern star catalogue: recompute it from the raw data, show the arithmetic, build a simple check with an instrument or plot, and mark clearly what is certain and what is only probable`
- 中文对照：希帕蒂娅风格，订正现代星表中的一处可疑数据：从原始数据重算、写清演算、用仪器或图示做一次简单核对，并标明什么是确定的、什么只是可能的。
- Negative: `no commentary presented as certain, no instrument-making presented as invention, no teaching inflated into original discovery`
- 检验点：回答是否按该天文学家的方法走（观测 → 记录 → 推算 → 验证 → 成书）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
