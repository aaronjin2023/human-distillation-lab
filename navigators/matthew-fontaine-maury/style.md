# Matthew Fontaine Maury — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Matthew Fontaine Maury: wind and current charts, thousands of ship logs aggregated into tables, clipper routes shortened by weeks, plain tabular data, no anecdote without a number`
- ZH: 莫里风格：风与洋流图，成千上万份船只日志汇成表格，快船航线缩短数周，平实的表格数据，没有数字就不讲故事。

## (2) 导航方法

定位：不靠单船实测，靠汇总成千上万份商船与军舰日志的风向、海流、航速记录，统计出最优航线。`artifact` 经度与纬度取自各船日志的定位点，误差以样本量抵消；信风带与洋流按季节分区制表，航线按月份给出。`artifact`

## (3) 造船与帆装

船型：不造船，服务对象是当时的帆船与飞剪船（clipper）；帆装按风图选航线而非改船。补给：航线优化本身就是补给——缩短航程即减少淡水与食物消耗。`impression`（航海史通说）

## (4) 航线规划习惯

路线：数据驱动的航线优化。去程与返程按季节风图分别选线，宁愿绕远走顺风顺流，也不顶风走直线。节奏：航线以周计缩短，纽约—旧金山、纽约—里约等航线在他的风图推广后普遍提速。`artifact`

## (5) 日志与海图语言

日志体例：表格化、数字化的航海记录——日期、位置、风向、风速、海流、航速逐栏登记，专为汇总统计而设计。语言风格：平实、去修辞，结论只写在数据之后；海图以等值线与箭头标示风与流，注记极简。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：风与洋流的统计制图、按季节优化的快船航线、以日志汇总改进航行效率。
- 不该探索：不没有数据支撑的航线断言；不浪漫化的冒险叙事；不单船奇遇式的航行记录。
- Negative prompt: `No uncharted claims without data, no romanticised adventure, no anecdotal navigation, no single-ship story without logs`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Matthew Fontaine Maury, an uncrewed cargo ship crosses the Pacific in 2026. Its route is chosen from aggregated wind and current tables, not from a single captain's hunch. Daily log entries record wind, current and speed in columns. No anecdote without a number.`
- 中文对照：莫里风格：一艘无人货轮 2026 年横渡太平洋。航线按汇总的风与洋流表选定，而非凭某位船长的直觉。每日日志以表格记录风向、洋流与航速。没有数字就不讲故事。
- Negative: `No romanticised adventure, no uncharted claims without data, no anecdotal navigation, no dramatic storms`
- 检验点：航线是否由数据表驱动；日志是否表格化；有无无数据支撑的断言。
