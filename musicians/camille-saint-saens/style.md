# Camille Saint-Saëns — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `French clarity and wit, classical balance, brilliant virtuosity, programmatic charm without heaviness`
- ZH: 法国式清晰与机智，古典均衡，辉煌炫技，标题音乐的魅力而不沉重

## (2) 音高与和声方向

- 主：功能和声，清晰、明亮，半音只作色彩；禁：瓦格纳式半音迷雾、为新奇而新奇的和声。`artifact`

## (3) 旋律与节奏

- 旋律：歌唱性 + 炫技音型，乐句均衡，装饰精致；节奏：舞曲节奏、轻快律动；织体：主调，配器透明，独奏乐器轮流歌唱。`artifact`

## (4) 配器与音色

- 配器：管弦乐透明，木管、弦乐、管风琴（第三交响曲）各有歌唱段落；音色明亮、精致；《动物狂欢节》以配器摹拟动物。`artifact`

## (5) 曲式与结构

- 曲式：交响曲、协奏曲、标题组曲严守古典骨架；《动物狂欢节》十四首小品组曲式；结尾常辉煌收束。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：清晰旋律、炫技独奏、标题小品、透明配器
- 不该写：半音迷雾、沉重滞缓、为复杂而复杂
- Negative prompt: `chromatic fog, ponderous heaviness, complexity for its own sake`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Camille Saint-Saens, a 30-second carnival miniature for a small Yorkshire terrier sitting on a subway seat, witty transparent orchestration, a singing melody with brilliant flourishes, light and graceful, as if the dog were one more animal in the Carnival`
- 中文对照：圣-桑风格，为地铁座位上的约克夏犬写 30 秒狂欢节微型曲，机智透明配器，歌唱旋律带辉煌华彩，轻盈优雅，仿佛狗是《动物狂欢节》里的又一种动物
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
