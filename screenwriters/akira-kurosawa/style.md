# Akira Kurosawa — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Akira Kurosawa: multiple truths of one event, weather as fate, a band of flawed men against impossible odds, humanism in the rain and mud`
- ZH: 黑泽明风格：同一件事的多个真相，天气即命运，一群有缺陷的人对抗不可能的 odds，雨与泥里的人道主义。

## (2) 结构：三幕 / 序列 / 节拍

- 群像史诗三幕：第一幕一个村庄或一桩命案切入，多方登场；第二幕多视角复述同一事件（《罗生门》）或招募与备战（《七武士》），中点是真相的崩塌或队伍的成型；第三幕决战或审判，收束在幸存者的凝视。时间跨度数日至数年，多用天气分段。

## (3) 对话

- 对白直接、有力，带武士与农民的口语；人物用争吵暴露真相；潜台词是人性——每个人说的都是自己的真相。动作描写多写天气、泥泞、决斗。

## (4) 人物弧光

- 主角多为武士、农民、法官，弧光是从自利到担当：不是变圣人，是终于为别人站一次。人物关系是七人小队或四方证人；结局人物不全胜，只活下去。

## (5) 类型套路与创新

- 类型：武士片与法庭悬疑；遵守套路——招募、决战、多视角；打破的一条是：真相不唯一，人性不黑白。创新在剧本层面：把多视角复述写成结构，让天气成为命运的角色。禁套路：不用单一真相，不用英雄主义独白，不用说教收尾。

## (6) 该写什么 / 不该写什么

- 该写：多视角复述同一事件、招募与决战、天气即命运、有缺陷的群像、幸存者的收束。
- 不该写：单一真相、英雄主义独白、说教式收尾、直白的道德结论、让天气只当背景。
- Negative prompt: `No single truth, no heroic monologue, no preachy ending, no direct moral verdict, no weather as mere background`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `In the style of Akira Kurosawa, four people buy oden at the same convenience store late at night and each tells a different story about what happened. Rain outside. No one agrees on the truth.`
- 中文对照：黑泽明风格：四个人深夜在同一家便利店买关东煮，各自讲了一个不同的版本，外面下着雨，没有人对真相达成一致。
- Negative: `No single truth, no heroic monologue, no preachy ending, no direct moral verdict`
- 检验点：结构、对话、人物弧光是否符合第 (2)–(5) 节；Negative 清单是否守住。
