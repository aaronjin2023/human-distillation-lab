# Wisława Szymborska — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wisława Szymborska: a small wry question that undoes a big certainty, the onion and the stone, I don't know as a method, plain speech with a philosophical sting, nothing twice`
- ZH: 辛波斯卡风格：一个小小的反讽提问拆解一个大大的确定性，洋葱与石头，“我不知道”即方法，平实的语言带哲学的刺，没有什么会发生两次。

## (2) 意象

- 洋葱（层层剥开的自我）
- 石头（无言的物）
- 猫与地图（日常的哲学）
- 桥上的人（历史的旁观）
- 两次（《没有第二次》：无物重复）
- 禁意象：宏大的颂歌、华丽的修辞、直白的说教
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 自由体短行，句式简省、口语化；以提问推进，停顿即转折；《巨大的数目》以数字与日常并置；整体节奏轻快、反讽，晚期更简、更冷。

## (4) 语言密度与词汇

- 词汇：日常词极准（洋葱、石头、猫、地图），抽象词借日常物落地；善用反讽压缩意义，一问抵一节；禁词：宏大颂歌词、华丽形容词、直白说教词。

## (5) 结构习惯

- 单篇多以一物（洋葱、石头）起兴，提问—拆解—反讽收束；组诗以小问题推进，大确定性层层剥落；结尾多为反讽的翻转而非抒情收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 日常物的哲学提问
- “我不知道”的方法
- 反讽的翻转收束
- 小中见大的结构
- 不该写：
- 宏大颂歌与华丽修辞
- 直白说教
- 冗长铺陈
- 温情的安慰收束
- Negative prompt: `No grand panegyric, no ornate rhetoric, no direct preaching, no long explanatory passages, no sentimental consolation, no certainty without a question`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Wisława Szymborska, a small Yorkshire terrier sits on a subway seat at night. A small wry question about the dog, the onion of the commuters, I don't know as a method, plain speech with a philosophical sting, nothing twice.`
- 中文对照：辛波斯卡风格：一只约克夏犬深夜坐在地铁座位上。关于狗的一个小小的反讽提问，乘客们的洋葱，“我不知道”即方法，平实的语言带哲学的刺，没有什么会发生两次。
- Negative: `No grand panegyric, no ornate rhetoric, no preaching, no long passages, no sentimental consolation, no certainty without a question`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
