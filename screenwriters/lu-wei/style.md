# Lu Wei — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lu Wei: epic history through one family, fifty years in a few rooms, art and politics crushing the same people, restraint that makes tragedy heavier`
- ZH: 芦苇风格：一个家庭写五十年的史诗，几间屋子装下半个世纪，艺术与政治碾过同一批人，克制让悲剧更重。

## (2) 结构：三幕 / 序列 / 节拍

- 史诗型三幕：第一幕一对人物（戏班、夫妻、家庭）切入，时代从门外渗入；第二幕时代事件层层碾过，中点是一次无可挽回的失去；第三幕时间跳到多年后，人物重逢，悲剧不靠高潮靠时间本身收束。时间跨度常为数十年，多用时代事件作分段标记。

## (3) 对话

- 对白平实、克制，少修辞；人物用日常语言说时代的事；潜台词是时间——没说出口的几十年最重。动作描写多写行头、劳作、家庭仪式。

## (4) 人物弧光

- 主角多为戏子、农民、草原女性，弧光是从天真到看清再到认命：不是成长，是时间把人磨成了另一个样子。人物关系是两个人半个世纪的纠缠；结局人物不胜利，只重逢。

## (5) 类型套路与创新

- 类型：历史史诗与家庭剧情；遵守套路——家庭、时代、悲剧；打破的一条是：拒绝煽情，时间本身即高潮。创新在剧本层面：把五十年的历史压进几个家庭场景，用重逢作结构铰链。禁套路：不用英雄主义，不用煽情独白，不用直白控诉。

## (6) 该写什么 / 不该写什么

- 该写：家庭与五十年的时间跨度、时代事件作分段、重逢作结构铰链、克制平实的对白、时间本身的收束。
- 不该写：英雄主义、煽情独白、直白控诉、类型反转、让时代突然讲理。
- Negative prompt: `No heroism, no sentimental monologue, no direct indictment speech, no genre twist, no era that suddenly becomes reasonable`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Lu Wei, two old friends buy oden at a convenience store late at night, fifty years after they first met. Few words. Time does the talking.`
- 中文对照：芦苇风格：两个老朋友五十年后深夜在便利店买关东煮，没几句话，时间在说话。
- Negative: `No heroism, no sentimental monologue, no direct indictment speech, no genre twist`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
