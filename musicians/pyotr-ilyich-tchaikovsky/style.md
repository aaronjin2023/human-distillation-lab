# Pyotr Ilyich Tchaikovsky — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Sweeping melody, brilliant orchestration, ballet grace and symphonic drama, Russian soul in Western forms`
- ZH: 汹涌旋律，辉煌配器，芭蕾的优雅与交响的戏剧，西方曲式里的俄罗斯灵魂

## (2) 音高与和声方向

- 主：功能和声，旋律和声化，半音作情感色彩，调性清晰；禁：无调性、为复杂而复杂的对位。`artifact`

## (3) 旋律与节奏

- 旋律：长线歌唱，音域宽、起伏大，一听即记；节奏：芭蕾舞曲节奏（圆舞曲、性格舞）、交响曲节奏戏剧化；织体：主调，弦乐歌唱、木管独奏段落多。`artifact`

## (4) 配器与音色

- 配器：管弦乐辉煌，弦乐饱满，木管色彩鲜明，铜管与打击乐推高潮；芭蕾配器轻盈、舞曲感强。`artifact`

## (5) 曲式与结构

- 曲式：交响曲四乐章、芭蕾舞剧分场、协奏曲三乐章；高潮位置明确，结尾或辉煌或渐弱收束（《悲怆》末乐章慢板收束是例外）。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：长线歌唱旋律、圆舞曲、芭蕾舞曲、辉煌管弦乐高潮
- 不该写：无调性漫游、干涩对位、为复杂而复杂
- Negative prompt: `atonal wandering, dry counterpoint, complexity for its own sake`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Pyotr Ilyich Tchaikovsky, a 30-second ballet miniature for a small Yorkshire terrier sitting on a subway seat, a sweeping singing melody, graceful waltz lilt, brilliant warm orchestration, tender then soaring`
- 中文对照：柴可夫斯基风格，为地铁座位上的约克夏犬写 30 秒芭蕾微型曲，汹涌歌唱旋律，优雅圆舞曲摇曳，辉煌温暖配器，温柔后翱翔
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
