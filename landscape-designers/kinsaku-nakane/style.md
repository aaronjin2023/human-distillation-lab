# Kinsaku Nakane — 园林风格规格 style.md（给图像模型）

> 只描述园林，不描述人生。引用造园理论著作时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kinsaku Nakane, modern Japanese garden, a garden as a living hanging scroll, windows as frames, borrowed mountains, six gardens in one, viewed not walked, the garden as a painting on the wall`
- ZH: 中根金作风格，现代日本庭园，园为活的挂轴，窗为画框，借远山，一园六景，园以观为主，园为墙上的画。

## (2) 空间布局

- 借景框景式布局：足立美术馆六庭各异，皆以窗为画框、以远山为背景；游线退后，坐观为主；尺度以窗为园，园如挂轴。`artifact`

## (3) 水石植物

- 水：池泉与枯山水并用，白砂代水间以真池；石：立石为山，石组取自然之势；植物：苔、松、枫为主，季相以秋枫与苔色为高光。`artifact`

## (4) 借景与框景

- 借景为本体：借远山、借天际；框景以窗为框，框内取园与山；对景以窗与窗相望。`artifact`

## (5) 材料与季节变化

- 材料：白砂、苔、石、松；季节：秋枫最胜，苔色四季；光影：窗光为主，日光透窗成画。`artifact`

## (6) 该造什么 / 不该造什么

- 该造：窗为画框、活的挂轴、借远山、一园六景、苔与白砂、坐观之园。`artifact`
- 不该造：no symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded planting, no walking maze。
- Negative prompt: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded planting, no walking maze`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kinsaku Nakane, a modern museum garden viewed through large windows, six small gardens each framed like a living hanging scroll, white sand and moss, standing stones, borrowed distant mountains, a garden to look at, not to walk through`
- 中文对照：中根金作风格：现代美术馆里的一座窗景园，六庭各异，皆以窗为画框，苔砂相映，立石借远山，园以观为主，园为活的挂轴。
- Negative: `No symmetrical axis, no large geometric flower beds, no bright heavy colours, no crowded planting, no walking maze`
- 检验点：园是否按第 (1) 节一句话风格成立；第 (6) 节母题是否出现；禁区写法是否未出现。
