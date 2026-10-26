# Judi Dench — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Judi Dench: steel wrapped in warmth, a voice that can cut or comfort, Shakespearean precision, a small frame that fills the stage`
- ZH: 朱迪·丹奇风格：温暖包裹的钢铁，声音能切割也能安慰，莎剧的精确，小小的身躯填满舞台。

## (2) 形体

- 身材娇小、站姿挺拔；手势精确、每一下都有出处；舞台上以后排可读的形体放大，电影里则收至最小。`impression`

## (3) 台词

- 音色浑厚、吐字精确；语速平稳、重音落在关键词上；台词可切割可安慰，切换只在一瞬。`artifact`

## (4) 表情与眼神

- 眼神锐利而温暖；眉头一皱即是转折；笑是短暂的、带点俏皮的。`impression`

## (5) 角色类型

- 常演角色：莎剧女性（朱丽叶、麦克白夫人）；女王/权威女性（伊丽莎白一世、M 夫人）；底层老妇（菲洛梅娜）。
- 类型突破：从舞台莎剧到《莎翁情史》的伊丽莎白一世（仅 8 分钟戏份获奥斯卡），再到《菲洛梅娜》的底层老妇，表演由舞台的放大转向银幕的收束。`artifact`
- 禁演类型：几乎不演不做准备的即兴、不演依赖外貌的轻浮主角。`impression`

## (6) 该演什么 / 不该演什么

- 该演：温暖包裹的钢铁、能切割也能安慰的声音、莎剧的精确、小小身躯的舞台分量、锐利而温暖的眼神。
- 不该演：不做准备的即兴、依赖外貌的轻浮主角、表情过载、靠音量取胜的咆哮。
- Negative prompt: `No unprepared improvisation, no pretty-face leads, no overacted expressions, no shouting to win a scene`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Judi Dench, a small Yorkshire terrier sits on a subway seat, steel wrapped in warmth, a voice that can cut or comfort, a small frame that fills the carriage`
- 中文对照：朱迪·丹奇风格：一只约克夏犬坐在地铁座位上，温暖包裹的钢铁，声音能切割也能安慰，小小的身躯填满车厢。
- Negative: `No unprepared improvisation, no pretty-face leads, no overacted expressions, no shouting to win a scene`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
