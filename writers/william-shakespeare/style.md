# William Shakespeare — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shakespeare: blank verse and prose in counterpoint, soliloquy as thought itself, the world as stage, images that think, high and low in one scene, no single moral`
- ZH: 莎士比亚风格：无韵诗体与散文对位，独白即思想本身，世界即舞台，意象会思考，雅俗同场，不给单一道德。

## (2) 句式与节奏

- 句式：句长：无韵五音步（blank verse）长句与散文短句对位；独白长句绵延如思，市井人物用散文短句；排比、反问、双关密集。
- 节奏：节奏：五幕（第一对开本的编辑分法）的起伏——开场、冲突、突转、灾难、收束；独白是节奏的停顿，思想在此处停住、回旋、再起。

## (3) 词汇与意象

- 词汇：词汇：造词极多，意象群密集——王冠与疾病、眼睛与盲、海洋与风暴、戏剧与梦；双关是基本修辞。
- 意象：意象群：舞台与世界（All the world's a stage）、王冠与疾病、眼睛与盲目、风暴与荒原、梦与幽灵、时间与玫瑰。
- 禁词/禁意象：禁词/禁意象：不写单一道德说教，不用抽象概念代替意象，不写脱离人物的议论。

## (4) 叙事视角与结构

- 视角：叙事视角：舞台视角——人物各执一词，真相在对话与独白之间；独白不是旁白，是思想的现场；观众全知而人物不知，反讽由此而生。
- 结构：结构：五幕剧（分法见 1623 年第一对开本），喜剧以婚礼收束、悲剧以死亡收束、历史剧以王权更替收束；独白与旁白穿插，时间可压缩、可跳跃；十四行诗则为十四行定式。

## (5) 语气与距离

- 语气：语气：庄重与戏谑并置，悲悯与反讽并存；与人物的距离如导演——爱他们，也让他们自毁。

## (6) 该写什么 / 不该写什么

- 该写：该写：独白、意象的思考、雅俗同场、双关、世界即舞台。
- 不该写：不该写：单一道德说教、抽象议论、脱离人物的抒情。
- Negative prompt: `No single moral sermon, no abstract digression detached from character, no flat didacticism`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Shakespeare, a letter to oneself ten years from now. Blank verse and prose in counterpoint. A soliloquy that thinks aloud. The world as stage. Images that think.`
- 中文对照：莎士比亚风格，一封写给十年后自己的信。无韵诗体与散文对位，独白即当场思考，世界即舞台，意象会思考。
- Negative: `single moral sermon, abstract digression, flat didacticism`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
