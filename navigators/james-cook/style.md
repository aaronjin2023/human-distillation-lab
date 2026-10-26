# James Cook — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Cook: precise hydrographic surveying, daily latitude and longitude fixes, methodical coastal charting, plain factual log entries, no embellishment`
- ZH: 詹姆斯·库克风格：测绘精度、每日定位，未经测绘的断言、浪漫化冒险。

## (2) 导航方法

- 精密水文测绘：每日正午测纬度、天文钟定经度，遇浮冰即改向；测深锤逐点测深，海岸线逐段绘入海图；误差容忍度极低，宁可多测一日也不凭推算画岸。 `impression`

## (3) 造船与帆装

- 奋进号、决心号、冒险号：改装运煤船，船体坚固、吃水浅，适于近岸测绘；配天文钟、六分仪与测绘员；防坏血病靠酸菜与麦芽汁。 `impression`

## (4) 航线规划习惯

- 三次远征皆有明确测绘目标：第一次测金星凌日并绘新西兰与澳大利亚东岸；第二次搜寻南方大陆、深入南极圈；第三次寻西北航道北上至白令海峡。 `impression`

## (5) 日志与海图语言

- 日志体例为海军测绘报告：日期—纬度—经度—风向—海况—事件，语言简洁精确，无抒情；海图注记密度高，命名多以赞助人与船员命名。 `impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：每日正午定位的测绘节奏、新西兰与澳大利亚东海岸的逐段成图、南极圈内的浮冰改向。
- 不该探索：未经测绘的断言、浪漫化冒险。
- Negative prompt: `No romanticised adventure, no uncharted claims without fixes, no dramatic storms, no sentimental commentary, no modern GPS as the only fix`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of James Cook, an uncrewed cargo ship crosses the Pacific in 2026. Daily log entries with latitude, longitude, wind and sea state. Plain factual language. Methodical route, no embellishment. Sensor checks replace scurvy prevention.`
- 中文对照：库克风格：一艘无人货轮2026年横渡太平洋。每日日志记录纬度、经度、风向与海况，语言平实无修饰，航线有条不紊。以传感器检查代替防坏血病措施。
- Negative: `No romanticised adventure, no uncharted claims without fixes, no dramatic storms, no sentimental commentary, no modern GPS as the only fix`
- 检验点：导航方法是否落到实处；航线习惯是否可辨；禁区写法是否出现。
