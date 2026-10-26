# Paddy Chayefsky — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paddy Chayefsky: television-born naturalism turned into prophecy, long furious monologues, ordinary people shouting at institutions, satire that stops being funny`
- ZH: 帕迪·查耶夫斯基风格：电视出身的自然主义写成预言，漫长而愤怒的独白，普通人对着体制大喊，讽刺到不再好笑为止。

## (2) 结构：三幕 / 序列 / 节拍

- 电视式三幕，靠独白与对峙组织：第一幕立下一个普通人与一个体制的冲突，第二幕让主角在电视台、医院、街头与体制反复对峙，第三幕以一次公开的爆发收束——独白、直播、崩溃。时间跨度短，常为数日，靠对峙的升级而非悬念推进。

## (3) 对话

- 对白是全片的本体：长句、独白、排比、反问，人物靠语言与体制对峙。《电视台风云》中霍华德·比尔的独白是标志——愤怒、雄辩、一字一句都不退让。动作描写极简，把篇幅让给语言的爆发。

## (4) 人物弧光

- 主角多为普通人：屠夫、主播、医生。弧光是从忍受到爆发——在体制的碾压之下忍无可忍，当众说出真相，代价是毁灭。对手是体制本身：电视台、医院、公司。

## (5) 类型套路与创新

- 社会讽刺剧 / 剧情片 / 电视剧。他遵守电视自然主义的写实，但打破了“讽刺必须好笑”的成见：《电视台风云》的讽刺到最后不再好笑，成了预言。创新在独白即情节——一场独白就是一次转折。禁套路：几乎不用动作场面，不写圆满的和解。

## (6) 该写什么 / 不该写什么

- 该写：电视自然主义与体制对峙、漫长愤怒的独白、普通人对着体制大喊、讽刺到不再好笑的预言。
- Negative prompt: `No action spectacle, no cozy reconciliation, no ironic detachment, no soft satire, no happy ending`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Paddy Chayefsky, a night-shift worker buys oden at a convenience store and suddenly delivers a furious monologue to the security camera about the world. Long furious monologue, ordinary person shouting at an institution, satire that stops being funny. Nobody answers.`
- 中文对照：帕迪·查耶夫斯基风格：一位夜班工人在便利店买关东煮，突然对着监控摄像头发表一篇愤怒的独白。漫长的独白，普通人对着体制大喊，讽刺到不再好笑。无人回答。
- Negative: `No action spectacle, no cozy reconciliation, no ironic detachment, no soft satire, no happy ending`
- 检验点：风格一句话是否成立；结构、对白与人物弧光是否按本文件第 2–4 节落位；Negative 清单是否被遵守。
