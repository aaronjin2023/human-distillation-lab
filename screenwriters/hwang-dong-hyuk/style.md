# Hwang Dong-hyuk — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hwang Dong-hyuk: a children's game turned into a class allegory, melodrama with a knife's edge, ordinary people forced to choose, the system as the real villain`
- ZH: 黄东赫风格：儿童游戏翻成阶级寓言，情节剧带着刀锋，普通人被迫选择，制度才是真正的反派。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧生存游戏：《鱿鱼游戏》每集一轮游戏，单集以游戏规则为骨架，季弧以人物选择为节点；《熔炉》三幕法庭结构，时间跨度数月。闪回揭示人物过去，游戏即结构。

## (3) 对话

- 对白直接、情绪饱满，人物用争吵、哀求、沉默交锋；潜台词少，处境本身即潜台词。动作描写细致（游戏规则、肢体、眼神），对白与动作互相印证。旁白不用。

## (4) 人物弧光

- 主角多为负债的普通人：成奇勋、教师，弧光是被迫选择后的崩塌或觉醒；人物越赢越失去，结尾常是苦涩的胜利。人物关系以同伴与制度的对照为主。

## (5) 类型套路与创新

- 类型：生存游戏 / 社会寓言。遵守‘游戏必有规则’的套路，打破‘游戏只为刺激’的成见：游戏即阶级。创新在把儿童游戏写成阶级寓言，把情节剧写进类型片。

## (6) 该写什么 / 不该写什么

- 该写：儿童游戏作阶级寓言、被迫的选择、情节剧的刀锋、制度作反派、苦涩的胜利。
- 不该写：脸谱化坏人、直白说教、类型化动作桥段、大团圆、无代价的胜利。
- Negative prompt: `No cartoon villain, no direct preaching, no action cliché, no happy ending, no cost-free victory`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Hwang Dong-hyuk, a man buys oden at a convenience store late at night with his last coins. A stranger offers him a game: win and eat free, lose and leave hungry. The game is simple. The choice is not.`
- 中文对照：黄东赫风格：一个男人深夜用最后几枚硬币在便利店买关东煮。陌生人邀他玩个游戏：赢了免费吃，输了饿着走。游戏很简单。选择不简单。
- Negative: `No cartoon villain, no direct preaching, no action cliché, no happy ending, no cost-free victory`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
