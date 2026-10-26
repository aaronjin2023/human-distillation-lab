# Béla Bartók — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Folk modes made modern, polymodality, arch form, night music, rhythm as drive, string writing of percussive clarity`
- ZH: 民间调式现代化，复调式，拱形曲式，夜之音乐，节奏即驱动力，打击性清晰的弦乐写法

## (2) 音高与和声方向

- 主：民间调式（多利亚、弗里吉亚、利底亚）+ 复调式（大小调并置）、半音作色彩；禁：德国式功能和声的圆滑解决。`artifact`

## (3) 旋律与节奏

- 旋律：民间式短动机，级进 + 跳进，装饰如民间歌唱；节奏：民间舞曲节奏、不规则重音、切分是驱动力；织体：复调 + 主调交替，弦乐织体打击性清晰。`artifact`

## (4) 配器与音色

- 配器：管弦乐分层精细，打击乐是结构声部（《弦乐、打击乐与钢片琴音乐》），钢片琴、钢琴作色彩；音色冷、亮、锐。`artifact`

## (5) 曲式与结构

- 曲式：拱形曲式（第四弦乐四重奏、乐队协奏曲）、变奏曲式、自由曲式；夜之音乐乐章是结构中的寂静。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：民间调式、复调式、拱形曲式、夜之音乐、民间舞曲节奏
- 不该写：德国式圆滑和声、无节奏驱动的抒情、模糊配器
- Negative prompt: `Germanic smooth harmony, lyricism without rhythmic drive, muddy orchestration`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Bela Bartok, a 30-second miniature for a small Yorkshire terrier sitting on a subway seat at night, a short folk-like motif, polymodal colour, driving folk-dance rhythm, night-music stillness in the middle, percussive clear strings`
- 中文对照：巴托克风格，为夜里坐在地铁座位上的约克夏犬写 30 秒微型曲，短民间式动机，复调式色彩，民间舞曲节奏驱动，中段夜之音乐寂静，打击性清晰弦乐
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
