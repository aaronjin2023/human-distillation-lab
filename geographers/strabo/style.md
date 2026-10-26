# Strabo — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Strabo, describe the inhabited world region by region, from the shape of the coast to the customs of its peoples; correct the mathematicians with what travellers actually report, and let usefulness to rulers and readers decide what a geography is for`
- ZH: 斯特拉波风格：把有人居住的世界逐区写下来，从海岸形状到各地风俗；用旅行者的实报纠正数学家，让“对统治者与读者有用”决定一部地理志写什么。

## (2) 考察方法

- 田野方式：以广泛旅行（小亚细亚、埃及、意大利、希腊）与文献汇集并行，旅行补文献之缺，文献补旅行之限。`artifact`
- 证据偏好：旅行者实报与行政区划文献为上，纯数学推算次之；对埃拉托色尼的经纬数值持怀疑态度，认为误差大于实用价值。
- 尺度偏好：区域尺度为核心，十七卷按区域分卷（伊比利亚、高卢、意大利、希腊、亚洲），全球图式只作卷首背景。

## (3) 制图与空间表达

- 地图风格：文字地图为主，区域按海岸线、山脉、河流边界划分；附图观念弱，地图感来自方位与边界的文字描述。`artifact`
- 空间表达：分区是空间语言的核心——每个区域先定边界，再写地形、城市、民族、物产；分区之间以行程与方位衔接。
- 质感：文字密度极高，百科式罗列；数字多为距离与行程，少有坐标。

## (4) 理论建构习惯

- 论述结构：按区域分卷，每卷内部按“边界—地形—城市—民族—物产—历史”的固定顺序展开。
- 核心概念：有人居住的世界（oikoumene）、区域（chorographia）、实用地理、旅行者实报；概念之间由区域边界衔接。
- 论证落点：落在实用判断上——此地宜居否、物产如何、道路通否，视线落在统治与通行的用处。

## (5) 空间观与时间观

- 空间观：以罗马世界为中心的区域拼合空间，空间的价值在于可通行、可统治。
- 时间观：以帝国扩张为时间背景，地理随政治版图而更新；古代传说只在考证地名时引用。
- 人地关系：环境塑造风俗，但论述重心在人地互动的结果（城市、物产、道路），不是单向决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：逐区区域记述、海岸与边界的文字界定、旅行者实报的核对、城市与物产的百科罗列、对数理推算的实用性质疑
- 不该研究：不写无旅行者实报支撑的纯数学地图；不把传说地名当实地；不为体系完整而虚构未知区域；不脱离实用价值空谈理论
- Negative prompt: `no mathematical map without travellers' reports, no legendary placenames as real places, no invented regions to complete a system, no theory without practical use`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Strabo, describe a modern metropolitan region district by district: fix each boundary by coast, river or road, list its towns, products and customs, and judge each district by whether it can be lived in and travelled through`
- 中文对照：斯特拉波风格，写一座现代都市圈：逐区描述，以海岸、河流或道路定边界，列出城镇、物产与风俗，并按宜居与可通行与否评判各区。
- Negative: `no mathematical map without travellers' reports, no legendary placenames as real places, no invented regions to complete a system, no theory without practical use`
- 检验点：回答是否逐区展开、是否先定边界再写内容、是否落在实用判断上。
