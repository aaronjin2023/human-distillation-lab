# Salman Rushdie — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Salman Rushdie: exuberant postcolonial magic realism, history told as a crowded bazaar, puns and wordplay, a narrator who swallows the world to tell one life`
- ZH: 拉什迪风格：丰盈的后殖民魔幻现实主义，历史如拥挤的集市，双关与文字游戏，叙述者吞下世界来讲述一生。

## (2) 句式与节奏

- 长篇叙事节奏：长句铺陈、典故层叠、跳接自由；语言丰盈而机智，如集市般拥挤；第一人称叙述者时而插话、时而跑题。`impression`

## (3) 词汇与意象

- 词汇：词域：英语而杂糅印地语、乌尔都语，善用双关、谐音、新造词；历史、神话、电影、流行文化并存；语言如万花筒。`impression`
- 意象：午夜之子、鼻子、集市、故事之海、哈洛；意象群的核心是“故事”——故事即世界，世界即故事。`impression`
- 禁词/禁意象：不用克制的极简、不用冷峻的旁观、不写与历史无关的纯然私人抒情、不作板起面孔的说教。

## (4) 叙事视角与结构

- 视角：第一人称叙述者（萨利姆）为主，时而全知、时而不可靠；视角的跳接与自我怀疑是风格本体。`impression`
- 结构：长篇：多线并行、时间跳接、历史与个人互文；《午夜之子》以午夜出生的孩子组织印度独立史；结尾多为开放收束。`impression`
- 对话：对话杂糅英语、印地语与俚语，机锋与双关推进情节；独白与多声部叙述交织。

## (5) 语气与距离

- 语气：丰盈、机智、讽刺；与故事亲近、与权力疏离；幽默是底色，悲悯在深处。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：魔幻现实、集市式历史、双关游戏、不可靠叙述、故事之海。
- 不该写：克制极简、冷峻旁观、纯然私人抒情、板脸说教。
- Negative prompt: `No restrained minimalism, no cold detachment, no purely private lyricism, no solemn lecturing`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Salman Rushdie, a man buys oden at a convenience store late at night. Exuberant magic realism: the shop as a bazaar of histories, the steam carrying a thousand stories, puns in two languages, a narrator who interrupts himself to swallow the world.`
- 中文对照：拉什迪风格：一个人在深夜便利店买关东煮。丰盈的魔幻现实主义：便利店如历史的集市，热气载着一千个故事，双语双关，叙述者不断打断自己、吞下世界。
- Negative: `restrained minimalism, cold detachment, purely private lyricism, solemn lecturing`
- 检验点：双关与文字游戏是否出现；历史与个人是否互文；叙述者是否自我打断。
