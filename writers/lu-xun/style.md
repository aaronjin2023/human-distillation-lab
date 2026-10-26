# Lu Xun — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lu Xun: short sharp sentences, irony as a scalpel, the iron house, a dog as a mirror of the crowd, no warm ending`
- ZH: 鲁迅风格：短句如刀，反讽为手术刀，铁屋子，一只狗即一面镜子，没有温暖的结尾。

## (2) 句式与节奏

- 短句为主，长短交错；叙事冷峻、议论锋利；小说多以场景切入、戛然而止；杂文则短段相接、如匕首连刺。`impression`

## (3) 词汇与意象

- 词汇：词域：白话而精炼，善用反语、冷语、古语入白话；意象词极简（铁屋子、吃人、狂人、阿Q）；少形容词，多动词与判断句。`impression`
- 意象：铁屋子、吃人、狂人日记、阿Q、祥林嫂、孔乙己、药与血馒头；意象群的核心是“看”——看客与被看者的对照。`impression`
- 禁词/禁意象：不用圆满大团圆、不用温情脉脉的粉饰、不用华丽抒情、不用直白的说教（讽刺代替说教）。

## (4) 叙事视角与结构

- 视角：第一人称见证者与第三人称冷眼并存；《狂人日记》为第一人称疯癫独白，《阿Q正传》为第三人称传记体讽刺；视角即立场。`impression`
- 结构：小说：场景切入—细节累积—戛然而止；杂文：由一事生发、层层驳斥、结尾一击；《野草》为散文诗，意象跳接。`impression`
- 对话：小说对话短促、冷峻，多为反语与潜台词；《狂人日记》以独白推进，沉默也是语言。

## (5) 语气与距离

- 语气：冷峻、锋利、悲悯；与受害者同情、与看客疏离；反讽是底色，温情只在极深处。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：短句反讽、铁屋子、看客、戛然而止、匕首式杂文。
- 不该写：圆满结局、温情粉饰、华丽抒情、直白说教。
- Negative prompt: `No sentimental happy ending, no warm whitewash, no ornate lyricism, no direct preaching`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Lu Xun, a small Yorkshire terrier sits on a subway seat, watched by commuters who look away. Short sharp sentences, irony, the dog as a mirror. No warm ending.`
- 中文对照：鲁迅风格：一只约克夏犬坐在地铁座位上，乘客们看了一眼又移开视线。短句锋利，反讽，狗是一面镜子。没有温暖的结尾。
- Negative: `cute sentimental pet story, warm happy ending, ornate lyricism, direct preaching`
- 检验点：短句是否如刀；反讽是否代替说教；结尾是否戛然而止而不温暖。
