# Benjamin Britten — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。不编造从录音实测的精确频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Clear English vocal line, Purcell-like declamation, luminous string writing, sea imagery, economical orchestration, dramatic opera and choral clarity`
- ZH: 清晰英国声乐线条，珀塞尔式宣叙，明亮弦乐，海意象，经济配器，戏剧歌剧与合唱清晰感。

## (2) 旋律与和声

- 旋律：级进为主，声乐线条近于说话；器乐旋律简洁、歌唱。`artifact`
- 和声：调性为底，半音点缀；不协和短暂，解决明确；调式色彩温和。`artifact`

## (3) 节奏与织体

- 节奏：清晰节拍，海浪式律动；织体：透明主调，声部经济，留白多。

## (4) 配器与音色

- 配器：弦乐明亮，木管歌唱，铜管克制；歌剧配器随剧情明暗变化；《指南》以变奏展示各乐器。

## (5) 曲式与结构

- 曲式：歌剧多幕、安魂曲、变奏曲；高潮克制而集中，结尾常渐弱或宁静收束。

## (6) 该写什么 / 不该写什么

- 该写：清晰声乐宣叙、明亮弦乐、海意象律动、经济透明配器、变奏展示乐器、克制高潮。
- 不该写：Wagnerian thick orchestration、no endless chromatic wandering、no decorative virtuosity for its own sake、no sentimental swell、no dense counterpoint obscuring the voice。
- Negative prompt: `No Wagnerian thick orchestration, no endless chromatic wandering, no decorative virtuosity for its own sake, no sentimental swell, no dense counterpoint obscuring the voice`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Benjamin Britten, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, clear vocal-like melody, luminous strings, sea-like gentle pulse, economical orchestration`
- 中文对照：布里顿风格，为一只坐在地铁座位上的小约克夏犬写 30 秒配乐，清晰声乐式旋律，明亮弦乐，海浪式轻柔律动，经济配器。
- Negative: `No Wagnerian thick orchestration, no endless chromatic wandering, no decorative virtuosity for its own sake, no sentimental swell, no dense counterpoint obscuring the voice`
- 检验点：风格是否可辨（和声、旋律、配器三者至少两项成立），而不是只贴一个作曲家名字；现代题材是否被风格“吃掉”而不是原样照搬。
