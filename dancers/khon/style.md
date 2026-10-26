# Khon — 舞蹈风格规格 style.md（给视频模型）

> 只描述舞蹈，不描述人生。引用演出录像时注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Khon: Thai classical masked dance-drama, stylised gestures, masked demons and monkeys, acrobatic Hanuman leaps, piphat music, the stage as a temple mural come alive, no ballet line`
- ZH: 泰国孔剧风格：泰国古典面具舞剧，程式化手势，戴面具的魔王与猴子，哈努曼的杂技跳跃，皮帕音乐，舞台即活过来的庙宇壁画，不取芭蕾线条。

## (2) 动作语汇

- 面具：魔王、猴子等角色戴面具，面部表情由面具承担。`artifact`
- 程式化手势：手势语体系严密，一个手势即一个词。`artifact`
- 哈努曼的跳跃：猴王角色的杂技跳跃与翻滚是奇观。`artifact`
- 皮帕音乐：泰式宫廷乐队实时伴奏，动作与鼓点对应。`artifact`

## (3) 身体线条与空间调度

- 身体线条：线条程式化，躯干直、手势成角；猴子角色屈身跳跃，魔王角色体量庞大；重心可高可低，随角色而变。`impression`
- 空间调度：群舞铺陈史诗场面，角色分区明确；猴子群舞满台跳跃，神与魔王对峙；视线在面具与跳跃之间流动。`impression`

## (4) 节奏与音乐关系

- 节奏：跟皮帕音乐走，鼓点与动作一一对应；猴子段落快而杂技，神的段落慢而庄严；节奏随角色切换。`impression`

## (5) 情绪表达

- 情绪：庄严、滑稽、奇观同体；情绪靠面具与身体的对照传达，猴子滑稽、神庄严、魔王威严。`impression`

## (6) 该编什么 / 不该编什么

- 该编：泰国孔剧的面具与程式化手势、哈努曼的杂技跳跃、皮帕音乐下的精确节奏、神魔对峙的群舞场面、庙宇壁画般的造型。
- 不该编：no ballet pointe work, no unmasked facial acting for masked roles, no improvised gestures outside the system, no Western theatrical mime, no realistic everyday movement。
- Negative prompt: `no ballet pointe work, no unmasked facial acting for masked roles, no improvised gestures outside the system, no Western theatrical mime, no realistic everyday movement`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Khon, a person buys oden at a convenience store late at night, Thai classical masked dance-drama, stylised gestures, masked demons and monkeys, acrobatic Hanuman leaps, piphat music, the stage as a temple mural come alive, no ballet line`
- 中文对照：按上述英文提示词，以该舞蹈家风格编排该现代题材。
- Negative: `no ballet pointe work, no unmasked facial acting for masked roles, no improvised gestures outside the system, no Western theatrical mime, no realistic everyday movement`
- 检验点：动作语汇是否对；身体线条与空间调度是否对；节奏与情绪是否对；禁区写法是否出现。
