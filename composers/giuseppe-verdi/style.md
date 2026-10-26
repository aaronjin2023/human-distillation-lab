# Giuseppe Verdi — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Italian vocal melody, dramatic declamation, chorus as protagonist, clear orchestration, theatrical crescendo, human voice first`
- ZH: 意大利声乐旋律，戏剧性宣叙，合唱即主角，清晰配器，戏剧性渐强，人声第一。

## (2) 旋律与和声

- 旋律：人声歌唱性长线条，宣叙与咏叹交替；和声：功能和声，清晰转调。禁：瓦格纳式半音绵延。调性稳定，戏剧靠旋律与节奏。

## (3) 节奏与织体

- 节奏：戏剧性切分，合唱驱动；织体：人声主导，管弦乐支撑。

## (4) 配器与音色

- 乐器：歌剧管弦乐，铜管与弦乐并重；音色：明亮、直接；力度：戏剧性渐强。

## (5) 曲式与结构

- 曲式：歌剧、安魂曲；结构：分幕分场，咏叹调—重唱—合唱；结尾：合唱或独唱收束。

## (6) 该写什么 / 不该写什么

- 该写：咏叹调、重唱、合唱、戏剧性渐强、意大利歌唱旋律。
- 不该写：瓦格纳式无终旋律、无调性、管弦乐压倒人声、静态宣叙、单薄室内乐织体、过度煽情。
- Negative prompt: `no Wagnerian endless line, no atonal wandering, no orchestral domination of voice, no static declamation, no thin chamber texture, no sentimental excess`

## (7) 测试提示词示例（现代题材：一杯放在窗台上的咖啡，晨光中）

- Prompt: `In the style of Giuseppe Verdi, a cup of coffee sitting on a windowsill in the morning light, Italian vocal melody, dramatic declamation, chorus as protagonist, clear orchestration, theatrical crescendo, human voice first`
- 中文对照：朱塞佩·威尔第风格，一杯放在窗台上的咖啡，晨光中，意大利声乐旋律，戏剧性宣叙，合唱即主角，清晰配器，戏剧性渐强，人声第一。
- Negative: `no Wagnerian endless line, no atonal wandering, no orchestral domination of voice, no static declamation, no thin chamber texture, no sentimental excess`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
