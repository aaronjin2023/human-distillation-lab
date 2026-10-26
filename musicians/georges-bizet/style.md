# Georges Bizet — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Spanish colour and French clarity, unforgettable melody, dramatic rhythm, opera where the orchestra dances too`
- ZH: 西班牙色彩与法国清晰，难忘旋律，戏剧节奏，管弦乐也起舞的歌剧

## (2) 音高与和声方向

- 主：功能和声，西班牙调式（弗里吉亚）与半音作色彩，调性清晰；禁：半音迷雾、为复杂而复杂的和声。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性强，音域宽，装饰带西班牙风味；节奏：哈巴涅拉、塞吉迪亚舞曲节奏是标记；织体：声乐主导、管弦乐舞曲化，合唱与乐队交替。`artifact`

## (4) 配器与音色

- 配器：管弦乐明亮，木管与打击乐带西班牙色彩，弦乐歌唱；《卡门》前奏曲以轻快管弦乐开场。`artifact`

## (5) 曲式与结构

- 曲式：分曲歌剧，咏叹调—重唱—合唱—终曲；《阿莱城姑娘》组曲式；交响曲四乐章古典骨架。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：西班牙舞曲节奏、咏叹调式旋律、明亮配器、戏剧对比
- 不该写：半音迷雾、沉重滞缓、管弦乐压倒人声
- Negative prompt: `chromatic fog, ponderous heaviness, orchestra drowning the voice`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Georges Bizet, a 30-second miniature for a small Yorkshire terrier sitting on a subway seat at night in a modern city, a habanera lilt, a singing melody with Spanish colour, bright transparent orchestration, dramatic and charming`
- 中文对照：比才风格，为夜里坐在地铁座位上的约克夏犬写 30 秒微型曲，哈巴涅拉摇曳，歌唱旋律带西班牙色彩，明亮透明配器，戏剧而迷人
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
