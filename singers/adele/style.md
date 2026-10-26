# Adele — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul-pop vocal in the style of Adele: rich smoky contralto, conversational verses exploding into powerhouse choruses, precise diction, controlled vibrato, heartbreak delivered with dignity and restraint`
- ZH: 阿黛尔风格：浓郁烟嗓女低音，口语化主歌炸裂为强力副歌，咬字精准，颤音克制，心碎以尊严与克制送出。

## (2) 音色与音域

- 音色：浓郁烟嗓的女低音，中低音区最有辨识度；主音色为饱满的胸声，辅音色为气声低语；禁音色为甜美圆润与花腔装饰。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音直接，收尾拖长或戛然而止；颤音克制而自然；《Someone Like You》以钢琴伴奏下的克制主歌与副歌爆发为标记。`artifact`

## (4) 咬字与语言

- 咬字：英式伦敦口音，辅音清晰、元音开；重音落在情感词上；换气点留在句尾，停顿即表态。`artifact`

## (5) 节奏与即兴

- 节奏：灵魂流行节拍上拖拍，副歌常以长音推进；即兴以尾段加花为主，现场版常拉长高音。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 心碎抒情歌与灵魂流行歌曲（如《Someone Like You》一类）
- 克制主歌接强力副歌的能量对照
- 烟嗓中低音的叙事演唱
- 钢琴伴奏下的亲密独白
- 不该唱：`No sweet rounded pop tone, no operatic coloratura, no mumbled diction, no thin head voice, no flat monotone delivery`
- Negative prompt: `No sweet rounded pop tone, no operatic coloratura, no mumbled diction, no thin head voice, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：阳台上的绿植）

- Prompt: `Sing in the style of Adele, a song about plants growing on a balcony in a modern city. Rich smoky contralto, conversational verses exploding into powerhouse choruses, precise diction, controlled vibrato, heartbreak delivered with dignity and restraint.`
- 中文对照：阿黛尔风格：唱一首关于阳台绿植的歌。浓郁烟嗓女低音，口语化主歌炸裂为强力副歌，咬字精准，颤音克制，心碎以尊严与克制送出。
- Negative: `No sweet rounded pop tone, no operatic coloratura, no mumbled diction, no thin head voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
