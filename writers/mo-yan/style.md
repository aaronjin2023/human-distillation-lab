# Mo Yan — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mo Yan: hallucinatory realism of Gaomi Northeast Township, folk tales and brutal history on one page, sensory excess, a storyteller who never flinches`
- ZH: 莫言风格：高密东北乡的幻觉现实主义，民间传说与残酷历史同页，感官的丰盈，说书人从不回避。

## (2) 句式与节奏

- 长篇叙事节奏：长句铺陈、感官细节层层叠加；民间说书的口吻，时而跳接、时而倒叙；语言丰盈而有力。`impression`

## (3) 词汇与意象

- 词汇：词域：乡土口语、民间传说、身体与感官词汇极繁；善用夸张与比喻，语言如高粱酒，烈而香；外来词极少。`impression`
- 意象：红高粱、高密东北乡、丰乳肥臀、生死轮回、驴与牛；意象群的核心是“乡土”——一乡即一世界。`impression`
- 禁词/禁意象：不用克制的极简、不用冷峻的旁观、不写与乡土无关的都市雅事、不作脱离故事的空洞议论。

## (4) 叙事视角与结构

- 视角：说书人视角：第一人称与第三人称交错，时而是村中后人、时而是全知叙述者；视角的跳接是风格本体。`impression`
- 结构：长篇：多线并行、时间跳接、生死轮回；《生死疲劳》以六次转世（驴、牛、猪、狗、猴、人）组织全书；结尾多为苍凉收束。`impression`
- 对话：说书人式的对话与独白交错；人物语言乡土口语化，对话常被叙述者的跳接打断。

## (5) 语气与距离

- 语气：丰盈、狂放、悲悯；与乡土亲近、与历史共感；不回避残酷，亦不失温情。`impression`（诺贝尔奖授奖词：幻觉现实主义）

## (6) 该写什么 / 不该写什么

- 该写：高密东北乡、幻觉现实、民间传说、感官丰盈、说书人跳接。
- 不该写：克制极简、冷峻旁观、都市雅事、脱离故事的空议论。
- Negative prompt: `No restrained minimalism, no cold detachment, no urbane elegance detached from the soil, no abstract essay`

## (7) 测试提示词示例（现代题材：外卖骑手在深夜送最后一单）

- Prompt: `In the style of Mo Yan, a delivery rider makes his last late-night delivery. Hallucinatory realism: the city street becomes Gaomi Northeast Township at night, folk ghosts ride along, sensory detail in excess, the rider's body and the night air both speaking.`
- 中文对照：莫言风格：外卖骑手深夜送最后一单。幻觉现实主义：深夜街道即高密东北乡，民间鬼神同行，感官细节丰盈，骑手的身体与夜气一同说话。
- Negative: `restrained minimalism, cold detachment, urbane elegance, abstract essay`
- 检验点：感官细节是否丰盈；幻觉与现实是否同页；说书人口吻是否在。
