# Fernanda Montenegro — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fernanda Montenegro: restrained Brazilian stage craft, weathered face that carries a whole life, low steady voice, silence as the loudest line, dignity without sentimentality`
- ZH: 费尔南达·蒙特内格罗风格：克制的巴西舞台功底，一张写满一生的脸，低沉平稳的声音，沉默是最响的台词，尊严而不煽情。

## (2) 形体

- 站姿挺直、步伐缓慢而有分量；手势极少，一抬手即有分量；坐姿端正、双手交叠；舞台上以后排可读的形体放大，电影里则收至最小。`impression`

## (3) 台词

- 低沉、平稳、带巴西葡萄牙语的柔和尾音；语速慢、停顿长；台词不靠音量靠重量，关键句几乎是耳语；沉默使用频繁。`impression`

## (4) 表情与眼神

- 皱纹即表演：不靠夸张表情，靠面部肌肉的细微收放；眼神直视、含泪而不落泪；笑极少，一笑即是转折。`impression`

## (5) 角色类型

- 常演角色：坚韧的底层女性（《中央车站》朵拉）；母亲/祖母（《甜蜜的母亲》）；舞台古典角色（巴西舞台剧目）。
- 类型突破：晚年以《中央车站》走向国际，70 岁后仍演主角；从舞台女王转为电影中的底层老妇，表演尺度由大收小。`artifact`
- 禁演类型：几乎不演煽情的哭戏、不演夸张的喜剧、不演依赖外貌的年轻主角。`impression`

## (6) 该演什么 / 不该演什么

- 该演：低沉平稳的台词、长停顿与沉默、写满一生的面部、缓慢而有分量的步态、尊严而不煽情。
- 不该演：煽情的哭戏、夸张的表情与手势、快速的插科打诨、依赖外貌的表演。
- Negative prompt: `No sentimental weeping, no exaggerated expressions, no broad gestures, no fast comic patter`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Fernanda Montenegro, an old woman buys oden at a convenience store late at night, slow steps, low steady voice, long silences, dignity without sentimentality`
- 中文对照：费尔南达·蒙特内格罗风格：一位老妇深夜在便利店买关东煮，步伐缓慢，声音低沉平稳，长久的沉默，尊严而不煽情。
- Negative: `No sentimental weeping, no exaggerated expressions, no broad gestures, no fast comic patter`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
