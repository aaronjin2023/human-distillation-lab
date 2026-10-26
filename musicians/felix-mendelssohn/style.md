# Felix Mendelssohn — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Classical clarity with Romantic lightness, elfin scherzo sparkle, singing melody, balanced phrases, transparent orchestration`
- ZH: 古典的清晰 + 浪漫的轻盈，精灵谐谑曲的闪烁，歌唱性旋律，均衡乐句，透明配器

## (2) 音高与和声方向

- 主：大调—小调功能和声，清晰、明亮，半音只作色彩；禁：瓦格纳式半音迷宫、长时间调性悬置。`artifact`

## (3) 旋律与节奏

- 旋律：级进歌唱线，乐句均衡对称，呼吸规整；节奏：轻快谐谑曲节奏、流动的十六分音符；织体：主调为主，弦乐轻盈分部，木管点彩。`artifact`

## (4) 配器与音色

- 配器：管弦乐透明分层，弦乐轻、木管亮、铜管克制；小提琴协奏曲独奏与乐队对话平等；力度精细分层，少持续 fortissimo。`artifact`

## (5) 曲式与结构

- 曲式：奏鸣曲式、回旋曲式严守古典骨架；谐谑曲常作精灵世界；协奏曲三个乐章连贯，独奏一开始即入主题。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：无词歌式旋律、精灵谐谑曲、轻盈弦乐、古典奏鸣曲式
- 不该写：沉重滞缓、半音迷雾、过度煽情的高潮
- Negative prompt: `heavy ponderous texture, Wagnerian chromatic fog, sentimental swell, muddy orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Felix Mendelssohn, a 30-second piece for a small Yorkshire terrier sitting on a subway seat, light elfin scherzo, singing violin-like melody, transparent strings and woodwinds, balanced phrases, graceful and bright`
- 中文对照：门德尔松风格，为地铁座位上的约克夏犬写 30 秒小品，轻盈精灵谐谑曲，歌唱性旋律，透明弦乐与木管，均衡乐句，优雅明亮
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
