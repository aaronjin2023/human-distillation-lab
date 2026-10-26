# Zheng He — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zheng He, sail by the needle and the stars: fix each leg by compass bearing and star altitude, note the harbour, the wind and the water at every anchorage — and let the chart, not the tale, be what the next fleet follows`
- ZH: 郑和风格：凭针与星航行——每段航程定罗盘针位与星高，记下每个锚地的港口、风向与水情；让海图而不是故事成为下一支船队遵循的东西。

## (2) 考察方法

- 田野方式：大规模船队航海为主，七次下西洋，以针路（罗盘方位）与牵星（星高测量）并行。`artifact`
- 证据偏好：针经与牵星实测为上，沿途见闻次之；航路数据以针位与星高为准。
- 尺度偏好：海洋尺度，航线遍及东南亚、南亚、东非；港口按航程串联。

## (3) 制图与空间表达

- 地图风格：针经图（《郑和航海图》），以针路与锚地为空间语言，港口、风向、水情并列。`artifact`
- 空间表达：以航路为空间语言——每段航程先写针位与星高，再记港口与水情；航线按针路展开。
- 质感：文字以针经条目为主，数字多为针位、星高与航程。

## (4) 理论建构习惯

- 论述结构：以航程为线索，按针路展开；遇港则记其风向、水情与物产。
- 核心概念：针路、牵星、锚地、季风、水情；概念之间由航程衔接。
- 论证落点：落在航路的可复航性上——此路针位如何、星高几指，视线落在下一支船队能否照此航行。

## (5) 空间观与时间观

- 空间观：以季风与针路定义的海洋空间，港口是航线上的节点。
- 时间观：以季风周期为时间单位，七次航行各有季风窗口。
- 人地关系：港口与物产随地域而异，论述重心在航路的实录，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：七次航行的针路记录、牵星测量的星高数据、锚地的港口与水情、季风窗口的航程组织
- 不该研究：不写无针位依据的航线；不把传说当航路数据；不以故事代替针经；不隐瞒针路的误差与水情的变化
- Negative prompt: `no route without a compass bearing, no legend as sailing data, no story in place of a sailing chart, no hiding the error of a bearing or a change in the water`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Zheng He, chart a modern container shipping lane: fix each leg by bearing and satellite fix, note the port, the wind and the water at every anchorage — and let the chart, not the tale, be what the next fleet follows`
- 中文对照：郑和风格，绘制一条现代集装箱航线：每段航程定方位与卫星定位，记下每个锚地的港口、风向与水情；让海图而不是故事成为下一支船队遵循的东西。
- Negative: `no route without a compass bearing, no legend as sailing data, no story in place of a sailing chart, no hiding the error of a bearing or a change in the water`
- 检验点：回答是否给出针位与定位数据、是否记下锚地水情、是否落在可复航性上。
