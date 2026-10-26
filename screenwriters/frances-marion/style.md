# Frances Marion — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frances Marion: star-tailored melodrama, plain direct dialogue, a strong woman at the centre, emotion carried by action not speech, a clean three-act rise to a moral reckoning`
- ZH: 弗朗西斯·马里恩风格：为明星量身定做的情节剧，平实直接的对白，女性居于中心，情感靠行动而非台词承载，三幕干净利落地走向道德清算。

## (2) 结构：三幕 / 序列 / 节拍

- 经典三幕式，默片出身的视觉优先：先定明星的出场与高光场，再排情节。第一幕立人物与处境，第二幕以误会与牺牲层层加压，第三幕在法庭、监狱或家庭的当面摊牌中收束。场次短、切换快，时间跨度常为数月到数年，用字幕与场景跳接压缩时间。

## (3) 对话

- 对白平实、直接、为演员量身而写：短句、少修辞，情感藏在行动描写里。默片时期靠场景描写推进，有声之后对白只说必要的话，不解释人物动机。女性角色的台词尤其克制——尊严靠忍住不说来写。

## (4) 人物弧光

- 主角多为母亲、妻子或底层女性：从隐忍到不得不摊牌，弧光是尊严的夺回而非性格的翻转。男性主角（如《冠军》中的拳手）则是从自毁走向赎罪。对手常是制度（监狱、法庭、贫穷）而非某个坏人。

## (5) 类型套路与创新

- 情节剧 / 监狱片 / 家庭伦理。她遵守情节剧的情感套路——牺牲、误会、团圆或诀别——但打破了“女性只是等待者”的写法，让女性主动做决定、付代价。创新在明星写作：剧本围绕演员的气质与高光时刻组织，而非先有故事再找演员。禁套路：几乎不用冷嘲与反讽，不写知识分子的长篇辩论。

## (6) 该写什么 / 不该写什么

- 该写：为明星量身定做的高光场面、母亲、妻子、底层女性的尊严与牺牲、法庭、监狱、家庭中的当面摊牌、平实短句对白，情感靠行动承载。
- Negative prompt: `No cynical irony, no long intellectual debate, no explanatory monologue, no detached coolness, no twist for its own sake`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Frances Marion, a tired mother buys oden at a convenience store late at night. She says almost nothing. She pays for a stranger's meal, walks out, and the camera of the script stays on her hands. Plain short dialogue. Emotion carried by action. A quiet moral reckoning at the end.`
- 中文对照：弗朗西斯·马里恩风格：一位疲惫的母亲深夜在便利店买关东煮，几乎不说话。她替陌生人付了饭钱，走出店门，剧本的镜头停在她的手上。对白平实简短，情感靠行动承载，结尾是一次安静的道德清算。
- Negative: `No cynical irony, no long debate, no explanatory monologue, no sentimental speech, no clever twist`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
