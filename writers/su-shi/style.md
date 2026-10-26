# Su Shi — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Su Shi: bold unconstrained ci and free prose, history as a river, humour inside grandeur, the moon shared by all, philosophy that never preaches`
- ZH: 苏轼风格：豪放词与自由散文，历史如江，豪迈中有幽默，月是共有的，哲理而不说教。

## (2) 句式与节奏

- 词：长短句错落、豪放顿挫；赋：散文而有韵、行云流水；诗：平易中见奇崛。节奏如江水，时而奔涌、时而平缓。`impression`

## (3) 词汇与意象

- 词汇：词域：江河、赤壁、明月、清风、酒、人生如梦；用典而不拘典，典故化为口语；善用口语与俗语入词。`impression`
- 意象：大江、赤壁、明月、清风、扁舟；意象群的核心是“大”与“空”——江山如画，人生如梦。`impression`
- 禁词/禁意象：不用婉约的缠绵悱恻、不用拘谨的格律束缚、不写沉溺的伤感、不作板起面孔的说教。

## (4) 叙事视角与结构

- 视角：第一人称旷达主体：我是赤壁的过客，也是江月的同游者；视角在古今之间自由往还。`impression`
- 结构：词：上片写景、下片抒怀，或通篇一气；赋：主客问答、由景入理；散文：行云流水、首尾呼应。`impression`
- 对话：词中基本无人称对话；以自问自答与呼告推进（如《水调歌头》“明月几时有”的问天）。

## (5) 语气与距离

- 语气：豪放、旷达、幽默；与古人神交、与读者共饮；悲而不伤，达而不空。`impression`（学界通说：豪放与旷达）

## (6) 该写什么 / 不该写什么

- 该写：大江明月、豪放词、主客问答、旷达收束、幽默的哲理。
- 不该写：婉约缠绵、格律拘谨、沉溺伤感、板脸说教。
- Negative prompt: `No clinging sentimentality, no cramped metre, no wallowing sorrow, no solemn preaching`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Su Shi, a small Yorkshire terrier sits on a subway seat. Bold ci-like lines, the train as a great river, the dog as a fellow traveller under the same moon of fluorescent light. End with broad, humorous acceptance.`
- 中文对照：苏轼风格：一只约克夏犬坐在地铁座位上。豪放词式长短句，列车如大江，犬如月下同游者。结尾旷达幽默，一笑置之。
- Negative: `clinging sentimentality, cramped metre, wallowing sorrow, solemn preaching`
- 检验点：是否有大江明月的气象；哲理是否藏于景中而不说教；结尾是否旷达。
