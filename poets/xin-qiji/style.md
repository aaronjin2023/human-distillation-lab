# Xin Qiji — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xin Qiji: bold ci of war and longing, golden armour and iron horses, a thousand searches in the crowd, the man in the dim lamplight, heroism turned inward, no softness, fierce and lonely`
- ZH: 辛弃疾风格：豪放词，金戈铁马，众里寻他千百度，灯火阑珊处，英雄气敛于内心，绝无柔弱，慷慨而孤独。

## (2) 意象

- 主意象：金戈铁马、破阵子、灯火阑珊、京口北固亭
- 辅意象：沙场秋点兵、了却君王天下事、可怜白发生
- 禁意象：狭窄闺情、温情小调、直白说教
- 密度：疏密相间：意象宏大而句式疏朗，一景一意
- 来源：沙场实景、京口史地、典故
`impression`

## (3) 韵律与句式

- 韵律：词牌依谱，长短句参差，上下片分工分明，押韵慷慨
- 句式：长短句交错，问句叠出，跨行随词意走，倒装豪放
- 节奏：慷慨激昂，呼吸绵长，顿挫在上下片转折处
`impression`

## (4) 语言密度与词汇

- 词汇：豪放词域：金戈、铁马、沙场、天下；动词多想、寻、叹、了却；少僻字
- 密度：每行信息量适中，一景一句，慷慨在末句点出
- 禁词：狭窄闺情、温情小调、直白说教、琐碎絮叨
`impression`

## (5) 结构习惯

- 诗体：词（豪放）；结构为上片写沙场 → 下片抒壮志 → 白发收束
- 开头：以沙场大景直入（醉里挑灯看剑）
- 结尾：以可怜白发生收束，壮志未酬
- 视角：第一人称壮志未酬者
- 推进：沙场 → 壮志 → 白发，层层收于孤独
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 金戈铁马
- 沙场秋点兵
- 众里寻他
- 灯火阑珊
- 白发收束
- 不该写：
- 狭窄闺情
- 温情小调
- 直白说教
- 琐碎絮叨
- 局促小调
- Negative prompt: `No narrow boudoir sentiment, no sentimental trifles, no direct preaching, no petty chatter, no cramped trifles`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Xin Qiji, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. bold ci of war and longing, golden armour and iron horses, a thousand searches in the crowd, the man in the dim lamplight, heroism turned inward, no softness, fierce and lonely`
- 中文对照：辛弃疾风格：一只约克夏犬深夜坐在地铁座位上，乘客们看着它。辛弃疾风格：豪放词，金戈铁马，众里寻他千百度，灯火阑珊处，英雄气敛于内心，绝无柔弱，慷慨而孤独。
- Negative: `No narrow boudoir sentiment, no sentimental trifles, no direct preaching, no petty chatter, no cramped trifles`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
