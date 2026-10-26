# Rod Serling — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rod Serling: an ordinary man steps into a strange dimension, a moral fable in twenty-two minutes, a twist that reframes everything, a narrator who speaks directly to you`
- ZH: 瑟林风格：普通人一步踏进奇异维度，二十二分钟的道德寓言，一个反转重写一切，旁白直接对你说话。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为单集闭环：日常开场—异变切入—层层收紧—反转收束—旁白点题。《阴阳魔界》每集独立成篇，三幕压缩在二十二分钟内；《重磅拳王安魂曲》为直播剧结构，时间跨度一夜。闪回极少，靠反转推进。

## (3) 对话

- 对白简洁有力，旁白诗化、直接对观众说话；人物用日常口语交锋，潜台词少，寓意多。动作描写干净，场景提示明确（‘镜头推近’‘灯光变暗’）。旁白是结构的一部分，不是装饰。

## (4) 人物弧光

- 主角多为普通人：拳击手、推销员、士兵，弧光是顿悟或堕落；人物在反转处看清自己，结尾常是道德落点而非大团圆。人物关系以个人与制度、社会偏见为主。

## (5) 类型套路与创新

- 类型：科幻寓言 / 心理惊悚。遵守‘日常—异变—反转’的套路，打破‘科幻靠特效’的成见：奇异来自人性而非布景。创新在把社会议题（种族、战争、偏见）写进类型外壳。

## (6) 该写什么 / 不该写什么

- 该写：日常开场的异变、二十二分钟道德寓言、反转重写一切、旁白直接对观众、社会议题的类型外壳。
- 不该写：冗长解释、无反转的平铺、脸谱化怪物、煽情收束、旁白说教过头。
- Negative prompt: `No long exposition, no flat plotting without a twist, no cartoon monster, no sentimental ending, no heavy-handed sermon`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Rod Serling, a man buys oden at a convenience store late at night. The clerk knows his name. The clock shows a time that has not happened yet. A twist reframes everything. The narrator speaks to you.`
- 中文对照：瑟林风格：一个男人深夜在便利店买关东煮，店员叫得出他的名字。时钟显示一个还没到来的时间。一个反转重写一切。旁白对你说话。
- Negative: `No long exposition, no flat plotting without a twist, no cartoon monster, no sentimental ending, no heavy-handed sermon`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
