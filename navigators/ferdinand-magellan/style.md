# Ferdinand Magellan — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ferdinand Magellan: a strait hunted fjord by fjord, a Pacific crossed on faith in its size, latitudes logged while the fleet starves, the log as a record of endurance rather than triumph`
- ZH: 斐迪南·麦哲伦风格：一条海峡逐湾逐峡搜寻，一片太平洋凭着对它大小的信念横渡，舰队挨饿时仍记纬度，日志是忍耐的记录而非凯旋。

## (2) 导航方法

- 定位：推测航法 + 纬度观测，横渡太平洋 98 日无陆地，靠纬度与航向推算船位。`artifact`
- 定向：南美东海岸南下寻海峡，入海峡后逐湾探查；出海峡乘东南信风横渡太平洋。`artifact`
- 误差容忍：太平洋宽度远超预想，补给耗尽仍按原航向西行，误差以到岸纬度纠正。`artifact`

## (3) 造船与帆装

- 船型：五船船队（特立尼达号等），卡拉克与卡拉维尔并用，1519 年自塞维利亚出发。`artifact`
- 帆装：横帆与拉丁帆并用，信风顺风横渡。`impression`
- 补给：太平洋横渡补给耗尽，食鼠、皮革与木屑——航史上最惨的补给崩溃之一。`artifact`
- 减员：哗变、逃亡、坏血病，抵菲律宾仅余三船。`artifact`

## (4) 航线规划习惯

- 路线：塞维利亚—大西洋—巴西—拉普拉塔—巴塔哥尼亚越冬—麦哲伦海峡—太平洋—关岛—菲律宾。`artifact`
- 节奏：寻峡慢（逾月逐湾探查），横渡太平洋 98 日，登陆后速战。`artifact`
- 返航：麦哲伦死于麦克坦（1521），余部由埃尔卡诺带回（见 #37）。`artifact`

## (5) 日志与海图语言

- 日志体例：麦哲伦本人日志已佚，航行见于同行者安东尼奥·皮加费塔《初次环球航行记》。`artifact`
- 海图语言：海峡逐湾记，太平洋记纬度与无陆地天数，岛屿按日命名。`artifact`
- 命名习惯：海峡初名“万圣海峡”，太平洋（Mar Pacifico）因风平浪静得名。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 麦哲伦海峡
- 太平洋横渡航线
- 南美—东南亚环球航路
- 海峡逐湾搜寻法
- 不该探索：
- No strait entered without sounding each inlet
- No Pacific crossing without provisions counted to the last biscuit
- No fleet kept together without a rendezvous plan
- No landfall claimed without a latitude fix
- Negative prompt: `No strait entered without sounding each inlet, No Pacific crossing without provisions counted to the last biscuit, No fleet kept together without a rendezvous plan, No landfall claimed without a latitude fix`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ferdinand Magellan, an uncrewed ship hunts a strait fjord by fjord in 2026, then crosses a wide ocean on faith in its size, latitudes logged while provisions run down.`
- 中文对照：斐迪南·麦哲伦风格：一艘无人船2026年逐湾逐峡搜寻一条海峡，再凭着对大洋大小的信念横渡，补给见底时仍记纬度。
- Negative: `No strait entered without sounding each inlet, No Pacific crossing without provisions counted to the last biscuit, No fleet kept together without a rendezvous plan, No landfall claimed without a latitude fix`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
