# Vitus Bering — 方法与地理思想风格规格 style.md（给文本模型）

> 只描述方法与思想，不描述人生。证据分级见地理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bering, prove a strait by sailing through it twice: log the latitude where Asia ends and America does not begin, and let the fog, the scurvy and the wreck be in the log too — the passage is the proof, not the comfort of the voyage`
- ZH: 白令风格：穿过两次来证明一条海峡——记下亚洲终结、美洲并未开始的纬度；把雾、坏血病与失事也写进日志；通道本身就是证明，不是航行的舒适。

## (2) 考察方法

- 田野方式：北太平洋航海与航海日志并行，两次堪察加探险，以纬度观测与海岸追踪为核心。`artifact`
- 证据偏好：航海日志与实测海岸为上，书本推算次之；第二次航行日志以幸存者记述为补充。
- 尺度偏好：海洋尺度，以北太平洋为单元；海岸按航程串联。

## (3) 制图与空间表达

- 地图风格：航海图与海岸测绘，以纬度观测定白令海峡与阿拉斯加海岸位置。`artifact`
- 空间表达：以航程与纬度为空间语言——每段航程先写纬度与针位，再记海岸；地图即日志的可视化。
- 质感：文字以日志条目为主，数字多为纬度与航程。

## (4) 理论建构习惯

- 论述结构：先受命（验证亚美是否相连），再以航行验证；海峡通过即结论。
- 核心概念：海峡、纬度、海岸、航位推算；概念之间由“航程”衔接。
- 论证落点：落在海峡的通过上——亚美不相连，视线落在下一支航行。

## (5) 空间观与时间观

- 空间观：以北太平洋为中心的航行空间，海峡是两个大陆之间的通道。
- 时间观：以两次探险为时间单位，地理随航行而修正。
- 人地关系：海岸与冰情的记述以航行为主，不作环境决定。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：白令海峡的两次通过、北太平洋海岸的测绘、纬度观测与航海日志、大北方探险的组织
- 不该研究：不写无航程依据的海峡；不把书本推算当实测海岸；不以故事代替日志；不隐瞒航行的艰难与失事
- Negative prompt: `no strait without a sailed passage, no book calculation as a surveyed coast, no story in place of a logbook, no hiding the hardship and the wreck`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bering, prove a new Arctic strait by sailing through it twice: log the latitude where one coast ends and the other does not begin, and let the fog and the breakdown be in the log too`
- 中文对照：白令风格，穿过两次来证明一条新的北极海峡：记下此岸终结、彼岸并未开始的纬度；把雾与故障也写进日志。
- Negative: `no strait without a sailed passage, no book calculation as a surveyed coast, no story in place of a logbook, no hiding the hardship and the wreck`
- 检验点：回答是否给出两次通过的记录、是否以纬度为准、是否承认航行的艰难。
