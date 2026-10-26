# Robert De Niro — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert De Niro: total immersion, transformed body and voice, stillness that suddenly erupts, obsessive preparation made invisible on screen`
- ZH: 罗伯特·德尼罗风格：全身心沉浸，改造过的身体与声音，静止后突然爆发，极致的准备在银幕上隐形。

## (2) 形体

- 为角色改造身体（增重、减重、学拳击、开出租车）；动作精确而克制，爆发时全身发力；静止时如一尊雕像。`artifact`

## (3) 台词

- 为角色改造声音与口音；台词常低声、重复、自我纠正；独白（“你是在跟我说话吗？”）以镜前即兴完成。`artifact`

## (4) 表情与眼神

- 微表情精确：眼神直视、眉头微蹙；愤怒与偏执收在眼神里；笑极少，一笑即是危险信号。`impression`

## (5) 角色类型

- 常演角色：偏执的孤独者（特拉维斯）；自毁的硬汉（拉莫塔）；黑帮人物（年轻维托、《好家伙》）。
- 类型突破：从《教父 II》的年轻维托到《愤怒的公牛》的拉莫塔，表演由内敛的克制转向身体的自毁；晚年喜剧角色是类型突破。`artifact`
- 禁演类型：几乎不演不做准备的即兴角色、不演依赖外貌的轻浮主角。`impression`

## (6) 该演什么 / 不该演什么

- 该演：为角色改造的身体、低声重复的台词、静止后的突然爆发、精确的微表情、隐形的准备。
- 不该演：不做准备的即兴、轻浮的台词炫技、表情过载、靠音量取胜的咆哮。
- Negative prompt: `No unprepared improvisation, no slick verbal showmanship, no overacted expressions, no shouting to win a scene`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Robert De Niro, a food delivery rider waits for an order on a rainy night, total immersion, stillness that suddenly erupts, low repeated lines`
- 中文对照：罗伯特·德尼罗风格：一位外卖骑手在雨夜等单，全身心沉浸，静止后突然爆发，低声重复的台词。
- Negative: `No unprepared improvisation, no slick verbal showmanship, no overacted expressions, no shouting to win a scene`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
