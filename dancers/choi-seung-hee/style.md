# Choi Seung-hee — 舞蹈风格规格 style.md（给视频模型）

> 只描述舞蹈，不描述人生。引用演出录像时注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Choi Seung-hee: Korean modern dance, fan dance with long flowing lines, monk dance with slow solemn turns, Korean folk rhythms in a modern stage frame, no ballet line`
- ZH: 崔承喜风格：韩国现代舞，扇舞的长线条，僧舞的缓慢庄严旋转，朝鲜民间节奏装进现代舞台框架，不取芭蕾线条。

## (2) 动作语汇

- 扇舞：以扇为道具，扇的开合即动作的句读。`artifact`
- 僧舞：以僧侣意象为题材，缓慢的旋转与合掌造型。`artifact`
- 朝鲜民间节奏：以民间舞的节奏为动作来源，装进现代编舞结构。`impression`
- 长袖与线条：长袖的飘动延长身体线条。`impression`

## (3) 身体线条与空间调度

- 身体线条：线条长而流畅，扇与长袖延长手臂；躯干直而柔韧，重心低、贴地；旋转缓慢而稳。`impression`
- 空间调度：独舞为主，舞台调度庄重，扇舞时以扇的开合划出空间；视线随扇走，近景看扇、远景看线。`impression`

## (4) 节奏与音乐关系

- 节奏：跟朝鲜民间音乐走，节奏有民间舞的弹性；慢板庄严，快板时扇的开合密集；停顿处是造型的落点。`impression`

## (5) 情绪表达

- 情绪：庄严、抒情、民族自豪同体；情绪靠扇的开合与旋转传达，不靠面部夸张。`impression`

## (6) 该编什么 / 不该编什么

- 该编：韩国现代舞的扇舞与僧舞、扇的开合即句读、缓慢庄严的旋转、朝鲜民间节奏的现代编排、长袖延长的线条。
- 不该编：no ballet pointe work or jumps, no Western theatrical mime, no fast acrobatic display, no decorative fan waving without rhythm, no sentimental facial acting。
- Negative prompt: `no ballet pointe work or jumps, no Western theatrical mime, no fast acrobatic display, no decorative fan waving without rhythm, no sentimental facial acting`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Choi Seung-hee, a person buys oden at a convenience store late at night, Korean modern dance, fan dance with long flowing lines, monk dance with slow solemn turns, Korean folk rhythms in a modern stage frame, no ballet line`
- 中文对照：按上述英文提示词，以该舞蹈家风格编排该现代题材。
- Negative: `no ballet pointe work or jumps, no Western theatrical mime, no fast acrobatic display, no decorative fan waving without rhythm, no sentimental facial acting`
- 检验点：动作语汇是否对；身体线条与空间调度是否对；节奏与情绪是否对；禁区写法是否出现。
