# Ferdinand Magellan — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Magellan, find the strait the maps say is not there: follow the coast south until it turns, take the narrow passage, and cross the ocean nobody has measured — the voyage, not the man, completes the circle`
- ZH: 麦哲伦风格：去找地图上说没有的海峡——沿海岸向南走到它转弯处，穿过狭窄的通道，横渡一片没人量过的洋；完成环绕的是航行，不是个人。

## (2) 考察方法

- 田野方式：远洋航海与航海日志并行，1519–1522 年船队环球航行，以海岸追踪与海峡搜寻为核心。`artifact`
- 证据偏好：航海日志与实测海岸为上，书本推算次之；船队日志以安东尼奥·皮加费塔的记述为主要来源。
- 尺度偏好：全球尺度，以环球航行为单元；海岸按航程串联。

## (3) 制图与空间表达

- 地图风格：航海图与海岸测绘，以海峡通过与太平洋横渡定航线走向。`artifact`
- 空间表达：以航程与海峡为空间语言——每段航程先写针位与里程，再记海岸与海峡；地图即日志的可视化。
- 质感：文字以日志条目为主，数字多为航程与纬度。

## (4) 理论建构习惯

- 论述结构：先立假设（南美南端有海峡通往亚洲），再以航行验证；航行完成即结论。
- 核心概念：海峡、环球、太平洋、航位推算；概念之间由“航程”衔接。
- 论证落点：落在环球航行的完成上——船队绕地球一周，视线落在航行本身。

## (5) 空间观与时间观

- 空间观：以大洋与海峡定义的全球空间，地球是可环绕的球体。
- 时间观：以三年航行为时间单位，地理随航行而修正。
- 人地关系：海岸与岛屿的记述以航行为主；殖民与暴力部分不作为蒸馏源。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：麦哲伦海峡的发现与通过、太平洋的横渡、环球航行的航海日志、皮加费塔记述的核对
- 不该研究：不把麦哲伦本人写成完成环球航行者；不写无航程依据的航线；不把传说当航路数据；不把殖民与暴力写成地理发现
- Negative prompt: `no crediting Magellan himself with completing the circumnavigation, no route without a sailed leg, no legend as sailing data, no colonial violence presented as geographical discovery`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Magellan, find the strait the charts say is not there: follow the coast south until it turns, take the narrow passage, and cross the ocean nobody has measured — the voyage, not the planner, completes the circle`
- 中文对照：麦哲伦风格，去找海图上说没有的海峡：沿海岸向南走到它转弯处，穿过狭窄的通道，横渡一片没人量过的洋；完成环绕的是航行，不是规划者。
- Negative: `no crediting Magellan himself with completing the circumnavigation, no route without a sailed leg, no legend as sailing data, no colonial violence presented as geographical discovery`
- 检验点：回答是否区分船队完成与个人完成、是否给出海峡搜寻过程、是否以日志为准。
