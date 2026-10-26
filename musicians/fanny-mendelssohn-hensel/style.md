# Fanny Mendelssohn Hensel — 作曲风格规格 style.md（给音乐模型）

> 只描述音乐，不描述人生。音高 / 和声只写通用术语，不编造实测频率值。

## (1) 一句话风格（prompt-ready）

- EN: `Romantic lyricism, song-like piano writing, chromatic warmth, intimate chamber textures, Beethovenian quartet ambition in a small frame`
- ZH: 浪漫主义抒情，歌唱性钢琴写法，半音化暖色，亲密室内乐织体，小篇幅里的贝多芬式四重奏抱负

## (2) 音高与和声方向

- 主：大调—小调功能和声，半音化经过音与借调频繁，属—主仍清晰；禁：空洞的炫技和声、为宏大而宏大的调性跳跃。`artifact`

## (3) 旋律与节奏

- 旋律：级进歌唱线为主，呼吸长，动机短而可反复变形；节奏：钢琴伴奏流动音型托住旋律，偶有交叉节奏；织体：主调 + 室内乐对话，钢琴常为主导声部。`artifact`

## (4) 配器与音色

- 配器：钢琴独奏与室内乐为主（钢琴三重奏、四重奏、艺术歌曲钢琴伴奏）；音色温暖、清晰、不求管弦乐的厚重；力度中幅为主，少极端爆发。`artifact`

## (5) 曲式与结构

- 曲式：套曲式《一年》十二首按月份循环；三重奏、四重奏用古典四乐章骨架，内填歌唱性慢乐章；结尾多收束于温暖主调而非轰然高潮。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：艺术歌曲式旋律、钢琴小品、《一年》式月令套曲、室内乐歌唱性慢乐章
- 不该写：空洞炫技、无歌唱性的机械音型、为宏大而牺牲亲密感
- Negative prompt: `empty virtuosity, mechanical figuration without song, bombastic climax, atonal wandering`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `In the style of Fanny Mendelssohn Hensel, a 30-second piano piece for a small Yorkshire terrier sitting on a subway seat, song-like melody, warm chromatic harmony, flowing piano figuration, intimate and tender, a Lied without words`
- 中文对照：范妮风格，为地铁座位上的约克夏犬写 30 秒钢琴小品，歌唱性旋律，温暖半音和声，流动钢琴音型，亲密温柔，如无词歌
- Negative: 见第 (6) 节。
- 检验点：风格是否一听可辨（和声 / 旋律 / 配器三者至少两项成立），而不是只换了个标题。
