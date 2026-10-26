# Wisława Szymborska — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wisława Szymborska: ironic clarity, a small question that undoes a big certainty, the ordinary looked at until it becomes strange, nothing twice, history from the side`
- ZH: 辛波斯卡风格：反讽的清晰，一个小问题拆解一个大确定性，日常被注视到变得陌生，什么都不发生两次，历史从侧面看。

## (2) 句式与节奏

句长：诗行短促、凝练，问句与短句交替；一首诗常以一个日常问题开始，以一个反讽的收束结束。节奏：轻快、精确，不拖泥带水；靠问句的推进而非叙事推进。韵律：早期格律工整，晚期转向自由的口语节奏。`impression`

## (3) 词汇与意象

词汇：波兰语日常词（土豆、石头、桥、雪人）与历史词（战争、数字、名单）并置；‘两次’‘可能’‘不知道’是核心词。意象群：石头（沉默的石头）、桥（历史之桥）、雪人（呼唤雪人）、数字（巨大的数目）；意象靠注视获得重量。禁词/禁意象：不用华丽的比喻堆砌，不用抽象的哲理议论，不用煽情的控诉。`verbatim`/`artifact`

## (4) 叙事视角与结构

视角：第一人称抒情‘我’直接提问，‘我’既是提问者也是被提问者；视角不切换，‘我’始终在场。结构：问句结构——一首诗即一个问题，问题比答案重要；开头多为一个日常细节，结尾多为反讽的收束。对话：诗中没有人物对话，只有‘我’与‘你’（读者、历史、石头）的独白式对话。`impression`

## (5) 语气与距离

语气：机智、反讽、带温柔的怀疑；与读者的距离是亲密而严肃的——像对一个朋友提问，读者被当作可以一起怀疑的‘你’。幽默是清澈的，悲悯藏在反讽之后。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一个小问题拆解一个大确定性；日常被注视到变得陌生；历史从侧面看；‘不知道’作为答案；反讽的收束。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No ornate metaphor, no abstract philosophising, no sentimental accusation, no flat reportage, no heroic rhetoric`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Wisława Szymborska, a letter to oneself ten years from now. Ironic clarity. A small question undoes a big certainty. Nothing happens twice. The ordinary looked at until it becomes strange. 'I don't know' as an answer.`
- 中文对照：辛波斯卡风格，一封写给十年后自己的信。反讽的清晰；一个小问题拆解一个大确定性；什么都不发生两次；日常被注视到变得陌生；‘不知道’作为答案。
- Negative: `ornate metaphor, abstract philosophising, sentimental accusation, flat reportage, heroic rhetoric`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
