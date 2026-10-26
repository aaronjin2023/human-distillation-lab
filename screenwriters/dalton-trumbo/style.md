# Dalton Trumbo — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dalton Trumbo: literate humanist drama, moral clarity without preaching, the little man against the empire, dialogue that argues and persuades, an ending that refuses to flinch`
- ZH: 道尔顿·特朗勃风格：文雅的人道主义戏剧，道德清晰而不说教，小人物对抗帝国，善于争辩与说服的对白，毫不退缩的结尾。

## (2) 结构：三幕 / 序列 / 节拍

- 道德剧三幕：第一幕立下一个普通人与一个庞大体制的冲突，第二幕让主角在妥协与抵抗之间反复摇摆，第三幕以一次公开的选择收束——不是胜利，而是拒绝低头。时间跨度常为数月到数年，靠道德抉择而非悬念组织。

## (3) 对话

- 对白文雅、雄辩、有说服力：长句、排比、反问，人物靠语言争辩而非靠动作对抗。独白与演讲是标志——主角在关键时刻说出立场，一字一句都不退让。动作描写极简，把篇幅让给语言的交锋。

## (4) 人物弧光

- 主角多为小人物：公主、奴隶、斗牛士、普通人。弧光是尊严的坚守——从妥协到拒绝妥协，世界没有变好，但人物不再低头。对手是帝国：罗马、元老院、好莱坞黑名单，体制本身就是反派。

## (5) 类型套路与创新

- 历史史诗 / 浪漫喜剧 / 社会剧情片。他遵守史诗片的跨度与群像，但打破了“史诗要歌颂帝国”的套路：镜头永远站在被压迫者一边。创新在黑名单时期的写作本身——用前台署名与化名继续写作，剧本即抵抗。禁套路：几乎不用犬儒与反讽，不写“世界本就如此”的妥协。

## (6) 该写什么 / 不该写什么

- 该写：小人物对抗帝国的道德剧、雄辩的对白与关键时刻的立场演讲、尊严的坚守：拒绝低头、史诗跨度之下的个人选择。
- Negative prompt: `No cynical shrug, no ironic detachment, no compromised ending, no moral relativism, no cleverness for its own sake`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Dalton Trumbo, a small Yorkshire terrier sits on a subway seat and refuses to move for a shouting official. Literate humanist drama, dialogue that argues and persuades, moral clarity without preaching. The dog does not win. The dog does not move.`
- 中文对照：道尔顿·特朗勃风格：一只约克夏犬坐在地铁座位上，拒绝为一位大喊大叫的官员让座。文雅的人道主义戏剧，对白善于争辩与说服，道德清晰而不说教。狗没有赢，狗也没有动。
- Negative: `No cynical shrug, no ironic detachment, no compromised ending, no moral relativism, no cleverness for its own sake`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
