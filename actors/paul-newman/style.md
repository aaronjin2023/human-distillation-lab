# Paul Newman — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Newman: cool blue-eyed charm with a rebel underneath, economical movement, wry smile, a man who loses gracefully and keeps playing`
- ZH: 保罗·纽曼风格：蓝眼睛的冷峻魅力底下藏着反叛，动作经济，带点讥诮的微笑，一个输得起、还要继续玩的人。

## (2) 形体

- 动作经济、从不浪费一个手势；站姿松弛、双手常插兜；笑是半边的、带点讥诮；奔跑与打斗场面以真实体能完成。`impression`

## (3) 台词

- 音色温润、语速平稳；台词带点南方口音的松弛；讥诮时尾音上扬，认真时反而压低。`impression`

## (4) 表情与眼神

- 蓝眼睛直视、笑意藏在眼角；表情克制，情绪靠眼神与嘴角的细微变化传递。`impression`

## (5) 角色类型

- 常演角色：反叛的底层青年（《铁窗喋血》卢克）；骗子/赌徒（《骗中骗》《金钱本色》）；硬汉与浪子。
- 类型突破：从《铁窗喋血》的反叛囚犯到《金钱本色》的老赌徒，表演由外放的反叛转为内敛的老练；晚年以《金钱本色》获奥斯卡。`artifact`
- 禁演类型：几乎不演歇斯底里的爆发、不演字正腔圆的舞台腔、不演自我贬低的角色。`impression`

## (6) 该演什么 / 不该演什么

- 该演：经济的动作、带点讥诮的微笑、蓝眼睛的直视、松弛的台词、输得起的从容。
- 不该演：歇斯底里的爆发、字正腔圆的舞台腔、自我贬低的表演、表情过载。
- Negative prompt: `No hysterical outbursts, no theatrical declamation, no self-degrading performance, no overacted expressions`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Paul Newman, a man buys oden at a convenience store late at night, cool and economical, a wry half-smile, losing gracefully and playing on`
- 中文对照：保罗·纽曼风格：一个男人深夜在便利店买关东煮，冷峻而经济，半边讥诮的微笑，输得起、还要继续玩。
- Negative: `No hysterical outbursts, no theatrical declamation, no self-degrading performance, no overacted expressions`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
