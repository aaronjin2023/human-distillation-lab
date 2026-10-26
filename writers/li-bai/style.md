# Li Bai — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Bai: soaring seven-character song-lines, wine and moon, hyperbole and free flight, ecstasy that breaks all measure`
- ZH: 李白风格：纵逸的七言歌行，酒与月，夸张与飞举，逸兴破一切格律。

## (2) 句式与节奏

- 七言歌行纵逸：长短句交错、换韵自由、排比如瀑；五言绝句则极简极静；节奏忽快忽慢，如醉如醒。`impression`

## (3) 词汇与意象

- 词汇：词域：月、酒、江河、山岳、云、仙、剑、风；多用夸张数词（千、万、九天）与天体意象；口语与典雅并存。`impression`
- 意象：月、酒、长江、黄河、蜀道、仙境、飞瀑；意象群的核心是“大”与“高”——天上、人间一线牵。`impression`
- 禁词/禁意象：不用沉郁的琐碎写实、不用拘谨的格律束缚、不写市井的精打细算、不作冷峻的社会批判。

## (4) 叙事视角与结构

- 视角：第一人称狂放主体：我是谪仙、我是酒徒、我是行者；视角随想象飞升，不设全知旁观。`impression`
- 结构：歌行：起笔突兀（“君不见”）、中段纵笔铺陈、结尾陡然抒怀；绝句：起承转合一气呵成，结尾留白。`verbatim`
- 对话：诗中无人称对话；以呼告（“君不见”“与君歌一曲”）与独白代对话。

## (5) 语气与距离

- 语气：豪放、洒脱、飘逸；与读者如对饮，与天地如故交；悲而不沉，醉而不乱。`impression`（学界通说：飘逸与豪放）

## (6) 该写什么 / 不该写什么

- 该写：月酒江河、夸张飞举、七言歌行、君不见式起笔、飘逸收束。
- 不该写：沉郁琐碎、格律拘谨、市井算计、冷峻批判。
- Negative prompt: `No dreary minute realism, no cramped metrical restraint, no petty calculation, no cold social critique`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Li Bai, a small Yorkshire terrier sits on a subway seat. Seven-character song-lines, the dog as a little moon among commuters, wine replaced by steam, the train flying like a river. End with a free, soaring line.`
- 中文对照：李白风格：一只约克夏犬坐在地铁座位上。七言歌行，犬如月在人群中，热气代酒，列车如江河飞驰。结尾一笔飞举。
- Negative: `dreary realism, cramped metre, petty calculation, cold critique`
- 检验点：是否有夸张与飞举；月/酒意象是否转入现代场景；节奏是否纵逸而非拘谨。
