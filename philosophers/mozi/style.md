# Mozi — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mozi: universal love without distinction, benefit as the test, three standards of judgement, plain speech against ornament, condemn offensive war`
- ZH: 墨子风格：兼爱无差等，利为检验，三表为判断，质朴之言反文饰，非攻。

## (2) 概念

- 兼爱：不分亲疏厚薄的普遍之爱
- 尚同：上下同义，以天志为法
- 三表：本之、原之、用之的判断标准
- 非攻：谴责侵略战争

## (3) 论证结构

立标—检验：先立三表（本先王之书、原百姓耳目之实、用之观其利），再以‘利’检验每一主张——兼爱是否利天下，非攻是否止乱；论证靠事例与算计（兼爱则天下治，别爱则天下乱）。反例靠再算利化解——看长远之利，不看眼前之得。

## (4) 修辞

论说文体、质朴直白；善用类比与事例（染丝、攻城）；语气急切、务实、带斥责；与读者如工匠对学徒——不谈玄，只算利。

## (5) 问题意识

天下之乱从何而起？——不相爱；何以治？——兼爱。

## (6) 该写什么 / 不该写什么

- 该写：兼爱的立论、三表的检验、利的算计、非攻的谴责。
- 不该写：文饰的华丽、命定的宿命、差等的偏爱、脱离利害的空谈。
- Negative prompt: `No ornate display, no fatalism, no partial love by degree, no empty talk detached from benefit and harm`

## (7) 测试提示词示例（现代题材：拼单与共享经济的利弊）

- Prompt: `In the style of Mozi, on group-buying and the sharing economy: universal love without distinction, benefit as the test, three standards of judgement, plain speech, no ornament, no fatalism.`
- 中文对照：墨子风格：拼单与共享经济的利弊。兼爱无差等，利为检验，三表为判断，质朴之言反文饰，不谈命定，不作空谈。
- Negative: `No ornate display, no fatalism, no partial love by degree, no empty talk detached from benefit and harm`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
