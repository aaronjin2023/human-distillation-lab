# Robert Towne — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Towne: intricate neo-noir plotting, withheld exposition, dialogue that reveals character through evasion, Los Angeles as a corrupt system, a detective who learns the truth too late`
- ZH: 罗伯特·汤恩风格：精密的新黑色电影情节， withheld 的 exposition（被扣住的说明），以回避暴露人物的对白，洛杉矶即一个腐败的系统，一位学到真相时为时已晚的侦探。

## (2) 结构：三幕 / 序列 / 节拍

- 调查式多线结构：《唐人街》以八序列组织，每序列只揭开一层真相，侦探的有限视角即结构本身。第一幕立下调查，第二幕层层揭开、每揭一层又被挡住，第三幕真相大白却为时已晚。时间跨度短，常为数日，靠调查的推进而非悬念组织。

## (3) 对话

- 对白以回避写人物：人物问三句、答三句 evasions（回避），真相藏在不说的话里。潜台词占比极高，一句台词常常同时完成误导、试探与暴露。动作描写写调查：跟踪、偷看、问话，日常细节即线索。

## (4) 人物弧光

- 主角多为侦探或局外人：越查越深、越接近真相越无力。弧光不是成长而是醒悟——明白自己一直被利用，明白真相无法改变什么。对手是系统本身：水权、土地、家族，腐败是一整套制度。

## (5) 类型套路与创新

- 新黑色电影 / 剧情片 / 喜剧剧情片。他遵守黑色电影的调查与宿命套路，但打破了“侦探总能破案”的成见：真相揭开之时就是悲剧来临之时。创新在 withheld exposition（扣住说明）——剧本宁愿让观众困惑，也不提前解释。禁套路：几乎不用直白的解释，不写大团圆。

## (6) 该写什么 / 不该写什么

- 该写：多线调查、层层揭开的真相、以回避暴露人物的对白、洛杉矶即腐败系统、侦探学到真相时为时已晚。
- Negative prompt: `No on-the-nose exposition, no clear-cut hero, no sentimental happy ending, no direct moralising, no explained motive`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Robert Towne, a private detective buys oden at a convenience store late at night in a modern city. He asks three questions and gets three evasions. The steam, the fluorescent light, the city outside. The truth is withheld until the last line. Dialogue only. No exposition.`
- 中文对照：罗伯特·汤恩风格：一位私家侦探深夜在现代城市的便利店买关东煮，问了三个问题，得到三句回避。蒸汽、荧光灯、店外的城市。真相一直扣到最后一句。只有对白，没有说明。
- Negative: `No on-the-nose exposition, no clear motive, no sentimental ending, no direct moralising, no explained truth`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
