# Modest Mussorgsky — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Russian speech melody, modal roughness, raw harmony, pictures in sound, truth before beauty`
- ZH: 俄罗斯语言旋律，调式粗粝，原始和声，声音里的图画，真实先于优美

## (2) 音高与和声方向

- 主：调式和声（自然小调、多利亚、弗里吉亚）、平行五度、意外转调，调性常游移；禁：学院式功能和声的圆滑解决。`artifact`

## (3) 旋律与节奏

- 旋律：语言式旋律——按俄语语调起伏，短句、重复、突然跳进；节奏：不规则、随语言呼吸；织体：主调 + 粗粝和声，钢琴原版织体干、硬。`artifact`

## (4) 配器与音色

- 配器：钢琴原版为主（《图画展览会》原为钢琴），管弦乐版是后人配器；音色粗粝、直接，少圆滑过渡。`artifact`

## (5) 曲式与结构

- 曲式：组曲式（《图画展览会》漫步主题 + 各画）、歌剧分场、自由曲式；漫步主题变形即结构。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：语言式旋律、调式和声、图画组曲、漫步主题
- 不该写：学院式圆滑和声、为优美而磨平粗粝、过度配器
- Negative prompt: `academic smooth harmony, polishing away roughness, over-orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Modest Mussorgsky, a 30-second piano miniature for a small Yorkshire terrier sitting on a subway seat, a speech-like short melody, modal roughness, a Promenade theme that returns transformed, raw and vivid, like a picture in an exhibition`
- 中文对照：穆索尔斯基风格，为地铁座位上的约克夏犬写 30 秒钢琴微型曲，语言式短旋律，调式粗粝，漫步主题变形重现，原始而生动，如展览会中的一幅画
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
