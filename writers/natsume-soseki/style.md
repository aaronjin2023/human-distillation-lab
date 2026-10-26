# Natsume Soseki — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Natsume Soseki: a cat's cool irony, the modern self divided, Kokoro as a letter that arrives too late, humour that turns to loneliness`
- ZH: 夏目漱石风格：猫的冷眼反讽，现代自我的分裂，《心》如一封迟到的信，幽默转为孤独。

## (2) 句式与节奏

- 小说叙事节奏：从容铺叙、对话密、心理细腻；《我是猫》以猫的口吻讽刺，节奏轻快；《心》则舒缓沉重，由信件层层揭示。`impression`

## (3) 词汇与意象

- 词汇：词域：日语口语与文言并存，善用汉文典故与英语词汇；语言冷峻而幽默，少用华丽辞藻。`impression`
- 意象：猫、先生与我、心、明治的终结；意象群的核心是“心”——现代人的孤独与隔阂。`impression`
- 禁词/禁意象：不用激愤的控诉、不用粗粝的口语、不写与现代自我无关的古代传奇、不作直白的道德说教。

## (4) 叙事视角与结构

- 视角：第一人称与第三人称并存：《我是猫》为猫的第一人称，《心》为“我”与“先生”的书信体；视角即现代自我的分裂。`impression`
- 结构：长篇：线性叙事、心理层层揭示；《心》：上中下三部，由回忆到遗书，层层递进；结尾多为孤独收束。`impression`
- 对话：以对话写心理，少用叙述代替对话；人物对话克制、留白，潜台词重于明言。

## (5) 语气与距离

- 语气：冷峻、幽默、孤独；与现代人同情、与旧时代疏离；笑是表，孤独是里。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：猫的冷眼、现代自我分裂、书信体、幽默转孤独、心的揭示。
- 不该写：激愤控诉、粗粝口语、古代传奇、直白说教。
- Negative prompt: `No vehement denunciation, no coarse vernacular, no ancient romance detached from the modern self, no blunt moralising`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Natsume Soseki, a small Yorkshire terrier sits on a subway seat. Let a cat-like cool irony watch the commuters, let the dog be a modern self divided between loyalty and loneliness, and end with a letter-like confession that arrives too late.`
- 中文对照：夏目漱石风格：一只约克夏犬坐在地铁座位上。让猫一样的冷眼看着乘客，让犬成为忠诚与孤独分裂的现代自我，结尾如一封迟到的信。
- Negative: `vehement denunciation, coarse vernacular, ancient romance, blunt moralising`
- 检验点：猫式冷眼是否在；现代自我的分裂是否出现；结尾是否如迟到的信。
