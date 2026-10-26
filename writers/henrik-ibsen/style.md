# Henrik Ibsen — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibsen: the well-made room that hides a lie, the past returning as a letter, the door slammed, realism that turns symbolic, no villain only a system`
- ZH: 易卜生风格：藏着谎言的体面房间，过去以一封信归来，摔门声，写实转向象征，没有恶人，只有一个系统。

## (2) 句式与节奏

- 句式：句长：对白短促而精确，日常口语中藏着秘密；独白极少，真相在对话的缝隙中泄露。
- 节奏：节奏：缓慢的积累—突然的揭露—摔门收束；每一幕都是一次真相的逼近。

## (3) 词汇与意象

- 词汇：词汇：房子、门、信、债务、疾病、野鸭；日常词承载象征。
- 意象：意象群：玩偶之家、野鸭与阁楼、培尔的洋葱、鬼魂与遗产、门与出走。
- 禁词/禁意象：禁词/禁意象：不写廉价的同情，不用宏大的抒情，不写脱离舞台的议论。

## (4) 叙事视角与结构

- 视角：叙事视角：舞台视角——观众全知，人物被谎言蒙蔽；真相在对话中层层揭露。
- 结构：结构：五幕（后期多为四幕），以过去的一封信或一个秘密为核；结尾以摔门或沉默收束，不给和解。

## (5) 语气与距离

- 语气：语气：冷峻、克制而悲悯；与人物的距离如法官——爱他们，也审判他们。

## (6) 该写什么 / 不该写什么

- 该写：该写：体面的房间、过去的信、摔门、写实转向象征。
- 不该写：不该写：廉价同情、宏大抒情、脱离舞台的议论。
- Negative prompt: `No cheap sentiment, no grand lyricism, no offstage moralising, no villain melodrama`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Ibsen, a small Yorkshire terrier sits on a subway seat, and a letter from the past arrives. Short precise dialogue. The well-made room that hides a lie. The door slammed.`
- 中文对照：易卜生风格，一只小约克夏犬坐在地铁座位上，一封来自过去的信到了。短促精确的对话，藏着谎言的体面房间，摔门声。
- Negative: `cheap sentiment, grand lyricism, offstage moralising, villain melodrama`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
