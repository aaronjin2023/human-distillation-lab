# Joshua Slocum — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joshua Slocum: alone aboard the Spray, dead reckoning with a tin clock, self-steering across oceans, plain seaman's log, no crew, no fuss, the sea as a workplace`
- ZH: 斯洛库姆风格：独自驾斯普雷号，凭一只锡钟推算航位，横渡大洋自操舵，平实的水手日志，无船员、无排场，大海就是工作场。

## (2) 导航方法

定位：推算航位为主，六分仪为辅；无天文钟，以一只锡钟计时，误差以陆标与天文观测校正。`artifact` 航向：自操舵装置使船自动保持航向，单人得以睡眠与修船；顺风航行优先，逆风不硬顶。`artifact`

## (3) 造船与帆装

船型：斯普雷号（Spray），旧牡蛎船改装，37 英尺，坚固、稳性好、可单人操纵。帆装简洁，一人可收放。补给：淡水、食物、备件一次备足，沿途港口补给。`artifact`

## (4) 航线规划习惯

路线：单人环球：东出大西洋、经麦哲伦海峡、横渡太平洋、经好望角返航；三年航程，停靠多港，不赶时间。节奏：独航步占全部，航速慢而稳。`artifact`

## (5) 日志与海图语言

日志体例：水手日志——日期、位置、风向、海况、修船、见闻，语言平实带幽默，少抒情。海图：沿用当时海图，手工标注航迹。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：单人环球航行、推算航位与自操舵、以旧船远航。
- 不该探索：不依赖仪器的炫技导航；不无补给的冒进；不浪漫化的孤独抒情。
- Negative prompt: `No instrument-dependent showmanship, no reckless sailing without supplies, no romanticised solitude, no modern GPS`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Joshua Slocum, a small Yorkshire terrier rides the subway alone. It navigates by dead reckoning: counting stops like days at sea, reading the flow of commuters like wind, steering itself with no crew and no fuss.`
- 中文对照：斯洛库姆风格：一只约克夏犬独自乘地铁。它凭推算航位导航：数站如数海上日数，读人流如读风，无船员、无排场，自己掌舵。
- Negative: `No GPS, no maps, no modern instruments, no romanticised solitude, no cute anthropomorphism`
- 检验点：导航是否靠推算与观察；是否无船员无排场；有无仪器依赖。
