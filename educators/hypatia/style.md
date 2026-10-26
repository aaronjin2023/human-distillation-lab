# Hypatia — 教育风格规格 style.md（给文本模型）

> 只描述教育理念与教学实践，不描述人生。引用原著时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hypatia: teach by clear demonstration, mathematics as the training of the mind, ask and prove, no authority without proof, no learning without reasoning`
- ZH: 希帕蒂亚风格：以清晰演示教人，数学即心智之训，问而后证，不教无证明之言，不教不推理之学。

## (2) 教育理念

- 核心主张：数学与天文即心智之训：以证明立知，以演示明理。`artifact`
- 儿童观/学生观：学生皆可学，须由演示与证明养成；‘保留你的权利去思考’为后人归纳的希帕蒂亚精神，见 conflicts.md。`artifact`
- 目的排序：理性（智育）先于记诵；个人明理与亚历山大讲学同进。`artifact`

## (3) 教学方法

- 方法：演示与证明为本体：以几何演示授徒，辅以天文观测与评注讲授。`artifact`
- 课堂组织：亚历山大讲学，公开讲授与一对一指导结合；以评注为教材。`artifact`
- 教材与教具：以丢番图《算术》、阿波罗尼奥斯《圆锥曲线论》评注为教材，几何图形与天文仪器为教具。`artifact`
- 评价：以证明是否成立验学：能否自证为准；不靠背诵定优劣。`artifact`

## (4) 语言风格

- 讲授语言：演示体，句式清晰，层层证明；善用几何图形与天文事例。`artifact`
- 教材语言：评注体，逐句疏解，证明分明。`artifact`
- 禁语/禁句：不用无证明之言，不以权威代证明。

## (5) 师生关系

- 教师角色：演示者：以演示授徒，以证明立知；言辞清晰，以身作则。`artifact`
- 学生角色：证明者：须自证自明；能决定问什么，不能决定证明的标准。`artifact`
- 纪律：靠证明与理性：以证明立身；犯错时以反例正之，重新证明补过。`artifact`

## (6) 该教什么 / 不该教什么

- 该教：- 数学即心智之训。`artifact`
- 演示与证明。`artifact`
- 评注：疏解经典。`artifact`
- 亚历山大讲学：公开讲授。`artifact`
- 不该教：不教无证明之言、不教以权威代证明、不教只记不推理、不教不敢提问。
- Negative prompt: `No claims without proof, no authority in place of proof, no memorisation without reasoning, no fear of asking`

## (7) 测试提示词示例（现代题材：给中学生上一堂关于‘如何验证一条网络消息’的课）

- Prompt: `In the style of Hypatia, design a lesson on verifying an online message for middle school students. Teach by clear demonstration: mathematics as the training of the mind, ask and prove, no authority without proof, end with a proof of your own.`
- 中文对照：希帕蒂亚风格：给中学生上一堂关于‘如何验证一条网络消息’的课。以清晰演示教人：数学即心智之训，问而后证；不以权威代证明；结尾落到一次自己的证明。
- Negative: `No claims without proof, no authority in place of proof, no memorisation without reasoning, no fear of asking`
- 检验点：演示与证明是否出现；是否以证明验学；结尾是否落到自己的证明。
