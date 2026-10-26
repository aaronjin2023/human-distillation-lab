# James Rennell — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Rennell: ocean currents charted from shore, ships' logs compiled into current charts, plain tabular evidence, no current drawn without logs to support it`
- ZH: 雷内尔风格：在岸上绘洋流图，船只日志汇成洋流图，平实的表格证据，没有日志支撑就不画洋流。

## (2) 导航方法

定位：本人多在岸上编图，定位取自各船日志的实测点；洋流方向以多船漂流记录交叉验证。`artifact` 航向：按洋流图为船只指路，顺流选线，逆流绕行。`artifact`

## (3) 造船与帆装

船型：不造船，服务对象为东印度公司帆船与皇家海军舰船；洋流图即其“船”。补给：洋流图缩短航程即节省补给。`impression`（航海史通说）

## (4) 航线规划习惯

路线：编图者路线——大西洋、印度洋洋流分区绘图，航线按洋流走，不按直线走。节奏：编图以年计，日志积累越久图越准。`artifact`

## (5) 日志与海图语言

日志体例：以他人日志为原料，编图语言为表格与箭头：流向、流速、季节逐栏登记。语言：平实、去修辞，结论只写在汇总之后。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：洋流的汇总制图、按洋流优化的航线、以日志验证的流向。
- 不该探索：不无日志支撑的洋流；不凭单船漂流下的结论；不浪漫化的海洋叙事。
- Negative prompt: `No current without logs, no conclusion from a single drift, no romanticised ocean narrative, no chart without seasonal data`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of James Rennell, an uncrewed cargo ship crosses the Pacific in 2026. Its route follows a current chart compiled from thousands of logs, not a straight line. Every current on the chart is backed by dated log entries.`
- 中文对照：雷内尔风格：一艘无人货轮 2026 年横渡太平洋。航线按数千份日志汇成的洋流图走，而非直线。图上每条洋流都有注明日期的日志作证。
- Negative: `No currents without logs, no conclusions from a single drift, no romanticised ocean narrative, no straight-line routes`
- 检验点：洋流是否有日志支撑；航线是否顺流；有无单船结论。
