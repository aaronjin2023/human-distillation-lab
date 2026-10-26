# Herman J. Mankiewicz — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Herman J. Mankiewicz: literate newspaper wit turned into screenplay, cynical epigrams, flashback mosaic, dialogue as a weapon, a great man taken apart piece by piece`
- ZH: 赫尔曼·J·曼凯维奇风格：报人机智写成的剧本，愤世嫉俗的警句，闪回拼贴，对白即武器，一个伟人被一片片拆解。

## (2) 结构：三幕 / 序列 / 节拍

- 非线性拼贴结构：《公民凯恩》以讣告开场，多位叙述者各自闪回，真相在碎片之间浮现而非被揭开。三幕被打散成证词与回忆的序列，时间跳跃靠一句台词过渡。其他作品则多用经典三幕，但同样以一场晚宴、一场审判式的聚会收束众人。

## (3) 对话

- 对白是报纸专栏式的机锋：长句、典故、双关与刻薄的俏皮话，人物用语言互相拆台。潜台词占比极高——人物说的永远不是心里想的。独白少，群戏多，一场戏常常是六七个人轮流开火。

## (4) 人物弧光

- 主角多为大人物：报业大王、棒球英雄、名流。弧光是拆解而非成长——从神坛上一步步走下来，结尾不是悔悟而是孤独。对手是主角自己的野心与过去，制度只是背景。

## (5) 类型套路与创新

- 传记片 / 讽刺喜剧 / 剧情片。他遵守传记片的史诗跨度，但打破了“伟人传记要歌颂”的套路：把伟人写成谜、写成碎片。创新在多视角闪回结构——剧本本身就是一次调查。禁套路：几乎不用直白的心理独白，不写煽情的救赎结尾。

## (6) 该写什么 / 不该写什么

- 该写：多视角闪回与拼贴结构、报人式的机锋与警句对白、伟人拆解：神坛上的人物一片片剥落、群戏中的轮流开火与互相拆台。
- Negative prompt: `No sentimental redemption, no direct psychological monologue, no linear hero biography, no on-the-nose moral, no single trustworthy narrator`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Herman J. Mankiewicz, a retired newspaper tycoon buys oden at a convenience store late at night. Three witnesses remember him three different ways. Witty epigrammatic dialogue, flashback mosaic, no single trustworthy narrator. He leaves alone, and the last line is a joke that lands like an epitaph.`
- 中文对照：赫尔曼·J·曼凯维奇风格：一位退休的报业大亨深夜在便利店买关东煮，三位目击者用三种不同的方式记得他。对白机锋警句，闪回拼贴，没有可信的单一叙述者。他独自离开，最后一句玩笑像一句墓志铭。
- Negative: `No sentimental redemption, no direct psychological monologue, no linear hero biography, no on-the-nose moral, no single trustworthy narrator`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
