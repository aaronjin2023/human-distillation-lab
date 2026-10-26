# Yang Hansheng — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yang Hansheng: epic of ordinary people in wartime, a child's eyes on a cruel city, history told through a family's rooms, anger held back by restraint`
- ZH: 阳翰笙风格：战时普通人的史诗，孩子的眼睛看残酷的城市，历史通过一家人的房间来讲，愤怒被克制压住。

## (2) 结构：三幕 / 序列 / 节拍

- 史诗型多线：第一幕家庭或流浪儿切入，城市日常与战争阴影并行；第二幕苦难层层累积，中点是一次全家或全城的失去；第三幕不靠胜利收束，靠幸存者的凝视收束。时间跨度数年，多用时代事件作分段标记。

## (3) 对话

- 对白平实、带时代口语，儿童视角的台词天真而锋利；成人对白克制，愤怒藏在停顿里；潜台词是战争与贫穷——没说的比说的多。

## (4) 人物弧光

- 主角多为流浪儿与城市小家庭，弧光是从天真到看清：不是成长为英雄，是学会在残酷里活下去。人物关系是家庭、邻里与时代的三重挤压；结局不胜利，只幸存。

## (5) 类型套路与创新

- 类型：战时史诗与社会现实主义；遵守套路——流浪、家庭、时代；打破的一条是：用儿童视角写成人世界的残酷，不靠说教。创新在剧本层面：把城市空间（弄堂、码头、戏院）写成史诗的舞台。禁套路：不用英雄主义高潮，不用煽情独白，不用直白口号。

## (6) 该写什么 / 不该写什么

- 该写：战时城市与小家庭、流浪儿视角、时代事件作分段、克制的愤怒、幸存者的收束。
- 不该写：英雄主义高潮、煽情独白、直白口号、类型反转、让儿童说成人式政治台词。
- Negative prompt: `No heroic climax, no sentimental monologue, no direct slogan, no genre twist, no child speaking adult political lines`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Yang Hansheng, a street child buys oden at a convenience store late at night with coins begged all day. He watches the city through the window. No rescue, only survival.`
- 中文对照：阳翰笙风格：一个流浪儿深夜用讨了一天的硬币在便利店买关东煮，隔着窗户看城市，没有救援，只有活下去。
- Negative: `No heroic climax, no sentimental monologue, no direct slogan, no genre twist`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
