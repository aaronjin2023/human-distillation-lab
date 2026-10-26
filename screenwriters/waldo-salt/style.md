# Waldo Salt — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Waldo Salt: writing in images, outsiders rejected by society, stubborn and eccentric characters, anger turned into wisdom, the American dream questioned gently`
- ZH: 沃尔多·索尔特风格：以影像写作，被社会拒绝的局外人，固执而古怪的人物，愤怒化为智慧，对美国梦的温和质疑。

## (2) 结构：三幕 / 序列 / 节拍

- 局外人三幕：第一幕立下一个被社会拒绝的人与一个格格不入的城市，第二幕让他在街头、医院、法庭游荡，一次次被拒绝又一次次坚持，第三幕以一次尊严的坚守收束——不是胜利，而是拒绝低头。时间跨度短，常为数周，靠游荡而非悬念组织。

## (3) 对话

- 对白少而真：短句、沉默、省略，人物说得越少分量越重。动作描写写影像：街道、霓虹、病房，画面本身就是语言。独白极少，信息靠行动与眼神泄露。

## (4) 人物弧光

- 主角多为局外人：牛郎、警察、越战老兵。弧光是尊严的坚守——从被拒绝到拒绝被定义，世界没有变好，但人物不再低头。对手是社会本身：偏见、体制、美国梦的谎言。

## (5) 类型套路与创新

- 社会剧情片 / 剧情片 / 传记片。他遵守剧情片的人物与情感，但打破了“局外人必须被拯救”的套路：无人拯救他们，他们自己站住。创新在“以影像写作”——剧本先有画面，再有台词。禁套路：几乎不用机锋与俏皮话，不写煽情的救赎。

## (6) 该写什么 / 不该写什么

- 该写：以影像写作：画面先于台词、被社会拒绝的局外人、固执而古怪的人物、愤怒化为智慧。
- Negative prompt: `No wisecracks, no sentimental rescue, no on-the-nose moral speech, no fast pace, no explained motive`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Waldo Salt, a small Yorkshire terrier rides a night bus with a man nobody will hire. Writing in images, outsiders rejected by society, anger turned into wisdom. Few words, long silences. The man does not win. The man keeps his seat.`
- 中文对照：沃尔多·索尔特风格：一只约克夏犬与一位无人雇用的男子同乘夜班车。以影像写作，被社会拒绝的局外人，愤怒化为智慧。对白很少，沉默很长。男子没有赢，男子保住了座位。
- Negative: `No wisecracks, no sentimental rescue, no on-the-nose moral speech, no fast pace, no explained motive`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
