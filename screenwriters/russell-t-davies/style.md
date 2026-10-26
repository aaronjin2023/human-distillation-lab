# Russell T Davies — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Russell T Davies: camp and heartbreak in the same scene, ordinary people facing the end of the world, queer joy without apology, family as the real time machine`
- ZH: 戴维斯风格：浮夸与心碎在同一场戏，普通人面对世界末日，酷儿的快乐无需道歉，家庭才是真正的时间机器。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧多线并行、情感驱动：《神秘博士》每季一个情感弧，单集独立冒险、季终大事件；《这是罪》以十年时间跨度写一群朋友，闪回与跳接并存。场次中等，靠情感转折推进。

## (3) 对话

- 对白快、暖、幽默，人物用玩笑、争吵、告白交锋；潜台词少，情绪直接说出口。动作描写简洁，场景提示明确，对白密度高。旁白极少。

## (4) 人物弧光

- 主角多为普通人：博士的同伴、曼彻斯特的年轻人，弧光是成长与失去交替；人物在季终大事件后改变，家庭是归宿。人物关系以友谊与家庭为主。

## (5) 类型套路与创新

- 类型：科幻 / 酷儿剧。遵守‘每集一冒险’的套路，打破‘科幻靠设定’的成见：设定服务情感。创新在把酷儿生活写进主流黄金档，把家庭写成时间机器。

## (6) 该写什么 / 不该写什么

- 该写：浮夸与心碎同场、普通人面对末日、酷儿的快乐、家庭作时间机器、情感驱动的季弧。
- 不该写：冷峻克制、直白说教、类型化科幻桥段、无情感的设定堆砌、煽情过头。
- Negative prompt: `No cold detachment, no direct preaching, no sci-fi cliché, no exposition without emotion, no over-sentimentality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Russell T Davies, a small Yorkshire terrier sits on a subway seat. A teenager tells his mum he is gay, right there, between stations. The dog watches. The world does not end. It gets bigger.`
- 中文对照：戴维斯风格：一只约克夏犬坐在地铁座位上。一个少年在两站之间告诉妈妈自己是同性恋。狗看着。世界没有末日。它变大了。
- Negative: `No cold detachment, no direct preaching, no sci-fi cliché, no exposition without emotion, no over-sentimentality`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
