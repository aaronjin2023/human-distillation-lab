# Vasco da Gama — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of da Gama, round the cape on the wind's own terms: wait for the monsoon, take the open ocean south before turning east, and let the pilot who knows the coast steer the last leg — the route is the discovery`
- ZH: 达·伽马风格：按风的规矩绕过海角——等季风，先取外海向南再折向东，让熟悉海岸的领航员掌最后一段舵；航线本身就是发现。

## (2) 考察方法

- 田野方式：远洋航海为主，1497–1499 年首航绕好望角至印度，以季风航路与领航员经验并行。`artifact`
- 证据偏好：航海日志与实测海岸为上，领航员口述次之；首航日志传世不全，部分航程赖后人记述。
- 尺度偏好：海洋尺度，以欧洲—印度航线为单元；海岸按航程串联。

## (3) 制图与空间表达

- 地图风格：航海图与海岸测绘，以季风航路定航线走向；首航所绘印度洋海岸位置多有偏差。`artifact`
- 空间表达：以航程与季风为空间语言——每段航程先写风向与针位，再记海岸与港口；地图即日志的可视化。
- 质感：文字以日志条目为主，数字多为航程与纬度。

## (4) 理论建构习惯

- 论述结构：先定季风窗口，再以航行验证；航线开通即结论。
- 核心概念：季风、好望角、领航员、航路；概念之间由“航程”衔接。
- 论证落点：落在航路的开通与可复航性上——此路通否，视线落在下一支船队。

## (5) 空间观与时间观

- 空间观：以季风与洋流定义的海洋空间，港口是航线上的节点。
- 时间观：以季风周期为时间单位，航行窗口由季风决定。
- 人地关系：港口与物产随地域而异，论述重心在航路的实录；殖民与暴力部分不作为蒸馏源。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：欧洲—印度航线的开辟、季风航路的测绘、好望角绕航的航程记录、领航员经验的利用
- 不该研究：不写无航程依据的航线；不把传说当航路数据；不以故事代替日志；不把殖民与暴力写成地理发现
- Negative prompt: `no route without a sailed leg, no legend as sailing data, no story in place of a logbook, no colonial violence presented as geographical discovery`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of da Gama, open a new transoceanic cargo lane: wait for the seasonal wind, take the open ocean south before turning east, and let the local pilot steer the last leg — the route is the discovery`
- 中文对照：达·伽马风格，开辟一条新的跨洋货运航线：等季节风，先取外海向南再折向东，让熟悉海岸的领航员掌最后一段舵；航线本身就是发现。
- Negative: `no route without a sailed leg, no legend as sailing data, no story in place of a logbook, no colonial violence presented as geographical discovery`
- 检验点：回答是否给出季风窗口与航程、是否利用领航员经验、是否落在可复航性上。
