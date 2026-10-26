# Charles Baudelaire — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Baudelaire: spleen and ideal, beauty drawn from evil, correspondences between senses, the city as hell and heaven, the sonnet as a jewel box`
- ZH: 波德莱尔风格：忧郁与理想，从恶中提炼美，感官的通感，城市既是地狱也是天堂，十四行诗如珠宝盒。

## (2) 句式与节奏

- 句式：句长：十四行诗句式工整，意象密集；散文诗则长句绵延，节奏如梦；短句只用在收束的警句处。
- 节奏：节奏：忧郁的缓慢与理想的升腾交替；十四行诗一节一转，散文诗一气呵成。

## (3) 词汇与意象

- 词汇：词汇：忧郁（spleen）、理想（idéal）、恶之花、通感词（香、色、声）、巴黎的街道与人群；爱用对立词对。
- 意象：意象群：恶之花、巴黎的街道、信天翁、猫、香水与音乐、深渊与天空。
- 禁词/禁意象：禁词/禁意象：不写田园的宁静，不用直白的说教，不写廉价的乐观。

## (4) 叙事视角与结构

- 视角：叙事视角：第一人称抒情我，直接对读者（hypocrite lecteur，伪善的读者）说话；我—你结构是全部。
- 结构：结构：《恶之花》以忧郁与理想、巴黎风光、酒、恶之花、反抗、死亡六辑构成；十四行诗为基本单位，散文诗为另一极。

## (5) 语气与距离

- 语气：语气：忧郁、炽热而挑衅；与读者的距离为零——直接指控。

## (6) 该写什么 / 不该写什么

- 该写：该写：忧郁与理想、通感、城市、十四行诗、从恶中提炼美。
- 不该写：不该写：田园宁静、直白说教、廉价乐观。
- Negative prompt: `No pastoral calm, no direct preaching, no cheap optimism, no formless free verse`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Baudelaire, a letter to oneself ten years from now. Spleen and ideal. Correspondences between senses. The city as hell and heaven. A sonnet's precision.`
- 中文对照：波德莱尔风格，一封写给十年后自己的信。忧郁与理想，感官的通感，城市既是地狱也是天堂，十四行诗的精确。
- Negative: `pastoral calm, direct preaching, cheap optimism, formless free verse`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
