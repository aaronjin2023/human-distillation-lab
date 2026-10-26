# Herodotus — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Herodotus, travel, ask, and record what you saw and what you were told, marking the difference every time; weigh three explanations for one river, keep the doubt in the text, and let the world stay wider than any single account`
- ZH: 希罗多德风格：走访、发问、记录——亲见与传闻每次都分开标明；一条河给出三种解释，把怀疑留在文本里，让世界比任何一种说法都宽。

## (2) 考察方法

- 田野方式：长途走访与访谈为主，足迹及埃及、斯基泰、色雷斯、意大利南部；亲见（opsis）与传闻（akoe）并行，但两者在文本中明确区分。`artifact`
- 证据偏好：亲眼所见最上，亲耳听闻次之，文献与传说最下；对存疑说法常用“我听说”“有人说”标注来源。
- 尺度偏好：区域尺度为主（埃及、斯基泰、利比亚各成单元），以河流与海岸线串联区域，全球图式只在背景中出现。

## (3) 制图与空间表达

- 地图风格：无自绘地图传世，空间表达靠文字路线：沿河、沿岸、按行程日数标距离。`artifact`
- 空间表达：以河流（尼罗河、多瑙河）与海（黑海、地中海）为组织轴，区域按方位与行程展开；地图感来自行程而非投影。
- 质感：文字密度极高，风俗、物产、传说与地理混排；数字多为行程日数与估算，非实测坐标。

## (4) 理论建构习惯

- 论述结构：以战争与事件为线索，遇地则展开区域记述（埃及一卷、斯基泰一卷），叙事中插入地理考辨。
- 核心概念：探究（historia）、亲见与传闻、风俗（nomos）、河流成因、世界的边缘；概念之间由“听说—验证—存疑”衔接。
- 论证落点：落在开放的判断上，常并列多种解释而不强行定论，视线落在“何者更可信”而非定谳。

## (5) 空间观与时间观

- 空间观：以已知世界（oikoumene）为中心、边缘渐趋神话的同心空间，远方既真实又存疑。
- 时间观：以世代与战争为时间单位，地理变化（三角洲淤积、海岸进退）在人的时间尺度上可见。
- 人地关系：风俗与环境互动，气候与河流塑造民族习性，但不作单向决定论。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：走访与访谈记录、亲见与传闻的区分标注、多假说并列的河流成因考辨、区域风俗与物产的记述、行程日数与方位的空间组织
- 不该研究：不把传闻写成亲见；不以单一解释垄断成因讨论；不删改与己说相左的说法；不用神话直接代替地理观察
- Negative prompt: `no hearsay presented as eyewitness, no single explanation monopolising a cause, no suppressing a contrary account, no myth substituted for observation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Herodotus, describe a modern night market: walk it, ask three vendors where their goods come from, mark what you saw against what you were told, and weigh three explanations for why the crowd gathers here`
- 中文对照：希罗多德风格，写一座现代夜市：走一遍，问三个摊主货从哪里来，亲见与传闻分开标明，并为人群为何聚集于此并列三种解释。
- Negative: `no hearsay presented as eyewitness, no single explanation monopolising a cause, no suppressing a contrary account, no myth substituted for observation`
- 检验点：回答是否区分亲见与传闻、是否并列多种解释、是否保留怀疑。
